import os
import pandas as pd
from azure.storage.blob import BlobServiceClient

ACCOUNT_NAME = os.getenv("AZURE_STORAGE_ACCOUNT_NAME")
ACCOUNT_KEY = os.getenv("AZURE_STORAGE_ACCOUNT_KEY")
CONTAINER_NAME = os.getenv("AZURE_CONTAINER_NAME")

DATA_PATH = "data/sales_data.csv"
RAW_OUTPUT = "raw_sales_data.csv"
PROCESSED_OUTPUT = "processed_sales_data.csv"

def process_sales_data():
    
    df = pd.read_csv(DATA_PATH)

    df = df.drop_duplicates(subset=["order_id"])

    df["region"] = df["region"].fillna("Unknown")
    df["revenue"] = df["revenue"].fillna(0)

    df["profit_margin"] = (df["revenue"] - df["cost"]) / df["revenue"].replace(0, 1)

    def segment_customer(revenue):
        if revenue > 100000:
            return "Platinum"
        elif revenue > 50000:
            return "Gold"
        else:
            return "Standard"

    df["customer_segment"] = df["revenue"].apply(segment_customer)

    pd.read_csv(DATA_PATH).to_csv(RAW_OUTPUT, index=False)  
    df.to_csv(PROCESSED_OUTPUT, index=False) 

def upload_to_blob(file_path, blob_name):
    try:
        connect_str = f"DefaultEndpointsProtocol=https;AccountName={ACCOUNT_NAME};AccountKey={ACCOUNT_KEY};EndpointSuffix=core.windows.net"
        blob_service_client = BlobServiceClient.from_connection_string(connect_str)
        blob_client = blob_service_client.get_blob_client(container=CONTAINER_NAME, blob=blob_name)

        with open(file_path, "rb") as data:
            blob_client.upload_blob(data, overwrite=True)
        print(f"Uploaded {file_path} to Blob as {blob_name}")
    except Exception as e:
        print(f"Upload failed for {file_path}: {e}")

if __name__ == "__main__":
    process_sales_data()
    upload_to_blob(RAW_OUTPUT, RAW_OUTPUT)
    upload_to_blob(PROCESSED_OUTPUT, PROCESSED_OUTPUT)

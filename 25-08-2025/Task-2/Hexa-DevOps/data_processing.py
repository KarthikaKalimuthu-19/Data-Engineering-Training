import pandas as pd
from pathlib import Path

data_folder = Path("data")
data_folder.mkdir(exist_ok=True)

raw_file = data_folder / "raw_sales_data.csv"
clean_file = data_folder / "clean_sales_data.csv"

def main():
    print("Starting data processing...")

    df = pd.read_csv(raw_file)
    print("Raw data loaded")

    df_clean = df.dropna()
    print("Missing values removed")

    for col in df_clean.columns:
        if "date" in col.lower():
            df_clean[col] = pd.to_datetime(
                df_clean[col], errors="coerce"
            ).dt.strftime("%Y-%m-%d")
    print("Date columns formatted")

    df_clean.columns = [col.strip().lower() for col in df_clean.columns]
    print("Column names normalized")

    df_clean.to_csv(clean_file, index=False)
    print(f"Cleaned file saved at: {clean_file}")

if __name__ == "__main__":
    main()


import pandas as pd
from pathlib import Path

# Define folder path
data_folder = Path("data")
data_folder.mkdir(exist_ok=True)

# File paths
raw_file = data_folder / "raw_sales_data.csv"
clean_file = data_folder / "clean_sales_data.csv"

def main():
    print("🚀 Starting data processing...")

    # Load raw data
    df = pd.read_csv(raw_file)
    print("✅ Raw data loaded")

    # Remove missing values
    df_clean = df.dropna()
    print("✅ Missing values removed")

    # Convert date columns to YYYY-MM-DD
    for col in df_clean.columns:
        if "date" in col.lower():
            df_clean[col] = pd.to_datetime(
                df_clean[col], errors="coerce"
            ).dt.strftime("%Y-%m-%d")
    print("✅ Date columns formatted")

    # Normalize column names
    df_clean.columns = [col.strip().lower() for col in df_clean.columns]
    print("✅ Column names normalized")

    # Save cleaned file
    df_clean.to_csv(clean_file, index=False)
    print(f"📂 Cleaned file saved at: {clean_file}")

if __name__ == "__main__":
    main()

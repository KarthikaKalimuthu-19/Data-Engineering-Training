import pandas as pd
import numpy as np

dfEmp = pd.read_csv(r"C:\Users\ELCOT\Desktop\GitHub\CapStone Project\Retail Sales Performance Dashboard\Week-2\Datasets\employees.csv")
dfPro = pd.read_csv(r"C:\Users\ELCOT\Desktop\GitHub\CapStone Project\Retail Sales Performance Dashboard\Week-2\Datasets\products.csv")
dfSales = pd.read_csv(r"C:\Users\ELCOT\Desktop\GitHub\CapStone Project\Retail Sales Performance Dashboard\Week-2\Datasets\sales.csv")
dfStor = pd.read_csv(r"C:\Users\ELCOT\Desktop\GitHub\CapStone Project\Retail Sales Performance Dashboard\Week-2\Datasets\stores.csv")

print(f"Null values: {dfEmp.isna().sum().any()}")
print(f"Null values: {dfPro.isna().sum().any()}")
print(f"Null values: {dfSales.isna().sum().any()}")
print(f"Null values: {dfStor.isna().sum().any()}")

dfSales = dfSales.dropna()

print(f"Null values: {dfSales.isna().sum().any()}")

df = dfPro.merge(dfSales, on="productID", how="inner")

df["revenue"] = df["quantity"] * df["price"]
df["profit"] = df["revenue"] - (df["quantity"] * df["cost"])
df["discountPercentage"] = round(100 - (df["price"] / df["price"]) * 100, 2)
df["totalCost"] = df["quantity"] * df["cost"]
df["profitMargins"] = round((df["profit"] / df["revenue"]), 2)

productSummary = df.groupby("productID").agg(
    productRevenue=pd.NamedAgg(column="revenue", aggfunc="sum")
).merge(dfPro[["productID", "name"]], on="productID", how="inner") \
.sort_values("productRevenue", ascending=False)

storeSummary = df.groupby("storeID").agg(
    storeRevenue=pd.NamedAgg(column="revenue", aggfunc="sum")
).merge(dfStor[["storeID", "name"]], on="storeID", how="inner") \
.sort_values("storeRevenue", ascending=False)

print("------------------Product Summary--------------------------")
print(productSummary[["name", "productRevenue"]].iloc[:5, :])
print("-----------------------------------------------------------\n")

print("------------------Store Summary----------------------------")
print(storeSummary[["name", "storeRevenue"]].iloc[:5, :])
print("-----------------------------------------------------------\n")

df.to_csv(r"C:\Users\ELCOT\Desktop\GitHub\CapStone Project\Retail Sales Performance Dashboard\Week-2\Delieverables\summary.csv", index=False)

totalRevenue = df["revenue"].sum()
totalProfit = df["profit"].sum()

topProduct = productSummary.iloc[0]["name"]
bottomProduct = productSummary.iloc[-1]["name"]

topStore = storeSummary.iloc[0]["name"]
bottomStore = storeSummary.iloc[-1]["name"]

report = pd.DataFrame({
    "totalRevenue": [totalRevenue],
    "totalProfit": [totalProfit],
    "topProduct": [topProduct],
    "bottomProduct": [bottomProduct],
    "topStore": [topStore],
    "bottomStore": [bottomStore]
})

print("------------------------------------Key Metrics------------------------------------")
print(report)
print("------------------------------------------------------------------------------------")

report.to_csv(r"C:\Users\ELCOT\Desktop\GitHub\CapStone Project\Retail Sales Performance Dashboard\Week-2\Delieverables\key_metrics_report.csv", index=False)
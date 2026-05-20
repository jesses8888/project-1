import csv
import numpy as np

products = []
price = []
stock = []
sales_volume = []

file_name = "Grocery_Inventory_and_Sales_Dataset.csv"

with open(file_name, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for row in reader:
        products.append(row["Product_Name"])
        clean_price = float(row["Unit_Price"].replace("$", "").strip())
        price.append(clean_price)
        stock.append(float(row["Stock_Quantity"]))
        sales_volume.append(float(row["Sales_Volume"]))

products = np.array(products)
price = np.array(price)
stock = np.array(stock)
sales_volume = np.array(sales_volume)

total_value = price * stock

hot_index = np.argmax(sales_volume)
hot_product = products[hot_index]
max_sales = sales_volume[hot_index]

discount_revenue = (price * 0.9) * sales_volume

output_file = "Grocery_Analysis_Result.csv"
with open(output_file, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(
        [
            "Product_Name",
            "Stock_Quantity",
            "Total_Inventory_Value",
            "Discounted_Revenue",
            "Is_Best_Seller",
        ]
    )

    for i in range(len(products)):
        w.writerow(
            [
                products[i],
                stock[i],
                round(total_value[i], 2),
                round(discount_revenue[i], 2),
                i == hot_index,
            ]
        )

print("=" * 50)
print(f"工作完成！結果已寫入：{output_file}")
print(f"本期最暢銷商品：{hot_product} (銷量: {int(max_sales)} 件)")
print("=" * 50)
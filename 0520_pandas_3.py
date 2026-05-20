import pandas as pd
df = pd.read_csv('SuperMarket Analysis.csv')

print(f"=== 1. 資料基本檢視 ===")
print(f"總資料筆數: {len(df)} 筆\n")
print("前 5 筆資料內容:")
print(df.head())
print("-" * 50)

filtered_df = df[
    (df['Branch'].isin(['A', 'Alex'])) &
    (df['Customer type'] == 'Member')
]

print(f"=== 2. 特定條件篩選 ===")
print(f"符合條件 (Branch 為 A 且為 Member) 的交易筆數: {len(filtered_df)} 筆")
print("-" * 50)

product_summary = df.groupby('Product line').agg(
    Total_Sales=('Sales', 'sum'),
    Average_Rating=('Rating', 'mean')
).round(2).reset_index()

print(f"=== 3. 各產品線銷售與評分彙總 ===")
print(product_summary)
print("-" * 50)

city_gender_summary = df.groupby(['City', 'Gender']).agg(
    Average_Sales=('Sales', 'mean'),
    Transaction_Count=('Sales', 'count')
).round(2).reset_index()

print(f"=== 4. 依城市與性別分組統計 ===")
print(city_gender_summary)
print("-" * 50)

top_product = product_summary.loc[product_summary['Total_Sales'].idxmax()]

print(f"=== 5. 銷售冠軍產品線 ===")
print(f"總銷售額最高的產品線為: {top_product['Product line']}")
print(f"總銷售金額為: {top_product['Total_Sales']}")
print("-" * 50)

product_summary.to_csv('0520_pandas_3OK.CSV', index=False, encoding='utf-8-sig')
print("=== 6. 檔案導出 ===")
print("已成功將產品線彙總結果輸出至 '0520_pandas_3OK.CSV' 檔案！")
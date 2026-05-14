import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Data/Final_cleaned_retail_data.csv")

print(df.head())

top_product = df.groupby('sub_category')['sales'].sum().sort_values(ascending=False)
print(top_product.head(10))

top_product.head(10).plot(kind='bar')
plt.title('Top Selling products')
plt.ylabel('Sales')
plt.show()

region_sales = df.groupby('region')['sales'].sum().sort_values(ascending=False)
print(region_sales)

region_sales.plot(kind='bar')
plt.title('Sales by Region')
plt.xlabel('Region')
plt.ylabel('Sales')
plt.show()

monthly_sales = df.groupby('month')['sales'].sum().sort_values(ascending=False)
print(monthly_sales)

monthly_sales.plot(kind = 'bar')
plt.title('Monthly Sales trend')
plt.show()

profit_category = df.groupby('category')['profit'].sum().sort_values(ascending=False)
print(profit_category)

profit_category.plot(kind='bar')
plt.title('Profit by category')
plt.show()

loss_products = df.groupby('sub_category')['profit'].sum().sort_values()
print(loss_products.head(10))
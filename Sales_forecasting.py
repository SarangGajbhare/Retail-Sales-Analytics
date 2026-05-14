import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# Load Clean Data
df = pd.read_csv("Data/Final_cleaned_retail_data.csv")

print(df.head())

# Create monthly sales
monthly_sales = df.groupby('month')['sales'].sum().reset_index()
print(monthly_sales)

# prepare feature and target
X = monthly_sales[['month']]
y = monthly_sales['sales']

# split data
X_train, X_test, y_train, y_test =\
    train_test_split(X, y, test_size=0.2, random_state=42
)

#train model
model = LinearRegression()
model.fit(X_train, y_train)

#predict future
prediction = model.predict(X_test)
print(prediction)

# check accuracy
error = mean_absolute_error(y_test, prediction)
print("Mean Absolute Error: ",error)

# predict future sales
future_month = [[13]]
future_prediction = model.predict(future_month)
print("Predicted Sales for next month", future_prediction)

# visualize result
plt.scatter(X, y)

plt.plot(X, model.predict(X), color='red')

plt.title("Sales Forecasting")

plt.xlabel("Month")

plt.ylabel("Sales")

plt.show()
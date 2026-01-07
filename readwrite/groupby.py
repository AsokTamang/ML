import pandas as pd

df = pd.read_csv("C:/Users/ashok/OneDrive/Desktop/practicefile.csv")
print(df.groupby('ProductCategory').agg(
    total_price=('Price', 'sum')))  # here we are applying aggregration method on the dataframe
# where we are grouping the data based on unique ProductCategory, and calculating the total price based on the sum of prices
grouped = df.groupby('ProductCategory')
print(grouped['Price'].sum())  # here we are doing the same thing which is getting the total sum of the items based on category but we are not assigning the new column in the dataframe

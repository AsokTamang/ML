import pandas as pd

# .fillna() is one of the most important feature of pandas DataFrame which is used to fill the N/A value with the custom data as an example
df = pd.read_csv("C:/Users/ashok/OneDrive/Desktop/final_movies.csv")
# here what we are doing is filling the null value of budget column with the mean value of whole budget column data
# and filling the null revenue data with the average of whole revenuw column data
df.fillna({
    'budget': df['budget'].mean(),
    'revenue': df['revenue'].mean()
}, inplace=True)
df.to_csv("C:/Users/ashok/OneDrive/Desktop/final_movies.csv", index=False)  # writing towards csv file
print(df)

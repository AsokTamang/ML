import pandas as pd
import numpy as np
df=pd.read_csv("C:/Users/ashok/OneDrive/Desktop/movies_data.csv")
g=df.groupby('industry')
for key,data in g:
  if key == 'Hollywood':
      print(data)
 # print(key)
 # print(data.size)  #the size means the total number of datas like whole datas in each group or key which is the industry currently
def grouper(x,df,col):
    if 1<= df[col].loc[x]<=3.9:
        return 'Poor'
    elif 4<= df[col].loc[x]<=7.9:
        return 'Average'
    elif 8 <= df[col].loc[x] <= 10:
        return 'Good'
    else:
        return 'others'
lastg = df.groupby(lambda x:grouper(x,df,'imdb_rating'))  #here we are using the customer grouper function inorder to group the whole data and x is the row index here
for k,v in lastg:
    print(k)
    print(v)

num_rows = 5
sales_df = pd.DataFrame({
'TransactionID': np.arange(1, num_rows+1),
'CustomerID': np.random.choice(['C001','C002','C003','C004','C005'], num_rows),
'ProductCategory': np.random.choice(['Electronics','Clothing','Groceries'], num_rows),
'Quantity': np.random.randint(1, 20, num_rows),
'Price': np.random.randint(5, 1000, num_rows),
'Date': pd.date_range(start='2023-01-01', periods=num_rows, freq='D')
})


employee_df = pd.DataFrame({
'EmployeeID': np.arange(6, 21),
'Department': np.random.choice(['HR','IT','Finance','Marketing'], 15),
'Gender': np.random.choice(['Male','Female'], 15),
'Salary': np.random.randint(40000, 120000, 15),
'JoiningYear': np.random.randint(2015, 2024, 15)
})

df_main = pd.concat([sales_df,employee_df],keys=['sales_df','employee_df'],axis=1)  #here we are merging the salesdf and employeedf using .concat method and axis helps to concat based on the direction or axis , either vertical or horizontal
print(df_main)

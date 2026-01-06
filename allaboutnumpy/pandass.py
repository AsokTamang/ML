import pandas as pd
#in pandas we can access the data title from an Excel file as property
import csv
df=pd.read_excel("C:/pythonprojects/start.csv.xlsx")
print(df.head(3))
print(df.shape)  #so our excel file consists of 10 rows and 8 columns
maximum_salary = df.salary.max()  #here we are getting the maximum value of the salary
print(df[df['salary']==maximum_salary]['name'])  #here we are getting the name of the staff having maximum salary
print(df.columns.astype(str))
print(df.department.unique())  #printing the unique departments
#counting the total number of unique department and conerting the returned data into dictionary
print(df['department'].value_counts().rename_axis(None).rename(None).to_dict())
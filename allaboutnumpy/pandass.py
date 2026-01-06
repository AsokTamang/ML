import pandas as pd
from datetime import date
# in pandas we can access the data title from an Excel file as property
import csv

df = pd.read_excel("C:/pythonprojects/start.csv.xlsx")
print(df.head(3))
print(df.shape)  # so our excel file consists of 10 rows and 8 columns
maximum_salary = df.salary.max()  # here we are getting the maximum value of the salary
print(df[df[
             'salary'] == maximum_salary].name)  # here we are getting the name of the staff having maximum salary using the mask method
# which prints alex
print(df.columns.astype(str))
print(df.department.unique())  # printing the unique departments
# counting the total number of unique department and conerting the returned data into dictionary
print(df['department'].value_counts().rename_axis(None).rename(None).to_dict())

# filtering the columns
df_new = df[['employee_id', 'name', 'department']]
print(df_new)
print(df_new[df_new['employee_id'] == df_new.employee_id.max()].name.rename(
    None))  # here .rename(None) removes the series name

# filtering the rows
df_latest = df[
    df['happiness_score'] > 5]  # here we are getting the dataframe where the happiness data is greater than 5
print(df_latest)
print(
    df.describe())  # here describe() calculates the count,mean,std of all the numeric columns data available in the dataframe
df['contract'] = date.today().year - df['join_date'].dt.year  #here we are creating a new column called 'contract' in our current dataframe
print(df[['name','contract']])  # here we are calculating how many years the staffs are in company with their name , by selecting the columns name and contract

df['number_of_years'] = df['join_date'].dt.year.apply(lambda x: 2026-x) #here first of all we are extracting the year from the join_date column then we are
#using .apply method inorder to calculate the number of years of employee in the company
maximum_years=df['number_of_years'].max()
most_experienced=df[df['number_of_years']==maximum_years]  #getting the df where the number of years column matches with the maximum years value
print(most_experienced[['name','contract']])  #again filtering the columns

#print(df.apply(lambda x:x['revenue']-x['budget'],axis=1))
#pandas df.apply() method is used for applying the function in the dataframe rows or columns
print(df.set_index('employee_id',inplace=True))    #here we are making the employee_id as the index
print(df.index)
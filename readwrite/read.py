import pandas as pd

def converter(value):
    if value == 0:
        return pd.NA  #here if the value of the salary is 0 then we assign NA to this column data
    return value


# df = pd.read_excel('C:/pythonprojects/start.csv.xlsx',skiprows=1)  #here this code will skip the very first row
# header helps us to assign which indexed row to be a header
# nrows helps us to retrieve the number of rows from the file
#df = pd.read_excel('C:/pythonprojects/start.csv.xlsx', header=0, nrows=5,names = ['id', 'name', 'field', 'age','expyears','salary', 'state', 'enrolled'])  #here we are making our own custom table title
df_main = pd.read_excel("C:/pythonprojects/start.xlsx",'main',converters={'salary':converter})  #here we are using converter in the salary column so that the salary column having data 0 will become null
df_main['sh'] = df_main['salary']* df_main['happiness_score']

print(df_main)
#here na_values give the proper null data to the empty or abnormal values in the column
    #in this case we are giving na_values to the salary column having data 0
 # reading the excel file
#creating dataframes for company revenue and staff data
df_stocks = pd.DataFrame({
    'company':['Google','Meta','Amazon','X'],
    'Revenue':[85,90,100,120]

})
df_staffs = pd.DataFrame({
    'name':['Asok','Shriya','Ram'],
    'Age':[24,22,26]
})
with pd.ExcelWriter('C:/pythonprojects/new.xlsx') as writer:  #writing to the excel file
    df_stocks.to_excel(writer,'Company_Revenue',index=False)
    df_staffs.to_excel(writer,'Staff_Data',index=False)
final = pd.merge(df_stocks,df_staffs,left_on='company',right_on='name')
print(final)
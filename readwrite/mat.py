
from matplotlib import pyplot as plt
import pandas  as pd
df2=pd.read_csv("C:/Users/ashok/OneDrive/Desktop/fruits_data.csv")
cols = df2.columns.drop("date") #here we are storing all the columns of df2 in cols variable except a column date which must be in the datetime format
df2[cols] = df2[cols].apply(pd.to_numeric,errors='coerce')#here we are converting all the columns data into numeric values except for the datetime
df2[cols] = df2[cols].fillna(0)  #here we filling the null values with 0 in all the columns except for the date one
df2.plot(kind="bar",x="date",figsize=(12,6))  #here we are using the pandas dataframe directly inorder to build a barchart where the x-axis value will be date
#fig,axes =plt.subplots(2,2)  #here we are using the graphical representation in multiple axes but in the same graphical figure which is 2 rows and 2 columns
#axes[0,0].plot(df['budget'],df['revenue']) #here we are passing the budget column in the x-axis and revenue column in the y-axis
#axes[0,1].plot(df2['apple(1kg)'],df2['grapes(1kg)'])
#axes[1,0].plot(df3['language_id'],df3['imdb_rating'])
#plt.show()
#total_quantity = df2[['apple(1kg)','banana(1 dozen)','grapes(1kg)']].sum()  #here we are finding the total quantity of the columns apple, banana and grapes which comes in the form of series or array
#print(total_quantity)
#print(total_quantity.index) #index gives us the name of each data
#plt.pie(total_quantity,labels=['apple','banana','grapes'],colors=['red','yellow','green'],autopct="%1.2f%%",startangle=140,explode=(0.2,0,0),shadow=True)  #here we are labeling the group based on the index for our piechart
plt.xticks(rotation=45)  #here this rotates the column name available in the x-axis into 45 degree
plt.show()



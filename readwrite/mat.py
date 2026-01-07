from matplotlib import pyplot as plt
import pandas  as pd
df2=pd.read_csv("C:/Users/ashok/OneDrive/Desktop/fruits_data.csv")

#fig,axes =plt.subplots(2,2)  #here we are using the graphical representation in multiple axes but in the same graphical figure
#axes[0,0].plot(df['budget'],df['revenue']) #here we are passing the budget column in the x-axis and revenue column in the y-axis
#axes[0,1].plot(df2['apple(1kg)'],df2['grapes(1kg)'])
#axes[1,0].plot(df3['language_id'],df3['imdb_rating'])
#plt.show()
total_quantity = df2[['apple(1kg)','banana(1 dozen)','grapes(1kg)']].sum()  #here we are finding the total quantity of the columns apple, banana and grapes
print(total_quantity)
print(total_quantity.index) #index gives us the name of each data
plt.pie(total_quantity,labels=['apple','banana','grapes'],colors=['red','yellow','green'])  #here we are labeling the group based on the index for our piechart
plt.show()



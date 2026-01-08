import pandas as pd
df_agg_bookings = pd.read_csv('C:/Users/ashok/OneDrive/Desktop/fact_aggregated_bookings.csv')
df_bookings = pd.read_csv("C:/Users/ashok/OneDrive/Desktop/fact_bookings.csv")
df_date=pd.read_csv("C:/Users/ashok/OneDrive/Desktop/dim_date.csv")
df_hotel=pd.read_csv("C:/Users/ashok/OneDrive/Desktop/dim_hotels.csv")
df_rooms=pd.read_csv("C:/Users/ashok/OneDrive/Desktop/dim_rooms.csv")
maximum = df_agg_bookings.capacity.max()

print(maximum)
print(df_agg_bookings[df_agg_bookings['capacity']==maximum]['property_id'])  #here we are selecting the property id having the maximum capacity
print(df_bookings.shape)
#df_total=pd.merge(df_agg_bookings[['successful_bookings','capacity','property_id']],df_bookings[['property_id','booking_date']],on='property_id')  #here we are taking only the required columns from the tables
#print(df_total[df_total['successful_bookings']>df_total['capacity']]['booking_date'])

#data cleaning
df_bookings = df_bookings.describe()
print(df_bookings[df_bookings['no_guests']<=0])  #here we are doing the logical condition on the rows of df_bookings dataframe in the column no_guests
def converter(value):
    if int(value)<=0:
        return 0
    return value
df_bookings['no_guests'].fillna(0,inplace=True)    #here first of all we are filling the null numbers with 0 inplace the current dataframe
df_bookings['no_guests']=df_bookings['no_guests'].apply(lambda x:converter(x))  #here we are converting the column no_guests data using the function converter
print(df_bookings)
df_agg_bookings.groupby('property_id')['successful_bookings'].value_counts()  #here we are grouping by the property id and counting the total successful
df_agg_bookings.groupby(['property_id', 'successful_bookings']).size()

df_bookings.describe()
print(df_bookings[df_bookings['no_guests']<=0])  #here we are doing the logical condition on the rows of df_bookings dataframe in the column no_guests
df_bookings['no_guests'].fillna(0,inplace=True)    #here first of all we are filling the null numbers with 0 inplace the current dataframe
df_bookings.loc[df_bookings['no_guests']<=0,'no_guests']=0 #here we are changing the column value of no_guests based on the row value of no_guests
df_bookings['revenue_generated'].max()
avg,std=df_bookings['revenue_generated'].mean(),df_bookings['revenue_generated'].std()  #here we are calculating the mean and standard deviation of the column revenue_generated
print(avg,std)
limit=avg + 3*std

#removing the outliers
#df_bookings= df_bookings[df_bookings['revenue_generated']<=limit]     #here we are removing the df data whose revenue_generated column data has value more than the limit value,
df_bookings['revenue_generated'].max()
print(df_bookings)
#bookings
#checking if any revenue_generated is lesser than 0
print(df_bookings[df_bookings['revenue_generated']<0])


#cleaning the revenue_realized column
df_bookings.revenue_realized.describe()
av,std2=df_bookings.revenue_realized.mean(),df_bookings.revenue_realized.std()
print(av,std2)
higher_limit = av + 3*std2
lower_limit = av - 3*std2   #here this one is the lower limit that the revenue_realized must be within
print(df_bookings[df_bookings.revenue_realized>higher_limit])  #here we are checking the datas where the revenue_realized is greater than the higher_limit
df_bookings=df_bookings[df_bookings.revenue_realized<higher_limit]  #here we are changing the original dataframe inplace by removing all the rows whose  revenue realized value is greater than higher_limit
print(df_bookings.revenue_realized.shape)


#observing the datas
df_bookings.revenue_realized.describe()
av,std2=df_bookings.revenue_realized.mean(),df_bookings.revenue_realized.std()
higher_limit = av + 3*std2

#29359
print(df_bookings[df_bookings.revenue_realized>higher_limit])  #observing the datas
print(df_rooms.head(5))
#df_bookings=df_bookings[df_bookings.revenue_realized<higher_limit]  #here we are changing the original dataframe inplace by removing all the rows whose  revenue realized value is greater than higher_limit
#df_bookings.revenue_realized.shape


#checking the outliers

df_bookings['ratings_given'].describe()
average = df_bookings['ratings_given'].mean()
standard_deviation = df_bookings['ratings_given'].std()
higher_limit = average + 3 * standard_deviation
lower_limit1 = average - 3 * standard_deviation
print(df_bookings[df_bookings['ratings_given']>higher_limit])
print(df_bookings[df_bookings['ratings_given']<lower_limit])
print(df_bookings.isnull().sum())   #then this calculates the sum of all the rows in specific columns whose value is null

#cleaning the null values
df_agg_bookings.isnull().sum()  #here this calculate the number of null values in each rows of each columns
mean = df_agg_bookings['capacity'].mean()
df_agg_bookings['capacity'].fillna(mean,inplace=True) #cleaning the data of capacity by replacing the null values with mean value
df_agg_bookings['capacity'].isnull().sum()
import pandas as pd
df_agg_bookings = pd.read_csv('C:/Users/ashok/OneDrive/Desktop/fact_aggregated_bookings.csv')
df_bookings = pd.read_csv("C:/Users/ashok/OneDrive/Desktop/fact_bookings.csv")
df_date=pd.read_csv("C:/Users/ashok/OneDrive/Desktop/dim_date.csv")
df_hotel=pd.read_csv("C:/Users/ashok/OneDrive/Desktop/dim_hotels.csv")
df_room=pd.read_csv("C:/Users/ashok/OneDrive/Desktop/dim_rooms.csv")
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
df_bookings= df_bookings[df_bookings['revenue_generated']<=limit]     #here we are removing the df data whose revenue_generated column data has value more than the limit value,
df_bookings['revenue_generated'].max()
print(df_bookings)
#bookings
#checking if any revenue_generated is lesser than 0
print(df_bookings[df_bookings['revenue_generated']<0])

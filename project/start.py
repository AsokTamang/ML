import pandas as pd
df_bookings = pd.read_csv("C:/Users/ashok/OneDrive/Desktop/fact_bookings.csv")
df_date=pd.read_csv("C:/Users/ashok/OneDrive/Desktop/dim_date.csv")
df_hotel=pd.read_csv("C:/Users/ashok/OneDrive/Desktop/dim_hotels.csv")
df_room=pd.read_csv("C:/Users/ashok/OneDrive/Desktop/dim_rooms.csv")
df_fact=pd.read_csv("C:/Users/ashok/OneDrive/Desktop/fact_aggregated_bookings.csv")
df_bookings.ratings_given.fillna(0,inplace=True)  #here the null value in ratings_given will be assigned 0 andwe must use inplace method
df_bookings.head(10)
print(df_bookings.shape)
total_booking_platform=df_bookings.groupby('booking_platform')
df_bookings.booking_platform.value_counts().plot(kind="barh",x="Booking_Platform",y="Number_of_bookings")
df_bookings.describe()  #it shows all the mathematical datas on the numeric columns
df_date.describe()
df_date['week no'].value_counts()
df_hotel.head(10)
df_hotel.city.value_counts()
df_fact.head(10)
df_fact.successful_bookings.max()

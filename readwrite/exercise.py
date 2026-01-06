import pandas as pd

df = pd.read_csv("C:/Users/ashok/Downloads/64101194a2364/source-code/2_pandas_basics_code/3_read_write_to_excel/Exercises/movies_data.csv")
df['year_classify']=df['release_year'].apply(lambda x:'before 2000' if x<2000 else 'after 2000')  #here based on the column release_year, we are designing a new column data
#year_classify
print(df)

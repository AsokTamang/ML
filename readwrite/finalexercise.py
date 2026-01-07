#cleaning the data
import pandas as pd
import numpy as np
df=pd.read_csv("C:/Users/ashok/OneDrive/Desktop/fruits_data.csv")
df.replace([-88888,-111111,-10000,-989898,-8989898,-7878787,-8989898,-989898,-9996585,-989898,'#NAME?'],np.nan,inplace=True)
df.to_csv("C:/Users/ashok/OneDrive/Desktop/fruits_data.csv",index=False)  #ignoring the indices

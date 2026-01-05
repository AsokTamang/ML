import numpy as np
import time

l1=np.arange(10)  #this np.arange creates the list upto 9
print(l1)
l2=np.arange(10)
start_time = time.time()
l3 = l1 + l2   #vector addition of arrays
endtime = time.time()
print(endtime-start_time)
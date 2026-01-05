import numpy as np
import time

#numpy arrays occupy less memory as well as they are much faster compared to the python lists
#as well as numpy has a lot of built-in functions

l1=np.arange(10)  #this np.arange creates the list upto 9
print(l1)
l2=np.arange(10)
start_time = time.time()
l3 = l1 + l2   #vector addition of arrays
endtime = time.time()
print(endtime-start_time)

rev=np.array([40,30,70])
rev2=np.array([[40,30,70],[90,100,200]],dtype=np.float32)
print(rev.ndim)  #number of dimensions
print(rev2.ndim)  #here .ndim gives us the number of dimension of an array
print(rev2[1,1])  #based on indexing, we are getting the number
print(rev2.dtype)  #here dtype means the type of bytes this array is occupying
print(rev2.size)  #here .size gives us the total number of elements in a array

print(rev2.shape) #here .shape gives us the number of rows and columns from a given array
a=(np.sort(rev2,axis=None))  #here we are sorting the 2 rowed array of matrix in a single array by using axis=None
print(a)
print(np.linspace(1,10,80))  #here we are generating 80 numbers of datas from 1 to 10 which are at an equal distance
print(rev2.sum(axis=0))  #here axis = 0 gives us the sum of the numbers in a matrix in a vertical order
print(rev2.sum(axis=1))  #here axis = 1 gives us the sum of the numbers in a matrix in a horizontal order


print(rev2.itemsize)

#here .itemsize gives us the amount of byte that each item or number in rev2 occupies

q1  = np.array([ [ 4  , 9 ,  1 ],
[ 7 , 6  , 2 ]])
q2  =np.array([ [ 8 , 3 , 5 ],
[ 11 , 2  , 6 ]])
print(np.cross(q1,q2))


#the first index represents the row and second index represents the column
print(q1[-1,0:2])  #here we are using slicing method on the very last row of a matrix q1
print(q1[0,:])  #here we are printing every column of only first row
print(q1[1:,:])  #here we are printing only  second row but its every column
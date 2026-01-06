import numpy as np
import time

#numpy arrays occupy less memory as well as they are much faster compared to the python lists
#as well as numpy has a lot of built-in functions

l1 = np.arange(10)  #this np.arange creates the list upto 9
print(l1)
l2 = np.arange(10)
start_time = time.time()
l3 = l1 + l2  #vector addition of arrays
endtime = time.time()
print(endtime - start_time)

rev = np.array([40, 30, 70])
rev2 = np.array([[40, 30, 70], [90, 100, 200]], dtype=np.float32)
print(rev.ndim)  #number of dimensions
print(rev2.ndim)  #here .ndim gives us the number of dimension of an array
print(rev2[1, 1])  #based on indexing, we are getting the number
print(rev2.dtype)  #here dtype means the type of bytes this array is occupying
print(rev2.size)  #here .size gives us the total number of elements in a array

print(rev2.shape)  #here .shape gives us the number of rows and columns from a given array
a = (np.sort(rev2, axis=None))  #here we are sorting the 2 rowed array of matrix in a single array by using axis=None
print(a)
print(np.linspace(1, 10, 80))  #here we are generating 80 numbers of datas from 1 to 10 which are at an equal distance
print(rev2.sum(axis=0))  #here axis = 0 gives us the sum of the numbers in a matrix in a vertical order
print(rev2.sum(axis=1))  #here axis = 1 gives us the sum of the numbers in a matrix in a horizontal order

print(rev2.itemsize)

#here .itemsize gives us the amount of byte that each item or number in rev2 occupies

q1 = np.array([[4, 9, 1],
               [7, 6, 2]])
q2 = np.array([[8, 3, 5],
               [11, 2, 6]])
print(np.cross(q1, q2))

#the first index represents the row and second index represents the column
print(q1[-1, 0:2])  #here we are using slicing method on the very last row of a matrix q1
print(q1[0, :])  #here we are printing every column of only first row
print(q1[1:, :])  #here we are printing only  second row but its every column

horizontal = np.hstack((q1, q2))  #this code combines the two matrices horizontally
print(horizontal)

vertical = np.vstack((q1, q2))  #this code combines the two matrices vertically
print(vertical)
#vertical -> columns
#horizontal -> rows

print(np.hsplit(horizontal, [2]))  #splitting the combined matrix horizontally from index 2

data = np.array([20, 30, 40, 60, 70])
print(data.max())
index = np.argmax(data)  #here np.argmax gives us the index of the maximum value in a given matrix
print(index)

transactions = np.array([
    ['101', 'Mohan', '250.5', '2023-08-01'],
    ['102', 'Sita', '120.0', '2023-08-02'],
    ['103', 'Ramesh', '560.75', '2023-08-03'],
    ['104', 'Geeta', '320.0', '2023-08-04'],
    ['105', 'Amit', '450.25', '2023-08-05'],
    ['106', 'Neha', '180.0', '2023-08-06'],
    ['107', 'Raj', '600.0', '2023-08-07'],
    ['108', 'Priya', '220.5', '2023-08-08'],
    ['109', 'Anil', '350.0', '2023-08-09'],
    ['110', 'Rita', '400.75', '2023-08-10']
])

index = (np.argmax(transactions[
                       :, 2]))  #here we are selecting the transaction column of every rows inorder to get index having the maximum transaction value

print(transactions[index][1])  #printing the name who made the highest transaction from the given data
print(transactions[:, 2].astype(
    float).max())  #here we must convert the type to float initially inorder to get the max value from given list of data

print(np.zeros((3, 4)))

# Employee Details: Employee ID, Department, Number of Years with AtliQ
employee_details = np.array([
    [101, 'Sales', 3],
    [102, 'HR', 5],
    [103, 'IT', 2],
    [104, 'Sales', 8],
    [105, 'IT', 6],
    [106, 'HR', 4],
    [107, 'IT', 7],
    [108, 'Sales', 1],
    [109, 'HR', 3]
])

# Survey Results: Employee ID, Happiness Score (1-10)
survey_results = np.array([
    [101, 8],
    [102, 10],
    [103, 9],
    [104, 6],
    [105, 7],
    [106, 8],
    [107, 9],
    [108, 5],
    [109, 7]
])

result = np.hstack(
    (employee_details, survey_results))  #here we are merging the employee details and survey results horizontally
print(result)
print(result.dtype)  #this gives us the type of output
print(np.sort(result[:, -1].astype(
    int)))  #here first of all we are converting the last column into integer then only we are using np.sort()

print(result[:, :2])  #here this code selects the employee id and the department
for row in result:
    print(f'employee id {row[0]} having happiness level of {row[-1]}')
print(result[:, -1].astype(float))  #converting the type of data using .astype

average_happiness_score = sum(result[:, -1].astype(int)) // len(result)
print(average_happiness_score)
print(np.mean(result[result[:,1] == 'HR'][:,4].astype(int)))  #here we are selecting only that rows whose department is equal to HR
#from this filtered rows we are only selecting the happiness level data by converting it into integer type







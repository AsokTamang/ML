import math

with open("C:/Users/ashok/Downloads/stocks.csv",'r') as file , open("C:/Users/ashok/OneDrive/Desktop/change.txt",'w') as outputfile:
    outputfile.write("Company Name , PE Ratio, PB Ratio\n")   #here \n skips the line means write at single line
    next(file)  #here next(file) skips the first sentence of the reading file
    for line in file:
        tokens=line.split(',')  #here .split() splits the given line at each words with ,
        stockade = tokens[0]
        pe_ratio=math.ceil(int(tokens[1]) / int(tokens[2]))
        pb_ratio = math.ceil(int(tokens[1]) / int(tokens[3]))
        outputfile.write(f'{stockade},{pe_ratio},{pb_ratio}\n')
    outputfile.close()
    file.close()

#GRADE CALCULATOR
def find_grade(num):
    if  90<=num<=100:
        return 'A'
    elif 80 <= num < 89:
        return 'B'
    elif 70 <= num < 79:
        return 'C'
    elif 60 <= num < 69:
        return 'D'
    else:
        return 'F'

try:
    ask = int(input("Enter a value: "))
    if ask>100 or ask < 0:
     raise ValueError('Marks must be between 0 and 100')
except ValueError as VE:  #if the entered value is not a number then we raise a valueError
     print(VE)
else:
    print(find_grade(ask))
finally:
    print("Thank you for using the Grade Calculator. Goodbye!")

class Employee:
    def __init__(self,id,name):
        self.id=id
        self.name=name
    def displaydata(self):
        return f'{self.id}: {self.name}'
e=Employee(1,'asok')
print(e.displaydata())
del e.id  #here if we are deleting the id



class Animal:
    def __int__(self,habitat):
        self.habitat=habitat
    def sound(self):
        print('some sound')
class Dog(Animal):
    def __init__(self):
     super().__init__('house')
    def sound(self):
        print('dog sound')


skills = 'javascript,python,datascientist,AIEngineer'
print(skills.split(',',maxsplit=2))














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

filename = 'helloworld.pdf'
print(filename.endswith('.txt'))


sentence = "The Himalayas are one of the youngest mountain ranges on the planet."
print(' '.join(sentence.split(' ')[0:2]))  #first we are splitting the given string at space then we are using slice method and join method
#inorder to join the sentence
print(' '.join(sentence.split(' ')[-4:-6:-1][::-1]))
first = ' '.join(sentence.split(' ')[:2])
second = ' '.join(sentence.split(' ')[-1:-4:-1][::-1])
print(f'{first} {second}')


monthly_sales=[42,38,40,33,45]
months = ['january','february','march','april','may']
for month,sale in zip(months,monthly_sales):
    print(f'{month}:{sale}')


for i,sale in enumerate(monthly_sales):
    if i % 2 == 0:
        continue
    print(sale)  #printing the sale which is at odd index only

products = ['iphone','ipad','macbook']
regions = ['USA','China','India']
revenue = [20,23,45,18,17,12,12,9,5]

i = 0
for product in products:
    for region in regions:
        print(f'Revenue of product {product} in region {region} is {revenue[i]} ')
        i+=1





avengers  = ['Iron Man', 'Captain America', 'Black Widow', 'Hulk', 'Thor', 'Hawkeye']
print(len(avengers))

avengers.append('spiderman')
avengers.remove('Captain America')
print(avengers)
avengers.insert(0,'Captain America')
print(avengers)
avengers.remove('Hulk')
print(avengers)
avengers.insert(2,'Hulk')
print(avengers)

scores = [92, 85, 76, 58, 89, 91, 73, 84]
print(scores[0])  #score of first student
print(scores[-1]) #score of last student
print(scores[:3]) #score of first 3 students
print(scores[2:5]) #score of roll 3 , 4 and 5
scores.append(83)
print(scores)







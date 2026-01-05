import json

data = {'tom': {
    'name': 'tom',
    'age': 18,
    'phone': 45612313},
    'james': {
        'name': 'james',
        'age': 22,
        'phone': 123456
    }}

f= open(r'C:\Users\ashok\OneDrive\Desktop\change.txt', 'r')
for line in f:
    total=line.split(' ')  #here we are splitting the line from the given file at space
    print(len(total))   #as the line.split(' ') splits the line at space and gives us an array
    #its length gives us the total number of words
f.close()


with open(r'C:\Users\ashok\OneDrive\Desktop\change.txt', 'r') as f:  #while using with we donot need to close like above
    for line in f:
        print(line)



def areaofshape(base,height,shape):
    multiplication = base * height
    if shape == "rectangle":
        return multiplication
    return (1/2) * multiplication


def  print_pattern(n):
    for i in range(1,n+1):
        print('*' * i)
print_pattern(4)

#dict and tuples

data = {'China':143,'India':136,'USA':32,'Pakistan':21}
random = [k.lower() for k in data.keys()]   #here we are making the keys of the data dict into lowercase
a=input('Enter something:')
if a.lower() =='print':
    for num in data:
       print(num+'==>'+str(data[num]))
elif a.lower() == 'add':
    question = input('Enter the name of country')
    if question.lower() in random:
        print(f'{question} already exists')
    else:
        question2=int(input('Enter the population'))
        data[question] = question2
        print(f'{data[question]} : {question2}')

elif a.lower() == 'remove':
    country = input('Enter the name of country')
    countryToRemove=None
    if country.lower() in random:
        for key in data:
            if key.lower() == country.lower():    #if the lowercase of the key in the given dict matches with the input
                countryToRemove=key
        del data[countryToRemove] #deleting with the country to be removed key
    else:
        print('This country does not exist')
elif a.lower()=='query':
    country = input('Enter the name of country')
    if country.lower() not in random:
        print(f'{country} does not exist')
    else:
        for key in data:
            if key.lower() == country.lower():  # if the lowercase of the key in the given dict matches with the input
                print(f'{key}:{data[key]}')





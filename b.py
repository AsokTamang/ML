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



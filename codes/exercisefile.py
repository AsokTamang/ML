data={}
with open("C:/Users/ashok/OneDrive/Desktop/customers.txt",'r') as f:
    for line in f.readlines():
     name,money=line.split(',')
     data[name]=int(money)
print(data)


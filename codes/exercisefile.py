data={}
with open("C:/Users/ashok/OneDrive/Desktop/customers.txt",'r') as f:
    for line in f.readlines():
     name,money=line.split(',')
     data[name]=int(money)
print(data)

def calculate_rewards(total):
    if 100<=total<=199:
        return 'Bronze'
    elif 200<=total<=499:
        return 'Silver'
    elif total>499:
        return 'Gold'

customers_summary = {}
for key,value in data.items():
    if 100<=value<=199:
        customers_summary[key]=(value,'Bronze')
    elif 200 <= value <= 499:
        customers_summary[key]=(value,'Silver')
    else:
        customers_summary[key] = (value, 'Gold')
print(customers_summary)

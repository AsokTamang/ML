with open("C:/Users/ashok/OneDrive/Desktop/change.txt",'r') as f:
     print(f.readlines())  #reading multiple lines
with open ("C:/Users/ashok/OneDrive/Desktop/expenses.txt",'w') as f:
     f.writelines(['I love to code\n','I love python and javascript']) #here \n is for line separator
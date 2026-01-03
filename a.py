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















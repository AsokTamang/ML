with open("C:/Users/ashok/OneDrive/Desktop/change.txt",'r') as f:
     print(f.readlines())  #reading multiple lines


#calculating the total points scored by players in whole tournament
with open("C:/Users/ashok/OneDrive/Desktop/change.txt",'r') as f:
    next(f)  #here we are skipping the very first line cause the very first line consists of the headings
    lines = f.readlines()
    data = {}
    for line in lines:
        line.strip()  #removing empty space from the beginning and the end of the line
        name,id,score = line.split('\t')
        if name in data:
            data[name].append(int(score))
        else:
            data[name]=[int(score)]
    #calculating the highest score,lowest score and average score which helps to determing the best players, average players and worst players
    for k,v in data.items():
        highest = max(v)
        lowest = min(v)
        avg=sum(v)/len(v)
        print(f'{k}==>highest score:{highest},lowest score:{lowest},average score:{avg}')


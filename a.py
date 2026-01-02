def calculateaverage(lst):
    return sum(lst)/len(lst)

stock_price={'info':[600,630,620],'ril':[1430,1490,1567],'mtl':[234,180,160]}
question = input('Enter your order: ')
if question.lower() == 'print':
   for data in stock_price:
       print(f'{data} ==> {calculateaverage(stock_price[data])}')
elif question.lower() == 'add':
    stockname=input('Enter the name of your stock')
    pricevalue = int(input('Enter the price of your stock'))
    if stockname.lower() in stock_price:

        stock_price[stockname].append(pricevalue)    #appending with the value from stock price
        print(stock_price[stockname])
    else:
        stock_price[stockname]=[pricevalue]  #if the stock name doesnot exist then we just create new pair for this







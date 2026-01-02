def calculateaverage(lst):
    return sum(lst)/len(lst)

stock_price={'info':[600,630,620],'ril':[1430,1490,1567],'mtl':[234,180,160]}
question = input('Enter your order: ')
if question.lower() == 'print':
   for data in stock_price:
       print(f'{data} ==> {calculateaverage(stock_price[data])}')




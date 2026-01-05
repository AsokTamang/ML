apples_revenue = {
    'USA':{
        'iphone':20,
        'ipad':12,
        'macbook':8
    },
    'China': {
        'iphone': 17,
        'ipad': 9,
        'macbook': 7
    },
'Nepal': {
        'iphone': 9,
        'ipad': 4,
        'macbook': 2
    }
}
for country,v in apples_revenue.items():  #printing the price of iphone only
  for k,val in v.items():
      print(f'{k}:{val}')

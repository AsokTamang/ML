#so we can also pass numerous key-value pair as arguments which is called kwargs, which is key-word arguments
def findTotal(*args):
    total=0
    for num in args:
        total+=num
    return total
print(findTotal(1,2,3,4,5))


#key-word arguments
def findkv(**kwargs):
    for key,value in kwargs.items():
        print(f' {key} : {value} ')
(findkv(name='Asok',Age='24'))


#name stores the name of current module and
#main indicates that this module or file is being executed directly
#otherwise if the below function is running in another file by importing this module then we get the name of this file instead not as a main
#cause its not being directly ran
def calculate_area(radius):
    print(__name__)  #this prints the name of
    print(f'Area is :{3.14 * radius **2}')
if __name__=='__main__':
    calculate_area(5)
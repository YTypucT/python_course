name = input ('Enter your first name: ')
age = int (input('Enter your age: '))

def main ():
    func_1(name)
    func_2(age)

def func_1 (name):
    print ('Hello ' + name + '!')

def func_2 (age):
    print ('Your age is '+ str(age) + '!')

main()
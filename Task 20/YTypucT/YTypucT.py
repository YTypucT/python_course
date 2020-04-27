def main ():
    num_1 = func_1(int(input('Enter 1st number:')), int(input('Enter 2nd number:')))
    str_1 = func_2(input('Enter any line:'))
    print (num_1)
    print (str_1)

def func_1(a, b):
    return a ** b

def func_2(str_1):
    return str_1 + "!"

main()
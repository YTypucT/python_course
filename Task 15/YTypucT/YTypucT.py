list = [13, 1313, 131313, 666]

for num in list:
    if num > 5000: 
        print('Num ' + str(num) +  ' greater than 5000')
        continue
        print(':c')
    else: print('Num less than 5000')

for num in list:
    if num == 1313:
        print('The number of found')
        break
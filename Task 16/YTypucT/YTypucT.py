num_1 = 10
num_2 = 0

while num_1 > 0:
    print(num_1)
    num_1 -= 1
else: print('Cycle completed')

while num_2 != 10 or num_2 == 9:
    if num_2 > 4:
        print('Cool', num_2)
    if num_2 == 8:
        print('8. exit.')
        break
    num_2 += 1


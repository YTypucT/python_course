number_1 = 903

if number_1 > 0 and number_1 * 3 <= 1500 and number_1 - 3 != 800:
    print('''Будет выполнено только в случае,
     если (число number_1 больше нуля) И (число number_1 * 3 меньше ИЛИ равно 1500) И
     (число number_1 - 3 не равно 800)
    ''')

if number_1 == 404 and number_1 < 500 and not(number_1 >= 2900):
    print('''Будет выполнено только в случае,
     если (число number_1 равно 404) И (число number_1 меньше 500) И (НЕ
     (число number_1 больше ИЛИ равно 2900))
    ''')
else: 
    print(':c')

if number_1 > -1 or number_1 + 40 > 30:
    print('Будет выполнено если (number_1 больше -1) ИЛИ (number_1 + 40 больше 30)')

if number_1 > 0 or number_1 != 300 or not(number_1 == 400):
    print('Будет выполнено если (number_1 больше 0) ИЛИ (number_1 не равно 300) ИЛИ (НЕ(number_1 равно 400))')
else:
    print(':c')

number_2 = 60

if number_2 > 0:
    if number_2 * 3 <= 1500:
        print('Число number_2 больше 0 И number_2 * 3 меньше ИЛИ равно 1500')
    else:
        print('Число number_2 больше 0, НО number_2 * 3 НЕ МЕНЬШЕ 1500 ИЛИ НЕ РАВЕН 1500')
else:
    print('Число number_2 не больше 0')

if number_2 != 30 and number_2 > 1 or number_2 == number_2:
    print('(number_2 не равно 30) И (number_2 больше 1) ИЛИ (number_2 равно number_2')
else:
    if number_2 == number_1 or number_1 * 5 < -30:
        print('В случае если перечисленные выше условия не были соблюдены, НО (number_2 равно number_1) ИЛИ (number_1 * 5 меньше -30)')
    else:
        print('В случае если НИ ОДНО из перечисленных выше условий не было соблюдено')

'''
В зависимости от контекста используйте разные подходы к решению либо через вложенность либо через 
логические операторы and, or, not (аналог not - восклицательный знак перед выражением, которое нужно
отрицать) либо используя их комбинации
'''
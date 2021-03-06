# Задание 17: Знакомство с циклами (for, while) Часть 4.1

#### Содержание:

+ [Теоретические материалы](#THEORETICAL_MATERIALS)
+ [Задание](#TASK)
+ [Дополнительные материалы](#ADDITIONAL_MATERIALS)
+ [При возникновении проблем](#ISSUES)

#### <a name="THEORETICAL_MATERIALS"></a> 1. Теоретические материалы



#### <a name="TASK"></a> 2. Задание

Создайте список `spisok_1`:

* *первым* элементом списка `spisok_1` является список, содержащий *3* элемента, каждый элемент списка является любым положительным целым числом
* *вторым* элементом списка `spisok_1` является список, содержащий *2* элемента, каждый элемент списка является произвольной строкой

Создайте переменную `number_1`, присвойте ей любое положительное целое число

Создайте переменную `number_2`, присвойте ей значение равное результату сложения значения переменной `number_1` и числа `5`

Создайте переменную `stroka_1`, присвойте ей любое строковое значение

Создайте многоуровневый цикл `for`: 

```
for переменная in множество:
    блок инструкций, в том числе и вложенные циклы
```

* в качестве *переменной* цикла используйте переменную: `spisok`
* в качестве *множества* цикла используйте список: `spisok_1`
* в качестве *блока инструкций* цикла используйте *вложенный цикл for*:
    * в качестве *переменной вложенного* цикла используйте переменную: `element`
    * в качестве *множества вложенного* цикла используйте значение переменной: `spisok`
    * в качестве *блока инструкций вложенного* цикла используйте следующий код: `print(element)`

```python
# Образец кода: 
for spisok in spisok_1:
    for element in spisok:
        print(element)
```

Создайте переменную `number_3`, присвойте ей значение равное `0`

Создайте многоуровневый цикл `while`: 

```
while условие(я):
    блок инструкций, в том числе и вложенные циклы
```

* в качестве *условия(ий)* цикла используйте следующие утверждения:
    * значение переменной `number_3` должно быть **меньше** числа `2`
* в качестве *блока инструкций* цикла используйте *вложенный цикл for* и операцию увеличения значения переменной `number_3` на `1`:
    * в качестве *переменной вложенного* цикла *for* используйте переменную: `element`
    * в качестве *множества вложенного* цикла *for* используйте значение элемента списка `spisok_1`, имеющего индекс равный значению переменной `number_3` 
    * в качестве *блока инструкций вложенного* цикла *for* используйте следующий код: `print(element)`
* последней командой в *блоке инструкций* цикла используйте следующий код: `number_3+=1`

Например:

```python
# Образец кода: 
while number_3 < 2:
    for element in spisok_1[number_3]:
        print(element)
    number_3+=1
```

* Образец решённого задания находится в папке <a href="./welpodron">`welpodron`</a> - файл <a href="./welpodron/welpodron.py">`welpodron.py`</a>

#### <a name="ADDITIONAL_MATERIALS"></a> 3. Дополнительные материалы



#### <a name="ISSUES"></a> Есть вопрос?

Свяжитесь с автором проекта: [welpodron](https://vk.com/welpodron)

> @welpodron 2020
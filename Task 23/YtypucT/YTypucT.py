num_1 = 69
str_1 = "It's a line"
list_1 = ["It's a list"]
dict_1 = {69: "it's a dictionary"}

print(type(num_1), type(str_1), type(list_1), type(dict_1))

class Animal:
    def __init__(self):
        print('Animal class constructor')

cat = Animal()

print(type(cat))
print(cat)
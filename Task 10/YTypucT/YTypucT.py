num_1 = 13
str_1 = "it's a string"
list_1 = ["it's a string in the list"]
dict_1 = {
    num_1 : 666,
    "it's a key" : str_1,
    num_1 + 50 : num_1,
    str_1[0] : list_1,
    str_1 : list_1[0],
    69 : 69
}
num_2 = dict_1[num_1]
print(num_2)
print(dict_1)
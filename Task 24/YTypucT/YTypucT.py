class Animal:
    def __init__(self, name, color, type = 'Animal'):
        self.name = name
        self.color = color
        self.type = type
    def out(self):
        print ("It's a %s. It's name %s. It's a %s." % (self.type, self.name, self.color))

cat_1 = Animal(input('Enter name: '), input('Enter color: '), input('Enter type: '))
cat_1.out()

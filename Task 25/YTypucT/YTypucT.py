class Animal:
    def __init__(self, kind):
        self.kind = kind
    def info(self):
        print ("It's an %s" % (self.kind))

class Bird:
    def __init__(self, kind):
        self.kind = kind
    def info(self):
         print ("It's a %s." % (self.kind))

class Cat(Animal):
    def __init__(self, name, color, kind = "Animal"):
        super().__init__(kind)
        self.__name = name
        self.__color = color

class Parrot(Bird):
    def __init__(self, name, color, kind = "Bird"):
        super().__init__(kind)
        self.__name = name
        self.__color = color

cat = Cat('Bars', 'Green')
parrot = Parrot ('Popka', 'Red')
cat.info()
parrot.info()
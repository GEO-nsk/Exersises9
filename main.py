'''
class Robot:
    pass

r = Robot()
# print(type(r))

a = 5
#print(type(a))

#print(isinstance(a, int))
#print(isinstance(a, Robot))

#print(dir(Robot))

d =[]
for i in range(5):
    d.append(Robot())

print(d)
'''


class Robot:
    elem = []

    def __new__(cls, *args, **kwargs):
        # print('это я __new__')
        obj = super().__new__(cls)
        return obj

    def __init__(self, number):
        self.number = number
        # print('а это я __init__')
        Robot.elem.append(self)
        Robot.say()
        self.__power == 100

    power = property

    @power.setter
    def power(self, value):
        self.__power = value

    @power.getter
    def power(self):
        return self.__power

    @power.deleter
    def power(self):
        del self.__power

    def __repr__(self):
        return f'Робот №{self.number}'

    def __str__(self):
        return f'Робот №{self.number}'

    @classmethod
    def deuble(cls):
        n = len(cls.elem)
        for i in range(n):
            cls.elem[i].number *= 2

    @staticmethod
    def say():
        print('Rrr-rr--r-r--rr!!')


d = []
for i in range(5):
    d.append(Robot(i))

# print(d)
# print(d[2])
# print(d[3].number)

d[3].num = d[3].number * 2
del d[3].num
print(d[3].num)

print((Robot.elem))
Robot.deuble()
Robot.deuble()
print(Robot.elem)


class Pet:
    def __init__(self, name=None):
        self.name = name


class Dog(Pet):
    def __init__(self, name, breed=None):
        super().__init__(name)
        self.breed = breed

    def say(self):
        return f'{self.name}: Гав!'


dog = Dog('Шарик', 'Доберман')
print(dog.name, dog.breed)
print(dog.say())
class Dog:
    '''
    class of dog

    parameters:
    name - name of dog
    '''
    def __init__(self, name):
        self.name = name

    def say(self):
        '''
        function teachs our dog how to bark
        '''
        return f'{self.name}: Гав!'

dog = Dog('Шарик')
print(dog.say())
class NotSleeping:
    '''
    class of someone who wants sleep

    parameters:
    sheep - number of counted sheeps
    '''

    def __init__(self):
        self.sheep = 0

    def add_Sheep(self):
        '''
        function adds 1 sheep
        '''
        self.sheep += 1

    def __repr__(self):
        return f'количество овец: {self.sheep}'

sleep = NotSleeping()

for itr in range(1,10):
    sleep.add_Sheep()

print(sleep)
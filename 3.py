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

    def lost(self):
        '''
        function rests to zero number of sheeps
        '''
        self.sheep = 0

    def get_count_sheeps(self):
        '''
        function prints current number of sheeps
        :return:
        '''
        print(self.sheep)

    def __repr__(self):
        return f'количество овец: {self.sheep}'

sleep = NotSleeping()

for itr in range(1,10):
    sleep.add_Sheep()

sleep.lost()

sleep.add_Sheep()

sleep.get_count_sheeps()
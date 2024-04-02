import random

doc = {'command1': 0, 'command2': 0}

class Game:
    '''
    class of basketball game

    parameters:
    doc - dictionary with 2 commands and their score
    '''
    def __init__(self, doc):
        self.doc = doc

    def ball_thrown(self, command, points):
        '''
        function adds points to selected command

        :param command: number of commend
        :param points: number of points
        '''
        command_num = 'command' + command
        doc[command_num] += points

    def get_score(self):
        '''
        function returns tuple with command's score
        '''
        s = [doc['command1'], doc['command2']]
        return tuple(s)

    def get_winner(self):
        '''
        function returns name of command that wins
        :return:
        '''
        if doc['command1'] > doc['command2']:
            return 'command1'
        if doc['command1'] < doc['command2']:
            return 'command2'
        if doc['command1'] == doc['command2']:
            return 'Ничья'


game1 = Game(doc)

for itr in range(20):
    game1.ball_thrown(str(random.randint(1,2)), random.randint(2,3))
    print(game1.doc)

print(game1.doc)
print(game1.get_score())
print(game1.get_winner())


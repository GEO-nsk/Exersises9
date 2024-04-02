class User:
    '''
    class of user

    parameters:
    id - number
    nick_name - not real name
    first_name - name of user
    last_name - last name of user
    middle_name - middle name of user
    gander - user's gender
    '''

    def __init__(self, id, nick_name, first_name, last_name=None, middle_name=None, gender=None):
        self.id = id
        self.nick_name = nick_name
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.gender = gender

    def __str__(self):
        return f'пользователь {self.id} ник-нэйм: {self.nick_name} имя: {self.first_name} фамилия: {self.last_name} отчество: {self.middle_name} пол: {self.gender}'


user1 = User(1, 'topshotta', 'NLE', 'Choppa', gender='man')

print(user1)
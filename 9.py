new_strands = ['CABBV', 'BACED', 'BABA']
strands = 'BUNF AADAC'

class StrandsDNA:
    '''
    calss of DNA

    parameters:
    all_strands - all strands in DNA
    '''

    def __init__(self, all_strands):
        self.all_strands = all_strands

    def add_strands(self,strands):
        '''
        function adds new strands to existed

        :param strands: new strands to add
        '''
        for itr in strands.split():
            self.all_strands.append(itr)

    def get_max_strands(self):
        '''
        function returns str with max strands
        '''
        s = []

        for itr in self.all_strands:
            s.append(len(itr))

        max_len = max(s)
        max_strands_list = []
        max_strands = ''

        for itr in self.all_strands:
            if len(itr) == max_len and itr not in max_strands_list:
                max_strands_list.append(itr)
        max_strands_list.sort()

        for itr in max_strands_list:
            max_strands += itr
            max_strands += ' '

        return max_strands


DNA1 = StrandsDNA(new_strands)
print(DNA1.all_strands)

DNA1.add_strands(strands)
print(DNA1.all_strands)

print(DNA1.get_max_strands())

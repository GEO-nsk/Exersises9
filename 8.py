morze_eng = {'a': '•—', 'b': '—•••', 'c': '—•—•', 'd': '—••',
         'e': '•', 'f': '••—•', 'g': '——•', 'h': '••••',
         'i': '••', 'j': '•———', 'k': '—•—', 'l': '•—••',
         'm': '——', 'n': '—•', 'o': '———', 'p': '•——•',
         'q': '——•—', 'r': '•—•', 's': '•••', 't': '—',
         'u': '••—', 'v': '•••—', 'w': '•——', 'x': '—••—',
         'y': '—•——', 'z': '——••'}

morze_ru = {'а': '.-', 'б': '-...','в': '.--', 'г': '--.', 'д': '-..','е': '.','ж': '...-',
              'з': '--..', 'и': '..', 'й': '.---', 'к': '-.-', 'л': '.-..' , 'м': '--', 'н': '-.',
              'о': '---', 'п': '.--.', 'р': '.-.', 'с': '...', 'т': '-', 'у': '..-', 'ф': '..-.',
              'х': '....', 'ц': '-.-.', 'ч': '---.', 'ш': '----', 'щ': '--.-' , 'ъ': '.--.-.',
              'ь': '-..-', 'э': '..-..', 'ю': '..--' , 'я': '.-.-'}

messege = str(input())

class MorseMsg:
    '''
    class that can work with morse masseges

    parameters:
    massege - str with massege in morse
    '''

    def __init__(self, messege):
        self.messege = messege

    def eng_decode(self):
        '''
        functions prints massege in english
        '''
        ptr = ''
        for itr in messege.split():
            for key, value in morze_eng.items():
                if itr == value:
                    ptr += key
        return ptr

    def ru_decode(self):
        '''
        functions prints massege in russian
        '''
        ptr = ''
        for itr in messege.split():
            for key, value in morze_ru.items():
                if itr == value:
                    ptr += key
        return ptr

    def get_vowels(self, lang):
        '''
        function returns only vowels

        :param lang: english or russian
        '''
        ptr = ''

        if lang == 'eng':
            for itr in messege.split():
                for key, value in morze_eng.items():
                    if itr == value:
                        if key == 'a' or key == 'e' or key == 'i' or key == 'o' or key == 'u' or key == 'y':
                            ptr += key
            return ptr
        else:
            for itr in messege.split():
                for key, value in morze_ru.items():
                    if itr == value:
                        if key == 'а' or key == 'е' or key == 'ё' or key == 'и' or key == 'о' or key == 'у' or key == 'э' or key == 'ю' or key == 'я':
                            ptr += key
            return ptr

    def get_consonants(self, lang):
        '''
        function returns only consonants
        
        :param lang: english or russian
        '''
        ptr = ''

        if lang == 'eng':
            for itr in messege.split():
                for key, value in morze_eng.items():
                    if itr == value:
                        if key != 'a' and key != 'e' and key != 'i' and key != 'o' and key != 'u' and key != 'y':
                            ptr += key
            return ptr
        else:
            for itr in messege.split():
                for key, value in morze_ru.items():
                    if itr == value:
                        if key != 'а' and key != 'е' and key != 'ё' and key != 'и' and key != 'о' and key != 'у' and key != 'э' and key != 'ю' and key != 'я':
                            ptr += key
            return ptr

messege1 = MorseMsg(messege)

print(messege1.get_consonants('eng'))
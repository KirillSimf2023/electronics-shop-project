from src.item import Item


class Mixlanguage():


    def __init__(self):
        self.__language = 'EN'


    def change_lang(self):
        if self.__language == 'EN':
            self.__language = 'RU'
            return self
        else:
            self.__language = 'EN'
            return self
    @property
    def language(self):
        return self.__language


class KeyBoard(Item, Mixlanguage):
    pass


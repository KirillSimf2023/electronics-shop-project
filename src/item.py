import csv
import os

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []
    CSV = os.path.abspath('../src/items.csv')

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    #Геттер для name
    @property
    def name(self) -> str:
        return f'{self.__name}'

    #Cеттер для name
    @name.setter
    def name(self, add_name):
        if len(add_name) > 10:
            raise Exception('Длина наименования товара превышает 10 символов')
        else:
            self.__name = add_name


    #класс-метод, инициализирующий экземпляры класса Item данными
    # из файла src/items.csv
    @classmethod
    def instantiate_from_csv(cls):
        cls.all.clear()
        try:
            with open(cls.CSV, newline='', mode='r', encoding='cp1251') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    cls(row['name'], row['price'], row['quantity'])
        except FileNotFoundError:
            print("Файл не найден")


    #статический метод, возвращающий число из числа-строки
    @staticmethod
    def string_to_number(number_string: str) -> int:
        return int(float(number_string))

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price*self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price=self.price*self.pay_rate


    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"


    def __str__(self):
        return f"{self.__name}"
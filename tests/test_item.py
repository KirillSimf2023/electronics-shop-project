"""Здесь надо написать тесты с использованием pytest для модуля item."""

from src.item import Item

def test_calculate_total_price():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000
    assert Item.pay_rate == 1
    Item.pay_rate = 0.8
    assert Item.pay_rate == 0.8

def test_apply_discount():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    Item.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 8000
    assert item2.price == 20000
    item2.apply_discount()
    assert item2.price == 16000

#Test для Домашнего задания №2
def test_HW_2():
    Item.instantiate_from_csv()  # создание объектов из данных файла
    assert len(Item.all) == 5  # в файле 5 записей с данными по товарам

    assert Item.all[0].name == 'Смартфон' # в записи с индексом 0 с данными по товарам имя 'Смартфон'
    assert Item.all[4].name == 'Клавиатура' # в записи с индексом 0 с данными по товарам имя 'Клавиатура'

    #Проверяем гуттер и сеттер
    item = Item('Ноутбук', 1000, 3)
    item.name = 'Смартфон' #проверка сеттера
    assert item.name == 'Смартфон' #проверка геттера

    #проверка на превышение длины в 10 симфолов.
    try:
        item.name = "СуперСмартфон"
    except Exception:
        print('Длина наименования товара превышает 10 символов')

    #проверка staticmethod
    assert Item.string_to_number('15') == 15
    assert Item.string_to_number('50.0') == 50
    assert Item.string_to_number('15.6') == 15

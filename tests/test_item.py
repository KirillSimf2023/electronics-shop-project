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
    item2.apply_discount()
    assert item1.price == 8000
    assert item2.price == 16000









#
# def test_apply_discount():
#     assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
#     assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
#     assert arrs.my_slice([1, 2, 3], -5) == [1, 2, 3]
#     assert arrs.my_slice([], -2) == []
#     assert arrs.my_slice([1, 2, 3], -1) == [3]
#

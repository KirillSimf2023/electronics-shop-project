from src.phone import Phone
import pytest

@pytest.fixture
def make_phone():
    return Phone("iPhone 14", 120_000, 5, 2)

def test_init(make_phone):
    # смартфон iPhone 14, цена 120_000, количество товара 5, симкарт 2
    phone1 = make_phone
    assert phone1.name == 'iPhone 14'
    assert phone1.price == 120000
    assert phone1.quantity == 5
    assert phone1.number_of_sim == 2

def test_str(make_phone):
    phone1 = make_phone
    assert str(phone1) == 'iPhone 14'
    phone1 = Phone("Samsung", 80_000, 10, 2)
    assert str(phone1) == 'Samsung'

def test_repr(make_phone):
    phone1 = make_phone
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"
    phone2 = Phone("Samsung", 80_000, 10, 2)
    assert repr(phone2) == "Phone('Samsung', 80000, 10, 2)"

def test_number_of_sim(make_phone):
    phone1 = make_phone
    assert phone1.number_of_sim == 2

    with pytest.raises(ValueError):
        phone2 = Phone('IQ', 25_000, 2, -1)

    with pytest.raises(ValueError):
        phone1.number_of_sim = 0






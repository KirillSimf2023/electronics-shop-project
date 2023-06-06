"""Здесь надо написать тесты с использованием pytest для модуля KeyBoard."""
from src.keyboard import KeyBoard
from pytest import fixture, raises


@fixture
def make_keyboard():
    return KeyBoard('Dark Project KD87A', 9600, 5)


def test_KeyBoard_init(make_keyboard):
    assert str(make_keyboard) == "Dark Project KD87A"
    assert make_keyboard.price == 9600
    assert make_keyboard.quantity == 5


def test_KeyBoard_change_lang(make_keyboard):
    assert make_keyboard.language == "EN"
    make_keyboard.change_lang()
    assert make_keyboard.language == "RU"
    make_keyboard.change_lang().change_lang()
    assert make_keyboard.language == "RU"

    with raises(AttributeError):
        make_keyboard.language = "CH"



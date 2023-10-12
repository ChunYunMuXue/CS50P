from project import get_random_word, guess_word, game_over
import pytest

def test_get_random_word():
    assert get_random_word() in [
        "Apple",
        "Bread",
        "Cloud",
        "Dance",
        "Early",
        "Adder",
        "Grape"
    ]



def test_guess_word():
    with pytest.raises(ValueError):
        guess_word(range(114514))


def test_game_over():
    with pytest.raises(ValueError):
        game_over('world','world',3)    
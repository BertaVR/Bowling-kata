from src.bowling import Bowling

def test_todo_numeros():
    assert Bowling("11111111111111111111").Calcular_puntuacion() == 20
    assert Bowling("12345123451234512345").Calcular_puntuacion() == 60

def test_numeros_y_nulos():
    assert Bowling("9-9-9-9-9-9-9-9-9-9-").Calcular_puntuacion() == 90
    assert Bowling("9-3561368153258-7181").Calcular_puntuacion() == 82


def test_strike_tirada_normal():
    assert Bowling("X1111111111111111111").Calcular_puntuacion() == 31

def test_strikes_nulos_num():
    assert Bowling("71X713-2634X334311").Calcular_puntuacion() == 83
    assert Bowling("X9-9-9-9-9-9-9-9-9-").Calcular_puntuacion() == 100
    assert Bowling("XXX9-9-9-9-9-9-9-").Calcular_puntuacion() == 141


from src.bowling import Bowling

def test_todo_numeros():
    assert Bowling("11111111111111111111").Calcular_puntuacion() == 20
    assert Bowling("12345123451234512345").Calcular_puntuacion() == 60

def test_numeros_y_nulos():
    assert Bowling("9-9-9-9-9-9-9-9-9-9-").Calcular_puntuacion() == 90

def test_Strike_tirada_normal():
    assert Bowling("X1111111111111111111").Calcular_puntuacion() == 31

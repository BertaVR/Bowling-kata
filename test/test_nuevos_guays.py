from src.bowling import Puntuacion_total_bolos






def test_todo_numeros():
    assert Puntuacion_total_bolos("11111111111111111111").puntuacion_partida() == 20
    assert Puntuacion_total_bolos("12345123451234512345").puntuacion_partida() == 60

def test_numeros_y_nulos():
    assert Puntuacion_total_bolos("9-9-9-9-9-9-9-9-9-9-").puntuacion_partida() == 90
    assert Puntuacion_total_bolos("9-3561368153258-7181").puntuacion_partida() == 82

def test_spare_tirada_normal():
    assert Puntuacion_total_bolos("5/5/5/5/5/1111111111").puntuacion_partida() == 81

def test_strike_tirada_normal():
    assert Puntuacion_total_bolos("X111111111111111111").puntuacion_partida() == 30

def test_strikes_nulos_num():
    assert Puntuacion_total_bolos("71X713-2634X334311").puntuacion_partida() == 83
    assert Puntuacion_total_bolos("X9-9-9-9-9-9-9-9-9-").puntuacion_partida() == 100
    assert Puntuacion_total_bolos("X9-X9-9-9-9-9-9-9-").puntuacion_partida() == 110
    assert Puntuacion_total_bolos("XXX9-9-9-9-9-9-9-").puntuacion_partida() == 141

def test_bolas_extra():
    assert Puntuacion_total_bolos("8/549-XX5/53639/9/X").puntuacion_partida() == 149
    assert Puntuacion_total_bolos("9-9-9-9-9-9-9-9-9-XXX").puntuacion_partida() == 111
    assert Puntuacion_total_bolos("X5/X5/XX5/--5/X5/").puntuacion_partida() == 175

def test_nulo_y_spare():
    
    assert Puntuacion_total_bolos("-/X1111111111111111").puntuacion_partida() == 48


def test_partida_perfecta():
    assert Puntuacion_total_bolos("XXXXXXXXXXXX").puntuacion_partida() == 300
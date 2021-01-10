
class Bowling:

    def __init__(self, tabla_tiradas):
        self.tabla_tiradas = tabla_tiradas
        self.numero_estandar_tiradas = 20 #entendemos como número estándar de tiradas una partida en la que no hay strikes. Esto será útil porque definiremos como última tirada (que tiene un algoritmo diferente para el puntaje) la 20. Jugaremos con el contador de tiradas para que aunque haya strikes la última caiga en 20 (esto es, si hay strike aunque en realidad tiramos solo una vez, lo contamos como 2 tiradas)
        self.max_bolos = 10
        self.numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.strike = 'X'
        self.nulo = '-'
        self.spare= '/'

    def Equivalencias_puntaje_signo(self, posicion_signo):
        if self.tabla_tiradas[posicion_signo] in self.numeros:
            puntaje = int(self.tabla_tiradas[posicion_signo])
        elif self.tabla_tiradas[posicion_signo] == self.strike:
            puntaje = self.max_bolos
        elif self.tabla_tiradas[posicion_signo] == self.nulo:
            puntaje = 0
        elif self.tabla_tiradas[posicion_signo] == self.spare:
            puntaje = self.max_bolos - self.tabla_tiradas[posicion_signo - 1]
        return puntaje


    @staticmethod
    def Open(puntuacion_tirada):
        puntuacion_open = int(puntuacion_tirada)
        return puntuacion_open


    def Strike_Puntuacion(self, posicion_actual):
        tirada_actual = self.max_bolos
        primera_siguiente = Bowling.Equivalencias_puntaje_signo(self, posicion_actual + 1)
        segunda_siguiente = Bowling.Equivalencias_puntaje_signo(self, (posicion_actual + 2))

        puntos_strike = tirada_actual + primera_siguiente + segunda_siguiente
        return puntos_strike


    def Calcular_puntuacion(self):
        puntuacion_total = 0
        contador_tiradas = 0
        posicion_actual = 0
        while contador_tiradas < 20: ###todas las tiradas excepto la última
            for puntuacion_tirada in self.tabla_tiradas:
                        ####NULO#### - simplemente seguimos con contador 
                if puntuacion_tirada == self.nulo:
                    contador_tiradas += 1 #no sumamos nada a la puntuación
                    posicion_actual += 1
                        #####NORMAL(numero)#### -actualizamos contador y sumamos numero de bolos al puntaje total
                elif puntuacion_tirada.isdigit() == True:
                    puntuacion_total += Bowling.Open(puntuacion_tirada)                    
                    contador_tiradas += 1
                    posicion_actual += 1
                        ####SPARE#### - 
                elif puntuacion_tirada == self.spare:
                    contador_tiradas += 1
                    posicion_actual += 1 
                elif puntuacion_tirada == self.strike:
                    puntuacion_total +=  Bowling.Strike_Puntuacion(self, posicion_actual)
                    contador_tiradas += 2 #aquí se suma otro(porque queremos que llegue hasta un numero fijo de tiradas, 20, independientemente de que se tiren menos porque se hacen strikes), no se suman los dos a la vez porque si no es un lío a la hora de calcular los puntos siguientes.
                    posicion_actual += 1


        return puntuacion_total

if __name__ == "__main__":
    #assert Bowling("11111111111111111111").Calcular_puntuacion() == 20
    #assert Bowling("X1111111111111111111").Calcular_puntuacion() == 31
    assert Bowling("XXX9-9-9-9-9-9-9-").Calcular_puntuacion() == 141

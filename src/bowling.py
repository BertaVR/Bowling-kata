
class Bowling:

    def __init__(self, tabla_tiradas):
        self.tabla_tiradas = tabla_tiradas
        self.numero_estandar_tiradas = 20 #entendemos como número estándar de tiradas una partida en la que no hay strikes. Esto será útil porque definiremos como última tirada (que tiene un algoritmo diferente para el puntaje) la 20. Jugaremos con el contador de tiradas para que aunque haya strikes la última caiga en 20 (esto es, si hay strike aunque en realidad tiramos solo una vez, lo contamos como 2 tiradas)
        self.total_bolos = 10
        self.strike = 'X'
        self.nulo = '-'
        self.spare= '/'


    @staticmethod
    def Open(puntuacion_tirada):
        puntuacion_open = int(puntuacion_tirada)
        return puntuacion_open

    @staticmethod
    def Spare_sumar_uno_siguiente(tabla_tiradas, contador_tiradas):
        sumar_siguiente = int(tabla_tiradas[contador_tiradas + 1])
        return sumar_siguiente


    @staticmethod
    def Strike_sumar_dos_siguientes(tabla_tiradas, contador_tiradas):
        primera_siguiente = int(tabla_tiradas[contador_tiradas + 1])
        segunda_siguiente = int(tabla_tiradas[contador_tiradas + 2])
        suma_strike = primera_siguiente + segunda_siguiente
        return suma_strike


    def Calcular_puntuacion(self):
        puntuacion_total = 0
        contador_tiradas = 0
        while contador_tiradas < 20: ###todas las tiradas excepto la última
            for puntuacion_tirada in self.tabla_tiradas:
                        #####NORMAL(numero)#### -actualizamos contador y sumamos numero de bolos al puntaje total
                if puntuacion_tirada.isdigit() == True:
                    contador_tiradas += 1 
                    puntuacion_total += Bowling.Open(puntuacion_tirada)  
                        ####NULO#### - simplemente seguimos con contador 
                elif puntuacion_tirada == self.nulo:
                    contador_tiradas += 1 #no sumamos nada a la puntuación
                        ####SPARE#### - 
                elif puntuacion_tirada == self.spare:
                    contador_tiradas += 1 
                elif puntuacion_tirada == self.strike: 
                    contador_tiradas += 1 #solo sumo 1, la otra dos lineas más abajo porque si aquí sumara 2 rompería la función de sumar las siguientes tiradas 
                    puntuacion_total += self.total_bolos + Bowling.Strike_sumar_dos_siguientes(self.tabla_tiradas, contador_tiradas)
                    contador_tiradas += 1 #vale, aquí sumamos al contador porque en caso de strike la siguiente tirada no se lleva a cabo. Esto es útil a la hora de saber si nos encontramos en la última tirada, que es especial y la marcamos como 20.

        return puntuacion_total

if __name__ == "__main__":
    #assert Bowling("11111111111111111111").Calcular_puntuacion() == 20
    assert Bowling("X1111111111111111111").Calcular_puntuacion() == 31
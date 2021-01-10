
class Bowling:

    def __init__(self, tabla_tiradas):
        self.tabla_tiradas = tabla_tiradas
        self.numero_estandar_tiradas = 20 #entendemos como número estándar de tiradas una partida en la que no hay strikes. Esto será útil porque definiremos como última tirada (que tiene un algoritmo diferente para el puntaje) la 20. Jugaremos con el contador de tiradas para que aunque haya strikes la última caiga en 20 (esto es, si hay strike aunque en realidad tiramos solo una vez, lo contamos como 2 tiradas)
        self.max_bolos = 10 #no estoy segura de si estoy haciendo el tonto con esto. Supongo que puede ser útil si de repente deciden que se juega a bolos con 15 bolos (??¿)
        ###### los siguientes son para la equivalencia puntaje-signo
        self.numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.strike = 'X'
        self.nulo = '-'
        self.spare= '/'

    def Equivalencias_puntaje_signo(self, posicion_signo):
        if self.tabla_tiradas[posicion_signo] in self.numeros:
            puntaje = int(self.tabla_tiradas[posicion_signo]) #el número tal cual, pero lo inteamos :)
        elif self.tabla_tiradas[posicion_signo] == self.strike:
            puntaje = self.max_bolos #strike vale el maximo de bolos, que son 10
        elif self.tabla_tiradas[posicion_signo] == self.nulo:
            puntaje = 0 #nulo es 0
        elif self.tabla_tiradas[posicion_signo] == self.spare: 
            puntaje = self.max_bolos - int(self.tabla_tiradas[posicion_signo - 1]) #esto es máximo de bolos (10) menos los bolos que ya habías tirado en la ronda anterior, aquí no me tengo que preocupar, ya que lo único que puede haber antes de un spare es un digito
        return puntaje


    @staticmethod
    def Open(puntuacion_tirada):
        puntuacion_open = int(puntuacion_tirada)
        return puntuacion_open


    def Strike_Puntuacion(self, posicion_actual): #llama al método equivalencias puntaje signo y le pasa la posicion siguiente y la segunda siguiente. Todo esto se suma a la puntuación del strike que sería el máximo de bolos, esto es 10.
        tirada_actual = self.max_bolos #10
        primera_siguiente = Bowling.Equivalencias_puntaje_signo(self, posicion_actual + 1) # ¿cuánto vale el signo siguiente?
        segunda_siguiente = Bowling.Equivalencias_puntaje_signo(self, (posicion_actual + 2)) # ¿Cuánto vale el signo de dos posiciones más adelante?

        puntos_strike = tirada_actual + primera_siguiente + segunda_siguiente #suma todo :)
        return puntos_strike
    
    def Spare_Puntuacion(self, posicion_actual):  #Para calcular los bolos tirados en la ronda resta a 10 el puntaje de la posicion anterior (la puntuacion anterior la sabe llamando al metodo de equivalencias y usando como parámetro una posicion menos que la acutal posicion_actual - 1) luego llamando al mismo método calcula el puntaje siguiente (porque se tiene que sumar) y lo suma
        tirada_actual = puntaje = self.max_bolos - Bowling.Equivalencias_puntaje_signo(self, posicion_actual - 1)
        posicion_siguiente = Bowling.Equivalencias_puntaje_signo(self, posicion_actual + 1)

        puntos_spare = tirada_actual + posicion_siguiente 
        return puntos_spare


    def Calcular_puntuacion(self):
        puntuacion_total = 0
        contador_tiradas = 0 #esto es para controlar cuál es la última posicion
        posicion_actual = 0 # Parece absurdo tener un contador de tiradas y otro de posicion pero es importante para luego calcular strikes, spares e historias
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
                if contador_tiradas <18:
                    puntuacion_total += Bowling.Spare_Puntuacion(self, posicion_actual)                    
                    contador_tiradas += 1
                    posicion_actual += 1
                if contador_tiradas >= 18:
                    puntuacion_total +=  Bowling.Equivalencias_puntaje_signo(self, posicion_actual)
                    posicion_actual += 1 #aquí seguir sumando en el contador de tiradas ya es irrelevante
            elif puntuacion_tirada == self.strike:
                if contador_tiradas <18:
                    puntuacion_total +=  Bowling.Strike_Puntuacion(self, posicion_actual)
                    contador_tiradas += 2 #aquí se suma otro(porque queremos que llegue hasta un numero fijo de tiradas, 20, independientemente de que se tiren menos porque se hacen strikes), no se suman los dos a la vez porque si no es un lío a la hora de calcular los puntos siguientes.
                    posicion_actual += 1
                if contador_tiradas >= 18:
                    puntuacion_total += self.max_bolos
                    posicion_actual += 1

    

        return puntuacion_total

if __name__ == "__main__":
    #assert Bowling("11111111111111111111").Calcular_puntuacion() == 20
    #assert Bowling("X1111111111111111111").Calcular_puntuacion() == 31
    assert Bowling("8/549-XX5/53639/9/X").Calcular_puntuacion() == 149

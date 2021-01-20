class Puntuacion_total_bolos:
    ##### defino las constantes en global#######
    ##### cuáles son los símbolos que representan cada tipo de tirada especial (entendiendo por especial la que no es open)
    NULO = '-'
    SPARE = '/'
    STRIKE = 'X'
    ####### máximo de bolos y máximo de turnos 
    MAX_BOLOS = 10
    MAX_TURNOS = 10
    
    def __init__(self, tabla_tiradas):
        self.tabla_tiradas = list(tabla_tiradas)
        self.puntuacion = 0 ######## La puntuación esta se irá actualizando con cada función####
        self.total_tiradas= 0 #### esto es para saber la posición, necesario para calcular las tiradas extra en el spare y el strike
        self.tiradas_por_turno = 0 #necesario para actualizar los turnos, en las puntuaciones open y nulo será necesario para poder actualizar cuando llega el siguiente turno (cuando llegue a 2 sumará 1 turno)
        self.turnos = 1 #este 1 lo pongo para que el frame especial sea el número 10 
        self.ultimo_numero = 0 ##### esto es para calcular la puntuacion del spare restando el último número que ha salido. Se va actualizando en cada open y cada nulo (en spare y strike no porque no puede haber un spare después de un strike o un spare)

    def equivalencias_puntuacion_simbolo(self, lista_tiradas): ###esto no está en el diagrama del modelo pero ha sido necesario añadirlo para implementar la lógica.
        puntuacion = 0
        for tirada in lista_tiradas:
            if tirada == Puntuacion_total_bolos.NULO:
                puntuacion += 0
                self.ultimo_numero = 0
            if tirada.isdigit():
                puntuacion += int(tirada)
                self.ultimo_numero = tirada  ### hay que actualizar el último número
            if tirada == Puntuacion_total_bolos.SPARE:
                puntuacion += Puntuacion_total_bolos.MAX_BOLOS - int(self.ultimo_numero) #int porque detrás de un spare solo puede ir un número (el numero de bolos que has tirado)
            if tirada == Puntuacion_total_bolos.STRIKE:
                puntuacion += Puntuacion_total_bolos.MAX_BOLOS
        return puntuacion



    def puntuacion_partida(self):
        for tirada in self.tabla_tiradas: ###esta función recorre la tabla de tiradas y distribuye: le pasa cada puntuación de tirada a la función correspondiente (open, strike...)
            if self.turnos < Puntuacion_total_bolos.MAX_TURNOS:
                if tirada.isdigit():
                    Puntuacion_total_bolos.puntuacion_open(self, tirada)
                if tirada == Puntuacion_total_bolos.NULO:
                    Puntuacion_total_bolos.puntuacion_nulo(self, tirada)
                if tirada == Puntuacion_total_bolos.SPARE:
                    self.puntuacion += Puntuacion_total_bolos.puntuacion_spare(self)
                if tirada == Puntuacion_total_bolos.STRIKE:
                    self.puntuacion += Puntuacion_total_bolos.puntuacion_strike(self)
                ######FRAME ESPECIAL########## -Lo pasa a una función que simplemente sumará todo de ahí en adelante (tomando las equivalencias ente la puntuación y el símbolo). Cuando el turno sea el 10 (lo he "hackeado un poquito empezando los turnos desde 1 y no desde 0")
            elif self.turnos == Puntuacion_total_bolos.MAX_TURNOS:
                    self.puntuacion += Puntuacion_total_bolos.puntuacion_tenth(self)
                    return self.puntuacion ###esto va aquí pq quiero que se ejecute después de haber contado la última tirada. como sólo necesitamos la puntuación final (y no puntuaciones intermedias) no molesta
            self.total_tiradas += 1 #actualizamos la posición de las tiradas en cada iteración del for


    
    def puntuacion_open(self, tirada):
        self.tiradas_por_turno += 1 ##hemos hecho 1 tirada, la sumamos al turno (esto no lo hacemos en puntuacion_partida() pq por ejemplo los strikes suman diferente)
        self.puntuacion += int(tirada) ##sumar tirada
        if self.tiradas_por_turno == 2: ##cada vez que sea la segunda tirada del turno reiniciamos el contador de tiradas por turno y actualizamos turno sumando 1.
            self.turnos += 1
            self.tiradas_por_turno = 0
        self.ultimo_numero = tirada

    def puntuacion_nulo(self, tirada):
        CERO = 0
        self.puntuacion += CERO ##si es nulo la puntuación es 0
        self.tiradas_por_turno += 1
        if self.tiradas_por_turno == 2: ##cada vez que sea la segunda tirada del turno reiniciamos el contador de tiradas por turno y actualizamos turno sumando 1.
            self.turnos += 1
            self.tiradas_por_turno = 0 ## Aquí no va como constante el 0 porque es diferente, no es 0 por ser nulo, es 0 porque hay que reiniciar el contador cuando llega a 2 
        self.ultimo_numero = CERO            

    
    def puntuacion_spare(self):
        lista_tiradas = self.tabla_tiradas[self.total_tiradas : self.total_tiradas + 2] ##le paso esta tirada y la siguiente a la función que interpreta símbolos
        self.turnos += 1  ##siempre que hay spare es en la segunda tirada, podemmos simplemete actualizar el turno y el contador de tiradas por turno
        self.tiradas_por_turno = 0  
        return Puntuacion_total_bolos.equivalencias_puntuacion_simbolo(self, lista_tiradas)


    def puntuacion_strike(self):
        lista_tiradas = self.tabla_tiradas[self.total_tiradas : self.total_tiradas + 3] ###pasas esta tirada y las 2 siguientes 
        self.turnos += 1 ##siempre que hay strike se salta de turno
        return Puntuacion_total_bolos.equivalencias_puntuacion_simbolo(self, lista_tiradas)

    def puntuacion_tenth(self): ###el nombre tenth puede ser cambiable por última tirada, teniendo en cuenta que se modificaran el número de tiradas que tiene el juego, pero la logica es la misma.
        lista_tiradas = self.tabla_tiradas[self.total_tiradas :] ##pasa de la tirada en adelante y se dedicará solo a sumar simbolitos, sin más lógica.
        return Puntuacion_total_bolos.equivalencias_puntuacion_simbolo(self, lista_tiradas)


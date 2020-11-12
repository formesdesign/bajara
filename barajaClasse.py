import baraja

class Baraja():

    def __init__(self, palos, numeros):
        self.palos = palos
        self.numeros = numeros
        self.mazacote = baraja.creaBaraja(palos, numeros)

    def barajar(self):
        baraja.barajar(self.mazacote)

    def repartir(self, numjugadores, numcartas):
        jugadores = [] #llists buida
        for i in range(numjugadores):
            jugadores.append([])

        for carta in range(numcartas):
            for jugador in range(numjugadores):
                jugadores[jugador].append(self.mazacote.pop(0)) #añade lo que estas sacando en la lista jugador

        return jugadores
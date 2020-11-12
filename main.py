'''
import baraja

# el contenido son distantas , fem dos listas diferentes
ordenada = baraja.creaBaraja()
print("Esta es la 1 baraja" ,ordenada)

desordenada = baraja.creaBaraja()
print ("esta es la 2 només crear-la", desordenada)
baraja.barajar(desordenada)
print("i ahora desordenada", desordenada)

'''
import barajaClasse

palos = ["o", "c", "e", "b"]
numeros = ["A", "2", "3", "4", "5", "6", "7", "S","C", "R"]

miBaraja = barajaClasse.Baraja(palos, numeros)

miBaraja.mazacote[2]

print(miBaraja.mazacote)

print(miBaraja.repartir(3,5))

miBaraja.barajar()
print(miBaraja.mazacote)


import baraja

# el contenido son distantas , fem dos listas diferentes
ordenada = baraja.creaBaraja()
print("Esta es la 1 baraja" ,ordenada)

desordenada = baraja.creaBaraja()
print ("esta es la 2 només crarla", desordenada)
baraja.barajar(desordenada)
print("i ahora desordenada", desordenada)
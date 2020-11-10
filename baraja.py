#crear unes llistes amb la baralla
palos = ["o", "c", "e", "b"]
numeros = ["A", "2", "3", "4", "5", "6", "7", "S","C", "R"]

#recorrem les llistes en un for: palo i numero son items de les cadenes x fer la conbinació de les dos llistes

def creaBaraja(): #definim funcion
    baraja = []  #variable local vuida
    for palo in palos:
        for numero in numeros:
            baraja.append(numero+palo) #iteración
    return baraja







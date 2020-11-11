import random
#crear unes llistes amb la baralla

#recorrem les llistes en un for: palo i numero son items de les cadenes x fer la conbinació de les dos llistes

def creaBaraja(palos, numeros): #definim funcion
    baraja = []  #variable local vuida
    for palo in palos:
        for numero in numeros:
            baraja.append(numero+palo) #iteración
    return baraja

def intercambio(primervalor,segonvalor): #funcionament intern aux (per intercanbiar) es un variable
    aux = primervalor
    primervalor=segonvalor
    segonvalor=aux
    return primervalor,segonvalor
'''
#son variables diferents a dalt
a = "coca"
b = "suc"
intercambio(a,b)
print (a,b)
'''
def barajar(listadenaipes):
    for i in range(len(listadenaipes)): #amb el for recorremos i modifiquem la carta
        nuevaposion = random.randrange(len(listadenaipes))
        # intercambio de cartas, tecnica vaso vacio
        aux = listadenaipes[nuevaposion]
        listadenaipes[nuevaposion] = listadenaipes[i]
        listadenaipes[i] = aux
    return listadenaipes

#crear baraja, barajear + imprimirla
'''
maza = creaBaraja()
barajar(maza)
print(maza)
'''
'''
print(barajar(creaBaraja())) #recordem () de crearBaraja

esta en ocult xq hem creat el main
'''

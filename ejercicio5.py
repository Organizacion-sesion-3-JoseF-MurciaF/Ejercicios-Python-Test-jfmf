# coding=utf-8
__Author__="José Gaspar Sánchez García"

import random

# Función que determina si un numero es par.

def esPar(numero) :
    if numero %2 == 0 :
        return True # --> Si el resto de la division por 2 es 0 es par <--
    else:
        return False

def esImpar(numero) :
    if numero %2 != 0 :
        return True # --> Si el resto de la division por 2 es distinto de 0 es impar  <--
    else:
        return False

def generarImpares(valores, inicio) :
    pares=[]
    numero=inicio
    # --> Validacion si es par o impar <-- 
    if esImpar(inicio):
        numero=inicio+1
        # --> Generamos el array de numeros <-- 
        for i in range(valores):
            pares.append(inicio)
            inicio += 2
    
    return pares

def generarPares(valores, inicio):
    impares=[]
    numero=inicio
    # --> Generamos el array de numeros <--
    if esPar(inicio):
        numero=inicio+1
        for i in range(valores):
            impares.append(inicio)
            inicio += 2
    return impares


# Programa principal
def main():
    print("Par e impar")
    n=int(input("Introduzca un numero: "))
    print("{0} es par --> {1}.".format(n,esPar(n)))
    valores=int(input("Introduzca el número de valores: "))
    inicio=int(input("Introduzca el número inicial: "))
    pares=generarPares(valores,inicio)
    impares=generarImpares(valores,inicio)
    print("Impares: ",impares)
    print("Pares: ",pares)    

if __name__== "__main__" :
   main()

# coding=utf-8
__Author__="José Gaspar Sánchez García"

def suma(x,y) :
    return x + y 

def resta(x,y) :
    return x - y

def multiplica(x,y) :
    return x * y 

def divide(x,y) :
    return x / y

# Función que crea el menú de la aplicacion.

def menuApp() :
    print("MENU CALCULADORA")
    opcion =-1

    while opcion !=0 :
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("0. Salir")

        opcion=int(input("Introduzca opción: "))
    
        if opcion == 1 :
            s1=int(input("Introduzca el primer sumando: "))
            s2=int(input("Introduzca el segundo sumando: "))
            print("La suma de {0} + {1} = {2}.".format(s1,s2,suma(s1,s2)))
        elif opcion == 2 :
            minuendo=int(input("Introduzca el minuendo: "))
            sustraendo=int(input("Introduzca el sustraendo: "))
            print("La resta de {0} - {1} = {2}.".format(minuendo,sustraendo,resta(minuendo,sustraendo)))
       # --> Completa el código fuente del programa <-- 
        elif opcion == 3 :
            multiplicando=int(input("Introduzca el multiplicando: "))
            multiplicador=int(input("Introduzca el multiplicaor: "))
            print("La multiplicación de {0} * {1} = {2}.".format(multiplicando,multiplicador,multiplica(multiplicando,multiplicador)))    
        elif opcion == 4 :
            dividendo=float(input("Introduzca el dividendo: "))
            divisor=float(input("Introduzca el divisor: "))
            print("La división de {0} / {1} = {2}.".format(dividendo,divisor,divide(dividendo,divisor)))
        elif opcion !=0 :
            print("Error: Opción incorrecta, introduzca una nueva opción.")

# Programa principal
def main():
    menuApp()
    

if __name__== "__main__" :
   main()

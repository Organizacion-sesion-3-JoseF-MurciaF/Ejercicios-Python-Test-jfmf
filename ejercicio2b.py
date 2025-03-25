# coding=utf-8
#Pide la edad y el nombre por teclado. En caso de ser mayor de 18 años indica que ya puede conducir.

# Implemente función esMayorEdad(e)
def esMayorEdad(edad,nombre) :
    if edad >= 18 :
        print('Ya puedes conducir '+nombre)
        return True
    else :
        print('No puedes conducir eres menor de edad ' +nombre)
        return False
# Programa principal
def main():
    nombre=input("Introduzca su nombre: ");
    edad=int(input(f"Introduzca su edad {nombre}: "));

    # Utilice la función definida
    esMayorEdad(edad,nombre)
    # Estructura alternativa Si (condidición con función) entonces --> sino ...


if __name__== "__main__" :
   main()
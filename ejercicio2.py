"""Pide la edad y el nombre por teclado. En caso de ser mayor de 18 años indica que ya puede conducir."""

def main():
    nombre=input("Introduzca su nombre: ");
    edad=int(input(f"Introduzca su edad {nombre}: "))
    
    # Comprobamos si es mayor de edad - Estructura condicional if - else
    # Si edad mayor o igual a dieciocho --> Usted es nayor de edad
    # Sino --> Todavía eres menor de edad
    # Resultado final de todas las tiradas
    if edad >= 18 :
       print("Eres mayor de edad "+nombre)
    else :
       print("Eres menor de edad "+nombre)

if __name__== "__main__" :
    main()

# coding=utf-8
__Author__="José Gaspar Sánchez García"

"""Pide una nota (número). Muestra la calificación según la nota:
    0-3: Muy deficiente.
    3-5: Insuficiente.
    5-6: Suficiente.
    6-7: Bien.
    7-9: Notable.
    9-10: Sobresaliente
- Utilice la estructura de control if-elif-else.
- Impltemente una función obtenerCalificacion(nota)."""

# Implemente función obtenerCalificacion
def obtenerCalificaion(n) :
   # Implemente aquí ... Si (condición) entonces ... sino ... si (condición) entonces ... sino ...
    if   n >= 0 and n <=2 :
        calificacion= "Muy deficiente"
    elif n >= 3 and n <= 4 :
        calificacion= "Insuficiente"
    elif n >= 5 and n < 6 :
        calificacion= "Suficiente"
    elif n >= 6 and n < 7 :
        calificacion= "Bien"
    elif n >= 7 and n < 9 :
        calificacion= "Notable"
    elif n >= 9 and n <= 10 :
        calificacion= "Sobresaliente"
    elif n >= 11 :
        calificacion="Incorrecta"
    elif n < 0 :
        calificacion="Incorrecta"
        
    return calificacion

# Programa principal
def main():
    n=int(input("Introduzca la nota: "));
    print('Calificación: '+obtenerCalificaion(n));

if __name__== "__main__" :
   main()

from funciones import *
#Ejercicio 1
nombre = input("Ingrese su nombre: ")
apellido =input("Ingrese su apellido: ")
ejercicio1(nombre,apellido)

#Ejercicio 2
num1 = input("Ingrese un numero: ")
num2 = input("Ingrese otro numero: ")
ejercicio2(num1,num2)

#Ejercicio 3
num = input("Ingrese un numero: ")
ejercicio3(num)

#Ejercicio 4
edad = input("Digite su edad su edad por favor: ")
ejercicio4(edad)

#Ejercicio 5
celsius = input("Digite la temperatura en celsius")
ejercicio5(celsius)

#Ejercicio 6
base = input("Digite la base: ")
altura = input("Digite la altura: ")
ejercicio6(base,altura)

#Ejercicio 7
lista = [int(x) for x in input("Ingrese números separados por coma: ").split(",")]
ejercicio7(lista)

#Ejercicio 8
palabra = input("Ingrese una palabra: ")
letra = input("Ingrese una letra: ")
ejercicio8(palabra, letra)

#Ejercicio 9
lista = [int(x) for x in input("Ingrese números separados por coma: ").split(",")]
ejercicio9(lista)

#Ejercicio 10
texto = input("Ingrese un texto: ")
ejercicio10(texto)

#Ejercicio 11
numero = int(input("Ingrese un número entero positivo: "))
ejercicio11(numero)

#Ejercicio 12
lista = [int(x) for x in input("Ingrese números separados por coma: ").split(",")]
ejercicio12(lista)

#Ejercicio 13
numero = int(input("Ingrese un número: "))
ejercicio13(numero)

#Ejercicio 14
cadena = input("Ingrese una cadena de texto: ")
ejercicio14(cadena)

#Ejercicio 15
texto = input("Ingrese un texto: ")
ejercicio15(texto)

#Ejercicio 16
clave = input("Ingrese una contraseña: ")
ejercicio16(clave)

#Ejercicio 17
ejercicio17()

#Ejercicio 18
lista = [int(x) for x in input("Ingrese números separados por coma: ").split(",")]
ejercicio18(lista)

#Ejercicio 19
longitud = int(input("Ingrese la longitud de la contraseña: "))
ejercicio19(longitud)

#Ejercicio 20
def doble(x): return x * 2
def cuadrado(x): return x ** 2
numero = int(input("Ingrese un número: "))
ejercicio20(doble, cuadrado, numero)

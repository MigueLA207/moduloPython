import random
import string
#Ejercicio 1
def ejercicio1(nombre,apellido):
    print(f"hola {nombre} {apellido}")
#Ejercicio 2
def ejercicio2(num1,num2):
    print(f"La suma de {num1} + {num2} es {num1+num2}")
#Ejercicio 3   
def ejercicio3(num):
    if num % 2 == 0:
        print("Numero primo")
    else:
        print("Numero no primo")
#Ejercicio 4
def ejercicio4(edad):
    if edad >= 18:
        print("mayor de edad")
    else: 
        print("menor de edad")
        
#Ejercicio 5
def ejercicio5(celsius):
    fahrenheit = (celsius * 9/5) + 32
    print(f"Temperatura convertida: {fahrenheit}")
    
#Ejercicio 6
def ejercicio6(base,altura):
    area = base * altura
    print(f"El area del triangulo es: {area}")
        
#Ejercicio 7
def ejercicio7(lista):
    print("El número mayor es:", max(lista))

#Ejercicio 8
def ejercicio8(palabra, letra):
    print(f"La letra '{letra}' aparece {palabra.count(letra)} veces")

#Ejercicio 9
def ejercicio9(lista):
    pares = [x for x in lista if x % 2 == 0]
    print("Números pares:", pares)

#Ejercicio 10
def ejercicio10(texto):
    texto = texto.replace(" ", "").lower()
    if texto == texto[::-1]:
        print("Es un palíndromo")
    else:
        print("No es un palíndromo")

#Ejercicio 11
def ejercicio11(numero):
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    print(f"El factorial de {numero} es {factorial}")

#Ejercicio 12
def ejercicio12(lista):
    sin_duplicados = list(set(lista))
    print("Lista sin duplicados:", sin_duplicados)

#Ejercicio 13
def ejercicio13(numero):
    if numero % 3 == 0 and numero % 5 == 0:
        print("FizzBuzz")
    elif numero % 3 == 0:
        print("Fizz")
    elif numero % 5 == 0:
        print("Buzz")
    else:
        print(numero)

#Ejercicio 14
def ejercicio14(cadena):
    vocales = "aeiouAEIOU"
    cantidad = sum(1 for c in cadena if c in vocales)
    print("Cantidad de vocales:", cantidad)

#Ejercicio 15
def ejercicio15(texto):
    print("Texto invertido:", texto[::-1])

#Ejercicio 16
def ejercicio16(clave):
    mayuscula = any(c.isupper() for c in clave)
    minuscula = any(c.islower() for c in clave)
    numero = any(c.isdigit() for c in clave)
    simbolo = any(c in string.punctuation for c in clave)
    if mayuscula and minuscula and numero and simbolo:
        print("Contraseña segura")
    else:
        print("Contraseña insegura")

#Ejercicio 17
def ejercicio17():
    resultado = random.randint(1, 6)
    print(f"Resultado del dado: {resultado}")

#Ejercicio 18
def ejercicio18(lista):
    suma = sum(x for x in lista if lista.count(x) == 1)
    print("Suma de elementos únicos:", suma)

#Ejercicio 19
def ejercicio19(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    print("Contraseña generada:", contraseña)

#Ejercicio 20
def ejercicio20(f1, f2, numero):
    resultado = f1(f2(numero))
    print("Resultado de la composición:", resultado)
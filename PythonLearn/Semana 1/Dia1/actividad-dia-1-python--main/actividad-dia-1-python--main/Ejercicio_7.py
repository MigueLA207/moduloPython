#Pide dos números al usuario. Imprime cuál es el mayor. Si son iguales, indícalo.
numero_1 = int(input("Digita el primer numero: "))
numero_2 = int(input("Digita el segundo numero: "))

numero_mayor = 0

if numero_1 == numero_2:
    numero_mayor = 0
elif numero_1 > numero_2:
    numero_mayor = numero_1
else: 
    numero_mayor = numero_2


if numero_mayor == 0:
    print("Los numeros son iguales")
else:
    print(f"El numero mayor es {numero_mayor}")
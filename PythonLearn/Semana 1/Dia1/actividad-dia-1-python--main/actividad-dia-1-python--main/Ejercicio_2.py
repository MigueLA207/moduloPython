#Pide un número al usuario. Di si es positivo, negativo o si es cero.

numero = int(input("Digita un numero: "))

if numero > 0:
    print(f"El numero {numero} es positivo")
elif numero < 0: 
    print(f"El numero {numero} es negativo")
elif numero == 0:
    print("Digitaste 0")
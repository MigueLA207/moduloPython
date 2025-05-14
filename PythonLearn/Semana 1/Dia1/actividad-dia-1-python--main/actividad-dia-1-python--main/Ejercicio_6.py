#Fija un número secreto (por ejemplo, 7). Pide al usuario que lo adivine. Di si su número es mayor, menor o igual al número secreto.
numero_secreto = 7
for intentos in range(10):  # Desde 0 hasta 9
    print(f"Te quedan {10-intentos} intentos")  
    numero = int(input("Digite un numero del 1 al 10: "))
    
    if numero == numero_secreto:
        print(f"Escogiste el numero correcto en {intentos + 1} intentos")
        break
    elif numero > numero_secreto:
        print("el numero es menor")
    else:
        print("el numero es mayor")
        
      

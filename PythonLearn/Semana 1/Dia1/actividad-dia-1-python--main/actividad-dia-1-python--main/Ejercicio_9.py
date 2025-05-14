#Pide un año al usuario. Determina si es bisiesto (es divisible entre 4 y no entre 100, excepto si también es divisible entre 400).


año = int(input("Digite un año: "))

if año % 4 == 0 and año % 100 != 0 or año % 4 == 0 and año % 100 == 0 and año % 400 == 0:
    print("Año bisiesto")
else:
    print("No es Año bisiesto")
    
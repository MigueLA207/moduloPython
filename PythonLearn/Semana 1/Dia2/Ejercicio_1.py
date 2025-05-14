#Menor de tres números
num_1 = int(input("Escriba el valor del primer numero: "))
num_2 = int(input("Escriba el valor del segundo numero: "))
num_3 = int(input("Escriba el valor del tercero numero: "))

numero_mayor = 0

if num_1>num_2:
    numero_mayor = num_1
    if numero_mayor > num_3:
        numero_mayor = numero_mayor
    else:
        numero_mayor = num_3
else:
    numero_mayor = num_2
    if numero_mayor > num_3:
        numero_mayor = numero_mayor
    else:
        numero_mayor = num_3

print(numero_mayor)

#Pide al usuario el total de una cuenta. Luego pregunta qué porcentaje de propina quiere dejar (10, 15 o 20). Calcula y muestra el valor de la propina.

total_cuenta = float(input("Digite el total de la cuenta: "))
porcentaje = float(input("Digite el porcentaje de propina que quiere dejar(10, 15 o 20): "))

while porcentaje not in [10,15,20]:
    print("Dato invalido")
    porcentaje = float(input("Digite el porcentaje de propina que quiere dejar(10, 15 o 20): "))


propina = total_cuenta*(porcentaje/100)
print(f"La propina es de: {propina: .0f}$")




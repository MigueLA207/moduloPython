#Edad válida
edad = int(input("Digita tu edad: "))

if edad < 0 or edad > 120:
    print("Edad no valida")
else:
    print("Edad válida")
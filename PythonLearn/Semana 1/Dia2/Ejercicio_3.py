#Lista vacía y append()
nombres = ["miguel", "Andres", "Santiagop"]


while True:
    
    nombre_usuario = str(input("Escriba su nombre: "))
    nombres.append(nombre_usuario)
    for i in nombres:   
        print(i)
    seguir = int(input("Digite 1 si quiere agregar mas nombres, digite 2 si quiere salir del programa:  "))
    if seguir == 2:
        break

print(nombres[0])


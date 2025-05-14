import sys
Contactos = {}
def mostrar_libros(contactos):
    for nombre,valores in contactos.items:
        telefono = valores['telefono']
        año = valores['año']
        print(f"nombre:{nombre} -- telefono: {telefono} -- email: {año}")
        

while True:
    print("Opciones del programa")
    print("1) Crear contacto")
    print("2) Mostrar contactos")
    print("3) Buscar contacto")
    print("4) Actualizar contacto")
    print("5) Eliminar contacto")
    print("6) Salir del programa")
    opcion_menu = int(input("Escoge una opcion: "))

    match opcion_menu:
        case 1: 

            while True:
                print("---------Agregar contacto----------")
                #Agregar libro a la biblioteca
                nombre = str(input("ingrese el nombre del nuevo contacto: "))
                telefono = str(input("ingrese el  nombre del autor: "))
                email = int(input("ingrese el año de creacion: "))

                info = {'telefono': telefono, 'email': email}
         

                Contactos[nombre] = info
                telefono = Contactos['telefono']
                email = Contactos['email']

                print("\nContacto ingresado:")
                print(f" titulo: {nombre}, telefono: {telefono}, email: {email}")

                op = int(input("\n¿Quieres salir del programa? digite 1 para agregar mas libros, digite 2 para salir: \n") )

                if op == 2:
                    break

        case 2:
            print("---------Mostrar contactos----------")
            mostrar_libros(Contactos)
        
        case 3:
            print("---------Buscar contacto----------")
            while True:
                nombre = input("Digita el nombre del contacto que quieres consultar: ")
                if nombre in Contactos:
                    print("Consultado con exito")
                    print(f"nombre: {nombre} -- telefono: {Contactos[nombre]['telefono']} -- email: {Contactos[nombre]['email']}")
                    break
                else:
                    print("el numero no esta en los contactos")    
            op = int(input("\n¿Quieres salir del programa? digite 1 para agregar mas libros, digite 2 para salir: \n") )
            if op == 2:
                break  
        case 4:
            print("---------Actualizar contacto----------")
            print("\n libros en la biblioteca")
            mostrar_libros(Contactos)
            while True: 
                nombre = input("Digita el nombre del contacto que quieres consultar: ")
                if nombre in Contactos:
                    desicion = input("Opciones\n (1).Actualizar telefono\n (2).Actualizar email")
                    if desicion == "1":
                        nuevo_telefono = input("ingrese el nuevo telefono por favor: ")
                        Contactos[nombre]['telefono'] = nuevo_telefono
                        print("Actualizado conexito")
                        break
                    elif desicion == "2":
                        nuevo_email = input("Ingrese el nuevo email por favor: ")
                        Contactos[nombre]['email'] = nuevo_email
                        print("Actualizado conexito")
                        break
                else:
                    print("El producto no se encuentra en los contactos")
            op = int(input("\n¿Quieres salir del programa? digite 1 para agregar mas libros, digite 2 para salir: \n") )
            if op == 2:
                break 
            

        case 5: 
            print("\n ---------Eliminar libro----------")  
            mostrar_libros(Contactos)          
            nombre = input("Ingrese el nombre del contacto que desea eliminar: ")    

            eliminado = Contactos.pop(nombre) 

            print(f"Valor eliminado: {eliminado}\n")   
            print("Estos son los libros disponibles")
            mostrar_libros(Contactos)
        case 6:
            sys.exit()
        case _:
            print("Opcion invalida")
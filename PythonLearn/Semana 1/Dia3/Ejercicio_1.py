import sys

def mostrar_libros(biblioteca):
    for i in biblioteca:

        titulo = biblioteca[str(i)]['titulo']
        autor = biblioteca[str(i)]['autor']
        año = biblioteca[str(i)]['año']

        print(f"id : {i} , titulo: {titulo}, autor: {autor}, año: {año}")

biblioteca = {}

while True:

    

    print("Opciones del programa")
    print("1) Agregar libro")
    print("2) Mostrar libros")
    print("3) Actualizar libro")
    print("4) Eliminar id")
    print("5) Salir del programa")
    opcion_menu = int(input("Escoge una opcion: "))

    match opcion_menu:
        case 1: 

            print("agregar libro al diccionario")
            id =0


            while True:
                print("---------Agregar libro----------")
                #Agregar libro a la biblioteca
                nombre = str(input("ingrese el nombre del libro: "))
                autor = str(input("ingrese el  nombre del autor: "))
                año = int(input("ingrese el año de creacion: "))

                info = {'titulo': nombre, 'autor': autor, 'año': año}
                id += 1  

                biblioteca[str(id)] = info

                titulo = biblioteca[str(id)]['titulo']
                autor = biblioteca[str(id)]['autor']
                año = biblioteca[str(id)]['año']

                print("\nLibro Ingresado:")
                print(f"id : {id} , titulo: {titulo}, autor: {autor}, año: {año}")

                op = int(input("\n¿Quieres salir del programa? digite 1 para agregar mas libros, digite 2 para salir: \n") )

                if op == 2:
                    break

        case 2:
            print("---------Mostrar libros----------")
            mostrar_libros(biblioteca)
        
        case 3:
            print("---------Editar libro----------")
            print("\n libros en la biblioteca")
            mostrar_libros(biblioteca)
            id_editar = int(input("Ingrese el id del libro que desea editar: "))

            titulo = biblioteca[str(id_editar)]['titulo']
            autor = biblioteca[str(id_editar)]['autor']
            año = biblioteca[str(id_editar)]['año']

            print("Ingrese el numero correspondiente al dato que quiere editar: ")
            print(f"1)titulo: {titulo}")
            print(f"2)autor: {autor}")
            print(f"3)año: {año}")

            value_editar = int(input("Ingrese numero: "))

            
            match value_editar:
                case 1: 
                    cambio_titulo = str(input("Ingrese el nuevo titulo para el libro:  "))
                    biblioteca[str(id_editar)]['titulo'] = cambio_titulo
                    print("Cambio realizado con exito")
                case 2: 
                    cambio_autor = str(input("Ingrese el nuevo autor del libro:  "))
                    biblioteca[str(id_editar)]['autor'] = cambio_autor
                    print("Cambio realizado con exito")
                case 3:
                    cambio_año = int(input("Ingrese el nuevo año del libro:  "))
                    biblioteca[str(id_editar)]['año'] = cambio_año
                    print("Cambio realizado con exito")
                case _:
                    print("Opcion invalida")
            
            print("\n Cambios hechos")
            mostrar_libros(biblioteca)
            print("\n")

        case 4: 
            print("\n ---------Eliminar libro----------")  
            mostrar_libros(biblioteca)          
            id_eliminar = int(input("Ingrese el id del libro que desea eliminar: "))       

            eliminado = biblioteca.pop(str(id_eliminar)) 

            print(f"Valor eliminado: {eliminado}\n")   
            print("Estos son los libros disponibles")
            mostrar_libros(biblioteca)
        case 5:
            sys.exit()
        case _:
            print("mucho bruto opcion invalida")
    









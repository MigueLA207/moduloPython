#Pide al usuario su edad. Si tiene 18 años o más, imprime "Eres mayor de edad". Si no, imprime "Eres menor de edad".
edad = int(input("Escriba su edad: "))

while edad <=0:
    edad = int(input("Dato invalida, Escriba su edad: "))
    
if edad >= 18:
    print(f"Tu edad es {edad}, entonces eres mayor de edad ")
else: 
    print(f"Tu edad es {edad}, entonces eres menor de edad ")       
        


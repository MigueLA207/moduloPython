#Pide una contraseña al usuario. Si coincide con "python123", imprime "Acceso concedido", de lo contrario, "Contraseña incorrecta".
contrasenaReal = "python123"
  
contrasena = str(input("Digite su contraseña: "))

while contrasena != contrasenaReal:
    print("Contraseña incorrecta")
    contrasena = str(input("Escriba de nuevo su contraseña: "))

print("Acceso concedido")
    
    

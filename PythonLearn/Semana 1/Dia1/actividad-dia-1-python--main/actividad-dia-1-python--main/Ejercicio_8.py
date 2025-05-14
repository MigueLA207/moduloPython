''' Pide al usuario su peso (kg) y altura (m). Calcula su IMC (peso / altura²) y muestra:

    "Bajo peso" si es menor a 18.5
    "Normal" si está entre 18.5 y 24.9
    "Sobrepeso" si está entre 25 y 29.9
    "Obesidad" si es mayor o igual a 30  '''

peso = float(input("Digite su peso en kg: "))
altura = float(input("Digite su altura en metros: "))
    

IMC = peso/(altura ** 2)

if IMC < 18.5:
    print(f"Bajo Peso. IMC = {IMC:.1f}")
elif IMC < 25: 
    print(f"Normal. IMC = {IMC:.1f}")
elif IMC < 30: 
    print(f"Sobrepeso. IMC = {IMC:.1f}")
else: 
    print(f"Obesidad. IMC = {IMC:.1f}")


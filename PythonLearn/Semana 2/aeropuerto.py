import sys
from datetime import datetime

# Sistema de Gestión y Costeo de Equipaje Aéreo
# Variables globales para almacenar información de compras
compras = {}
contador_id = 0

# Constantes de configuración
RUTAS = {
    "nacional": {"destino": "Bogotá → Medellín", "precio": 230000},
    "internacional": {"destino": "Bogotá → España", "precio": 4200000}
}

COSTOS_EQUIPAJE = {
    20: 50000,
    30: 70000,
    50: 110000
}

LIMITE_EQUIPAJE_MANO = 13  # kg

def generar_id_compra():
    """Genera un ID único para cada compra"""
    global contador_id
    contador_id += 1
    return f"COMP{contador_id:04d}"

def validar_peso_equipaje_principal(peso):
    """Valida si el peso del equipaje principal es admitido"""
    if peso > 50:
        return "No admitido", 0
    elif peso <= 20:
        return "Admitido", COSTOS_EQUIPAJE[20]
    elif peso <= 30:
        return "Admitido", COSTOS_EQUIPAJE[30]
    else:  # peso <= 50
        return "Admitido", COSTOS_EQUIPAJE[50]

def validar_equipaje_mano(lleva_mano, peso_mano):
    """Valida si el equipaje de mano es admitido"""
    if not lleva_mano:
        return "No lleva", 0
    
    if peso_mano > LIMITE_EQUIPAJE_MANO:
        return "Rechazado (excede 13kg)", 0
    else:
        return "Admitido", 0

def mostrar_resumen_compra(id_compra):
    """Muestra el resumen de una compra específica"""
    if id_compra not in compras:
        print(f"No se encontró la compra con ID: {id_compra}")
        return
    
    compra = compras[id_compra]
    print("\n╔═════════════════════════════════════════════════════════════╗") 
    print("║                    RESUMEN DE COMPRA                        ║") 
    print("╚═════════════════════════════════════════════════════════════╝")
    print(f"ID de compra: {id_compra}")
    print(f"Nombre del pasajero: {compra['nombre']}")
    print(f"Destino: {compra['destino']}")
    print(f"Fecha: {compra['fecha']}")
    print(f"Estado del equipaje principal: {compra['estado_equipaje_principal']}")
    print(f"Estado del equipaje de mano: {compra['estado_equipaje_mano']}")
    print(f"Costo total: ${compra['costo_total']:,.0f}")
    print("─────────────────────────────────────────────────────────────")

def registrar_compra():
    """Registra una nueva compra de boleto"""
    print("\n--- Registro de Compra de Boleto ---")
    
    # Solicitar nombre del pasajero
    while True:
        nombre = input("Ingrese el nombre del pasajero: ")
        if nombre.replace(" ", "").isalpha():
            break
        else:
            print("Por favor, ingrese un nombre válido (solo letras y espacios).")
    
    # Solicitar tipo de viaje
    while True:
        tipo_viaje = input("Tipo de viaje (nacional/internacional): ").lower()
        if tipo_viaje in RUTAS:
            break
        else:
            print("Por favor, ingrese 'nacional' o 'internacional'.")
    
    # Obtener información del destino y precio base
    destino = RUTAS[tipo_viaje]["destino"]
    precio_base = RUTAS[tipo_viaje]["precio"]
    
    # Solicitar peso del equipaje principal
    while True:
        try:
            peso_equipaje = float(input("Ingrese el peso del equipaje principal (kg): "))
            if peso_equipaje >= 0:
                break
            else:
                print("El peso no puede ser negativo.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
    
    # Validar equipaje principal
    estado_equipaje_principal, costo_equipaje_principal = validar_peso_equipaje_principal(peso_equipaje)
    
    # Si el equipaje principal no es admitido, preguntar si desea continuar
    if estado_equipaje_principal == "No admitido":
        print("El peso del equipaje principal excede el límite permitido de 50 kg.")
        while True:
            opcion = input("¿Desea continuar sin equipaje principal? (sí/no): ").lower()
            if opcion == "sí" or opcion == "si":
                estado_equipaje_principal = "Viaja sin equipaje principal"
                costo_equipaje_principal = 0
                break
            elif opcion == "no":
                print("Compra cancelada.")
                return
            else:
                print("Por favor, responda 'sí' o 'no'.")
    
    # Solicitar información sobre equipaje de mano
    while True:
        lleva_mano = input("¿Lleva equipaje de mano? (sí/no): ").lower()
        if lleva_mano in ["sí", "si", "no"]:
            lleva_mano = lleva_mano in ["sí", "si"]
            break
        else:
            print("Por favor, responda 'sí' o 'no'.")
    
    peso_mano = 0
    if lleva_mano:
        while True:
            try:
                peso_mano = float(input("Ingrese el peso del equipaje de mano (kg): "))
                if peso_mano >= 0:
                    break
                else:
                    print("El peso no puede ser negativo.")
            except ValueError:
                print("Por favor, ingrese un número válido.")
    
    # Validar equipaje de mano
    estado_equipaje_mano, costo_equipaje_mano = validar_equipaje_mano(lleva_mano, peso_mano)
    
    # Solicitar fecha del viaje
    while True:
        try:
            fecha_str = input("Ingrese la fecha del viaje (DD/MM/YYYY): ")
            fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
            fecha_formateada = fecha.strftime("%d/%m/%Y")
            break
        except ValueError:
            print("Formato de fecha inválido. Utilice DD/MM/YYYY.")
    
    # Calcular costo total
    costo_total = precio_base + costo_equipaje_principal + costo_equipaje_mano
    
    # Generar ID de compra
    id_compra = generar_id_compra()
    
    # Almacenar la información de la compra
    compras[id_compra] = {
        "nombre": nombre,
        "tipo_viaje": tipo_viaje,
        "destino": destino,
        "fecha": fecha_formateada,
        "peso_equipaje_principal": peso_equipaje,
        "estado_equipaje_principal": estado_equipaje_principal,
        "peso_equipaje_mano": peso_mano if lleva_mano else 0,
        "estado_equipaje_mano": estado_equipaje_mano,
        "precio_base": precio_base,
        "costo_equipaje_principal": costo_equipaje_principal,
        "costo_total": costo_total
    }
    
    # Mostrar resumen de la compra
    mostrar_resumen_compra(id_compra)
    
    return id_compra

def total_recaudado():
    """Muestra el total recaudado en todas las compras"""
    if not compras:
        print("No hay compras registradas.")
        return
    
    total = sum(compra["costo_total"] for compra in compras.values())
    print(f"\nTotal recaudado en todas las compras: ${total:,.0f}")
    print(f"Número de pasajeros procesados: {len(compras)}")

def recaudado_por_fecha():
    """Muestra el total recaudado para una fecha específica"""
    if not compras:
        print("No hay compras registradas.")
        return
    
    while True:
        try:
            fecha_str = input("Ingrese la fecha para consultar (DD/MM/YYYY): ")
            fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
            fecha_formateada = fecha.strftime("%d/%m/%Y")
            break
        except ValueError:
            print("Formato de fecha inválido. Utilice DD/MM/YYYY.")
    
    compras_fecha = {id_comp: comp for id_comp, comp in compras.items() if comp["fecha"] == fecha_formateada}
    
    if not compras_fecha:
        print(f"No hay compras registradas para la fecha {fecha_formateada}.")
        return
    
    total = sum(compra["costo_total"] for compra in compras_fecha.values())
    print(f"\nTotal recaudado para la fecha {fecha_formateada}: ${total:,.0f}")
    print(f"Número de pasajeros procesados: {len(compras_fecha)}")

def estadisticas_pasajeros():
    """Muestra estadísticas de pasajeros procesados"""
    if not compras:
        print("No hay compras registradas.")
        return
    
    nacionales = sum(1 for compra in compras.values() if compra["tipo_viaje"] == "nacional")
    internacionales = sum(1 for compra in compras.values() if compra["tipo_viaje"] == "internacional")
    
    print("\n--- Estadísticas de Pasajeros ---")
    print(f"Total de pasajeros procesados: {len(compras)}")
    print(f"Pasajeros nacionales: {nacionales}")
    print(f"Pasajeros internacionales: {internacionales}")

def consultar_compra():
    """Consulta una compra por su ID"""
    id_compra = input("Ingrese el ID de compra a consultar (ejemplo: COMP0001): ")
    mostrar_resumen_compra(id_compra)

def menu_admin():
    """Muestra el menú de administración"""
    while True:
        print("\n╔═════════════════════════════════════════════════════════════╗") 
        print("║                       MENÚ ADMINISTRADOR                    ║") 
        print("╚═════════════════════════════════════════════════════════════╝")
        print("1. Total recaudado en todas las compras")
        print("2. Total recaudado para una fecha específica")
        print("3. Estadísticas de pasajeros")
        print("4. Consultar compra por ID")
        print("5. Volver al menú principal")
        
        while True:
            try:
                opcion = int(input("\nSeleccione una opción: "))
                if 1 <= opcion <= 5:
                    break
                else:
                    print("Por favor, seleccione una opción válida (1-5).")
            except ValueError:
                print("Por favor, ingrese un número válido.")
        
        if opcion == 1:
            total_recaudado()
        elif opcion == 2:
            recaudado_por_fecha()
        elif opcion == 3:
            estadisticas_pasajeros()
        elif opcion == 4:
            consultar_compra()
        elif opcion == 5:
            return

def menu_principal():
    """Muestra el menú principal del sistema"""
    print("\n╔═════════════════════════════════════════════════════════════╗") 
    print("║           SISTEMA DE GESTIÓN Y COSTEO DE EQUIPAJE           ║") 
    print("╚═════════════════════════════════════════════════════════════╝")
    
    while True:
        print("\nMenú Principal:")
        print("1. Registrar compra de boleto")
        print("2. Menú Administrador")
        print("3. Salir")
        
        while True:
            try:
                opcion = int(input("\nSeleccione una opción: "))
                if 1 <= opcion <= 3:
                    break
                else:
                    print("Por favor, seleccione una opción válida (1-3).")
            except ValueError:
                print("Por favor, ingrese un número válido.")
        
        if opcion == 1:
            registrar_compra()
            input("\nPresione Enter para continuar...")
        elif opcion == 2:
            menu_admin()
        elif opcion == 3:
            print("\n¡Gracias por utilizar el Sistema de Gestión y Costeo de Equipaje!")
            sys.exit()

# Iniciar el programa
if __name__ == "__main__":
    menu_principal()
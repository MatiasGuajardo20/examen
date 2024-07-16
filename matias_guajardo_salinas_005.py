import random
import math
import csv

# Lista de empleados
empleados = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez", 
             "Pedro Rodríguez", "Laura Hernández", "Miguel Sánchez", 
             "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]

# Función para asignar sueldos aleatorios
def asignar_sueldos():
    sueldos = {empleado: random.randint(300000, 2500000) for empleado in empleados}
    return sueldos

# Función para clasificar sueldos y mostrar el reporte
def clasificar_sueldos(sueldos):
    sueldos_menores = {empleado: sueldo for empleado, sueldo in sueldos.items() if sueldo < 800000}
    sueldos_medios = {empleado: sueldo for empleado, sueldo in sueldos.items() if 800000 <= sueldo <= 2000000}
    sueldos_altos = {empleado: sueldo for empleado, sueldo in sueldos.items() if sueldo > 2000000}
    
    # Reporte de clasificación
    reporte = ""
    total_sueldos = sum(sueldos.values())
    
    reporte += "Sueldos menores a $800.000 TOTAL: {}\n".format(len(sueldos_menores))
    reporte += "Nombre empleado\tSueldo\n"
    for empleado, sueldo in sueldos_menores.items():
        reporte += "{}\t${}\n".format(empleado, sueldo)
    
    reporte += "\nSueldos entre $800.000 y $2.000.000 TOTAL: {}\n".format(len(sueldos_medios))
    reporte += "Nombre empleado\tSueldo\n"
    for empleado, sueldo in sueldos_medios.items():
        reporte += "{}\t${}\n".format(empleado, sueldo)
    
    reporte += "\nSueldos superiores a $2.000.000 TOTAL: {}\n".format(len(sueldos_altos))
    reporte += "Nombre empleado\tSueldo\n"
    for empleado, sueldo in sueldos_altos.items():
        reporte += "{}\t${}\n".format(empleado, sueldo)
    
    reporte += "\nTOTAL SUELDOS: ${}\n".format(total_sueldos)
    
    return reporte

# Función para ver estadísticas
def ver_estadisticas(sueldos):
    total_sueldos = sum(sueldos.values())
    promedio_sueldos = total_sueldos / len(sueldos)
    sueldo_maximo = max(sueldos.values())
    sueldo_minimo = min(sueldos.values())
    
    # Calcular la media geométrica
    producto_sueldos = math.prod(sueldos.values())
    media_geometrica = producto_sueldos ** (1 / len(sueldos))
    
    return total_sueldos, promedio_sueldos, sueldo_maximo, sueldo_minimo, media_geometrica

# Función para generar reporte de sueldos con descuentos
def generar_reporte_con_descuentos(sueldos):
    reporte = ""
    reporte_csv = [["Nombre empleado", "Sueldo Base", "Descuento Salud", "Descuento AFP", "Sueldo Líquido"]]
    for empleado, sueldo in sueldos.items():
        descuento_salud = sueldo * 0.07
        descuento_afp = sueldo * 0.12
        sueldo_liquido = sueldo - descuento_salud - descuento_afp
        reporte += f"{empleado}\t${sueldo}\t${descuento_salud}\t${descuento_afp}\t${sueldo_liquido}\n"
        reporte_csv.append([empleado, sueldo, descuento_salud, descuento_afp, sueldo_liquido])
    return reporte, reporte_csv

# Función para exportar reporte a CSV
def exportar_reporte_csv(reporte_csv, nombre_archivo="reporte_sueldos.csv"):
    with open(nombre_archivo, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(reporte_csv)

# Menú principal
def menu():
    sueldos = {}
    while True:
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadísticas")
        print("4. Reporte de sueldos")
        print("5. Salir del programa")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            sueldos = asignar_sueldos()
            print("Sueldos asignados.")
        elif opcion == "2":
            if sueldos:
                reporte_clasificacion = clasificar_sueldos(sueldos)
                print(reporte_clasificacion)
            else:
                print("Primero asigne los sueldos.")
        elif opcion == "3":
            if sueldos:
                total, promedio, maximo, minimo, media_geometrica = ver_estadisticas(sueldos)
                print(f"Total sueldos: ${total}")
                print(f"Promedio sueldos: ${promedio}")
                print(f"Sueldo máximo: ${maximo}")
                print(f"Sueldo mínimo: ${minimo}")
                print(f"Media geométrica: ${media_geometrica}")
            else:
                print("Primero asigne los sueldos.")
        elif opcion == "4":
            if sueldos:
                reporte, reporte_csv = generar_reporte_con_descuentos(sueldos)
                print("Reporte de sueldos con descuentos:")
                print(reporte)
                exportar_reporte_csv(reporte_csv)
                print("Reporte exportado a reporte_sueldos.csv")
            else:
                print("Primero asigne los sueldos.")
        elif opcion == "5":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Ejecutar el menú
menu()


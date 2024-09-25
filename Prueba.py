import math

def leer_asistencia() -> list:
    asistencias = []
    try:
        with open('asistencia_congreso.txt', 'r') as file:
            for line in file:
                asistencias.append(line.strip().split(';'))
    except FileNotFoundError:
        print("El archivo no se encontró.")
    else:
        print("Archivo leído correctamente.")
    return asistencias

def calcular_porcentaje(num_asistencias: int, total: int) -> int:
    porcentaje = (num_asistencias / total) * 100
    return math.ceil(porcentaje)

def clasificar_estudiante(porcentaje: int) -> str:
    if porcentaje >= 75:
        return "Cumple con la asistencia"
    else:
        return "No cumple con la asistencia"

def escribir_reporte(asistencias: list):
    try:
        with open('reporte_asistencia.txt', 'w') as file:
            for asistencia in asistencias:
                nombre = asistencia[0]
                num_asistencias = asistencia[1:].count('P')
                total_sesiones = len(asistencia) - 1
                porcentaje = calcular_porcentaje(num_asistencias, total_sesiones)
                clasificacion = clasificar_estudiante(porcentaje)
                file.write(f"{nombre};{porcentaje};{clasificacion}\n")
    except Exception as e:
        print(f"Error al escribir el archivo: {e}")
    else:
        print("Reporte generado correctamente.")

def procesar_asistencia():
    asistencias = leer_asistencia()
    if len(asistencias) > 0:
        escribir_reporte(asistencias)

procesar_asistencia()
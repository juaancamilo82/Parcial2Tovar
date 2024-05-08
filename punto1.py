import numpy as np

# Función para generar tiempo de llegada aleatorio
def generar_tiempo_llegada():
    minutos, segundos = np.random.randint(0, 60, size=2)
    return minutos * 60 + segundos

# Tiempo de servicio determinístico
tiempo_servicio = 240  # segundos (4 minutos)

# Capacidad máxima del sistema (servicio y espera)
capacidad_maxima = 3

w = 28
# Tiempos de llegada de los clientes (minutos:segundos)
tiempos_llegada = [(3, w), (2, 21), (3, 25), (1, 5), (5, w), (6, 9), (4, 12)]

# Ordenar los tiempos de llegada por orden de llegada
tiempos_llegada.sort()

# Variables de estado
tiempo_actual = 0
cola_espera = []
clientes_atendidos = 0
clientes_rechazados = 0
tiempo_espera_total = 0
tiempo_servicio_total = 0

# Simulación del sistema
for minutos, segundos in tiempos_llegada:
    # Avance del tiempo
    tiempo_actual = minutos * 60 + segundos

    # Verificar si hay clientes que deben salir del sistema
    while cola_espera and cola_espera[0] <= tiempo_actual - tiempo_servicio:
        cola_espera.pop(0)

    # Si hay espacio en la cola, el cliente es atendido
    if len(cola_espera) < capacidad_maxima:
        tiempo_entrada = tiempo_actual
        cola_espera.append(tiempo_actual)
        clientes_atendidos += 1
        tiempo_espera = max(0, tiempo_actual - cola_espera[0]) if cola_espera else 0
        tiempo_espera_total += tiempo_espera
        tiempo_servicio_total += tiempo_servicio
        tiempo_salida = tiempo_actual + tiempo_servicio
        minutos_entrada = tiempo_entrada // 60
        segundos_entrada = tiempo_entrada % 60
        minutos_salida = tiempo_salida // 60
        segundos_salida = tiempo_salida % 60
        # Ajustar la impresión de los segundos para agregar un 0 si es necesario
        print(f"Cliente atendido en el tiempo {minutos_entrada}:{segundos_entrada:02} (Entrada: {minutos_entrada}:{segundos_entrada:02}) - Tiempo de salida: {minutos_salida}:{segundos_salida:02} (Duración: {tiempo_servicio} segundos)")
    else:
        # Si el sistema está lleno, el cliente es rechazado
        clientes_rechazados += 1
        print(f"Cliente rechazado en el tiempo {minutos}:{segundos}")

# Cálculo del tiempo de espera promedio y tiempo de utilización
tiempo_espera_promedio = tiempo_espera_total / clientes_atendidos if clientes_atendidos > 0 else 0
tiempo_utilizacion = tiempo_servicio_total / (tiempo_actual / 60)

# Impresión de resultados
print("\nResultados de la simulación:")
print(f"Clientes atendidos: {clientes_atendidos}")
print(f"Clientes rechazados: {clientes_rechazados}")
print(f"Tiempo de espera promedio: {tiempo_espera_promedio:.2f} segundos")


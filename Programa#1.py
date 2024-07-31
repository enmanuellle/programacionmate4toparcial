from munkres import Munkres

def aplicar_metodo_hungaro(cost_matrix):
    # Crear instancia del algoritmo de asignación óptima de Munkres
    m = Munkres()

    # Aplicar el algoritmo de asignación óptima en la matriz de costos
    asignacion = m.compute(cost_matrix)

    # Obtener las asignaciones óptimas y los costos totales
    asignacion_optima = []
    costo_total = 0

    for row, col in asignacion:
        costo = cost_matrix[row][col]
        asignacion_optima.append((row, col))
        costo_total += costo

    # Devolver las asignaciones óptimas y el costo total
    return asignacion_optima, costo_total

# Ejemplo de uso
matriz_costos = [
    [7, 3, 9, 4],
    [8, 1, 7, 6],
    [5, 4, 2, 1],
    [6, 7, 9, 5]
]

asignacion_optima, costo_total = aplicar_metodo_hungaro(matriz_costos)

print("Asignación óptima:", asignacion_optima)
print("Costo total:", costo_total)
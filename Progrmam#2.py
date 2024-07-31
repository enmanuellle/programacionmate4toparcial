from pulp import LpMinimize, LpProblem, LpStatus, LpVariable, lpSum, value

# Definición de datos
fuentes = ['A', 'B', 'C']
destinos = ['1', '2', '3', '4']

capacidades = {'A': 1500, 'B': 1500, 'C': 1500}
necesidades = {'1': 1000, '2': 1200, '3': 1500, '4': 1000}

costos = {
    'A': {'1': 80, '2': 100, '3': 85, '4': 90},
    'B': {'1': 95, '2': 85, '3': 80, '4': 100},
    'C': {'1': 90, '2': 80, '3': 95, '4': 90}
}

# Crear el modelo de optimización
modelo = LpProblem('Problema_de_Transporte', LpMinimize)

# Definir variables de decisión
envios = [(i, j) for i in fuentes for j in destinos]
cantidad_envio = LpVariable.dicts('Envio', (fuentes, destinos), 0)

# Definir la función objetivo
modelo += lpSum(cantidad_envio[i][j] * costos[i][j] for (i, j) in envios), "Costo_Total_Envio"

# Añadir restricciones de demanda
for j in destinos:
    modelo += lpSum(cantidad_envio[i][j] for i in fuentes) == necesidades[j], f"Satisfacer_Demanda_{j}"

# Añadir restricciones de oferta
for i in fuentes:
    modelo += lpSum(cantidad_envio[i][j] for j in destinos) <= capacidades[i], f"Satisfacer_Oferta_{i}"

# Resolver el modelo
modelo.solve()

# Imprimir el estado del modelo
print("Estado de la solución:", LpStatus[modelo.status])

# Imprimir la solución óptima
if LpStatus[modelo.status] == 'Optimal':
    for i in fuentes:
        for j in destinos:
            if cantidad_envio[i][j].varValue > 0:
                print(f"Enviar {cantidad_envio[i][j].varValue} unidades desde {i} hasta {j}")

    # Imprimir el costo total mínimo
    print('El costo mínimo total es:', value(modelo.objective))
else:
    print("No se encontró una solución óptima.")

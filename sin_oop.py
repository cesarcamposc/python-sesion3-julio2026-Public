# SIN OOP - Programación orientada a objetos
# 4 listas paralelas - sincronizarlas
nombres = ["Juan", "Ana", "Pedro"]
matriculas = ["123", "456", "789"]
notas_python = [85, 90, 78]
notas_java = [88, 92, 80]

# Para el promedio de Juan, necesito saber que es índice 0.
i = 0
promedio = (notas_python[i] + notas_java[i]) / 2 
print(f"El promedio es: {promedio}")

# ¿Cómo busco a Ana? Necesito saber que es índice 1.
for i in range(len(nombres)):
    if nombres[i] == "Ana":
        promedio = (notas_python[i] + notas_java[i]) / 2
        print(f"El promedio de Ana es: {promedio}")

# ¿Ordenar por promedio? Necesito calcular los promedios de todos y luego ordenarlos esto es una pesadilla.
# ¿Agregar materia nueva? agregar una nueva lista y sincronizarla con las otras listas, esto es un dolor de cabeza.
# ¿Guardar en un JSON? tengo que sincronizar las 4 listas manualmente, esto es un dolor de cabeza.
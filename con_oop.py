"""
from estudiante import Estudiante
ana = Estudiante("Ana Torres", "ana@gmail.com", "001")

ana.agregar_calificacion("Python", 85)
ana.agregar_calificacion("Java", 90)

# Promedio: El objeto lo sabe calcular, no necesito sincronizar listas ni buscar índices. Esto es mucho más organizado y limpio.
promedio = ana.calcular_promedio()
print(f"El promedio de {ana.nombre} es: {promedio}") # 87.5

# Buscar: Una función de la academia puede buscar a Ana y devolver el objeto.
alumna = academia.buscar_estudiante("Ana Torres")

#Ordenar: Una línea de código para ordenar los estudiantes por promedio, sin tener que sincronizar listas ni buscar índices.
academia.ranking_estudiantes()

#Guardar: Una línea de código para guardar la información de los estudiantes en un JSON, sin tener que sincronizar listas manualmente.
academia.guardar_estudiantes_json()

"""
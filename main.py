from academia import Academia
from estudiante import Estudiante

def main():

    # Crear una instancia de la academia
    academia = Academia("Python Academy")

    # Agregar estudiantes a la academia
    estudiante1 = Estudiante("Juan Pérez", "juan@example.com", "2026-001")
    estudiante2 = Estudiante("María Gómez", "maria@example.com", "2026-002")
    estudiante3 = Estudiante("Carlos López", "carlos@example.com", "2026-003")

    # Agregar calificaciones a los estudiantes
    estudiante1.agregar_nota("Python", 50)
    estudiante1.agregar_nota("Java", 40)
    estudiante1.agregar_nota("JavaScript", 60)

    estudiante2.agregar_nota("Python", 75)
    estudiante2.agregar_nota("Java", 80)
    estudiante2.agregar_nota("JavaScript", 70)

    estudiante3.agregar_nota("Python", 60)
    estudiante3.agregar_nota("Java", 65)
    estudiante3.agregar_nota("JavaScript", 75)

    # Inscribir estudiantes en la academia
    academia.inscribir_estudiante(estudiante1)
    academia.inscribir_estudiante(estudiante2)
    academia.inscribir_estudiante(estudiante3)

    #mostrar la boleta de cada estudiante
    print("Boleta de Estudiantes:")
    print(estudiante1.boleta())
    print(estudiante2.boleta())
    print(estudiante3.boleta())

    # Mostrar el ranking de estudiantes
    ranking = academia.ranking_estudiantes()
    print("Ranking de Estudiantes:")
    for i, estudiante in enumerate(ranking, start=1):
        print(f"{i}. {estudiante.nombre} - Promedio: {estudiante.promedio_general():.2f} - Letra: {estudiante.letra()}")

if __name__ == "__main__":
    main()
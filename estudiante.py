import statistics
from persona import Persona

class Estudiante(Persona):

    MATERIAS = ["Python", "Java", "C++", "JavaScript", "SQL"]  # Lista de materias disponibles en la academia.
    """
    Un Estudiante es una persona(hereda nombre, email) que pertenece a la academia y además tiene calificaciones en diferentes cursos y matrícula.
    """
    def __init__(self, nombre, email, matricula):
        super().__init__(nombre, email)  # Llamar al constructor de la clase padre (Persona) para inicializar nombre y email.
        self.matricula = matricula.strip().upper()  # Eliminar espacios en blanco al inicio y al final además establezca en mayúscula.

        #Usamos Dict comprehension para crear una lista vacía en la academia por materia.
        self.notas: dict[str, list[float]] = {
            materia: [] for materia in self.MATERIAS
        }  # Diccionario para almacenar las notas de los cursos.

    def agregar_nota(self, materia, nota):
        # validación 1: ¿la materia existe en el plan de estudios?
        if materia not in self.MATERIAS:
            raise ValueError(f"La materia {materia} no existe.")

        # validación 2: ¿la nota está entre el rango de 0 y 100?
        if not (0 <= nota <= 100):
            raise ValueError("La nota {nota} debe estar entre 0 y 100.")

        # Agregar la nota a la lista de notas de la materia correspondiente.
        self.notas[materia].append(round(nota,2)) # Redondear la nota a 2 decimales y agregarla a la lista de notas

    def promedio_materia(self, materia):
        notas = self.notas.get(materia, [])
        return statistics.mean(notas) if notas else 0.0  # Calcular el promedio de las notas de la materia, si no hay notas, devolver 0.0

    def promedio_general(self):
        todas_las_notas = [nota for notas in self.notas.values() for nota in notas]
        return statistics.mean(todas_las_notas) if todas_las_notas else 0.0  # Calcular el promedio de todas las notas, si no hay notas, devolver 0.0

    def letra(self):
        promedio = self.promedio_general()
        """        
        if promedio >= 90:
            return "A"
        elif promedio >= 80:
            return "B"
        elif promedio >= 70:
            return "C"
        elif promedio >= 60:
            return "D"
        else:
            return "F"
        """
        return "A" if promedio >= 90 else "B" if promedio >= 80 else "C" if promedio >= 70 else "D" if promedio >= 60 else "F"

    def boleta(self):
        boleta = f"Boleta de Notas de {self.nombre} (Matrícula: {self.matricula})\n"
        boleta += "-" * 50 + "\n"
        for materia, notas in self.notas.items():
            promedio = self.promedio_materia(materia)
            boleta += f"{materia}: {notas} | Promedio: {promedio:.2f}\n"
        boleta += "-" * 50 + "\n"
        boleta += f"Promedio General: {self.promedio_general():.2f} | Letra: {self.letra()}\n"
        return boleta
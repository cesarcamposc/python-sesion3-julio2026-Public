"""
PLATAFORMA ACADEMICA CON PROGRAMACIÓN ORIENTADA A OBJETOS
Una academia de programación tiene 150 estudiantes. Todo se maneja en una hoja de excel, pero se quiere pasar a un sistema más organizado. Se desea crear un sistema que permita manejar la información de los estudiantes, sus cursos y calificaciones.

VOCABULARIO OOP
Clase: Es un molde o plantilla que define las propiedades y comportamientos de un objeto. En este caso, podríamos tener clases como "Estudiante", "Curso" y "Calificación".

Objeto: Es una instancia de una clase. Por ejemplo, un objeto de la clase "Estudiante" podría representar a un estudiante específico con su nombre, edad y calificaciones.

Atributo: Son las características o propiedades de una clase. Por ejemplo, la clase "Estudiante" podría tener atributos como "nombre", "edad" y "calificaciones".

Método: Son las funciones o comportamientos que una clase puede realizar. Por ejemplo, la clase "Estudiante" podría tener métodos como "agregar_calificación" o "calcular_promedio".

Herencia: Una clase "Hija" que hereda de una clase "Padre" puede acceder a los atributos y métodos de la clase padre. Por ejemplo, podríamos tener una clase "EstudianteAvanzado" que herede de la clase "Estudiante" y tenga métodos adicionales.

self: Es una referencia al objeto actual de la clase. Se utiliza para acceder a los atributos y métodos de la instancia actual.

__init__: El constructor de la clase, que se llama automáticamente cuando se crea un objeto. Se utiliza para inicializar los atributos del objeto.
"""

class Academia:
    """
    Contiene y gestiona la información de los estudiantes, cursos y calificaciones. Permite inscribir, buscar, ver el ranking y guardar la información de manera organizada.
    Relación: composición. La clase Academia contiene objetos de la clase Estudiante(tiene estudiantes, no hereda de ellos).
    """
    def __init__(self, nombre):
        self.nombre = nombre
        self.estudiantes = []  # Lista para almacenar los objetos de la clase Estudiante.

    def inscribir_estudiante(self, estudiante):
        """
        Inscribe un estudiante en la academia.
        """
        self.estudiantes.append(estudiante)

    def buscar_estudiante(self, nombre):
        """
        Busca un estudiante por su nombre y devuelve el objeto Estudiante correspondiente.
        """
        for estudiante in self.estudiantes:
            if estudiante.nombre == nombre:
                return estudiante
        return None  # Si no se encuentra el estudiante, devuelve None.

    def ranking_estudiantes(self):
        """
        Devuelve una lista de estudiantes ordenados por su promedio general de mayor a menor.
        """
        if not self.estudiantes:
            print("No hay estudiantes inscritos en la academia.")
            return []

        ordenados = sorted(
            self.estudiantes, 
            key=lambda e: e.promedio_general(), 
            reverse=True
        )
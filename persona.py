class Persona:

    """
    Clase Base o Padre. Todo el que pertenece a la academia es una persona, por lo que esta clase contendrá los atributos y métodos comunes a todos.

    Por qué existe: Evitar duplicar código cuando creamos las clases Estudiante y Instructor. Por ejemplo, ambos tienen un nombre, un correo y un ID, por lo que estos atributos se definen en la clase Persona y no en las clases hijas.
    """
    
    def __init__(self, nombre, email):
        #strip(): Eliminar espacios en blanco al inicio y al final.
        #title(): Poner la primera letra de cada palabra en mayúscula.
        self.nombre = nombre.strip().title()  # Eliminar espacios en blanco al inicio y al final.
        self.email = email.strip().lower()  # Eliminar espacios en blanco al inicio y al final y poner en minúscula.
        

    #def saludar(self):
    #    print(f"Hola, soy {self.nombre} y mi correo es {self.correo}")

    def __repr__(self):
        return f"{self.__class__.__name__}(nombre={self.nombre}, email={self.email})"



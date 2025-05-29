"""
Módulo para gestionar información de estudiantes.

Este módulo proporciona una clase para representar estudiantes,
sus calificaciones y operaciones relacionadas con su desempeño académico.
"""


class Student:
    """
    Representa a un estudiante con sus calificaciones y estado académico.    
    Esta clase permite gestionar la información de un estudiante,
    incluyendo sus datos personales, calificaciones, reconocimientos
    académicos y estado de aprobación.
    
    Attributes:
        student_id (str): Identificador único del estudiante.
        name (str): Nombre completo del estudiante.
        grades (list): Lista de calificaciones numéricas.
        is_passed (bool): Indica si el estudiante ha aprobado.
        honor (bool): Indica si el estudiante está en cuadro de honor.
        letter_grade (str): Calificación en formato de letra (A-F).
    """
    def __init__(self, student_id, name):
        """
        Inicializa un objeto Student con ID y nombre.
        
        Args:
            student_id (str): Identificador único del estudiante.
            name (str): Nombre completo del estudiante.
            
        Raises:
            ValueError: Si el ID o nombre están vacíos.
        """
        if not student_id or not name:
            raise ValueError("El ID y nombre del estudiante no pueden estar vacíos")
        
        self.student_id = student_id
        self.name = name
        self.grades = []
        self.is_passed = False
        self.honor = False
        self.letter_grade = None

    def add_grade(self, grade):
        """
        Añade una calificación a la lista de calificaciones del estudiante.
        
        Args:
            grade (float): La calificación a añadir (0-100).
            
        Raises:
            TypeError: Si la calificación no es un número.
            ValueError: Si la calificación está fuera del rango 0-100.
        """
        if not isinstance(grade, (int, float)):
            raise TypeError("La calificación debe ser un número")
        
        if grade < 0 or grade > 100:
            raise ValueError("La calificación debe estar en el rango 0-100")
            
        self.grades.append(grade)
        self._update_status()

    def calculate_average(self):
        """
        Calcula y retorna el promedio de calificaciones del estudiante.
        
        Returns:
            float: El promedio de calificaciones.
            None: Si no hay calificaciones registradas.
        """
        if not self.grades:
            return None

        total = 0
        for grade in self.grades:
            total += grade

        return total / len(self.grades)

    def get_letter_grade(self):
        """
        Determina la calificación en letra basada en el promedio numérico.
        
        Returns:
            str: Calificación en letra (A, B, C, D o F).
            None: Si no hay calificaciones registradas.
        """
        average = self.calculate_average()
        if average is None:
            return None
            
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"

    def _update_status(self):
        """
        Actualiza el estado del estudiante (letter_grade, is_passed, honor).
        
        Este método se invoca automáticamente cuando se modifica la lista
        de calificaciones.
        """
        average = self.calculate_average()
        if average is None:
            return
            
        # Actualizar calificación en letra
        self.letter_grade = self.get_letter_grade()
        
        # Actualizar estado de aprobación
        self.is_passed = average >= 60
        
        # Actualizar estado de honor
        self.honor = average >= 90

    def check_honor(self):
        """
        Determina si el estudiante merece honor basado en su promedio.
        
        Un promedio superior a 90 otorga honor al estudiante.
        No realiza ninguna acción si no hay calificaciones registradas.
        
        Returns:
            bool: True si el estudiante está en el cuadro de honor, False en caso contrario.
        """
        self._update_status()
        return self.honor

    def delete_grade(self, index=None, value=None):
        """
        Elimina una calificación por índice o valor.
        
        Args:
            index (int, optional): El índice de la calificación a eliminar.
            value (float, optional): El valor de la calificación a eliminar.
            
        Raises:
            IndexError: Si el índice está fuera de rango.
            ValueError: Si el valor no existe o si no se proporciona ni índice ni valor.
            
        Returns:
            bool: True si se eliminó la calificación correctamente.
        """
        if index is not None:
            if index < 0 or index >= len(self.grades):
                raise IndexError(
                    f"Índice {index} fuera de rango. "
                    f"Solo hay {len(self.grades)} calificaciones."
                )
            del self.grades[index]
            self._update_status()
            return True
            
        elif value is not None:
            if value in self.grades:
                self.grades.remove(value)
                self._update_status()
                return True
            else:
                raise ValueError(f"No se encontró la calificación {value}")
        else:
            raise ValueError("Debe proporcionar un índice o un valor para eliminar")

    def report(self):
        """
        Imprime un reporte completo con toda la información del estudiante.
        
        Muestra ID, nombre, cantidad de calificaciones, promedio final,
        calificación en letra, estado de aprobación y estado de honor.
        """
        print(f"ID: {self.student_id}")
        print(f"Nombre: {self.name}")
        print(f"Total de calificaciones: {len(self.grades)}")

        average = self.calculate_average()
        if average is not None:
            print(f"Calificación promedio: {average:.2f}")
            print(f"Calificación en letra: {self.get_letter_grade()}")
            print(f"Estado: {'Aprobado' if self.is_passed else 'Reprobado'}")
            print(f"Cuadro de honor: {'Sí' if self.honor else 'No'}")
        else:
            print("Calificación promedio: No disponible")
            print("Calificación en letra: No disponible")
            print("Estado: No disponible")
            print("Cuadro de honor: No")


def start_run():
    """
    Función de demostración que crea un estudiante
    y muestra sus funcionalidades.
    """
    try:
        # Crear un estudiante con datos de ejemplo
        estudiante = Student("S001", "Juan Pérez")
        
        # Agregar calificaciones
        estudiante.add_grade(85)
        estudiante.add_grade(92)
        estudiante.add_grade(78)
        
        # Demostrar el manejo de errores
        try:
            estudiante.add_grade(105)  # Fuera de rango
        except ValueError as e:
            print(f"Error controlado: {e}")
            
        try:
            estudiante.add_grade("Cincuenta")  # Tipo incorrecto
        except TypeError as e:
            print(f"Error controlado: {e}")
        
        # Mostrar reporte completo
        print("\n--- REPORTE DE ESTUDIANTE ---")
        estudiante.report()
        
        # Demostrar eliminación de calificación
        print("\n--- DESPUÉS DE ELIMINAR UNA CALIFICACIÓN ---")
        estudiante.delete_grade(value=92)  # Eliminar por valor
        estudiante.report()
        
    except Exception as e:
        print(f"Error inesperado: {e}")


if __name__ == "__main__":
    start_run()
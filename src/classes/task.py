import datetime

class Task:
    def __init__(self, description, responsibles):
        self.description = description[:150]  # Descripcion de max 150 carcteres
        self.responsibles = responsibles  #Miembros del tablero responsables
        self.creation_date = datetime.datetime.now().strftime('%d/%m/%Y %H:%M')  # Fecha de creación actual
        self.finish_date = None  # Fecha de fin inicialmente vacia
    
    def __str__(self):
        """Obtenga la tarea en texto"""
        return f"Task: {self.description}, Responsibles: {', '.join(self.responsibles)}, Created: {self.creation_date}, Finished: {self.finish_date}"

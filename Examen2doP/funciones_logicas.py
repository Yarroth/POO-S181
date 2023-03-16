import random
import datetime

class MatriculaGenerator:
    def __init__(self, nombre, apellido_paterno, apellido_materno, ano_nacimiento, carrera):
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.ano_nacimiento = ano_nacimiento
        self.carrera = carrera

    def generar_matricula(self):
        ano_actual = datetime.datetime.now().year % 100
        ano_nacimiento_2d = str(self.ano_nacimiento % 100).zfill(2)
        letra_nombre = self.nombre[0]
        letras_apellidos = self.apellido_paterno[:2] + self.apellido_materno[:2]
        digitos_aleatorios = str(random.randint(0, 99)).zfill(2)
        letras_carrera = self.carrera[:3]

        matricula = f"{ano_actual}{ano_nacimiento_2d}{letra_nombre}{letras_apellidos}{digitos_aleatorios}{letras_carrera}"
        return matricula

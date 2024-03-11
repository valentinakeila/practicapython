from profesional import Profesional
from concurso import Concurso
from inscripcion import Inscripcion
from titulo import Titulo
from datetime import *

# Inicializo una lista vacía para almacenar las inscripciones
inscripciones = []

# Creo un profesional (aspirante)
aspirante = Profesional("Juan", "Perez", "42704897")

# Creo los títulos
titulos = [
    Titulo("Ingeniero Mecánico", 1),
    Titulo("Contador Público Nacional", 2),
    Titulo("Ingeniería Civil Mecanica", 3)
]



# Creo los concursos
concursos = [
    Concurso("Maestria en Ciencia de los Materiales"),
    Concurso("Doctorado en Finanzas"),
    Concurso("Letras") ]






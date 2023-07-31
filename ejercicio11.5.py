"""
    Crear las clases Materia y Carrera, que se comporten según el siguiente ejemplo:
    >>> analisis2 = Materia("61.03", "Análisis 2", 8)
    >>> fisica2 = Materia("62.01", "Física 2", 8)
    >>> algo1 = Materia("75.40", "Algoritmos 1", 6)
    >>> c = Carrera([analisis2, fisica2, algo1])
    >>> str(c)
    Créditos: 0 -- Promedio: N/A -- Materias aprobadas:
    >>> c.aprobar("95.14", 7)
    ValueError: La materia 95.14 no es parte del plan de estudios
    >>> c.aprobar("75.40", 10)
    >>> c.aprobar("62.01", 7)
    >>> str(c)
    Créditos: 14 -- Promedio: 8.5 -- Materias aprobadas:
    75.40 Algoritmos 1 (10)
    62.01 Física 2 (7)
"""


def esta_materia(lista_materia,codigo_materia):
    
    error = False
    mate = ''

    for materia in lista_materia:
        if codigo_materia == materia.codigo:
            error = True
            mate = materia
            return error, mate
            
    return error, mate


def string_materias_aprobadas(materias_aprobadas):
    
    cadena = ""

    for materia, nota in materias_aprobadas:
        cadena += (f"{materia.codigo} {materia.nombre} ({nota})\n")
    
    return cadena

class Materia:
    def __init__(self, codigo: str, nombre: str, creditos: float):
        self.codigo = codigo
        self.nombre = nombre
        self.creditos = creditos
        
    def __str__(self):
        return (f"Código materia: '{self.codigo}' | Nombre materia: '{self.nombre}' | Créditos materia: {self.creditos}")


class Carrera:
    def __init__(self, lista_materias: list, total_creditos=0 , total_notas=0, promedio="N/A", materias_aprobadas=[]):
        self.lista_materias = lista_materias
        self.total_creditos = total_creditos
        self.promedio = promedio
        self.total_notas = total_notas
        self.materias_aprobadas = materias_aprobadas

    def __str__(self):
        cadena = string_materias_aprobadas(self.materias_aprobadas)
        return (f"Créditos: {self.total_creditos} -- Promedio: {self.promedio:.3} -- Materias aprobadas:\n{cadena}") 
        
        
        
    def aprobar(self, codigo_materia, nota_materia):

        error, materia = esta_materia(self.lista_materias,codigo_materia)
        
        if not error:
            print(f"ValueError: La materia {codigo_materia} no es parte del plan de estudios.\n")
        else:
            self.materias_aprobadas.append((materia, nota_materia))
            self.total_notas = self.total_notas + nota_materia
            self.total_creditos = self.total_creditos + materia.creditos
            self.promedio = self.total_notas / len(self.materias_aprobadas)

            
            
            


analisis2 = Materia("61.03", "Análisis 2", 8)
fisica2 = Materia("62.01", "Física 2", 8)
algo1 = Materia("75.40", "Algoritmos 1", 6)
c = Carrera([analisis2, fisica2, algo1])


print(c)
c.aprobar("95.14", 7)
c.aprobar("75.40", 10)
print(c)
c.aprobar("62.01", 7)
print(c)
c.aprobar("61.03", 5)
print(c)

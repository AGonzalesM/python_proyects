'''
Ejercicio 1: Transformación y Filtrado de Listas

Dada una lista de tuplas donde cada tupla contiene un nombre y una edad,
crea una nueva lista que contenga solo los nombres de las personas que son mayores de 18 años,
pero convierte esos nombres a mayúsculas.
'''
personas = [("Ana", 17), ("Pedro", 23), ("Luis", 15), ("Maria", 19)]
personas_mayores = [name.upper() for name, edad in personas if edad > 18]
print(personas_mayores)

'''
Ejercicio 2: Generación de un Diccionario de Frecuencias

Dada una lista de palabras, crea un diccionario donde las claves sean las palabras y los valores sean la cantidad de veces que esa palabra aparece en la lista,
pero solo incluye en el diccionario las palabras que aparezcan más de una vez.
'''
palabras = ["python", "java", "python", "c", "c++", "java", "c"]
from collections import Counter
counter_palabras = {palabra: cantidad for palabra, cantidad in Counter(palabras).items() if cantidad > 1}
print(counter_palabras)

'''
Ejercicio 3: Diccionario de Longitudes de Palabras

Dado un texto, crea un diccionario donde las claves sean las palabras del texto y los valores sean la longitud de esas palabras,
pero solo incluye en el diccionario las palabras que tienen más de 3 letras.
'''
texto = "El rápido zorro marrón salta sobre el perro perezoso"
dict_palabras = {palabra: len(palabra) for palabra in texto.split() if len(palabra) > 3}
print(dict_palabras)

'''
Ejercicio 4: Filtrado y Transformación de Números en Listas Anidadas

Dada una lista de listas que contiene números enteros, genera una nueva lista que contenga la suma de los números pares de cada sublista.
'''
numeros = [[1, 2, 3, 4], [10, 11, 12, 13], [7, 8, 9]]
suma_items_pares = [sum(num for num in sublista if num % 2 == 0) for sublista in numeros]
print(suma_items_pares)
#Opcion 2
#import functools
#suma_items_pares = list(map(lambda item_numbers: functools.reduce(lambda a, b: a + b, item_numbers) ,numeros))


'''
Ejercicio 5: Anidación Compleja de Diccionarios

Dado un diccionario donde las claves son los nombres de los estudiantes y los valores son diccionarios con las asignaturas y sus calificaciones,
genera un nuevo diccionario que contenga solo los estudiantes que aprobaron todas sus asignaturas (nota >= 5), mostrando sus nombres y sus asignaturas aprobadas.
'''
calificaciones = {
    "Ana": {"matemáticas": 6, "historia": 4, "biología": 5},
    "Pedro": {"matemáticas": 8, "historia": 7, "biología": 6},
    "Luis": {"matemáticas": 3, "historia": 5, "biología": 4},
    "Maria": {"matemáticas": 7, "historia": 9, "biología": 6},
}

def cursos_aprobados(cursos):
    return all(nota >= 5 for nota in cursos.values())

estudiantes_aprobados = {estudiante: cursos for estudiante, cursos in calificaciones.items() if cursos_aprobados(cursos)}
print(estudiantes_aprobados)
'''
def cursos_aprobados(cursos):
    for nota in cursos.values():
        if nota < 5:
            return False
    return True
estudiantes_aprobados = {estuiante: curso for estuiante, curso in calificaciones.items() if cursos_aprobados(curso)}
print(estudiantes_aprobados)
'''
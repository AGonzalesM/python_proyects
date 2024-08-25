'''
Ejercicio 1: Filtrado de Palabras con Múltiples Condiciones

Dada una lista de palabras, crea una nueva lista que contenga solo las palabras que comienzan y terminan con la misma letra, pero también filtra las palabras que tienen más de 4 letras.
'''
palabras = ["aroma", "anaconda", "civic", "python", "solos", "java", "aa", "aba"]
palabras_misma_letra = [palabra for palabra in palabras if palabra[0] == palabra[-1] and len(palabra) > 4]

print(palabras_misma_letra)
'''
Ejercicio 2: Diccionario Invertido

Dado un diccionario donde las claves son nombres de personas y los valores son sus edades,
genera un nuevo diccionario donde las edades son las claves y los valores son listas de nombres de personas que tienen esa edad.
'''
edades = {"Ana": 23, "Pedro": 34, "Maria": 23, "Luis": 40, "Laura": 34}
edades_personas = {edad: [nombre for nombre, e in edades.items() if e == edad] for edad in set(edades.values())}
print(edades_personas)
'''
Ejercicio 3: Lista de Productos Cruzados

Dadas dos listas de números, genera una lista que contenga todas las posibles sumas de un número de la primera lista y un número de la segunda lista,
pero solo incluye las sumas que sean pares.
'''
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

suma_listas = [n1 + n2 for n1 in lista1 for n2 in lista2 if (n1 + n2) % 2 == 0]
print(suma_listas)
'''
Ejercicio 4: Transformación de Diccionario de Listas

Dado un diccionario donde las claves son categorías y los valores son listas de números, genera un nuevo diccionario donde las claves son las mismas,
pero los valores son la suma de los números de cada lista, solo si la suma es un número impar.
'''
categorias = {"a": [1, 2, 3], "b": [4, 5, 6], "c": [7, 8, 9], "d": [10, 11, 12]}
suma_categorias = {x: sum(y) for x, y in categorias.items() if sum(y) % 2 != 0}
print(suma_categorias)
'''
Ejercicio 5: Mapeo Condicional de Nombres

Dado un diccionario donde las claves son nombres y los valores son listas de calificaciones,
genera un nuevo diccionario donde las claves son los nombres y los valores son "Aprobado" o "Reprobado" dependiendo de si la calificación promedio es mayor o igual a 5.5.
'''
calificaciones = {"Ana": [6, 7, 8], "Pedro": [4, 5, 6], "Luis": [3, 4, 4], "Maria": [9, 8, 7]}
calificaciones_finales = {nombre: ('Aprobado' if sum(lista_nota) / len(lista_nota) >= 5.5 else 'Reprobado') for nombre, lista_nota in calificaciones.items()}
print(calificaciones_finales)
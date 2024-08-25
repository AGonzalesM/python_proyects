#Ejercicio 1: Operaciones Básicas con Listas
#Crea una lista de números enteros que contenga los números del 1 al 10.
#Luego, realiza las siguientes operaciones:
numero_entero = list(range(1, 11))
print(numero_entero)
#Añade el número 11 al final de la lista.
numero_entero.append(11)
print(numero_entero)
#Inserta el número 0 al inicio de la lista.
numero_entero.insert(0, 0)
print(numero_entero)
#Elimina el tercer elemento de la lista.
numero_entero.pop(2)
print(numero_entero)
#Encuentra el índice del número 7.
index_siete = numero_entero.index(7)
print(index_siete)
#Ordena la lista en orden descendente.
numero_entero.sort(reverse=True)
print(numero_entero)

#Ejercicio 2: Contando Palabras con Diccionarios
#Dado un texto, cuenta cuántas veces aparece cada palabra en él y almacena los resultados en un diccionario.
#Luego, muestra la palabra que más veces se repite y cuántas veces aparece.
texto = "El aprendizaje automático es fascinante y el aprendizaje profundo es aún más fascinante"
from collections import Counter
print(texto.split())
print(Counter(texto.lower().split()).most_common(1))
'''
#opcion 2
texto = texto.lower()
palabras_no_duplicadas = list(set(texto.split(" ")))
contando_palabras = []
for palabra in palabras_no_duplicadas:
    contando_palabras.append(texto.count(palabra))

dicts = dict(zip(palabras_no_duplicadas, contando_palabras))
print(dicts)
print(max(dicts, key=dicts.get))
'''

#Ejercicio 3: Operaciones con Conjuntos
#Crea dos conjuntos de números enteros:
# Conjunto A: {1, 2, 3, 4, 5, 6, 7}   Conjunto B: {5, 6, 7, 8, 9, 10}
#Realiza las siguientes operaciones:
A = {1, 2, 3, 4, 5, 6, 7}
B = {5, 6, 7, 8, 9, 10}
#Encuentra la intersección de los dos conjuntos.
print(A.intersection(B))
#Encuentra la unión de los dos conjuntos.
print(A.union(B))
#Encuentra la diferencia entre el Conjunto A y el Conjunto B.
print(A - B)
#Comprueba si el Conjunto A es un subconjunto del Conjunto B.
print(B.issuperset(A))

#Ejercicio 4: Filtrando Elementos en una Lista
#Dada una lista de números enteros, filtra los números que son múltiplos de 3 y almacénalos en una nueva lista.
#Luego, elimina cualquier duplicado de esa lista usando conjuntos y devuelve el resultado final ordenado.

lista_inicial = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 3, 9, 15]
#lista_multi_tres = list(filter(lambda item: item % 3 == 0,lista_inicial))
lista_multi_tres = sorted({x for x in lista_inicial if x % 3 == 0})
print(lista_multi_tres)
#lista_no_duplicados = sorted(set(lista_multi_tres))
#print(lista_no_duplicados)

#Ejercicio 5: Combinando Listas y Diccionarios
#Dada una lista de nombres y una lista de edades, crea un diccionario que asocie cada nombre con su edad correspondiente.
#Luego, realiza lo siguiente:
Nombres = ["Ana", "Pedro", "Luis", "Maria"]
Edades = [28, 34, 22, 30]
personas = dict(zip(Nombres, Edades))
print(personas)
#Añade una nueva entrada con el nombre "Carlos" y edad 29.
personas.update({'Carlos': 29})
print(personas)
#Modifica la edad de "Ana" a 32.
#personas.update({'Ana': 32})
personas['Ana'] = 32
print(personas)
#Elimina a "Pedro" del diccionario.
personas.pop('Pedro')
print(personas)
#Muestra todos los nombres que tienen una edad mayor a 25.
personas_mayores = {key: values for key, values in personas.items() if values > 25}
print(personas_mayores)
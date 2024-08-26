'''
Ejercicio 1: Análisis de Ventas por Producto

Objetivo: Determinar cuál es el producto más vendido en términos de cantidad y en términos de valor total de ventas.
Instrucciones:

    Carga los datos de ventas_ropa.csv en un DataFrame.
    Agrupa los datos por el campo Producto y calcula la cantidad total vendida para cada producto.
    Agrupa los datos por el campo Producto y calcula el valor total de ventas para cada producto.
    Determina el producto con la mayor cantidad vendida y el de mayor valor total de ventas.
'''
import pandas as pd
df = pd.read_csv('./datos.csv')

#df_groupby_product = df.groupby('Producto')
#df_cantidad_product = df_groupby_product['Cantidad'].sum()
#df_venta_product = df_groupby_product['Total Venta'].sum()
#print(f'El producto {df_cantidad_product.idxmax()} tiene la mayor cantidad vendida con {df_cantidad_product.max()} prendas vendidas')
#print(f'El producto {df_venta_product.idxmax()} tiene el mayor importe de venta vendida con {df_venta_product.max()} soles')

df_summary = df.groupby('Producto').agg({
    'Cantidad': 'sum',
    'Total Venta': 'sum'
})
print(df_summary)
print(f'El producto {df_summary["Cantidad"].idxmax()} tiene la mayor cantidad vendida con {df_summary["Cantidad"].max()} prendas vendidas')
print(f'El producto {df_summary["Total Venta"].idxmax()} tiene el mayor importe de venta con {df_summary["Total Venta"].max()} soles')


'''
Ejercicio 2: Análisis de Clientes Frecuentes

Objetivo: Identificar a los clientes que han realizado más de una compra en la tienda.
Instrucciones:

    Carga los datos de ventas_ropa.csv en un DataFrame.
    Agrupa los datos por Documento y cuenta el número de transacciones por cada cliente.
    Filtra los clientes que tienen más de una compra.
    Muestra la lista de clientes frecuentes y el número de transacciones que realizaron.
'''

df_counting_documento = df.groupby('Documento').size()
clientes_frecuentes = df_counting_documento[df_counting_documento > 1]
print(clientes_frecuentes)

'''
Ejercicio 3: Análisis de Descuentos

Objetivo: Calcular el porcentaje promedio de descuento aplicado en las ventas y determinar cuántas ventas tuvieron algún descuento aplicado.
Instrucciones:

    Carga los datos de ventas_ropa.csv en un DataFrame.
    Calcula el porcentaje promedio de descuento sobre el precio total.
    Filtra las ventas donde se haya aplicado algún descuento (es decir, donde el campo Descuento sea mayor a 0).
    Cuenta cuántas ventas tuvieron descuento y calcula el porcentaje respecto al total de ventas.
'''

df_promedio_descuento = df['Descuento'].mean()
df_ventas_con_descuento = df[df['Descuento'] > 0]
df_cantidad_ventas_descuento = df_ventas_con_descuento.shape[0]  # Forma correcta de contar las ventas con descuento
df_total_ventas = df.shape[0]
porcentaje_ventas_descuento = (df_cantidad_ventas_descuento / df_total_ventas) * 100

print(f'Promedio de descuento: {df_promedio_descuento}')
print(f'Cantidad de ventas con descuento: {df_cantidad_ventas_descuento}')
print(f'Porcentaje de ventas con descuento: {porcentaje_ventas_descuento:.2f}%')

'''
Ejercicio 4: Ventas por Mes

Objetivo: Analizar las ventas mensuales para identificar tendencias.
Instrucciones:

    Supón que los datos incluyen un campo de fecha de la venta (puedes agregar este campo o generar uno aleatorio).
    Carga los datos en un DataFrame.
    Agrupa las ventas por mes y suma el total de ventas (Total Venta) para cada mes.
    Crea un gráfico de barras que muestre el total de ventas por mes.
'''
import matplotlib.pyplot as plt
import numpy as np

num_records = 48
# Definir un rango de fechas
fecha_inicio = pd.to_datetime('2023-01-01')
fecha_fin = pd.to_datetime('2023-12-31')
# Generar fechas aleatorias dentro del rango definido
#fechas_aleatorias = pd.to_datetime(np.random.uniform(fecha_inicio.value, fecha_fin.value, num_records), unit='ns')
# Generar fechas secuenciales uniformemente distribuidas
fechas_uniformes = pd.date_range(start=fecha_inicio, end=fecha_fin, periods=num_records)
# Agregar algo de variabilidad aleatoria (por ejemplo, +/- 5 días)
variabilidad_dias = np.random.randint(-5, 6, size=num_records)
fechas_finales = fechas_uniformes + pd.to_timedelta(variabilidad_dias, unit='D')
# Asignar la columna de fechas generadas al DataFrame existente
df['Fecha Venta'] = fechas_finales

# Convertir la columna 'Fecha Venta' a formato de fecha
#df['Fecha Venta'] = pd.to_datetime(df['Fecha Venta'])
# Crear una nueva columna 'Mes' que contenga el mes y el año
df['Mes'] = df['Fecha Venta'].dt.to_period('M')
# Agrupar por la columna 'Mes' y sumar el 'Total Venta'
ventas_mensuales = df.groupby('Mes')['Total Venta'].sum()
# Crear un gráfico de barras de las ventas mensuales
ventas_mensuales.plot(kind='bar', figsize=(10, 6))
plt.title('Ventas Mensuales')
plt.xlabel('Mes')
plt.ylabel('Total de Ventas (Soles)')
plt.xticks(rotation=45)
plt.show()

'''
Ejercicio 5: Análisis de Impuestos Recaudados

Objetivo: Calcular el total de impuestos recaudados por la tienda y el promedio de impuestos por venta.
Instrucciones:

    Carga los datos de ventas_ropa.csv en un DataFrame.
    Suma el valor total de la columna Impuesto para obtener el total recaudado.
    Calcula el promedio de impuestos por venta.
    Muestra los resultados obtenidos.
'''

df_impuestos_recaudados = df['Impuesto'].sum()
df_promedio_impuestos = df['Impuesto'].mean()
print(f'El importe total de los impuestos recaudados son: {df_impuestos_recaudados}')
print(f'El promedio de los impuestos recaudados son: {df_promedio_impuestos}')


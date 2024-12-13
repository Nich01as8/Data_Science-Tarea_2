# Importamos la librería math
import math

# Cuartiles y percentiles
# Definimos la función que calcula el cuartil
def cuartil(datos, q):
    """
    Resumen: Calcula el cuartil de un conjunto de datos.
    
    Args:
        - datos (list): lista de datos numéricos.
        - q (int): número de cuartil a calcular.
        - vals (list): Lista de valores finitos (revisados por math.isfinite(v) en un bucle for).
        - bloque if: Después de revisar si los datos son integers, se calcula la posición del cuartil.
        
    Returns:
        float: retorna el cuartil de los datos.
        """
    # Revisamos si los datos son valores finitos.
    vals = []
    for v in datos:
        if math.isfinite(v):
            vals.append(v)
    
    # Ordenamos los datos
    vals.sort()
    
    # Calculamos el cuartil
    n = len(vals)
    pos = (n + 1) * q / 4
    if type(pos) == int:
        return vals[int(pos) - 1]
    else:
        k = int(pos)
        return (vals[k - 1] + vals[k]) / 2

# Definimos la función que calcula el percentil
def percentil(datos, p):
    """
    Resumen: Calcula el percentil de un conjunto de datos.
    
    Args:
        - datos (list): lista de datos numéricos.
        - p (int): número de percentil a calcular.
        - vals (list): Lista de valores finitos (revisados por math.isfinite(v) en un bucle for).
        - bloque if: Después de revisar si los datos son integers, se calcula la posición del percentil.
    Returns:
        float: retorna el percentil de los datos.
        """
    # Revisamos si los datos son valores finitos.
    vals = []
    for v in datos:
        if math.isfinite(v):
            vals.append(v)
    
    # Ordenamos los datos
    vals.sort()
    
    # Calculamos el percentil
    n = len(vals)
    pos = (n * p) / 100         # posición del percentil
    if type(pos) == int:        # si la posición es un entero, retornamos el valor en esa posición.
        return vals[int(pos) - 1]
    else:                       # si la posición no es un entero, retornamos el promedio de los valores
        k = int(pos)            # en las posiciones k y k+1.
        return (vals[k - 1] + vals[k]) / 2
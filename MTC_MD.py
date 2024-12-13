# Importamos la librería math
import math

# Medidas de tendencia central
# Definimos la función que calcula la media aritmética
def media(datos: list):
    """
    Resumen: Calcula la media aritmética de un conjunto de datos cualquiera.

    Args:
        datos (list): lista de datos numéricos tipo integer o float. Ej: [1, 2, 3, 4, 5]
        vals (list): Lista de valores finitos (revisados por math.isfinite(v) en un bucle for).
    Returns:
        float: Retorna la media aritmética de los datos.
    """
    # Revisamos si los datos son valores finitos.
    vals = []
    for v in datos:
        if math.isfinite(v):
            vals.append(v)
    
    return sum(vals)/len(vals)

# Definimos la función que calcula la mediana
def mediana(datos: list):
    """
    Resumen: Calcula la mediana de un conjunto de datos cualquiera.
    
    Args:
        - datos (list): lista de datos numéricos
        - vals (list): Lista de valores finitos (revisados por math.isfinite(v) en un bucle for).
        - n (int): Número de datos en la lista.
        - Bloque if: Revisamos si el número de datos es par o impar. Para ambos casos, se calcula la mediana.
        
    Returns:
        float: Retorna la mediana de los datos.
    """
    
    # Revisamos si los datos son valores finitos.
    vals = []
    for v in datos:
        if math.isfinite(v):
            vals.append(v)
    
    vals.sort()
    n = len(vals)
    if n % 2 == 0:
        mediana = (vals[n//2 - 1] + vals[n//2]) / 2
    else:
        mediana = vals[n//2]
        
    return mediana

# Definimos la función que calcula la moda
def moda(datos: list):
    """
    Resumen: Calcula la moda de un conjunto de datos cualquiera.

    Args:
        - datos (list): lista de datos numéricos
        - vals (list): Lista de datos. Si estos son integers, floats o strings, se añaden a la lista.
        - categorias (list): Lista de categorías únicas en los datos.
        - cuentas (list): Lista de cuentas de cada categoría.
        - bucle for: Itera sobre las categorías para contar cuántas veces aparece cada una.
        Se añade el número de veces que aparece cada categoría a la lista cuentas.
        - val_max (int): Número máximo de veces que aparece una categoría.
        - modas (list): Lista de modas.
        - bucle for: Itera sobre las categorías para añadir a la lista modas las categorías que aparecen.
        
    Returns:
        list: Retorna la moda de los datos.
        """
    vals = [v for v in datos if isinstance(v, (int, float, str))]
    
    categorias = list(set(vals))
    cuentas = []
    
    for c in categorias:
        n = 0
        for val in vals:
            if val == c:
                n += 1
        cuentas.append(n)
    
    val_max = max(cuentas)
    modas = []
    for i in range(len(categorias)):
        if cuentas[i] == val_max:
            modas.append(categorias[i])
    return modas


# Medidas de dispersión
# Definimos la función que calcula el rango
def rango(datos: list):
    """
    Resumen: Calcula el rango de un conjunto de datos cualquiera.
    
    Args:
        - datos (list): lista de datos numéricos.
        - vals (list): Lista de valores finitos (revisados por math.isfinite(v) en un bucle for).
        
    Returns:
        float: Retorna el rango de los datos.
    """
    # Revisamos si los datos son valores finitos.
    vals = []
    for v in datos:
        if math.isfinite(v):
            vals.append(v)
    
    return max(vals) - min(vals)

# Definimos la función que calcula la varianza
def varianza(datos: list):
    """
    Resumen: Calcula la varianza de un conjunto de datos cualquiera.

    Args:
        - datos (list): lista de datos numéricos.
        - vals (list): Lista de valores finitos (revisados por math.isfinite(v) en un bucle for).
        - media_datos (float): Media aritmética de los datos (calculada por la función media(datos)).
        - varianza (float): Varianza de los datos.
        
    Returns:
        float: Retorna la varianza de los datos.
    """
    # Revisamos si los datos son valores finitos.
    vals = []
    for v in datos:
        if math.isfinite(v):
            vals.append(v)
    
    media_datos = media(vals)
    varianza = sum((val - media_datos)**2 for val in vals) / len(vals)
    
    return varianza

# Definimos la función que calcula la desviación estándar
def desviacion_estandar(datos: list):
    """
    Resumen: Calcula la desviación estándar de un conjunto de datos cualquiera.
    
    Args:
        - datos (list): lista de datos numéricos.
        - vals (list): Lista de valores finitos (revisados por math.isfinite(v) en un bucle for).
        - varianza_datos (float): Varianza de los datos (calculada por la función varianza(datos)).
        
    Returns:
        float: Retorna la desviación estándar de los datos.
    """
    # Revisamos si los datos son valores finitos.
    vals = []
    for v in datos:
        if math.isfinite(v):
            vals.append(v)
    
    return math.sqrt(varianza(vals))

# Definimos la función que calcula la MAD
def mad(datos: list):
    """
    Resumen: Calcula la desviación absoluta mediana (MAD, en ingles) de un conjunto de datos cualquiera.

    Args:
        - datos (list): lista de datos numéricos.
        - vals (list): Lista de valores finitos (revisados por math.isfinite(v) en un bucle for).
        - median_datos (float): Mediana de los datos.
        - mad (float): MAD de los datos.
        
    Returns:
        float: Retorna la MAD de los datos.
    """
    # Revisamos si los datos son valores finitos.
    vals = []
    for v in datos:
        if math.isfinite(v):
            vals.append(v)
    
    median_datos = mediana(vals)
    mad = sum(abs(val - median_datos) for val in vals) / len(vals)
    
    return mad

# Definimos la funcion que calcula la covarianza
def covarianza(datos1: list, datos2: list):
    """
    Resumen: Calcula la covarianza de dos conjuntos de datos cualquiera.
    
    Args:
        - datos1 (list): lista de datos numéricos.
        - datos2 (list): lista de datos numéricos.
        - vals1 (list): Lista de valores finitos (revisados por math.isfinite(v) en un bucle for).
        - vals2 (list): Lista de valores finitos (revisados por math.isfinite(v) en un bucle for).
        - media_datos1 (float): Media aritmética de los datos 1 (calculada por la función media(datos1)).
        - media_datos2 (float): Media aritmética de los datos 2 (calculada por la función media(datos2)).
        - covarianza (float): Covarianza de los datos.
        
    Returns:
        float: Retorna la covarianza de los datos.
    """
    vals1 = []
    for v in datos1:
        if math.isfinite(v):
            vals1.append(v)

    vals2 = []
    for v in datos2:
        if math.isfinite(v):
            vals2.append(v)

    n = len(vals1)
    media_datos1 = media(vals1)
    media_datos2 = media(vals2)
    covarianza = (1 / n) * sum((vals1[i] - media_datos1) * (vals2[i] - media_datos2) for i in range(n))
    
    return covarianza









# Para importar un archivo desde una carpeta:






# a) import foldername.filename desde una terminal Python.
# b) from foldername.filename import functionname1, functionname2, 
# functionname3 para importar funciones específicas desde un archivo.
edades = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# a
edades.sort()
edad_minima = min(edades)
edad_maxima = max(edades)
print("Lista ordenada:", edades)
print("Edad mínima:", edad_minima)
print("Edad máxima:", edad_maxima)

# b
edades.append(edad_minima)
edades.append(edad_maxima)
print("Lista con edad mínima y máxima añadidas:", edades)

# c
n = len(edades)
if n % 2 == 0:
    mediana = (edades[n // 2 - 1] + edades[n // 2]) / 2
else:
    mediana = edades[n // 2]
print("Edad mediana:", mediana)

# d
promedio = sum(edades) / len(edades)
print("Edad promedio:", promedio)

# e
rango = edad_maxima - edad_minima
print("Rango de edades:", rango)

# f
diferencia_minima = abs(edad_minima - promedio)
diferencia_maxima = abs(edad_maxima - promedio)
print("Diferencia absoluta (mínimo - promedio):", diferencia_minima)
print("Diferencia absoluta (máximo - promedio):", diferencia_maxima)

# ejercicio 02
frase = "Soy profesor y me encanta inspirar y enseñar a la gente"

palabras = frase.split()          # Dividir la frase en palabras

palabras_unicas = set(palabras)   # Usar un conjunto para obtener palabras únicas

numero_palabras_unicas = len(palabras_unicas)  # Contar las palabras únicas

print("Número de palabras únicas:", numero_palabras_unicas)

# ejercicio 03

l1 = [("one", 1), ("two", 2), ("three", 3), ("four", 4), ("five", 5)]
l2 = [("one", 1), ("two", 2), ("six", 6)]

# a. Crear conjuntos
s1 = set(l1)
s2 = set(l2)

# b. Encontrar elementos comunes
s3 = s1.intersection(s2)

# c. Encontrar elementos únicos
s4 = s1.symmetric_difference(s2)

# d. Crear lista l3 ordenada
l3 = sorted(s3.union(s4), key=lambda x: x[1])

print("s1:", s1)
print("s2:", s2)
print("s3 comunes:", s3)
print("s4 únicos:", s4)
print("l3 ordenada:", l3)
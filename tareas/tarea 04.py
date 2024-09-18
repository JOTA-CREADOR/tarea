# ejercicio 01
'''suma de numeros pares:
 la suma de todos los numeros pares dede 2 hasta N'''

N = int(input('ingrese un numero positivo: '))
suma = 0
i = 2
while i <= N:
    suma += i
    i += 2
print(f"la suma de pares desde 2 hasta {N} es: ",suma)

# ejercicio 02
#conjetura de collatz

entero = int(input('ingrese un numero positivo: '))
print(f'la conjetura de collatz para {entero} es: ')
while entero != 1:
    print(entero,end= ' ')
    if entero % 2 ==0:
        entero = entero // 2
    else:
        entero= 3 *entero + 1
print(1)

# ejercicio 03
'''Tabla de Multiplicar con for:
Pide al usuario un número entero positivo. Imprime la tabla de multiplicar de ese número
utilizando un bucle for.'''

n = int(input('ingrese un numero positivo: '))

for i in range(1,6):      # de 1 al 5 
    resultado = n * i
    print(f'{n} x {i} = {resultado}')

# ejercicio 04
'''Imprimir Patrón de Triángulo:
Pide al usuario un número entero positivo 'n'. Imprime un triángulo de asteriscos con 'n' filas
utilizando un bucle for anidado.'''

numero = int(input('ingrese un numero positivo: '))
for i in range(1,numero +1):
    for j in range(i):
        print('*', end=' ')
    print()

# ejercicio 05
# conteo de vocales en una frase
frase = input('ingresa una frase: ')
contador = 0
vocales = "aeiouAEIOU"
for v in frase:
    if v in vocales:
        contador += 1
print(f'el numero de vocales es: {contador}')

# ejercico 06
# Suma de Dígitos
usuario = int(input('ingrese un numero positivo: '))
suma_digitos = 0
while usuario > 0:
    digito = usuario % 10
    suma_digitos += digito
    usuario//= 10
print(f'la suma de digitos es: {suma_digitos}')

# ejercicio 07
# Invertir una Cadena
cadena = input('ingrese una cadena: ')
invierte =" "
for i in cadena:
    invierte = i + invierte
print('la cadena invertida es: ',invierte)

# ejercicio 08
# Número de Fibonacci
num = int(input('ingrese un numero positivo: '))
x,y = 0,1
for i in range(num):
    x,y = x,x+y

    print(f'el enésimo número de Fibonacci para{num}es:',x)

# ejercicio 09
# Verificar si una Cadena es Palíndromo:
cad = input('ingrese una cadena: ')
invert = ""
for y in cad:
    invert = y + invert
    if cad == invert:
        print('es palindroma')
    else:
        print('no es palindroma')

# ejercicio 10 
# Calculadora de Promedio
entrada = input("Introduce una serie de números separados por comas: ")

numeros= entrada.split(',')

suma = 0
contador = 0

for numero in numeros:
    suma += float(numero)
    contador += 1   

if contador > 0:
    promedio = suma / contador
    print(f"El promedio de los números es: {promedio}")
else:
    print("No se introdujeron números válidos.")
print()
print()
print('----------------------------------------')
print('----------     CALCULADORA    ----------')
print('----------------------------------------')
print()
print()
print('  "Para realizar la operacion deseada, \n      sigue las instrucciones: -->"')
print()
print()
print(' *** Si deseas sumar ingresa el signo -------->    + ')
print(' *** Si deseas restar ingresa el signo ------->    - ')
print(' *** Si deseas multiplicar ingresa el signo -->    * ')
print(' *** Si deseas dividir ingresa el signo ------>    / ')
print()
print()
print()

operadores = ['+', '-', '*', '/']

operacion = input('Ingresa el simbolo de la operacion a realizar: \n')

while operacion not in operadores:
    print('Error -> No es una operación reconocida, trata de nuevo')
    operacion = input('Ingresa el simbolo de la operacion a realizar: \n')

while True:
    try:
        valor1 = input('Ingresa el primer valor de la operación: \n')
        valor1 = float(valor1)

    except ValueError:
        print('debiste poner un número')

    else:
        break

while True:
    try:
        valor2 = input('Ingresa el segundo valor de la operación: \n')
        valor2 = float(valor2)

    except ValueError:
        print('debiste poner un número')

    else:
        break

if operacion == '+':
    mas = valor1 + valor2
    print('El resultado de la suma de {} más {} es {}'.format(valor1, valor2, mas))

elif operacion == '-':
    menos = valor1 - valor2
    print('El resultado de la resta {} menos {} es {}'.format(valor1, valor2, menos))

elif operacion == '*':
    multiplicacion = valor1 * valor2
    print('El resultado de la multiplicación de {} por {} es {}'.format(valor1, valor2, multiplicacion))

elif operacion == '/':
    division = valor1 / valor2
    print('El resultado de la división de {} entre {} es {}'.format(valor1, valor2, division))
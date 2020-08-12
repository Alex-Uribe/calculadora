print('----------------------------------------')
print('----------     CALCULADORA    ----------')
print('----------------------------------------')
print('----------------------------------------')
print('----------------------------------------')
print('  "Para realizar la operacion deseada, \n sigue las instrucciones:"')
print('----------------------------------------')
print('----------------------------------------')
print('Si deseas sumar ingresa el signo +')
print('Si deseas restar ingresa el signo -')
print('Si deseas multiplicarar ingresa el signo *')
print('Si deseas dividir ingresa el signo /')
print('----------------------------------------')
print('----------------------------------------')
print('----------------------------------------')

operacion = input('Ingresa el simbolo de la operacion a realizar: \n')
valor1 = int(input('Ingresa el primer valor de la operación: \n'))
valor2 = int(input('Ingresa el primer valor de la operación: \n'))


if operacion == '+':
    mas = valor1 + valor2
    print('El resultado de la suma es {}'.format(mas))
elif operacion == '-':
    menos = valor1 - valor2
    print('El resultado de la resta es {}'.format(menos))
elif operacion == '*':
    multiplicacion = valor1 * valor2
    print('El resultado de la multiplicación es {}'.format(multiplicacion))
elif operacion == '/':
    division = valor1 / valor2
    print('El resultado de la división es {}'.format(division))
else:
    print('No es una operacin reconocida')
incognita, intentos = 15,0
try:
    while intentos<5:
        ingreso = int(input('Ingrese un número: '))
        if ingreso==incognita:
            print('Has acertado')
            break
        else:
            intentos = intentos+1
            incognita = incognita+1
except ValueError:
    print('Por favor, ingrese un número válido')
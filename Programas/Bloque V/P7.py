def operaciones( num1, num2, digitos):
    suma = num1 + num2
    resta = num1 - num2
    multi = num1 * num2
    div = (num1 / num2)
    modulo = num1 % num2
    
    print(f'La suma de {num1} + {num2} es: {suma}')
    print(f'La resta de {num1} - {num2} es: {resta}')
    print(f'La multiplicación de {num1} * {num2} es: {multi}')
    print(f'La división de {num1} / {num2} es: {div:.{digitos}f}')
    print(f'El modulo de {num1} % {num2} es: {modulo}')

ciclo = int(input("Digite la cantidad de veces que desea ejecutar el programa: "))

num1 = int(input("Digite el primer numero: "))
num2 = int(input("Digite el segundo numero: "))
digitos = int(input("Digite la cantidad de decimales a mostrar en la división: "))

for _ in range(ciclo):
    operaciones( num1, num2, digitos)
    num1 = num1 * 2
    num2 = num2 * 2
    digitos = digitos * 2

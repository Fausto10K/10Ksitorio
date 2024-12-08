def operaciones(num1, num2, digitos):
    suma = num1 + num2
    resta = num1 - num2
    multi = num1 * num2
    div = (num1 / num2)
    modulo = num1 % num2

    print(f'La suma de {num1} + {num2} es: {suma}')
    print(f'La resta de {num1} - {num2} es: {resta}')
    print(f'La multiplicacion de {num1} * {num2} es: {multi}')
    print(f'La división de {num1} / {num2} es: {div:.{digitos}}')
    print(f'El modulo de {num1} % {num2} es: {modulo}')

num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese elsegundo numero: "))
digitos = int(input("Ingrese la cantidad de decimales mostrar en el modulo: ")) 
i = 0
while i == 0:
    operaciones(num1, num2, digitos)

    num1 = num1 * 2
    num2 = num2 * 2
    digitos = digitos * 2
    rep = input("Desea repetir el programa? (Digite 'salir' si no lo desea) ")
    reps = rep.lower()
    if reps == "salir":
        i += 5

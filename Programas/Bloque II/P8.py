calf1 = float(input("Digite su calf en una escala del 1 al 100 de la U1: "))
calf2 = float(input("Digite su calf en una escala del 1 al 100 de la U2: "))
calf3 = float(input("Digite su calf en una escala del 1 al 100 de la U3: "))
calf4 = float(input("Digite su calf en una escala del 1 al 100 de la U4: "))
calf5 = float(input("Digite su calf en una escala del 1 al 100 de la U5: "))
calf = (calf1 + calf2 + calf3 + calf4 + calf5) / 5
if calf >= 70:
    print("Su calificación es aprobatoria, su calificación final es: "+str(calf))
    print("¡GRACIAS POR USAR NUESTRO SISTEMA!")
else:
    print("Lo sentimos su calificación no es aprobatoria, su calificación final es: "+str(calf))
    print("¡GRACIAS POR USAR NUESTRO SISTEMA!")

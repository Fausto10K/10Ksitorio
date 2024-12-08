edades = [10, 15, 18, 8, 36, 5, 67, 89 ,95, 43, 26, 10, 65, 55, 81, 90]
menores_18 = [] 
adultos = [] 
mayores_65 = [] 
for edad in edades:
    if edad < 18:
        menores_18.append(edad)
    elif edad >= 18 and edad <= 65:
        adultos.append(edad)
    else: mayores_65.append(edad)


print("La lista de edades es: ",edades)
print("La lista de menores es: ",menores_18)
print("La lista de adultos es: ",adultos)
print("La lista de mayores a 65 es: ",mayores_65)

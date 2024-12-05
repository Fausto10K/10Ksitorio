puntos=[10, 30, 20]
puntos_2=[10,30,20]
ordenados=[10,20,30]
puntos_texto=["10,20,30"]
print("COMPARACIÓN (==)")

print(puntos == puntos_2) # True
print(puntos == ordenados) # False
print( puntos == puntos_texto ) # False

print("AHORA COMPARAMOS CON !=")

print(puntos != puntos_2) # False
print( puntos != ordenados) #True
print( puntos != puntos_texto) # True

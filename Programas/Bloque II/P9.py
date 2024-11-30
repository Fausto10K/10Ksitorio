art = int(input("digite el numero de articulos:  "))

if art <= 3:
    costo = art * 45
else:
    costo = art * 35
print("El costo total es de:", costo)
print("gracias por usar el programa")

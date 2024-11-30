edad = int(input("Digite su edad: "))
if edad >= 18:
    compra = int(input("¿Compró la pelicula?\n 1(si)\n 0(no)\n"))
    if compra == 1:
        print("Puede ver la película")
    else:
        print("A casa pajin")
    print("¡Gracias por usar Netflix!")

if edad <= 17:  
    print("No") 

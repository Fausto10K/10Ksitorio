num = int(input("Digite un número entre 10 y 99: "))

if num >= 10 and num <= 99:
    for i in  range(2, num +1):
        res= num % i
        if res == 0:
            print("Tu número no es un número primo")
            break
        else:
            print("Tu número es un numero primo")
            break
    
else:
    print("Tu número no está entre 10 y 99")

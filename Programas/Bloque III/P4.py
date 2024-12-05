ingresos = input("¿Cuales son sus ingresos? ")
ingresos = float(ingresos)
if ingresos <=1000:
    impuestos = ingresos * 0.05
    print("Tus ingresos menos los impuestos son de "+str(impuestos))
elif ingresos > 1000 and ingresos <=2500:
    impuestos = ingresos * 0.08
    print("Tus ingresos menos los impuestos son de "+str(impuestos))
elif ingresos > 2500 and impuestos <= 6000:
    print("Tus ingresos menos los impuestos son de "+str(impuestos))
    impuestos= ingresos * 0.12
else:
    impuestos = ingresos * 0.15
    salario_total = ingresos - impuestos
    print("Tus impuestos son "+str(impuestos) + "y tu salario final es" +str(salario_total))

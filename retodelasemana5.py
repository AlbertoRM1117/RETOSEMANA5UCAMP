while True:
    
    try :
        anioactual = int(input("Ingrese el año actual: "))
        break
    except ValueError:
        print("Error, fecha invalida soló debe de ingresar números")
        


while True:
    try :
        aniodiferente = int(input("Ingrese otro año:"))
        break
    except ValueError:
        print("Error, fecha invalida soló debe de ingresar números")
        

if anioactual > aniodiferente:

    diferenciaanio = anioactual-aniodiferente
    if diferenciaanio > 1:
        print("Han pasado " + str(diferenciaanio) + " años")

    elif diferenciaanio == 1:
        print("Desde el año " + str(aniodiferente)+ " pasado tan solo 1 año")

elif anioactual < aniodiferente:
    diferenciaanio = aniodiferente - anioactual

    if diferenciaanio > 1:
        print("Aún faltan " + str(diferenciaanio) + " años para el año " + str(aniodiferente))
        
    elif diferenciaanio == 1:
        print("Para llegar a " + str(aniodiferente) + " falta 1 año" )   

elif anioactual == aniodiferente:
    print("Haz introducido el mismo año que el actual.")


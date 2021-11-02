cadena = input("Introduzca una palabra: ")

def calclong(cadena):
    cont=0
    for letra in cadena:
        cont+=1
    return cont  

print("La palabra "+cadena+"tiene: "+str(calclong(cadena))+" letras")

  




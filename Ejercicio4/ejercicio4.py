cadena = input("Introduzca un caracter: ")
cadena = cadena.lower()

def longitud(cadena):
    if(len(cadena) > 1):
          return False
    if(len(cadena) == 1):
          return True

def vocal_cons(cadena):
    if(longitud(cadena)==True):
        for letra in cadena:
            if(letra =='a')|(letra=='e')|(letra=='i')|(letra=='o')|(letra=='u'):
                print("La letra es una vocal")
            else:
                print("La letra es una consonante")    
    else:
        print("No es un solo carácter")

vocal_cons(cadena)        



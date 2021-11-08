actual = int(input("Escribe el ano en curso: "))
nombre1 = input("Introduzca el nombre de la persona: ")
year1 = int(input("Introduzca el año de nacimiento de "+nombre1+": "))
nombre2 = input("Introduzca el nombre de la persona: ")
year2 = int(input("Introduzca el año de nacimiento de "+nombre2+": "))
nombre3 = input("Introduzca el nombre de la persona: ")
year3 = int(input("Introduzca el año de nacimiento de "+nombre3+": "))

edad1 = actual - year1
edad2 = actual - year2
edad3 = actual - year3


print(nombre1+" tiene: "+str(edad1)+" años")
print(nombre2+" tiene: "+str(edad2)+" años")
print(nombre3+" tiene: "+str(edad3)+" años")


     

            
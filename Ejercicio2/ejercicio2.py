num1 = input("Introduzca un numero: ")
num2 = input("Introduzca un segundo numero: ")
num3 = input("Introduzca un tercer numero: ")

def max_entre_3(num1,num2,num3):
    if(num1>num2) & (num1>num3):
        return num1
    
    if(num2>num3) & (num2>num1):
        return num2

    if(num3>num1) & (num3>num2):
        return num3    
print("El numero mayor es: "+max_entre_3(num1,num2,num3))
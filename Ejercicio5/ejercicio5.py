def sum(array):
        sum=0
        for numero in array:
           sum+=numero
        return sum        

def multip(array):
        mul=1
        for numero in array:
           mul= mul*numero
        return mul

print( "La suma es: "+sum([1,2,3,4]))   
print( "La multiplicación es: "+multip([1,2,3,4]))        
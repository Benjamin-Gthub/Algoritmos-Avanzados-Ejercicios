#Modulos para hallar si dos numeros son co-primos

#MCD(para numeros enteros positivos)
def mcd(a,b):
    #Hallar el menor entre ambos
    mini=min(a,b)
    i=mini
    encontrado=False
    divisor=1
    #Hallamos el maximo comun divisor entre ambos numeros:
    while(i>0 and not(encontrado)):
        if(a%i==0 and b%i==0):
            divisor=i
            encontrado=True
        i=i-1
    return divisor


#Determinar si dos numeros son Co-Primos
#(donde a,b son numeros enteros positivos)
def sonCoPrimos(a,b):
    if(mcd(a,b)==1):
        return True
    return False
        
#Ejemplo:
print("DETERMINAR SI DOS NUMEROS SON co-Primos\n\n")
A=int(input("Digite un numero(entero positivo)   : "))
B=int(input("Digite otro numero(entero positivo) : "))
print()
Resultado=sonCoPrimos(A,B)
print("Los dos numeros SI son co-Primos"*Resultado+"Los dos numeros NO son co-Primos"*(not(Resultado)))



    
            

#Numeros co-Primos de un arreglo de numeros

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


#Programa Principal
entrada=input("Digite los numeros(enteros positivos):")
#extraemos los numeros
numeros=entrada.split()
#hallamos los numeros Co-Primos
coPrimos=[]
for a in numeros:
    for b in numeros:
        if(a!=b and [int(a),int(b)] not in coPrimos and [int(b),int(a)] not in coPrimos and sonCoPrimos(int(a),int(b))):
            coPrimos.append([int(a),int(b)])
            
print("Los numeros Co-Primos, son:")
print(coPrimos)
            
            
            

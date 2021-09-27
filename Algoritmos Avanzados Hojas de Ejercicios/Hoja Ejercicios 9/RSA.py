from math import gcd
import random
def phi(a,b):
    return (a-1)*(b-1)

def coprimo(n):
    #Encontremos el valor mas grande co-primo con n
    j=1
    for i in range(2,(n-1)):
        if(gcd(n,i)==1):
            j=i
            if(random.randint(1,300)%4==0):
                return j

def esprimo(n):
    #aseguramos que n es positivo
    n=abs(int(n))
    #0 y 1 no son primos
    if n<2:
        return False
    #2 es el unico primo par
    if n==2:
        return True
    #Todos los otros numeros pares no son primos
    if not n&1:
        return False
    #range inicia en 3 y crece la raiz cuadrada de n
    #Para todos los numeros impares
    for x in range(3,int(n**0.5)+1,2):
        if n%x==0:
            return False
    return True

def encriptar(n,e):
    ci=int(input("Ingresa el valor numerico a ser encriptado: "))

    print("c=%i"%pow(ci,e,n))

def desencriptar(n,d,c):
    print("Desencriptando c...")

    print("Resultado: m=%i"%pow(c,d,n))

def generadoresclaves(primos):
    # La salida debe ser n y e y mantener p,q y d secretos
    p,q=primos
    n=p*q
    e=coprimo(phi(p,q))

    d=1
    #Calculando d
    for d in range(3,phi(p,q)):
        if((d*e)%phi(p,q)==1):
            break
    #Salida
    print("Entrega estos valores a quien te enviara mensajes(clave publica): \ne=%i \nn=%i \n\n"%(e,n))
    print("Almacena estos valores para futura referencia:")
    print("d=%i \np=%i\nq=%i\n"%(d,primos[0],primos[1]))


if __name__=="__main__":
    while(True):
        b=input("Tipea e para encriptar, d para desencriptar, c para generar claves: ")

        if b=='d':
            n=int(input("n = "))
            d=int(input("d = "))
            c=int(input("c = "))
            desencriptar(n,d,c)
        elif b=='e':
            n=int(input("n = "))
            e=int(input("e = "))
            encriptar(n,e)
        elif b=='c':
            i=tuple(int(x.strip())for x in input("Ingresa p,q (cualquier par de primos): ").split(","))
            #Validamos si los dos numeros son primos
            n1,n2=i
            while(not(esprimo(n1) and esprimo(n2))):
                print("INGRESE NUEVAMENTE LOS NUMEROS(tienen que ser primos)")
                i=tuple(int(x.strip())for x in input("Ingresa p,q (cualquier par de primos): ").split(","))
                n1,n2=i
            generadoresclaves(i)
            

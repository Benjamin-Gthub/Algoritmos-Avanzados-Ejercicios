#Programa Que halla congruencias Usando El TEOREMA CHINO DEL RESTO
#Modulo que sirve para hallar la inversa de una ecuacion modular
def inverse_mod(a,b):
    x=a
    y=b
    oldolds=1
    olds=0
    oldoldt=0
    oldt=1
    while y!=0:
        q=x//y#Cociente
        r=x%y#Residuo
        x=y#X toma el valor de y
        y=r#y toma el valor del residuO
        s=oldolds-q*olds
        t=oldoldt-q*oldt
        oldolds=olds
        oldoldt=oldt
        olds=s
        oldt=t
    return oldolds

#Teorema del chino(modulo principal)[mn es la lista que contiene a los modulos, an contiene los coeficientes de los modulos]
def chi_rem_them(mn,an):
    m=1
    Mn=[]
    yn=[]
    #Hallar el producto tota de los modulos "n"
    for k in range(0,len(mn)):
        m=m*mn[k]
    #Hallar xi para cada ecucacion modular
    for k in range(0,len(mn)):
        Mk=m/mn[k] #En una ecuacion este es el valor de Ni
        Mn.append(Mk)
        yk=inverse_mod(Mn[k],mn[k])%mn[k]#Halla el valor de Xi
        yn.append(yk)
    #Halla la suma total de las multiplicaciones de Ni*Xi*bi
    x=0
    for k in range(0,len(yn)):
        x=x+an[k]*Mn[k]*yn[k]
    #Halla el valor de X
    while x>=m:
        x=x-m
    #Retornar el valor de X
    return x

#======================================================================
#PROGRAMA PRINCIPAL
#Ingresamos los valores del ejercicio anterior
LN=input("Digite n_i de las ecuaciones modulares:")
LN=LN.split()
LN=[int(i)for i in LN ]
LB=input("Digite b_i de las ecuaciones modulares:")
LB=LB.split()
LB=[int(i)for i in LB ]

#Mostramos las ecuaciones modulares:
print("Las ecuaciones modulares ingresadas, son las siguientes:")
for i in range(len(LN)):
    print(" X = "+str(LB[i])+" mod("+str(LN[i])+")")

#Hallamos el valor de X de las ecuaciones modulares:
print("El valor de X, es:", chi_rem_them(LN,LB))
    

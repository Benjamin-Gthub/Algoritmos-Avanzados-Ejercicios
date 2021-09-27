import matplotlib.pyplot as plt
from math import gcd
#Mostrar la grafica de para los n primeros totientes de euler:

def phi(n):
    cantidad=0
    for k in range(1,n+1):
        if gcd(n,k)==1:
            cantidad+=1
    return cantidad

#Graficar para los primeros 1000 totientes:
n=[]
phi_n=[]
for i in range(1,1001):
    n.append(i)
    phi_n.append(phi(i))

plt.plot(n,phi_n,'.')
plt.xlabel('n')
plt.xlabel('phi(n)')
plt.show()

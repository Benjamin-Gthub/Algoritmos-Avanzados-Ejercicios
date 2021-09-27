#Hallar d en d*e=1mod(totiente(n))
import math
encontro=False
d=0
e=5#esto
totiente=12#esto
while(not(encontro)):
    d=d+1
    if(((d*e)-1)%totiente==0):
        encontro=True
print(d)

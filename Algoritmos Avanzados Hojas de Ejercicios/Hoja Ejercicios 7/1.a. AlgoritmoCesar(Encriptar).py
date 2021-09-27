#Ejercicio 1(Algoritmo Cesar)
def encriptar(texto,s):
    resultado=""
    #Traversar texto
    for i in range(len(texto)):
        char=texto[i]

        #Encriptar caracteres mayuscula
        if(char.isupper()):
            resultado+=chr((ord(char)+s-65)%26+65)

        #Encriptar caracteres minuscula
        else:
            resultado+=chr((ord(char)+s-97)%26+97)
    return resultado

#Ejemplo
texto="LOS ALUMNOS DE ALGORITMOS AVANZADOS SON MUY RESPONSBALES"
s=4
print("Texto        : "+texto)
print("Variante     : "+str(s))
print("Texto cifrado: "+encriptar(texto,s))



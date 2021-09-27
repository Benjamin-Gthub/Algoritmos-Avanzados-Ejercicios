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


def desencriptar(texto,n):
    resultado=""
    #Traversar texto
    for i in range(len(texto)):
        char=texto[i]

        #Desencriptar caracteres mayuscula
        if(char.isupper()):
            resultado+=chr((ord(char)-n-65)%26+65)

        #Desencriptar caracteres minuscula
        else:
            resultado+=chr((ord(char)-n-97)%26+97)
    return resultado


#Programa Principal

#Ejercicio
#Desencriptar el texto ETgKXTEBSTVBHGgWXEgIKHRXVMHgYBGTEgXLgOBMTEgITKTgTIKHUTKgETgTLBZGTMNKT
textCirado="ETgKXTEBSTVBHGgWXEgIKHRXVMHgYBGTEgXLgOBMTEgITKTgTIKHUTKgETgTLBZGTMNKT"
for s in range(26):
    print("-------------------------------------------")
    print("Texto cifrado       : "+textCirado)
    print("Variante            : "+str(s))
    print("Texto descifrado    : "+desencriptar(textCirado,s))
    print("-------------------------------------------")





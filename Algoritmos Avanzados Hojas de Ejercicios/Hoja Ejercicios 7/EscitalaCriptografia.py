#Algoritmo para encriptar Texto Plano(Escitala)
def encriptarEscitala(texto,clave):
    #Eliminamos los expacios en blanco
    texto=texto.replace(" ","")
    #Dividimos la cadena en clave-partes
    if(len(texto)%clave==0):
        NroSubCadenas=len(texto)//clave
    else:#se rellena con espacios en blanco o con el siguiente simbolo(º)
        NroSubCadenas=(len(texto)//clave)+1
        texto=texto+(" "*(clave-(len(texto)%clave)))
    #Encriptamos
    TextoCifrado=""
    for i in range(clave):
        SubCadena=""
        for j in range(NroSubCadenas):
            SubCadena=SubCadena+texto[(j*clave):((j*clave)+clave)][i]
                
        TextoCifrado=TextoCifrado+SubCadena

    #Retornamos el texto cifrado eliminando los caracteres en blanco si en
    #Caso se le agregaron
    return TextoCifrado.replace(" ","")



#Algoritmo para desencriptar un texto cifrado
def desencriptarEscitala(texto,clave):
    if(len(texto)%clave==0):
        tamaño=len(texto)//clave

        TextoDescifrado=""
        for i in range(tamaño):
            SubCadena=""
            for j in range(clave):
                SubCadena=SubCadena+texto[(j*tamaño):((j*tamaño)+tamaño)][i]
            TextoDescifrado=TextoDescifrado+SubCadena
        
    else:
    
        tamaño=(len(texto)//clave)+1
        Arreglo=[]
        #Agregamos un pedazo del texto a la matriz:
        for x in range(len(texto)%clave):
            Arreglo.append(texto[(x*tamaño):(x*tamaño)+tamaño])

        nuevoTexto=texto[(x+1)*tamaño::]
        #Agregamos el texto rstante a la matriz:
        for y in range(clave-(len(texto)%clave)):
            Arreglo.append(nuevoTexto[(y*(tamaño-1)):((y*(tamaño-1))+(tamaño-1))]+" ")
        
        #Desencirptamos el mensaje:
        TextoDescifrado=""
        for i in range(tamaño):
            SubCadena=""
            for j in range(clave):
                SubCadena=SubCadena+Arreglo[j][i]
            TextoDescifrado=TextoDescifrado+SubCadena

            
    return TextoDescifrado.replace(" ","")



#Ejemplo1:
print("============================ Ejemplo 1 ================================")
print("---------------------------- Cifrado ----------------------------------")
textoPlano1="TRES TRISTES TIGRES TRAGAN TRIGO"
clave=4
textCifrado1=encriptarEscitala(textoPlano1,clave)
print("Texto Plano =",textoPlano1)
print("Clave=",clave)
print("Texto Cifrado =",textCifrado1)
print("-----------------------------------------------------------------------")

print("---------------------------- Descifrado ----------------------------------")
clave=4
textdesCifrado1=desencriptarEscitala(textCifrado1,clave)
print("Texto Cifrado =",textCifrado1)
print("Clave=",clave)
print("Texto DesCifrado =",textdesCifrado1)
print("-----------------------------------------------------------------------")

#Ejemplo2:
print()
print("============================ Ejemplo 2 ================================")
print("---------------------------- Cifrado ----------------------------------")
clave=4
textoPlano2="TRES TRISTES TIGRES TRAGAN TRIGO EN El TRIGAL"
textCifrado2=encriptarEscitala(textoPlano2,clave)
print("Texto Plano =",textoPlano2)
print("Clave=",clave)
print("Texto Cifrado =",textCifrado2)
print("-----------------------------------------------------------------------")

print("---------------------------- Descifrado ----------------------------------")
clave=4
textdesCifrado2=desencriptarEscitala(textCifrado2,clave)
print("Texto Cifrado =",textCifrado2)
print("Clave=",clave)
print("Texto DesCifrado =",textdesCifrado2)
print("-----------------------------------------------------------------------")

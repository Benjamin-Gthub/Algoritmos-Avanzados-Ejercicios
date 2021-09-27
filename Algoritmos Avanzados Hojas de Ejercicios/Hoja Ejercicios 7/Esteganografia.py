#Importamos la libreria que ttrabaja con imagenes
from PIL import Image

#Modulo para convertir los datos en numeros de 8 bits
def genData(data):
    newd=[]
    for i in data:
        newd.append(format(ord(i),'08b'))
    return newd

#Modulo para 
def modPix(pix,data):
    datalist=genData(data)
    lendata=len(datalist)
    imdata=iter(pix)
    for i in range(lendata):
        pix=[value for value in imdata.__next__()[:3]+imdata.__next__()[:3]+imdata.__next__()[:3]]
        for j in range(0,8):
            if(datalist[i][j]=='0' and pix[j]%2!=0):
                pix[j]-=1
            elif(datalist[i][j]=='1'and pix[j]%2==0):
                if(pix[j]!=0):
                    pix[j]-=1
                else:
                    pix[j]+=1
        if(i==lendata-1):
            if(pix[-1]%2==0):
                if(pix[-1]!=0):
                    pix[-1]-=1
                else:
                    pix[-1]+=1
        else:
            if(pix[-1]%2!=0):
                pix[-1]-=1
                
        pix=tuple(pix)
        yield pix[0:3]
        yield pix[3:6]
        yield pix[6:9]

def encode_enc(newimg,data):
    w=newimg.size[0]
    (x,y)=(0,0)

    for pixel in modPix(newimg.getdata(),data):
        newimg.putpixel((x,y),pixel)
        if(x==w-1):
            x=0
            y+=1
        else:
            x+=1

#Modulo para encodificar 
def encode():
    img=input("Ingresa el nombre de la imagen(con extension) : ")
    image=Image.open(img,'r')#Abrir la imagen

    data=input("Ingresa los datos a ser codificados : ")
    if(len(data)==0):#Si el texto es vacio
        raise ValueError('Los datos son vacios')
    #Creamos una copia de la imagen para que no afecte a la imagen original
    newimg=image.copy()
    #Ocultamos el texto en la imagen
    encode_enc(newimg,data)

    #Ingresamos un nombre para almacenar la imagen con el texto oculto
    new_img_name=input("Ingresa el nombre de la nueva imagen(con extension) : ")
    #Creamos y guardamos la imagen con texto oculto
    newimg.save(new_img_name, str(new_img_name.split(".")[1].upper()))

def decode():
    img=input("Ingrese el nombre de la imagen(con extension): ")
    image=Image.open(img,"r")#Abrir la imagen

    data=''
    imgdata=iter(image.getdata())#Obtener todos los pixeles de la imagen en 3 bytes

    while(True):
        pixels=[value for value in imgdata.__next__()[:3]+
                                imgdata.__next__()[:3]+
                                imgdata.__next__()[:3]]
        binstr=''

        for i in pixels[:8]:
            if(i%2==0):
                binstr+='0'
            else:
                binstr+='1'
        data+=chr(int(binstr,2))#Extraer los pixeles y convertir a numero decimal y obtener cada caracter de cada pixel que fue modificado
        if(pixels[-1]%2!=0):
            return data #Retornamos el mensaje oculto

#El modulo principal, es:
        
def main():
    a=int(input(":: Bienvenidos a esteganografia ::\n"
                    "1. Codificar\n2. Decodificar\n"))
    if(a==1):
        encode()
    elif(a==2):
        print("Palabra decodificada : "+decode())
    else:
        raise Exception("Ingresa una opcion valida")
if __name__=='__main__':
    main()
            
        
        

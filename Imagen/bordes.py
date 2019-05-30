
import time
import cv2
from PIL import Image

def brillantes(im):
    tiempoin=time.time()  
    img=grises(im)
    print(img.size[0]," _ ", img.size[1])
    suma=0
    ind=numpy.array(img)
    distA_i=[]
    distF_i=[]
    distS_i=[]
    
    #indice de brillantes
    """ i=0
    while i< img.size[0]:
        #recorremos filas
        j = 0
        ind.append([])
        while j < img.size[1]:# reocrremos columnas
            ind[i].append(img.getpixel((i,j))[0])
            j+=1
        i+=1
     """
     #calculamos A_i
    i=0
    while i< len(ind):
        #recorremos filas
        j = 0
        distA_i.append([])
        while j < len(ind[i]):# reocrremos columnas
            #print(i," ",len(ind))
            if(len(ind)-1==i):
                distA_i[i].append((ind[i-1][j]+ind[i][j]+ind[0][j])/3)
            else:
                distA_i[i].append((ind[i-1][j]+ind[i][j]+ind[i+1][j])/3)    
            j+=1
        i+=1
    #calculamos f_i
    i=0
    while i< len(distA_i):
        #recorremos filas
        j = 0
        distF_i.append([])
        while j < len(distA_i[i]):# reocrremos columnas
            #print(i," ",len(ind))
            if(len(distA_i)-1==i):
                distF_i[i].append( (distA_i[i-1][j]-distA_i[i][j]) /2)
            else:
                distF_i[i].append((distA_i[i-1][j]-distA_i[i+1][j])/2)  
            j+=1
        i+=1
    #calculamos s_i
    i=0
    while i< len(distF_i):
        #recorremos filas
        j = 0
        distS_i.append([])
        while j < len(distF_i[i]):# reocrremos columnas
            #print(i," ",len(ind))
            if(len(distF_i)-1==i):
                distS_i[i].append( (distF_i[i-1][j]-distF_i[i][j]) //2)
            else:
                distS_i[i].append( (distF_i[i-1][j]-distF_i[i+1][j]) //2)
            valor=int(distS_i[i][j])
            img.putpixel((i,j),(valor,valor,valor))
            j+=1
        i+=1

    
    tiempofin=time.time() 
    print("Fin brillantes ", tiempofin-tiempoin) 
    return img

def canny(ruta):
    tiempoin=time.time()    
    img = cv2.imread(ruta,0)
    laplacian = cv2.Canny(img,100,200)
    cv2.imwrite('resultado/6.can'+ruta,laplacian)
    timefin=time.time()
    print(timefin,"   " ,tiempoin,"total canny :" , timefin-tiempoin)
    return Image.open('resultado/6.can'+ruta)


def lap(ruta):
    tiempoin=time.time()    
    img = cv2.imread(ruta,0)
    laplacian = cv2.Laplacian(img,cv2.CV_64F)
    cv2.imwrite('resultado/5.lap'+ruta,laplacian)
    timefin=time.time()
    print(timefin,"   " ,tiempoin," total laplace :" , timefin-tiempoin)
    return Image.open('resultado/5.lap'+ruta)

def extractorHorizontal(im):
    tiempoin=time.time()
    imgH=grises(im)
    i=0
    masc=[]
    while i < imgH.size[0]:#recorremos filas
        j=0
        masc.append([])
        while j < imgH.size[1]-1:#recorremos columnas
            masc[i].append(imgH.getpixel((i,j))[0]-imgH.getpixel((i,j+1))[0])
            imgH.putpixel((i,j),(masc[i][j],masc[i][j],masc[i][j]))
            #imgH.putpixel((i,j),(masc[i][j],masc[i][j],masc[i][j]))
            j+=1
        i+=1
    timefin=time.time()
    print(timefin,"   " ,tiempoin,"total Horizontal :" , timefin-tiempoin)  
    return imgH
def extractorVertical(im):
    tiempoin=time.time()
    imgV=grises(im)
    i=0
    masc=[]
    while i < imgV.size[0]-1:#recorremos filas
        j=0
        masc.append([])
        while j < imgV.size[1]:#recorremos columnas
            masc[i].append(imgV.getpixel((i,j))[0]-imgV.getpixel((i+1,j))[0])
            imgV.putpixel((i,j),(masc[i][j],masc[i][j],masc[i][j]))
            j+=1
        i+=1
    timefin=time.time()
    print(timefin,"   " ,tiempoin,"total vertical :" , timefin-tiempoin)  
    return imgV



def gradiente(im):
    tiempoin=time.time()
    img=grises(im)
    i=0
    mascx=[]
    mascy=[]
    while i < img.size[0]:#recorremos filas
        j=0
        mascx.append([])
        while j < img.size[1]-1:#recorremos columnas
            mascx[i].append(img.getpixel((i,j))[0]-img.getpixel((i,j+1))[0])
            j+=1
        i+=1  
    
    i=0
    while i < img.size[0]-1:#recorremos filas
        j=0
        mascy.append([])
        while j < img.size[1]:#recorremos columnas
            mascy[i].append(img.getpixel((i,j))[0]-img.getpixel((i+1,j))[0])
            j+=1
        i+=1   
    resultado=im.copy()
    gradiente=0
    i=0
        
    while i < resultado.size[0]-1:#recorremos filas
        j=0
        while j < resultado.size[1]-1:#recorremos columnas
            gradiente = int( pow(pow(mascx[i][j],2)+pow(mascy[i][j],2)  ,1/2))
            #if(masc[i][j])>20 :
            resultado.putpixel((i,j),(gradiente,gradiente,gradiente))
            j+=1
        i+=1
    timefin=time.time()
    print(timefin,"   " ,tiempoin,"total Gradiente :" , timefin-tiempoin)  

    return resultado

    


def grises(im):
    #tiempoim=time.time()    
    #escala de grises
    im2=im.copy()
    i=0
    while i< im2.size[0]:
        #recorremos filas
        j = 0
        while j < im2.size[1]:# reocrremos columnas
            r,g,b=im2.getpixel((i,j))
            gris=(r+g+b)//3
            pixel = tuple([gris,gris,gris])
            im2.putpixel((i,j), pixel)
            #print(gris," ")
            j+=1
        i+=1
    #timefin=time.time()
    #print(timefin,"   " ,tiempoim)
    return im2
def grises0255(im):
    tiempoim=time.time()    
    #escala de grises
    im2=im.copy()
    i=0
    while i< im2.size[0]:
        #recorremos filas
        j = 0
        while j < im2.size[1]:# reocrremos columnas
            r,g,b=im2.getpixel((i,j))
            gris=(r+g+b)//3
            if(gris<120):
                pixel = tuple([0,0,0])
            else:
                pixel = tuple([255,255,255])

                
            im2.putpixel((i,j), pixel)
            #print(gris," ")
            j+=1
        i+=1
    timefin=time.time()
    print(timefin,"   " ,tiempoim)
    return im2


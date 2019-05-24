import cv2
import bordes
from PIL import Image

nombre="eric"
ext=".jpg"

ruta=nombre+ext

im = Image.open(ruta)


gris=bordes.grises(im)
gris.save("resultado/1."+ruta)

fotoH = bordes.extractorHorizontal(im)
fotoH.save("resultado/2.H"+ruta)

fotoV = bordes.extractorVertical(im)
fotoV.save("resultado/3.V"+ruta)

grad=bordes.gradiente(im)
grad.save("resultado/4.grad"+ruta)


laplaciano = bordes.lap(ruta)
canny=bordes.canny(ruta)


#im.show()
#gris.show()
#fotoH.show()
#fotoV.show()
#grad.show()
#laplaciano.show()
#canny.show()



#print(numpy.array(gris)[0][0],numpy.array(gris)[0][1] )
    
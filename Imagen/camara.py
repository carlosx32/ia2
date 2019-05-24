import cv2
import bordes



"""
	En este caso, 0 quiere decir que queremos acceder
	a la cámara 0. Si hay más cámaras, puedes ir probando
	con 1, 2, 3...
"""

try:
    cap = cv2.VideoCapture(0)
    leido, frame = cap.read()

    if leido == True:
        cv2.imwrite("fotoCamara.png", frame)
        imagen=Image.open("fotoCamara.png")
        bordes.gradiente(imagen)
        imagen.show()
        print("Foto tomada correctamente")
    else:
        print("Error al acceder a la cámara")
except:
    print("Ha ocurrido un error")
finally:
    cap.release()

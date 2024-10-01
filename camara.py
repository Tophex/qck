import face_recognition
import numpy as np
from picamera2 import Picamera2

# Inicializa la cámara
picam2 = Picamera2()
picam2.configure(picam2.preview_configuration(main={"format": 'RGB888', "size": (640, 480)}))
picam2.start()

try:
    while True:
        # Captura un frame
        frame = picam2.capture_array()

        # Convierte la imagen a un formato adecuado para face_recognition
        rgb_frame = frame[:, :, ::-1]  # Cambia de BGR a RGB

        # Encuentra todas las caras en la imagen
        face_locations = face_recognition.face_locations(rgb_frame)

        # Dibuja rectángulos alrededor de las caras detectadas
        for (top, right, bottom, left) in face_locations:
            picam2.set_preview_crop(left, top, right - left, bottom - top)

        # Aquí puedes agregar código para mostrar el frame o procesar las imágenes de otras maneras

        # Salida del bucle al presionar 'q' (puedes usar otro método para salir)
        if input() == 'q':
            break

finally:
    picam2.close()

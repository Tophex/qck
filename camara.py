import cv2
import numpy as np
import picamera
import picamera.array

# Carga el clasificador de caras preentrenado de Haar
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Inicializa la cámara
with picamera.PiCamera() as camera:
    # Establece la resolución de la cámara
    camera.resolution = (640, 480)
    camera.framerate = 24

    # Usa un array de numpy para almacenar los frames
    with picamera.array.PiRGBArray(camera) as output:
        for frame in camera.capture_continuous(output, format='bgr', use_video_port=True):
            # Obtén el frame actual
            image = frame.array

            # Convierte el frame a escala de grises
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            # Detecta caras
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

            # Dibuja rectángulos alrededor de las caras detectadas
            for (x, y, w, h) in faces:
                cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

            # Muestra el frame con las detecciones
            cv2.imshow('Face Detection', image)

            # Limpia el array para el siguiente frame
            output.truncate(0)

            # Sale del bucle al presionar 'q'
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

# Cierra todas las ventanas al finalizar
cv2.destroyAllWindows()

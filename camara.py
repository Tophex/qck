(
import sys
# Asegúrate de especificar la ruta solo si es necesario
# sys.path.append('/ruta/a/tu/opencv')
import cv2
import time
from picamera2 import Picamera2, Preview

# Inicializa la cámara
picam2 = Picamera2()

# Configura la vista previa
preview_config = picam2.create_preview_configuration()
picam2.configure(preview_config)

# Inicia la vista previa
picam2.start_preview(Preview.QT)

# Inicia la cámara
picam2.start()

# Carga el clasificador de Haar para la detección de rostros
haarcascade_path = '/home/usc/Desktop/haarcascades/haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(haarcascade_path)

try:
    while True:
        # Captura el frame
        frame = picam2.capture_array()  # Captura un frame como un array de NumPy
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convierte a escala de grises
        
        # Detección de rostros
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        # Dibuja rectángulos alrededor de los rostros detectados
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Muestra el frame con detección de rostros
        cv2.imshow('Detección de Rostros', frame)

        # Sale del bucle si se presiona 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    print("Captura Detenida.")
finally:
    picam2.stop()
    cv2.destroyAllWindows()  # Cierra las ventanas de OpenCV
)
import cv2
import time
from picamera2 import Picamera2, Preview

# Inicializa la cámara
picam2 = Picamera2()

# Configura la vista previa
preview_config = picam2.create_preview_configuration()
picam2.configure(preview_config)

# Inicia la vista previa
picam2.start_preview(Preview.QT)

# Inicia la cámara
picam2.start()

# Carga el clasificador de Haar para la detección de rostros
haarcascade_path = '/home/usc/Desktop/haarcascades/haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(haarcascade_path)

frame_rate = 1  # Captura un frame por segundo
last_capture_time = time.time()

try:
    while True:
        current_time = time.time()
        if current_time - last_capture_time >= 1.0 / frame_rate:
            last_capture_time = current_time
            
            # Captura el frame
            frame = picam2.capture_array()
            frame = cv2.resize(frame, (640, 480))  # Redimensiona a 640x480
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convierte a escala de grises
            
            # Detección de rostros
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

            # Dibuja rectángulos alrededor de los rostros detectados
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            # Muestra el frame con detección de rostros
            cv2.imshow('Detección de Rostros', frame)

        # Sale del bucle si se presiona 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    print("Captura Detenida.")
finally:
    picam2.stop()
    cv2.destroyAllWindows()  # Cierra las ventanas de OpenCV

import cv2
from picamera2 import Picamera2, Preview

# Inicializa la cámara
picam2 = Picamera2()

# Configura la vista previa
preview_config = picam2.create_preview_configuration(main={"format": "RGB888", "size": (640, 480)})
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
        frame = picam2.capture_array()

        # Convierte el frame a escala de grises
        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

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

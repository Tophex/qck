import cv2
import os

# Carga el clasificador de caras
haarcascade_path = os.path.join(cv2.__file__, '..', 'data', 'haarcascades', 'haarcascade_frontalface_default.xml')
face_cascade = cv2.CascadeClassifier(haarcascade_path)

# Verifica si se cargó correctamente el clasificador
if face_cascade.empty():
    print("Error: No se pudo cargar el clasificador de caras.")
    exit()

# Inicia la captura de video desde la cámara
cap = cv2.VideoCapture(0)

# Verifica si la cámara se abrió correctamente
if not cap.isOpened():
    print("Error: No se pudo abrir la cámara.")
    exit()

while True:
    # Captura un fotograma
    ret, frame = cap.read()
    if not ret:
        print("Error: No se pudo capturar el video.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detecta caras
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Dibuja rectángulos alrededor de las caras detectadas
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Muestra el fotograma con las caras detectadas
    cv2.imshow('Face Detection', frame)

    # Salir si se presiona 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera la captura y cierra las ventanas
cap.release()
cv2.destroyAllWindows()

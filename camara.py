import cv2

# Carga el clasificador de caras
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Inicia la captura de video desde la cámara
cap = cv2.VideoCapture(0)

while True:
    # Captura un fotograma
    ret, frame = cap.read()
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

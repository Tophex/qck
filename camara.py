from picamera2 import Picamera2

# Inicializa la cámara
picam2 = Picamera2()

# Inicia la cámara
picam2.start()

# Captura una imagen
image = picam2.capture_array()

# Guarda la imagen
output_path = 'foto.jpg'  # Cambia el nombre del archivo según lo necesites
picam2.save_image(output_path, image)

# Detiene la cámara
picam2.stop()

print(f'Imagen guardada como {output_path}')

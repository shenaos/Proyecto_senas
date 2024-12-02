import cv2

# Intentar abrir la cámara con el índice 0
cap = cv2.VideoCapture(0)

# Verificar si la cámara se ha abierto correctamente
if not cap.isOpened():
    print("Error: No se pudo abrir la cámara.")
    exit()

while True:
    # Capturar un frame de la cámara
    ret, frame = cap.read()
    
    # Verificar si el frame se ha capturado correctamente
    if not ret:
        print("Error: No se pudo capturar el frame.")
        break

    # Mostrar el frame capturado en una ventana
    cv2.imshow('frame', frame)

    # Salir del bucle si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara y cerrar todas las ventanas
cap.release()
cv2.destroyAllWindows()

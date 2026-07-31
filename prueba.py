from ultralytics import YOLO
import cv2

# Cargar el modelo
model = YOLO("runs/detect/runs/HD-L70/weights/best.pt")

# Abrir la cámara
cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Detectar objetos
    results = model(frame, conf=0.05)

    # Dibujar las detecciones
    annotated_frame = results[0].plot()

    cv2.imshow("Detección HD70", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
import cv2
from ultralytics import YOLO

model_path = 'last.pt'
model = YOLO(model_path)

img = cv2.imread('C:/Users/danie/Desktop/dev/python/parking-detection-example/pk_451.jpg')
results = model(img)
print(results)

for result in results:
    for box in result.boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        conf = box.conf[0]
        cls = int(box.cls[0])
        label = f'{model.names[cls]} {conf:.2f}'

        # Dibujar el bounding box
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

        # Poner la etiqueta
        cv2.putText(img, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# Mostrar la imagen con los bounding boxes
cv2.imshow('Detected Objects', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
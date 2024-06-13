import cv2
from ultralytics import YOLO
import firebase_admin
from firebase_admin import credentials, firestore
import base64
import time

cred = credentials.Certificate('service.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

model_path = 'last.pt'
model = YOLO(model_path)




image_files = ['pk_451.jpg', 'pk_455.jpg', 'pk_466.jpg', 'pk_459.jpg', 'pk_412.jpg']
image_index = 0


def detect_and_upload():
    global image_index

    img = cv2.imread(image_files[image_index])
    results = model(img)
    print(results)

    array_result = []
    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = box.conf[0]
            cls = int(box.cls[0])
            label = f'{model.names[cls]} {conf:.2f}'
            item = {"x": x1, "y": y1, "w": x2 - x1, "h": y2 - y1, "class": True}
            if cls == 0:
                array_result.append(item)
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(img, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    if array_result:
        data = {f'item': array_result}
        doc_ref = db.collection('parkingdb').document('yaxkVGHlS2jtOOzAgrdD')
        doc_ref.set(data)

    _, buffer = cv2.imencode('.jpg', img)
    base64_image = base64.b64encode(buffer).decode('utf-8')

    doc_ref = db.collection('photodb').document('CKivyegoNF9Z68VWkI3z')
    doc_ref.set({'image': base64_image})

    image_index = (image_index + 1) % len(image_files)


while True:
    start_time = time.time()
    detect_and_upload()
    elapsed_time = time.time() - start_time
    sleep_time = max(0, 180 - elapsed_time)  # Asegurarse de que no sea negativo
    time.sleep(sleep_time)
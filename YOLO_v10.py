import cv2
import os

import cv2
import supervision as sv
from ultralytics import YOLOv10


model = YOLOv10(f'best.pt')

bounding_box_annotator = sv.BoundingBoxAnnotator()
label_annotator = sv.LabelAnnotator()

cap = cv2.VideoCapture(0)


if not cap.isOpened():
    print("Unable to read camera ... !")

outputDir = "output_images"
os.makedirs(outputDir, exist_ok=True)

imageCount = 94

while True:
    ret, frame = cap.read()

    if not ret:
        break

    results = model(frame)[0]
    detections = sv.Detections.from_ultralytics(results)

    annotated_image = bounding_box_annotator.annotate(scene=frame, detections=detections)
    annotated_image = label_annotator.annotate(scene=annotated_image, detections=detections)

    cv2.imshow("Webcam", annotated_image)

    k = cv2.waitKey(1)

    if k%256 == 27: # press 'esc' to save the frame ... 
        print("Escape hit, closing ... !")
        break


cap.release()
cv2.destroyAllWindows()
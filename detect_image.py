from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")

def detect_image(image_path):

    img = cv2.imread(image_path)

    results = model(img)

    annotated_frame = results[0].plot()

    # -------- Object Counter --------
        
    if results[0].boxes is not None:

        classes = results[0].boxes.cls.tolist()
        names = results[0].names

        counts = {}

        for c in classes:
            label = names[int(c)]
            counts[label] = counts.get(label,0) + 1

        y_offset = 30

        for k,v in counts.items():

            cv2.putText(annotated_frame, 
                        f"{k}:{v}",
                        (10,y_offset),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.6,
                        (255,255,0),
                        2)
            y_offset +=25

    cv2.imshow("Image Detection", annotated_frame)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
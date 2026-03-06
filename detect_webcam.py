from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")

def detect_webcam():

    cap = cv2.VideoCapture(0)

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        results = model(frame)

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

        cv2.imshow("Webcam Detection", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
from ultralytics import YOLO
import cv2
import numpy as np

model = YOLO("yolov8n.pt")

bar_height = 25

def format_time(seconds):
    mins = int(seconds // 60)
    secs = int(seconds % 60)
    return f"{mins:02d}:{secs:02d}"

def detect_video(video_path):
    
    cap = cv2.VideoCapture(video_path)

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    window_name = "Videol Detection"

    paused = False

    fps = cap.get(cv2.CAP_PROP_FPS) # Frames Per Second
    total_time = total_frames/fps

    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Mouse click function
    def seek(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:

            # If click is inside progress bar
            if y >= frame_height:

                progress = x / frame_width
                target_frame = int(progress * total_frames)

                cap.set(cv2.CAP_PROP_POS_FRAMES, target_frame)
    
    cv2.namedWindow(window_name)
    cv2.setMouseCallback(window_name, seek)

    while True:

        if not paused:
            ret, frame = cap.read()

            if not ret:
                break
        
        current_frame = int(cap.get(cv2.CAP_PROP_POS_FRAMES))

        results = model(frame)

        annotated_frame = results[0].plot()

        h, w, _ = annotated_frame.shape

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
                            1)
                y_offset +=25
            
        # -------- Progress Bar --------

        # Create space for progress bar (below video)
        bar_area = np.zeros((bar_height, w, 3), dtype=np.uint8)

        # Progress calculation
        progress = current_frame / total_frames
        bar_width = int(progress * w)

        # Background bar
        cv2.rectangle(bar_area, (0, 0), (w, bar_height), (60,60,60), -1)

        #Progress bar
        cv2.rectangle(bar_area, (0, 0), (bar_width, bar_height), (0,255,0), -1)

        # percent = int(progress * 100)

        # cv2.putText(bar_area, f"{percent}%",
        #             (10, bar_height-7),
        #             cv2.FONT_HERSHEY_SIMPLEX,
        #             0.5,
        #             (255,255,255),
        #             2)

        # time text
        # Current time

        # -------- Time Display --------

        current_time = current_frame / fps

        time_text = f"{format_time(current_time)} / {format_time(total_time)}"

        cv2.putText(bar_area,
                    time_text,
                    (w-150, bar_height-7),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (255,255,255),
                    1)

        # Combine video + progress bar
        final_frame = np.vstack((annotated_frame, bar_area))


        cv2.imshow(window_name,final_frame)

        # -------- KEY CONTROLS --------

        key = cv2.waitKey(1) & 0xFF
        
        if key == ord("q"):
            break

        elif key == ord(" "):
            paused = not paused

        elif key == ord("f"):
            frame_jump = int(fps * 5)
            cap.set(cv2.CAP_PROP_POS_FRAMES, current_frame + frame_jump)

        elif key == ord("b"):
            frame_jump = int(fps * 5)
            cap.set(cv2.CAP_PROP_POS_FRAMES, current_frame - frame_jump)

    cap.release()
    cv2.destroyAllWindows()
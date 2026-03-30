import cv2
from ultralytics import YOLO

# Load YOLO model
model = YOLO("yolov8n.pt")

# Known values
KNOWN_HEIGHT = 0.3   # your bottle height (meters)
FOCAL_LENGTH = 733
    # your calibrated focal length

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    results = model(frame)

    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            label = model.names[cls]

            # Detect only bottle
            if label == "bottle":
                x1, y1, x2, y2 = map(int, box.xyxy[0])

                h_pixels = y2 - y1

                # Distance calculation
                distance = (FOCAL_LENGTH * KNOWN_HEIGHT) / h_pixels

                # Draw box
                cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), 2)

                cv2.putText(frame, f"{distance:.2f} m",
                            (x1, y1-10),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.7, (0,255,0), 2)

    cv2.imshow("YOLO Distance Detection", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()

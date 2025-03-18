import cv2

def capture_face(image_path="user_face.jpg"):
    cap = cv2.VideoCapture(0)  # Open webcam
    if not cap.isOpened():
        print("Error: Could not open webcam")
        return None

    ret, frame = cap.read()  # Capture frame
    if ret:
        cv2.imwrite(image_path, frame)  # Save image
        print("✅ Face captured successfully:", image_path)
    cap.release()
    cv2.destroyAllWindows()

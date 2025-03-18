import cv2
import dlib
import time
from imutils import face_utils

# Load face detector & landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")  # Download from dlib

# Extract eye landmarks
(left_eye_start, left_eye_end) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(right_eye_start, right_eye_end) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

def eye_aspect_ratio(eye):
    """Calculate Eye Aspect Ratio (EAR) to detect blinking."""
    A = ((eye[1][1] - eye[5][1]) ** 2 + (eye[1][0] - eye[5][0]) ** 2) ** 0.5
    B = ((eye[2][1] - eye[4][1]) ** 2 + (eye[2][0] - eye[4][0]) ** 2) ** 0.5
    C = ((eye[0][1] - eye[3][1]) ** 2 + (eye[0][0] - eye[3][0]) ** 2) ** 0.5
    return (A + B) / (2.0 * C)

def detect_liveness():
    """Detects if a user blinks & moves their head for liveness detection."""
    cap = cv2.VideoCapture(0)
    blink_detected = False
    move_detected = False
    start_time = time.time()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detector(gray)

        for face in faces:
            landmarks = predictor(gray, face)
            landmarks = face_utils.shape_to_np(landmarks)

            # Detect eyes & calculate blinking
            left_eye = landmarks[left_eye_start:left_eye_end]
            right_eye = landmarks[right_eye_start:right_eye_end]
            left_EAR = eye_aspect_ratio(left_eye)
            right_EAR = eye_aspect_ratio(right_eye)
            avg_EAR = (left_EAR + right_EAR) / 2.0

            if avg_EAR < 0.20:  # Threshold for blink detection
                blink_detected = True

            # Detect head movement
            nose_tip = landmarks[30]  # Nose tip landmark
            if nose_tip[0] < face.left() + 20 or nose_tip[0] > face.right() - 20:
                move_detected = True

        cv2.imshow("Liveness Detection", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # Stop if both checks pass or after 10 seconds
        if blink_detected and move_detected or time.time() - start_time > 10:
            break

    cap.release()
    cv2.destroyAllWindows()
    
    return blink_detected and move_detected

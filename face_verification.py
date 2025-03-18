from deepface import DeepFace

def verify_face(initial_image="user_face.jpg", new_image="new_face.jpg"):
    try:
        result = DeepFace.verify(initial_image, new_image, model_name='Facenet')
        return result["verified"]
    except Exception as e:
        print("Error:", e)
        return False

import streamlit as st
import face_capture
import face_verification
import ai_branch_manager

st.title("AI Branch Manager - Video-Based Loan Assistance")

st.header("📹 Step 1: AI Video Assistant")
if st.button("Start AI Loan Assistant"):
    ai_branch_manager.play_ai_video()

st.header("🖼 Step 2: Capture Initial Face")
if st.button("Capture Initial Face"):
    face_capture.capture_face("user_face.jpg")
    st.image("user_face.jpg", caption="Captured Face", use_column_width=True)
    st.success("✅ Face Captured Successfully!")

st.header("📤 Step 3: Upload a New Image for Verification")
uploaded_file = st.file_uploader("Upload a new image for verification", type=["jpg", "png", "jpeg"])

if uploaded_file:
    with open("new_face.jpg", "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.image("new_face.jpg", caption="Uploaded Face", use_column_width=True)

    if st.button("Verify Face"):
        is_verified = face_verification.verify_face("user_face.jpg", "new_face.jpg")
        
        if is_verified:
            st.success("✅ Same user detected! Proceed with loan process.")
        else:
            st.error("❌ Different user detected! Verification failed.")

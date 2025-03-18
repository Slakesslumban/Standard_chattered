import streamlit as st
import os

def play_ai_video(video_path="ai_manager.mp4"):
    if os.path.exists(video_path):
        st.video(video_path)
    else:
        st.error("🚨 Error: AI Manager video not found!")

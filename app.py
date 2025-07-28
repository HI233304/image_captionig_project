import streamlit as st
from login import check_login, register_user, load_users, generate_otp, reset_password
from model_captioning import generate_caption
from model_segmentation import segment_image
from util import capture_image_from_camera
from PIL import Image
import os

st.set_page_config(page_title="Image Captioning & Segmentation", layout="centered")
st.title("🔐 Login or Register")
section = st.radio("Select Action", ["Login", "Register", "Forgot Password", "View Users (Admin)"])
username = st.text_input("Username")
password = st.text_input("Password", type="password")

if section == "Login":
    if st.button("Login"):
        if check_login(username, password):
            st.success("Login Successful ✅")
            st.title("📸 Image Captioning & Segmentation")
            option = st.radio("Choose Image Source:", ["Upload", "Camera"])
            image_path = "input.jpg"
            if option == "Upload":
                uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
                if uploaded_file is not None:
                    img = Image.open(uploaded_file)
                    img.save(image_path)
                    st.image(img, caption="Uploaded Image")
            elif option == "Camera":
                if st.button("Capture Image"):
                    image_path = capture_image_from_camera("input.jpg")
                    st.image(image_path, caption="Captured Image")
            if os.path.exists(image_path):
                st.subheader("🧠 Caption:")
                caption = generate_caption(image_path)
                st.success(caption)
                st.subheader("🖼 Segmented Image:")
                segmented = segment_image(image_path)
                st.image(segmented, caption="Segmented Output")
        else:
            st.error("Invalid login credentials ❌")
elif section == "Register":
    email = st.text_input("Email")
    if st.button("Register"):
        result = register_user(username, password, email)
        if result == "ok":
            st.success("Registration Successful ✅ You can now login.")
        elif result == "exists":
            st.error("Username already exists ❌")
        elif result == "weak":
            st.warning("Password must be at least 6 characters long ⚠")
        elif result == "invalid_email":
            st.warning("Invalid email format. Please enter a valid email. ⚠")
elif section == "Forgot Password":
    email = st.text_input("Registered Email")
    if st.button("Send OTP"):
        otp = generate_otp(username)
        if otp:
            st.info(f"Simulated OTP (for demo only): {otp}")
            st.session_state["otp_sent"] = True
        else:
            st.error("Username not found ❌")
    if st.session_state.get("otp_sent"):
        entered_otp = st.text_input("Enter OTP")
        new_password = st.text_input("New Password", type="password")
        if st.button("Reset Password"):
            result = reset_password(username, entered_otp, new_password)
            if result == "ok":
                st.success("Password reset successful ✅")
                st.session_state["otp_sent"] = False
            elif result == "invalid_otp":
                st.error("Invalid OTP ❌")
            elif result == "not_found":
                st.error("Username not found ❌")
elif section == "View Users (Admin)":
    st.subheader("📋 Registered Users (Admin View)")
    users = load_users()
    if users:
        for user, data in users.items():
            st.write(f"👤 **{user}** — 📧 {data.get('email', 'N/A')}")
    else:
        st.info("No users registered yet.")
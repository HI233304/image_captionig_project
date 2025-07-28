# 🧠 Image Captioning & Segmentation App

This Streamlit web app allows users to:
- Register/login with secure password hashing
- Reset passwords via OTP (simulated)
- Upload or capture images
- Generate image captions (simulated)
- View basic image segmentation

## 📂 Project Structure
- `app.py` - Main Streamlit app
- `login.py` - Handles user registration, login, OTP reset
- `model_captioning.py` - Simulated image captioning model
- `model_segmentation.py` - Simulated image segmentation model
- `util.py` - Captures images from webcam
- `requirements.txt` - Python dependencies

## 🚀 How to Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

✅ Prepared for Internship Submission  
📧 Add real OTP/email integrations if required
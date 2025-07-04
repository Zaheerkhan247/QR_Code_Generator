import streamlit as st
import qrcode
from PIL import Image
from io import BytesIO

# Page config
st.set_page_config(page_title="QR Code Generator", page_icon="🔳")

# 🔷 Styling via custom CSS
st.markdown("""
    <style>
        body {
            background-color: #f5f5f5;
            font-family: 'Segoe UI', sans-serif;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            border-radius: 10px;
            padding: 8px 16px;
            font-weight: bold;
            transition: all 0.3s ease-in-out;
        }
        .stButton>button:hover {
            background-color: #45a049;
            transform: scale(1.05);
        }
    </style>
""", unsafe_allow_html=True)

# 🔷 App Heading
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🔳 QR Code Generator</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: gray;'>Turn any text or link into a QR Code in seconds ✨</h4>", unsafe_allow_html=True)
st.markdown("---")

# 🔷 Input field
text = st.text_input("📝 Enter text or URL to convert into QR Code:")

# 🔷 Generate button
if st.button("Generate QR Code"):
    if text.strip() == "":
        st.warning("⚠️ Please enter something first!")
    else:
        qr = qrcode.make(text).convert("RGB")
        buf = BytesIO()
        qr.save(buf, format="PNG")

        # 🔷 Center image in styled div
        st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
        st.image(qr, caption="✅ Here's your QR Code", width=250)
        st.markdown("</div>", unsafe_allow_html=True)

        # 🔷 Download button
        st.download_button(
            label="⬇️ Download QR Code",
            data=buf.getvalue(),
            file_name="qr_code.png",
            mime="image/png"
        )

# 🔷 Sidebar info
st.sidebar.markdown("## ℹ️ About this App")
st.sidebar.info("This app was built using Python and Streamlit. It can generate downloadable QR codes from any text or URL.")
st.sidebar.markdown("Created by **Zaheer** 💚")

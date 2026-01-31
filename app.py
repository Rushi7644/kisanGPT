import streamlit as st
import base64

# 🔹 MUST be first Streamlit command
st.set_page_config(
    page_title="KrishiSahay 🌾",
    layout="centered"
)

# 🔹 Convert image to base64
def get_base64_bg(image_path):
    with open(image_path, "rb") as img:
        return base64.b64encode(img.read()).decode()

bg_image = get_base64_bg("farmer_bg.jpg")

# 🌾 Background Image + Overlay
st.markdown(
    f"""
    <style>
    .stApp {{
        background:
            linear-gradient(rgba(0,0,0,0.65), rgba(0,0,0,0.65)),
            url("data:image/jpg;base64,{bg_image}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    .block-container {{
        max-width: 850px;
        padding: 3rem;
        background: rgba(0,0,0,0.55);
        border-radius: 18px;
        box-shadow: 0 0 30px rgba(0,0,0,0.7);
    }}

    h1, h2, h3 {{
        color: #f1f8e9;
    }}

    label {{
        color: #e8f5e9 !important;
        font-weight: 600;
    }}

    input, textarea, select {{
        background-color: #1e1e1e !important;
        color: white !important;
        border-radius: 10px !important;
    }}

    .stButton > button {{
        background-color: #2e7d32;
        color: white;
        font-size: 16px;
        font-weight: 600;
        padding: 0.6em 1.4em;
        border-radius: 12px;
        border: none;
        width: 100%;
    }}

    .stButton > button:hover {{
        background-color: #1b5e20;
        transform: scale(1.02);
    }}

    .stAlert {{
        border-radius: 12px;
        font-size: 15px;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# ================= APP LOGIC =================

from gemini_helper import get_gemini_answer
from offline_search import get_offline_answer

st.title("🌾 KrishiSahay – Farmer AI Assistant")
st.write("Ask questions about crops, pests, fertilizers, and government schemes")

language = st.selectbox(
    "Select Language",
    [
        "English",
        "Hindi",
        "Telugu",
        "Tamil",
        "Kannada",
        "Malayalam",
        "Marathi",
        "Gujarati",
        "Punjabi",
        "Bengali",
        "Odia",
        "Assamese",
        "Urdu",
        "Sanskrit",
        "Nepali",
        "Konkani",
        "Manipuri (Meitei)",
        "Bodo",
        "Dogri",
        "Maithili",
        "Santhali",
        "Sindhi"
    ]
)

query = st.text_input("Enter your farming question")

if st.button("Get Answer"):
    if query.strip() == "":
        st.warning("Please enter a question")
    else:
        offline = get_offline_answer(query)
        if offline:
            st.success("📘 Offline Answer")
            st.write(offline)
        else:
            with st.spinner("🤖 Generating AI Answer..."):
                try:
                    answer = get_gemini_answer(query, language)
                    st.success("🌐 AI Answer")
                    st.write(answer)
                except Exception as e:
                    st.error("AI error")
                    st.write(e)

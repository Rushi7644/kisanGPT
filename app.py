import streamlit as st
from gemini_helper import get_gemini_answer
from offline_search import get_offline_answer

st.set_page_config(page_title="KrishiSahay 🌾")

st.title("🌾 KrishiSahay – Farmer AI Assistant")
st.write("Ask questions about crops, pests, fertilizers, and government schemes")

language = st.selectbox("Select Language", ["English", "Hindi"])
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
                    st.error("Gemini API error")
                    st.write(e)

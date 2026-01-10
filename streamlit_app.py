import os
import streamlit as st
import google.generativeai as genai

# Load API key from Streamlit secrets or environment variable.
API_KEY = st.secrets.get("GENAI_API_KEY") if hasattr(st, "secrets") else None
if not API_KEY:
    API_KEY = os.getenv("GENAI_API_KEY")

if API_KEY:
    genai.configure(api_key=API_KEY)

st.set_page_config(page_title="Mithilesh AI", page_icon="💎")

with st.sidebar:
    st.title("💎 VIP Member")
    st.header("फीस: ₹99 मात्र")
    password = st.text_input("पासवर्ड डालें", type="password")
    st.markdown("[🔴 YouTube: Crazy Marg](https://www.youtube.com/@MithileshDubey-f2e)")

if 'password' not in locals():
    password = ""

if password == "12345":
    st.title("🚀 Mithilesh AI Pro")
    prompt = st.chat_input("यहाँ सवाल लिखें...")
    if prompt:
        if not API_KEY:
            st.error("API key not found. Set GENAI_API_KEY in Streamlit secrets or environment variables.")
        else:
            try:
                model = genai.GenerativeModel('gemini-1.5-flash')
                res = model.generate_content(prompt)
                # `res` may be complex; write text safely
                text = getattr(res, 'text', None) or str(res)
                st.write(text)
            except Exception as e:
                st.error(f"Generation error: {e}")
else:
    st.title("🔒 ऐप अभी लॉक है")
    st.write("### इसे खोलने के लिए ₹99 का सब्सक्रिप्शन चाहिए।")
    st.info("डेमो पासवर्ड है: 12345 (इसे साइडबार में डालें)")
import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

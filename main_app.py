import streamlit as st
import os
import time

# 1. प्रोफेशनल ऐप सेटिंग्स
st.set_page_config(
    page_title="SAMAD SENTRY v1.0",
    layout="centered", 
    initial_sidebar_state="collapsed",
    page_icon="🛡️"
)

# 2. पूरी तरह से रिस्पॉन्सिव (Responsive) CSS
st.markdown("""
<style>
    .stApp {
        background-color: #0B0F19; 
        color: #E2E8F0;
    }
    h1 {
        text-align: center; 
        color: #10B981; 
        font-family: 'Segoe UI', Roboto, Helvetica, sans-serif;
        font-size: calc(24px + 1.5vw);
    }
    .stButton>button {
        background: linear-gradient(135px, #059669 0%, #10B981 100%);
        color: white; 
        border: none;
        padding: 12px 24px;
        width: 100%; 
        border-radius: 8px; 
        font-weight: bold;
        box-shadow: 0 4px 6px -1px rgba(16, 185, 129, 0.2);
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 15px -3px rgba(16, 185, 129, 0.3);
    }
</style>
""", unsafe_allow_html=True)

# 3. टाइटल
st.title("🛡️ SAMAD SENTRY v1.0")

# 4. फोटो लोड करने का सबसे पक्का तरीका
image_path = "cyber-security-concept-digital-art.jpg"

# अगर विंडोज ने नाम के पीछे छुपा हुआ एक्सटेंशन लगा दिया हो तो उसे भी चेक करेगा
if not os.path.exists(image_path):
    if os.path.exists("cyber-security-concept-digital-art.jpg.jpg"):
        image_path = "cyber-security-concept-digital-art.jpg.jpg"
    elif os.path.exists("cyber-security-concept-digital-art.jpg.ico"):
        image_path = "cyber-security-concept-digital-art.jpg.ico"

if os.path.exists(image_path):
    st.image(image_path, width=600)
else:
    st.warning("⚠️ फोटो फोल्डर में तो है, पर उसका नाम मैच नहीं हो रहा है।")

st.markdown("<p style='text-align: center; font-size: 18px;'>Global Autonomous Defense System</p>", unsafe_allow_html=True)

# 5. सिक्योरिटी फीचर
if st.button("ENGAGE GLOBAL SHIELD"):
    with st.spinner('सिस्टम सक्रिय हो रहा है...'):
        time.sleep(1)
        st.write("🔍 AI Security Scanner: Active")
        st.success("SAMAD SENTRY: पूरी तरह सक्रिय है।")
        st.balloons()

st.markdown("---")
st.markdown("<p style='text-align: center;'>Status: 24/7 Professional Protection | © 2026</p>", unsafe_allow_html=True)
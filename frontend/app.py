import sys
import os

# 1. THIS MUST BE LINE 1-4
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 2. NOW you can do your other imports
import streamlit as st
import asyncio
from streamlit_mic_recorder import speech_to_text
from backend.query_engine import ask_dastoor
import edge_tts



# Adds the root directory (dastoordesk) to the python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# --- Your other imports (like 'from backend.query_engine import ask_dastoor') should come AFTER this ---
st.set_page_config(page_title="Dastoor Desk", page_icon="⚖️")

# Custom CSS for the Dastoor Desk branding
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 20px; }
    </style>
    """, unsafe_allow_html=True)

st.title("⚖️ Dastoor Desk")
st.caption("AI-Powered Legal Awareness & Guidance Platform")

# 1. VOICE INPUT SECTION
st.subheader("How can we help you today?")
col1, col2 = st.columns([4, 1])

with col2:
    # This button handles Urdu and English speech automatically
    text_input = speech_to_text(
        language='ur', # Set to 'ur' for Urdu support; it also handles English well
        start_prompt="🎤 Speak",
        stop_prompt="🛑 Stop",
        key='speech'
    )

with col1:
    user_query = st.chat_input("Describe your legal problem...")

# Use voice input if available, otherwise use typed input
final_query = text_input if text_input else user_query

if final_query:
    with st.chat_message("user"):
        st.write(final_query)

    with st.chat_message("assistant"):
        with st.spinner("Analyzing legal documents..."):
            response = ask_dastoor(final_query)
            st.write(response)
            
            # 2. VOICE OUTPUT SECTION
            if st.button("🔊 Listen to Advice"):
                async def text_to_speech(text):
                    # Uses the high-quality Pakistani Urdu voice
                    communicate = edge_tts.Communicate(text, "ur-PK-AsadNeural")
                    await communicate.save("output.mp3")
                
                asyncio.run(text_to_speech(response))
                st.audio("output.mp3", format="audio/mp3", autoplay=True)
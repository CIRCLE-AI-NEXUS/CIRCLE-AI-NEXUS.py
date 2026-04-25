import streamlit as st
from groq import Groq

# 1. SETUP HALAMAN & CSS CUSTOM (Biar UI/UX Berkelas)
st.set_page_config(page_title="KopiKita AI Barista", page_icon="☕", layout="centered")

st.markdown("""
    <style>
    /* Gradient Background untuk Header */
    .main {
        background-color: #0e1117;
    }
    .stChatInputContainer {
        padding-bottom: 20px;
    }
    /* Styling Title & Badge */
    .title-text {
        font-size: 2.5rem;
        font-weight: 800;
        color: #FFFFFF;
        margin-bottom: 0px;
    }
    .subtitle-text {
        font-size: 1rem;
        color: #A0A0A0;
        margin-bottom: 20px;
    }
    .powered-by {
        font-size: 0.8rem;
        font-weight: 600;
        letter-spacing: 1px;
        color: #00FFA3;
        text-transform: uppercase;
    }
    /* Custom Card for AI Info */
    .info-card {
        background: rgba(255, 255, 255, 0.05);
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #00FFA3;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. API SETUP
# Jangan lupa ganti API Key lo di sini kalau mau dideploy!
client = Groq(api_key="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")

# 3. SYSTEM PROMPT (The Brain)
SYSTEM_PROMPT = """
Nama kamu adalah "Barista AI KopiKita". Kamu adalah asisten digital tercanggih di Jakarta Selatan.
Gaya bicara: Ramah, santai, profesional, sedikit aksen Jaksel (code-switching) tapi tetep jelas.
Powered by: CIRCLE-AI (Inovasi Digital Indonesia).

INFO MENU:
- Espresso (20rb), Cappuccino (30rb), Latte (32rb), Matcha (35rb).
- Snack: Croissant (25rb), Brownies (28rb).

PROMO: 
- Diskon 20% buat pelajar. 
- Jumat: Buy 1 Get 1 Latte.

Tugas: Bantu customer milih menu, jelasin promo, dan bikin mereka ngerasa dilayani barista pro.
"""

# 4. SIDEBAR (UX: Biar Klien liat Benefit Bisnis)
with st.sidebar:
    st.markdown("<p class='powered-by'>SYSTEM STATUS</p>", unsafe_allow_html=True)
    st.success("CIRCLE-AI Engine: Online")
    st.info("Model: CIRCLE-AI-NEXUS")
    st.divider()
    st.markdown("### ☕ KopiKita Info")
    st.write("📍 Jakarta Selatan")
    st.write("⏰ 08.00 - 23.00")
    st.divider()
    st.caption("© 2026 Inovasi Digital Indonesia. Managed by CIRCLE-AI Ecosystem.")

# 5. HEADER UI
st.markdown("<p class='powered-by'>PREMIUM DIGITAL EXPERIENCE</p>", unsafe_allow_html=True)
st.markdown("<h1 class='title-text'>AI Barista KopiKita ☕</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle-text'>Experience the future of ordering with Indonesian Digital Innovation.</p>", unsafe_allow_html=True)

# UX: Info Card buat First-time User
with st.container():
    st.markdown("""
    <div class='info-card'>
        <b>Barista AI Ready!</b><br>
        Tanya soal rekomendasi kopi, promo pelajar, atau lokasi kita hari ini.
    </div>
    """, unsafe_allow_html=True)

# 6. CHAT LOGIC
if "messages" not in st.session_state:
    st.session_state.messages = []

# Tampilkan history chat dengan icon modern
for msg in st.session_state.messages:
    avatar = "👤" if msg["role"] == "user" else "🤖"
    with st.chat_message(msg["role"], avatar=avatar):
        st.markdown(msg["content"])

# User Input
if prompt := st.chat_input("Mau pesen apa hari ini, Bestie?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)

    # AI Response
    with st.chat_message("assistant", avatar="🤖"):
        with st.spinner("Analyzing request via CIRCLE-AI..."):
            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    *st.session_state.messages
                ],
                temperature=0.7,
            )
            reply = response.choices[0].message.content
            st.markdown(reply)
            
    st.session_state.messages.append({"role": "assistant", "content": reply})

# 7. FOOTER (Branding)
st.divider()
st.markdown("<center style='color: grey;'>Powered by <b>CIRCLE-AI</b> | Masa Depan Inovasi Digital Indonesia 🇮🇩</center>", unsafe_allow_html=True)
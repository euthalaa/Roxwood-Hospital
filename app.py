import streamlit as st
import streamlit.components.v1 as components

# Mengatur tampilan halaman Streamlit agar memenuhi layar (Full Width)
st.set_page_config(
    page_title="RH Portal - Roxwood Hospital",
    page_icon="🏥",
    layout="wide"
)

# MENYEMBUNYIKAN PADDING (Sudah diperbaiki parameternya)
st.markdown("""
    <style>
        .block-container { padding: 0px !important; }
        footer { visibility: hidden; }
        #MainMenu { visibility: hidden; }
    </style>
""", unsafe_allow_html=True)

# 1. Ambil API Key Gemini secara aman dari Streamlit Secrets
try:
    GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
except Exception:
    st.error("API Key tidak ditemukan! Pastikan Anda sudah mengatur 'GEMINI_API_KEY' di Secrets.")
    GEMINI_API_KEY = ""

# 2. Baca file HTML asli tanpa mengubah isinya di harddisk
with open("rh_portal_v3.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# 3. Masukkan API Key secara dinamis ke baris variabel kosong di Javascript HTML
html_terbuka_dengan_key = html_content.replace(
    'const apiKey = "";', 
    f'const apiKey = "{GEMINI_API_KEY}";'
)

# 4. Tampilkan HTML yang sudah berisi API Key ke dalam aplikasi Streamlit
components.html(html_terbuka_dengan_key, height=900, scrolling=True)

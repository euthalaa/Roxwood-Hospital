import streamlit as st
import streamlit.components.v1 as components

# 1. Konfigurasi Halaman (Full Width)
st.set_page_config(
    page_title="Roxwood Hospital - Integrated Medical Systems",
    page_icon="🏥",
    layout="wide"
)

# Integrasi Tailwind CSS untuk mendesain dashboard utama
st.markdown("""
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        .block-container { padding: 0px !important; }
        footer { visibility: hidden; }
        #MainMenu { visibility: hidden; }
        body { background-color: #f8fafc; }
    </style>
""", unsafe_allow_html=True)

# 2. Ambil API Key Gemini secara aman
try:
    GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
except Exception:
    GEMINI_API_KEY = ""

# 3. Inisialisasi Session State agar Streamlit ingat halaman yang sedang dibuka
if "halaman_aktif" not in st.session_state:
    st.session_state.halaman_aktif = "dashboard_utama"

# --- FUNGSI UNTUK MEMBACA & SUNTIK API KEY KE HTML ---
def tampilkan_portal(nama_file_html):
    # Tombol Kembali ke Dashboard Utama
    if st.button("⬅ Kembali ke Dashboard Utama", type="secondary"):
        st.session_state.halaman_aktif = "dashboard_utama"
        st.rerun()
        
    try:
        with open(nama_file_html, "r", encoding="utf-8") as f:
            html_content = f.read()
        # Suntikkan API Key ke variabel JavaScript
        html_dengan_key = html_content.replace('const apiKey = "";', f'const apiKey = "{GEMINI_API_KEY}";')
        components.html(html_dengan_key, height=950, scrolling=True)
    except FileNotFoundError:
        st.error(f"File '{nama_file_html}' tidak ditemukan di server/GitHub Anda!")

# ==============================================================================
# JIKA HALAMAN AKTIF ADALAH DASHBOARD UTAMA (Mendesain UI Persis Seperti Gambar)
# ==============================================================================
if st.session_state.halaman_aktif == "dashboard_utama":
    
    # 🌟 Bagian Header Dashboard
    st.markdown("""
    <div style="text-align: center; font-family: sans-serif; padding-top: 40px; padding-bottom: 20px;">
        <!-- Logo Perisai Medis -->
        <div style="font-size: 70px; color: #a11a1a; line-height: 1;">🛡️</div>
        <h1 style="color: #6b0f0f; font-size: 45px; font-weight: 800; tracking-style: tight; margin: 10px 0 2px 0; letter-spacing: 2px;">ROXWOOD HOSPITAL</h1>
        <p style="color: #64748b; font-size: 14px; font-weight: 600; text-transform: uppercase; letter-spacing: 3px; margin-bottom: 15px;">Integrated Medical Systems</p>
        <div style="color: #a11a1a; font-size: 24px; margin-bottom: 15px;">⚡📈⚡</div>
        <h3 style="color: #1e293b; font-size: 22px; font-weight: 700; margin-bottom: 5px;">Welcome to Roxwood Hospital Integrated Portal</h3>
        <p style="color: #64748b; font-size: 15px;">Pilih sistem yang ingin Anda akses</p>
    </div>
    """, unsafe_allow_html=True)

    # 🌟 Bagian Grid Menu 4 Kartu (Menggunakan Kolom Streamlit)
    col1, col2, col3, col4 = st.columns(4)

    # --- KARTU 1: DIAGNOSE AND SURGERY ---
    with col1:
        st.markdown("""
        <div style="background: white; border-radius: 20px; padding: 30px 20px; text-align: center; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); min-height: 320px;">
            <div style="background: #fdf2f2; width: 80px; height: 80px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 20px auto; font-size: 35px;">🧑‍⚕️</div>
            <h4 style="font-size: 18px; font-weight: 700; color: #1e293b; margin-bottom: 10px;">Diagnose and Surgery</h4>
            <p style="font-size: 13px; color: #64748b; line-height: 1.5; margin-bottom: 25px;">Manajemen diagnosis, tindakan bedah, dan rekam medis pasien.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Akses ➔", key="btn_diag", use_container_width=True, type="primary"):
            st.session_state.halaman_aktif = "portal_diagnosis"
            st.rerun()

    # --- KARTU 2: RADIOLOGY ---
    with col2:
        st.markdown("""
        <div style="background: white; border-radius: 20px; padding: 30px 20px; text-align: center; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); min-height: 320px;">
            <div style="background: #fdf2f2; width: 80px; height: 80px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 20px auto; font-size: 35px;">🩻</div>
            <h4 style="font-size: 18px; font-weight: 700; color: #1e293b; margin-bottom: 10px;">Radiology</h4>
            <p style="font-size: 13px; color: #64748b; line-height: 1.5; margin-bottom: 25px;">Sistem informasi radiologi dan pencitraan diagnostik.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Akses ➔", key="btn_rad", use_container_width=True, type="primary"):
            st.session_state.halaman_aktif = "portal_radiologi"
            st.rerun()

    # --- KARTU 3: LABORATORY ---
    with col3:
        st.markdown("""
        <div style="background: white; border-radius: 20px; padding: 30px 20px; text-align: center; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); min-height: 320px;">
            <div style="background: #fdf2f2; width: 80px; height: 80px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 20px auto; font-size: 35px;">🧪</div>
            <h4 style="font-size: 18px; font-weight: 700; color: #1e293b; margin-bottom: 10px;">Laboratory</h4>
            <p style="font-size: 13px; color: #64748b; line-height: 1.5; margin-bottom: 25px;">Manajemen data laboratorium dan hasil pemeriksaan darah/urine.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Akses ➔", key="btn_lab", use_container_width=True, type="primary"):
            st.session_state.halaman_aktif = "portal_lab"
            st.rerun()

    # --- KARTU 4: PSYCHIATRIC ---
    with col4:
        st.markdown("""
        <div style="background: white; border-radius: 20px; padding: 30px 20px; text-align: center; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); min-height: 320px;">
            <div style="background: #fdf2f2; width: 80px; height: 80px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 20px auto; font-size: 35px;">🧠</div>
            <h4 style="font-size: 18px; font-weight: 700; color: #1e293b; margin-bottom: 10px;">Psychiatric</h4>
            <p style="font-size: 13px; color: #64748b; line-height: 1.5; margin-bottom: 25px;">Sistem informasi psikiatri dan rekam medis kesehatan mental.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Akses ➔", key="btn_psi", use_container_width=True, type="primary"):
            st.session_state.halaman_aktif = "portal_psikiatri"
            st.rerun()

    # 🌟 Bagian Footer Merah di Bawah
    st.markdown("""
    <div style="background-color: #8b1111; color: white; text-align: center; padding: 25px; margin-top: 60px; font-size: 13px; border-top: 4px solid #5a0a0a;">
        <div style="font-size: 20px; margin-bottom: 5px;">🛡️</div>
        © 2026 Roxwood Hospital. All rights reserved.
    </div>
    """, unsafe_allow_html=True)

# ==============================================================================
# LOGIKA PENGALIHAN HALAMAN PORTAL MEDIS (IFRAME HTML)
# ==============================================================================
elif st.session_state.halaman_aktif == "portal_diagnosis":
    tampilkan_portal("rh_portal_v3.html")

elif st.session_state.halaman_aktif == "portal_radiologi":
    tampilkan_portal("rh_radiology.html")

elif st.session_state.halaman_aktif == "portal_lab":
    tampilkan_portal("rh_laboratory.html")

elif st.session_state.halaman_aktif == "portal_psikiatri":
    tampilkan_portal("rh_psychiatric.html")

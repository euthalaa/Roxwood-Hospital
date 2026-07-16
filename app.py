import streamlit as st
import streamlit.components.v1 as components

# ==============================================================================
# 1. KONFIGURASI HALAMAN UTAMA STREAMLIT
# ==============================================================================
st.set_page_config(
    page_title="Roxwood Hospital - Integrated Medical Systems",
    page_icon="🏥",
    layout="wide"
)

# Menyembunyikan padding bawaan Streamlit agar layout HTML menyatu penuh
st.markdown("""
    <style>
        .block-container { padding: 0px !important; }
        footer { visibility: hidden; }
        #MainMenu { visibility: hidden; }
        body { background-color: #f8fafc; }
        /* Mengubah warna tombol bawaan Streamlit agar senada dengan tema merah */
        .stButton>button {
            background-color: #ffffff;
            color: #8b1111;
            border: 1px solid #8b1111;
            font-weight: bold;
            border-radius: 8px;
            transition: all 0.2s ease;
        }
        .stButton>button:hover {
            background-color: #8b1111;
            color: #ffffff;
            border-color: #8b1111;
        }
    </style>
""", unsafe_allow_html=True)

# ==============================================================================
# 2. SISTEM KEAMANAN API KEY GEMINI
# ==============================================================================
try:
    GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
except Exception:
    GEMINI_API_KEY = ""

# ==============================================================================
# 3. MANAGEMENT NAVIGATION (SESSION STATE)
# ==============================================================================
if "halaman_aktif" not in st.session_state:
    st.session_state.halaman_aktif = "dashboard_utama"

# ==============================================================================
# 4. FUNGSI UNTUK MEMBUKA FILE HTML & SUNTIK API KEY (DENGAN TOMBOL BACK AMAN)
# ==============================================================================
def tampilkan_portal(nama_file_html):
    # Membuat container khusus di bagian paling atas untuk Tombol Kembali ke Dashboard
    col_back, col_space = st.columns([1, 4])
    
    with col_back:
        # Tombol resmi Streamlit Python (Berada di luar Iframe sehingga aman dari blokir browser)
        st.write("") # Memberi sedikit jarak atas
        if st.button("⬅ Kembali ke Dashboard", use_container_width=True):
            st.session_state.halaman_aktif = "dashboard_utama"
            st.rerun() # Memaksa Streamlit langsung memuat ulang halaman utama saat itu juga

    # Garis pembatas dekoratif antara navigasi atas dan portal rumah sakit
    st.markdown("<hr style='margin-top: 5px; margin-bottom: 15px; border-color: #e2e8f0;'>", unsafe_allow_html=True)
        
    # Proses membaca file HTML
    try:
        with open(nama_file_html, "r", encoding="utf-8") as f:
            html_content = f.read()
        
        # Menyisipkan API Key rahasia ke dalam kode JavaScript HTML yang kosong secara otomatis
        html_dengan_key = html_content.replace('const apiKey = "";', f'const apiKey = "{GEMINI_API_KEY}";')
        
        # Menampilkan file HTML ke layar web
        components.html(html_dengan_key, height=950, scrolling=True)
        
    except FileNotFoundError:
        st.error(f"File '{nama_file_html}' tidak ditemukan! Pastikan nama file di GitHub sudah benar.")

# ==============================================================================
# 5. STRUKTUR HALAMAN UTAMA DASHBOARD (KORIDOR RUMAH SAKIT)
# ==============================================================================
if st.session_state.halaman_aktif == "dashboard_utama":
    
    # Header Dashboard (Logo Perisai, Judul Besar Roxwood Hospital, dll)
    st.markdown("""
    <div style="text-align: center; font-family: sans-serif; padding-top: 40px; padding-bottom: 20px;">
        <!-- Logo Perisai Medis -->
        <div style="font-size: 70px; color: #a11a1a; line-height: 1;">🛡️</div>
        <h1 style="color: #6b0f0f; font-size: 45px; font-weight: 800; margin: 10px 0 2px 0; letter-spacing: 2px;">ROXWOOD HOSPITAL</h1>
        <p style="color: #64748b; font-size: 14px; font-weight: 600; text-transform: uppercase; letter-spacing: 3px; margin-bottom: 15px;">Integrated Medical Systems</p>
        <div style="color: #a11a1a; font-size: 24px; margin-bottom: 15px;">⚡📈⚡</div>
        <h3 style="color: #1e293b; font-size: 22px; font-weight: 700; margin-bottom: 5px;">Welcome to Roxwood Hospital Integrated Portal</h3>
        <p style="color: #64748b; font-size: 15px;">Pilih sistem yang ingin Anda akses</p>
    </div>
    """, unsafe_allow_html=True)

    # Membuat Layout 4 Kolom Berjejer untuk Kartu Menu Akses
    col1, col2, col3, col4 = st.columns(4)

    # --- KARTU MENU 1: DIAGNOSE AND SURGERY ---
    with col1:
        st.markdown("""
        <div style="background: white; border-radius: 20px; padding: 30px 20px; text-align: center; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); min-height: 310px;">
            <div style="background: #fdf2f2; width: 80px; height: 80px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 20px auto; font-size: 35px;">🧑‍⚕️</div>
            <h4 style="font-size: 18px; font-weight: 700; color: #1e293b; margin-bottom: 10px;">Diagnose and Surgery</h4>
            <p style="font-size: 13px; color: #64748b; line-height: 1.5; margin-bottom: 25px;">Manajemen diagnosis, tindakan bedah, dan rekam medis pasien.</p>
        </div>
        """, unsafe_allow_html=True)
        # Tombol Akses Pindah ke Portal Diagnosis
        if st.button("Akses ➔", key="btn_diag", use_container_width=True):
            st.session_state.halaman_aktif = "portal_diagnosis"
            st.rerun()

    # --- KARTU MENU 2: RADIOLOGY ---
    with col2:
        st.markdown("""
        <div style="background: white; border-radius: 20px; padding: 30px 20px; text-align: center; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); min-height: 310px;">
            <div style="background: #fdf2f2; width: 80px; height: 80px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 20px auto; font-size: 35px;">🩻</div>
            <h4 style="font-size: 18px; font-weight: 700; color: #1e293b; margin-bottom: 10px;">Radiology</h4>
            <p style="font-size: 13px; color: #64748b; line-height: 1.5; margin-bottom: 25px;">Sistem informasi radiologi dan pencitraan diagnostik.</p>
        </div>
        """, unsafe_allow_html=True)
        # Tombol Akses Pindah ke Portal Radiologi
        if st.button("Akses ➔", key="btn_rad", use_container_width=True):
            st.session_state.halaman_aktif = "portal_radiologi"
            st.rerun()

    # --- KARTU MENU 3: LABORATORY ---
    with col3:
        st.markdown("""
        <div style="background: white; border-radius: 20px; padding: 30px 20px; text-align: center; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); min-height: 310px;">
            <div style="background: #fdf2f2; width: 80px; height: 80px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 20px auto; font-size: 35px;">🧪</div>
            <h4 style="font-size: 18px; font-weight: 700; color: #1e293b; margin-bottom: 10px;">Laboratory</h4>
            <p style="font-size: 13px; color: #64748b; line-height: 1.5; margin-bottom: 25px;">Manajemen data laboratorium dan hasil pemeriksaan darah/urine.</p>
        </div>
        """, unsafe_allow_html=True)
        # Tombol Akses Pindah ke Portal Lab
        if st.button("Akses ➔", key="btn_lab", use_container_width=True):
            st.session_state.halaman_aktif = "portal_lab"
            st.rerun()

    # --- KARTU MENU 4: PSYCHIATRIC ---
    with col4:
        st.markdown("""
        <div style="background: white; border-radius: 20px; padding: 30px 20px; text-align: center; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); min-height: 310px;">
            <div style="background: #fdf2f2; width: 80px; height: 80px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 20px auto; font-size: 35px;">🧠</div>
            <h4 style="font-size: 18px; font-weight: 700; color: #1e293b; margin-bottom: 10px;">Psychiatric</h4>
            <p style="font-size: 13px; color: #64748b; line-height: 1.5; margin-bottom: 25px;">Sistem informasi psikiatri dan rekam medis kesehatan mental.</p>
        </div>
        """, unsafe_allow_html=True)
        # Tombol Akses Pindah ke Portal Psikiatri
        if st.button("Akses ➔", key="btn_psi", use_container_width=True):
            st.session_state.halaman_aktif = "portal_psikiatri"
            st.rerun()

    # Bagian Footer Merah bawah seperti contoh gambar
    st.markdown("""
    <div style="background-color: #8b1111; color: white; text-align: center; padding: 25px; margin-top: 60px; font-size: 13px; border-top: 4px solid #5a0a0a;">
        <div style="font-size: 20px; margin-bottom: 5px;">🛡️</div>
        © 2026 Roxwood Hospital. All rights reserved.
    </div>
    """, unsafe_allow_html=True)

# ==============================================================================
# 6. LOGIKA PENGALIHAN NAVIGASI KE MASING-MASING FILE HTML PORTAL MEDIS
# ==============================================================================
elif st.session_state.halaman_aktif == "portal_diagnosis":
    tampilkan_portal("rh_portal_v3.html")

elif st.session_state.halaman_aktif == "portal_radiologi":
    tampilkan_portal("rh_radiology.html")

elif st.session_state.halaman_aktif == "portal_lab":
    tampilkan_portal("rh_laboratory.html")

elif st.session_state.halaman_aktif == "portal_psikiatri":
    tampilkan_portal("rh_psychiatric.html")

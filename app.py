
import streamlit as st
import pandas as pd
import os
from datetime import datetime
from utils import simpan_absen, load_absensi, export_pdf

DATA_PATH = "data/absensi.csv"

st.title("📚 Sistem Absensi TK Tadika Mesra")

menu = st.sidebar.radio("Navigasi", ["Absen Masuk", "Lihat Rekap", "Cetak Laporan"])

if menu == "Absen Masuk":
    st.header("Form Absensi Harian")
    nama = st.selectbox("Pilih Nama Anak", ["Ali", "Budi", "Citra", "Dina", "Eka"])
    tanggal = datetime.today().strftime('%Y-%m-%d')
    waktu = datetime.now().strftime('%H:%M:%S')
    status = st.selectbox("Status", ["Masuk", "Pulang"])
    
    if st.button("Simpan Absensi"):
        simpan_absen(nama, tanggal, waktu, status, DATA_PATH)
        st.success(f"Absensi untuk {nama} berhasil disimpan.")

elif menu == "Lihat Rekap":
    st.header("Rekap Absensi")
    df = load_absensi(DATA_PATH)
    st.dataframe(df)

elif menu == "Cetak Laporan":
    st.header("Cetak Laporan PDF")
    df = load_absensi(DATA_PATH)
    if not df.empty:
        pdf_path = export_pdf(df, "laporan/laporan_absensi.pdf")
        with open(pdf_path, "rb") as f:
            st.download_button("📄 Download PDF", f, file_name="laporan_absensi.pdf")
    else:
        st.warning("Data absensi kosong.")

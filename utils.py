
import pandas as pd
import os
from fpdf import FPDF

def simpan_absen(nama, tanggal, waktu, status, path):
    df = pd.read_csv(path) if os.path.exists(path) else pd.DataFrame(columns=["Nama", "Tanggal", "Waktu", "Status"])
    new_row = pd.DataFrame([[nama, tanggal, waktu, status]], columns=df.columns)
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv(path, index=False)

def load_absensi(path):
    return pd.read_csv(path) if os.path.exists(path) else pd.DataFrame(columns=["Nama", "Tanggal", "Waktu", "Status"])

def export_pdf(df, output_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Laporan Absensi TK Tadika Mesra", ln=True, align="C")
    pdf.ln(10)

    for col in df.columns:
        pdf.cell(45, 10, col, border=1)
    pdf.ln()

    for _, row in df.iterrows():
        for item in row:
            pdf.cell(45, 10, str(item), border=1)
        pdf.ln()

    pdf.output(output_path)
    return output_path

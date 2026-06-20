"""
automate_Ahmaddani.py
Konversi otomatis dari tahapan preprocessing yang sudah dilakukan secara manual
pada notebook Eksperimen_SML_Ahmaddani.ipynb.

Fungsi ini akan:
1. Memuat dataset_raw/diabetes.csv
2. Membersihkan data (drop duplikat + imputasi median pada kolom medis yang bernilai 0)
3. Menyimpan hasilnya sebagai dataset baru yang siap dipakai untuk training (dataset_preprocessing.csv)
"""

import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

COLS_TO_CLEAN = ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]


def run_preprocessing(input_path: str, output_path: str) -> pd.DataFrame:
    print("Memulai proses preprocessing otomatis...")

    # 1. Load data
    df = pd.read_csv(input_path)
    print(f"Data awal: {df.shape[0]} baris, {df.shape[1]} kolom.")

    # 2. Hapus data duplikat jika ada
    df_clean = df.drop_duplicates()

    # 3. Nilai 0 pada kolom medis berikut secara klinis tidak masuk akal,
    #    sehingga diperlakukan sebagai missing value dan diisi dengan median.
    for col in COLS_TO_CLEAN:
        df_clean[col] = df_clean[col].replace(0, df_clean[col].median())

    print(f"Data setelah dibersihkan: {df_clean.shape[0]} baris.")

    # 4. Simpan dataset hasil preprocessing agar siap dipakai pada tahap modelling
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    df_clean.to_csv(output_path, index=False)
    print(f"Selesai! Dataset hasil preprocessing disimpan di: {output_path}")

    return df_clean


if __name__ == "__main__":
    input_file = os.path.join(BASE_DIR, "..", "dataset_raw", "diabetes.csv")
    output_file = os.path.join(BASE_DIR, "dataset_preprocessing.csv")
    run_preprocessing(input_file, output_file)

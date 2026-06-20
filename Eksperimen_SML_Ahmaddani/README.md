# Eksperimen_SML_Ahmaddani

Repository ini berisi proses eksperimen dan otomatisasi *data preprocessing* untuk submission kelas
**Membangun Sistem Machine Learning (Dicoding)**, menggunakan dataset Pima Indians Diabetes.

## Struktur

```
Eksperimen_SML_Ahmaddani/
├── .github/workflows/preprocessing.yml   # CI: menjalankan preprocessing otomatis tiap ada trigger
├── dataset_raw/
│   └── diabetes.csv
└── preprocessing/
    ├── Eksperimen_SML_Ahmaddani.ipynb    # eksplorasi manual (loading, EDA, preprocessing)
    ├── automate_Ahmaddani.py             # versi otomatis dari notebook
    └── dataset_preprocessing.csv         # output: dataset siap latih (dihasilkan otomatis)
```

## Cara menjalankan

```bash
cd preprocessing
python automate_Ahmaddani.py
```

Akan menghasilkan `dataset_preprocessing.csv` yang dipakai pada tahap *modelling*.

## Prediksi Harga Rumah di Tebet

- Sumber dataset
  https://www.kaggle.com/datasets/wisnuanggara/daftar-harga-rumah
- Persiapan data
  data_preparation.py & src/data_preparation.py.ipynb berisi data defense, splitting
- Eksplorasi data
  eda.ipynb berisi eksplorasi dataset khususnya visualisai untuk melihat korelasi data dan juga outlier
- Pemrosesan data
  preprocessing.ipynb & src/preprocessing.py digunakan untuk menghapus outlier khususnya pada bagian def fungsi cek_data & cek_outlier
- Pemodelan 
  modelling.ipynb & src/modelling.py diperuntukkan untuk membuat model prediksi dengan menggunakan Linear Regression
- API & Streamlit
  src/api.py & src/streamlit.py
  api.py diperuntukan untuk jembatan antar muka komunikasi dengan aplikasi lain yang membutuhan prediksi harga rumah
  streamlit.py untuk antar muka (user interface) dalam tampilan web untuk prediksi menggunakan API tadi
  namun dikarenakan satu dan lain hal, fungsi tersebut belum bisa berjalan
  dan sebagai gantinya dibuat alternatif apliakasi pyhton yang mempunyai fungsi yang kurang lebih sama dengan API/streamlit
 
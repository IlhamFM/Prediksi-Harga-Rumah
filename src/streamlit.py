import streamlit as st
import requests
import joblib
from PIL import Image

# Load and set images in the first place
header_images = Image.open('assets/banner.png')
st.image(header_images)

# Add some information about the service
st.title("Smoke Prediction")
st.subheader("Just Masukkan variabel below then click Predict button :sunglasses:")

# Create form of input
with st.form(key = "air_data_form"):
    # Create box for number input
    HARGA = st.number_input(
        label = "1.\tMasukkan Harga Rumah :",
        min_value = 300000000,
        max_value = 70000000000,
        help = "Value range from 300.000.000 to 70.000.000.000"
    )

    LB = st.number_input(
        label = "2.\tMasukkan Luas Bangunan (m2) :",
        min_value = 30,
        max_value = 2000,
        help = "Value range from 30 to 2000"
    )
    
    LT = st.number_input(
        label = "3.\tMasukkan Luas Tanah (m2) :",
        min_value = 20,
        max_value = 2000,
        help = "Value range from 20 to 2000"
    )

    KT = st.number_input(
        label = "4.\tMasukkan Jumlah Kamar Tidur :",
        min_value = 1,
        max_value = 15,
        help = "Value range from 1 to 15"
    )

    KM = st.number_input(
        label = "5.\tMasukkan Jumlah Kamar Mandi :",
        min_value = 1,
        max_value = 15,
        help = "Value range from 1 to 15"
    )

    GRS = st.number_input(
        label = "6.\tMasukkan Kapasitas Garasi Mobil :",
        min_value = 0,
        max_value = 15,
        help = "Value range from 0 to 15"
    )

    # Create button to submit the form
    submitted = st.form_submit_button("Predict")

    # Condition when form submitted
    if submitted:
        # Create dict of all data in the form
        raw_data = {
            "HARGA": HARGA,
            "LB": LB,
            "LT": LT,
            "KT": KT,
            "KM": KM,
            "GRS": GRS
        }

        # Create loading animation while predicting
        with st.spinner("Sending data to prediction server ..."):
            res = requests.post("http://api_backend:8080/predict", json = raw_data).json()
            
        # Parse the prediction result
        if res["error_msg"] != "":
            st.error("Error Occurs While Predicting: {}".format(res["error_msg"]))
        else:
            if res["res"] != "Tidak ada api.":
                st.warning("Ada api.")
            else:
                st.success("Tidak ada api.")
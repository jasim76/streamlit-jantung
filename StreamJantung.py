import pickle
import numpy as np
import streamlit as st

#load sav file
model = pickle.load(open('Penyakit_Jantung.sav','rb'))

#judul web
st.title('Prediksi Penyakit Jantung')
#perhatikan inputan adalah number : st.number_input atau st.slide
col1,col2,col3 = st.columns(3)
with col1 :
    age = st.number_input('Umur')
    sex = st.number_input('Jenis Kelamin')
    cp = st.number_input('Nyeri Dada')
    trestbps = st.number_input('Tekanan Darah')
    chol = st.number_input('Nilai Kolesterol')
with col2 :
    fbs = st.number_input('Gula Darah')
    restecg = st.number_input('Hasil ElektroKardiografi')
    thalach = st.number_input('Detak Jantung Maksimum')
    exang = st.number_input('Induksi Angina')
with col3 :
    oldpeak= st.number_input('ST Depression')
    slope = st.number_input('Slope')
    ca = st.number_input('Nilai Ca Pembuluh Darah')
    thal = st.number_input('Nilai Thal')

#Code untuk prediksi
heart_diagnosis = ""

#tombol prediksi
if st.button ('Prediksi Penyakit Jantung') :
    heart_prediction = model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
    if (heart_prediction[0]==1):
        heart_diagnosis = 'Pasien Terkena Penyakit Jantung'
    else :
        heart_diagnosis = 'Pasien Tidak Terkena Penyakit Jantung'
st.success(heart_diagnosis)

import streamlit as st

st.title("🐇 indira's ")
st.write(" welcome y'all" )
st.image("e81a359c23fad9b6d603adcf4acfe918.jpg")
st.header("Aplikasi Mengecek Nilai Genap/Ganjil")
angka = st.number_input("Tulis sebuah Angka:", value=0, step=1)

if (angka % 2) ==0:
  st.write(f"{angka} adalah Bilangan Genap")
else:
  st.write(f"{angka} adalah Bilangan Ganjil")

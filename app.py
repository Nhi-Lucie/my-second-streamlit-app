import streamlit as st
import sklearn
import pickle

st.title("REVENUE PREDICTION")
a = st.number_input('Input Temperature')

model = pickle.load(open('model.pickle', "rb"))
x_new = a.reshape(-1, 1)

if st.button('Predict'):
  st.write(model.predict(x_new))
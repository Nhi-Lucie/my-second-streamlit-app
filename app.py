import streamlit as st
import sklearn
import pickle

st.title("REVENUE PREDICTION")
a = st.number_input('Input Temperature')

model = pickle.load(open('model.pickle', "rb"))
y_new = model.predict(a)
if st.button('Predict'):
  st.write(y_new)

import streamlit as st
import sklearn
import pickle

st.title("REVENUE PREDICTION")
# a = st.number_input('Input Temperature')

a = np.array([st.number_input('Input Temperature')])
model = pickle.load(open('model.pickle', "rb"))

if st.button('Predict'):
  st.write(y_new)

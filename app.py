import streamlit as st
import sklearn
import pickle

st.title("REVENUE PREDICTION")
a = st.number_input('Input Temperature')

a = np.array([a])
model = pickle.load(open('model.pickle', "rb"))
x_new = a.reshape(-1, 1)
y_new = model.predict(x_new)

if st.button('Predict'):
  st.write(y_new)

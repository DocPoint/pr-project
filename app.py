import pickle
import streamlit as st

global detect_Model
detectFile = open('model.pkl','rb')
detect_Model = pickle.load(detectFile)
detectFile.close()
st.title("Language Detection App")
input_test = st.text_input("Type or Copy your text", 'This is Surya Teja ')

clicked = st.button("Detect Language")
if clicked:
	st.text(*detect_Model.predict([input_test]))
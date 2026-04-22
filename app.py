import streamlit as st
import numpy as np
import pickle

model = pickle.load(open("placement_model.pkl", "rb"))

st.title("🎓 Placement Prediction App")

cgpa = st.number_input("CGPA", 0.0, 10.0)
skills = st.number_input("Skills (1-10)", 1, 10)
internship = st.selectbox("Internship", ["No", "Yes"])
aptitude = st.number_input("Aptitude Score", 0, 100)

internship_val = 1 if internship == "Yes" else 0

if st.button("Predict"):
    data = np.array([[cgpa, skills, internship_val, aptitude]])
    result = model.predict(data)

    if result[0] == 1:
        st.success("Placed ✅")
    else:
        st.error("Not Placed ❌")

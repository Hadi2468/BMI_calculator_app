import streamlit as st

st.title("BMI Calculator")
my_height = st.slider("Select your height (cm)", 50, 250, 170)
my_weight = st.slider("Select your weight (Kg)", 50, 300, 70)
my_bmi = my_weight / ((my_height/100)**2)

if st.button("Calculate BMI"):
    st.write(f"Your BMI is {my_bmi}")
    if my_bmi < 18.5:
        st.write("You are underweight")
    elif my_bmi >= 18.5 and my_bmi < 25:
        st.write("You are normal")
    elif my_bmi >= 25 and my_bmi < 30:
        st.write("You are overweight")
    else:
        st.write("You are obese")
# This program is to check if you are underweight or overweight through the BMI calculator formula to calculate BMI:

import streamlit as st

st.title("BMI Calculator")
st.write("Adjust your Height and Weight parameters")

person_height = st.slider("Enter your height in meters: ",100, 250, 175)
person_height = person_height / 100
person_weight = st.slider("Enter your weight in kilograms: ", 40, 200, 70)

bmi = person_weight / (person_height * person_height)
st.markdown(f"Your BMI is: **{bmi:.02f}**")

if bmi < 18.5:
  st.markdown("**You are Underweight**")
elif 18.5 <= bmi <= 24.9:
  st.markdown("**You weight is normal and you are healthy**")
elif 25 <= bmi <= 29.9:
  st.markdown("**You are Overweight**")
else:
  st.markdown("You are in Obese range")

st.markdown("___")
st.markdown("*BMI Categories*")
st.markdown("- *Underweight: BMI less than 18.5*")
st.markdown("- *Normal weight: BMI between 18.5 and 24.9*")
st.markdown("- *Overweight: BMI between 25 and 29.9*")
st.markdown("- *Obesity: BMI 30 or greater*")
st.markdown("___")



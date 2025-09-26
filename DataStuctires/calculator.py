#streamlit run calculator.py
#alternative :python-m streamlit run calculator.py
import streamlit as st
st.title("Simple Calculator")
#st.subheader("perform basic arithematic calculator")
st.markdown("This is a Simple Calculator app built with Streamlit")

#input feilds for numbers
c1,c2=st.columns(2)
fnum=c1.number_input("Enter the first number",value=0)
snum=c2.number_input("Enter the second number",value=0)

options=["Addition","Subtraction","Multiplication","Division"]
choice=st.radio("Select an operation",options)

button=st.button("calculate")


result=0

if button:
    if choice=="Addition":
        result=fnum+snum
    if choice =="Subtraction":
        result=fnum-snum
    if choice =="Multiplication":
        choice==fnum*snum
    if choice =="Division":
        choice==fnum/snum
st.warning(f"result is:{result}")


st.balloons()
st.snow()
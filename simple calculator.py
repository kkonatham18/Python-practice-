import streamlit as st
st.title("Simple Calculator")
num1 = st.number_input("Enter the first number:", format="%.2f")
num2 = st.number_input("Enter the second number:", format="%.2f")
operation = st.selectbox("Select operation", ["Addition", "Subtraction", "Multiplication", "Division"])
if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
        st.success(f"Result: {num1} + {num2} = {result}")
    elif operation == "Subtraction":
        result = num1 - num2
        st.success(f"Result: {num1} - {num2} = {result}")
    elif operation == "Multiplication":
        result = num1 * num2
        st.success(f"Result: {num1} × {num2} = {result}")
    elif operation == "Division":
        if num2 == 0:
            st.error("Cannot divide by zero.")
        else:
            result = num1 / num2
            st.success(f"Result: {num1} ÷ {num2} = {result}")

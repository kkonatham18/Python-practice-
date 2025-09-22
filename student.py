import streamlit as st
st.title("Student Grading System")
project = st.number_input("Enter Project Marks (0-100)", min_value=0, max_value=100, step=1)
internal = st.number_input("Enter Internal Marks (0-100)", min_value=0, max_value=100, step=1)
external = st.number_input("Enter External Marks (0-100)", min_value=0, max_value=100, step=1)
total = project + internal + external
def calculate_grade(total):
    # Example out of 300
    if total >= 240:
        return "A+"
    elif total >= 200:
        return "A"
    elif total >= 160:
        return "B"
    elif total >= 120:
        return "C"
    elif total >= 90:
        return "D"
    else:
        return "F"

# Show results
if st.button("Calculate Grade"):
    grade = calculate_grade(total)
    st.success(f"Total Marks: {total} | Grade: {grade}")
import streamlit as st
pm= st.number_input("Enter Project Marks")
im= st.number_input("Enter Internal Marks")
em= st.number_input("Enter External Marks")
if(pm>50 and im>50 and em>50):
 total=(pm*70)/100 + (im*20)/100 + (em*10)/100
 if(total>90):
 return "a grade"
 elif(total>70):
  return "b grade"
 else:
  return "c grade"
else:
 return "fail in exam"


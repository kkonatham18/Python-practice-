import streamlit as st
st.set_page_config(page_title="🧮 Custom Tax Calculator", layout="centered")
st.title("💰 Income Tax Calculator (Custom Slabs)")
st.markdown("Enter your annual income to estimate your tax based on custom tax slab rules.")
salary = st.number_input("Enter your annual salary (₹)", min_value=0, step=1000)
def calculate_custom_tax(salary):
    tax = 0
    if salary <= 500000:
        return 0
    taxable = max(0, salary - 300000)
    if salary <= 800000:
        slab1 = min(taxable, 500000)  
        tax += slab1 * 0.15
    elif salary <= 1200000:
        slab1 = min(500000, taxable)  
        slab2 = max(0, taxable - 500000)  
        tax += slab1 * 0.15 + slab2 * 0.20
    else:
        slab1 = 500000                   
        slab2 = 400000                   
        slab3 = salary - 1200000         
        tax += slab1 * 0.15 + slab2 * 0.20 + slab3 * 0.25
    return round(tax, 2)
if st.button("🧾 Calculate Tax"):
    tax = calculate_custom_tax(salary)
    st.subheader("📄 Tax Summary")
    st.write(f"**Annual Salary**: ₹{salary:,.2f}")
    st.write(f"**Tax Payable**: ₹{tax:,.2f}")
    if tax == 0:
        st.success("✅ You do not need to pay tax.")
    else:
        st.warning("💸 Tax payable calculated as per the given slab rules.")
st.markdown("---")
st.caption("This is a custom logic tax calculator. Please consult a professional for official tax filing.")


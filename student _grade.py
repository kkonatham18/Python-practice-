st.title("student certification")
pm=st.number_input("enter project marks",min_value=0,max_value=100,step=1)
em=st.number_input("enter external marks",min_value=0,max_value=100,step=1)
im=st.number_input("enter internal marks",min_value=0,max_value=100,step=1)
if(pm>50 and im>50 and em>50:
    total=(pm*70)/100 + (im*10)/100 + (em*20)/100
def certificate_grade(total):
    if(total>=90):
        return "A+"
    elif(total>=70):
        return "B+"
    else:
        return "c+"
else:
    if(pm<50):
        return "failed in project"
    elif(em<50):
        return "failed in external"
    else:
        return "failed in internal"

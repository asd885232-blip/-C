import streamlit as st

st.title("帳務計算機")

total_income = st.number_input("總收入", value=0)

st.subheader("家豪")
j_days = st.number_input("家豪工作天數", value=0)
j_wage = st.number_input("家豪工資", value=0)
j_mat = st.number_input("家豪材料費", value=0)
j_lun = st.number_input("家豪中餐費", value=0)

st.subheader("定暘")
d_days = st.number_input("定暘工作天數", value=0)
d_wage = st.number_input("定暘工資", value=0)
d_mat = st.number_input("定暘材料費", value=0)
d_lun = st.number_input("定暘中餐費", value=0)

if st.button("計算"):
    j_cost = (j_days * j_wage) + j_mat + j_lun
    d_cost = (d_days * d_wage) + d_mat + d_lun
    result = (total_income - j_cost - d_cost) / 2
    st.success(f"每人可分得: {result}")

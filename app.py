import streamlit as st

st.title("帳務計算機")

total_income = st.number_input("總收入", value=0.0, step=100.0, format="%f")

st.subheader("家豪")
# 改用「總人天數」來輸入，完美解決每天人數不同的問題
j_total_man_days = st.number_input("家豪總人天數 (例如: 1+2=3天)", value=0.0, step=0.5, format="%f")
j_wage = st.number_input("家豪工資 (單人/天)", value=0.0, step=100.0, format="%f")
j_mat = st.number_input("家豪材料費", value=0.0, step=100.0, format="%f")
j_lun = st.number_input("家豪中餐費", value=0.0, step=50.0, format="%f")

st.subheader("定暘")
d_days = st.number_input("定暘總工作天數", value=0.0, step=0.5, format="%f")
d_wage = st.number_input("定暘工資", value=0.0, step=100.0, format="%f")
d_mat = st.number_input("定暘材料費", value=0.0, step=100.0, format="%f")
d_lun = st.number_input("定暘中餐費", value=0.0, step=50.0, format="%f")

if st.button("計算", use_container_width=True):
    # 邏輯：總人天數 * 單人日薪 = 總人工資
    j_cost = (j_total_man_days * j_wage) + j_mat + j_lun
    d_cost = (d_days * d_wage) + d_mat + d_lun
    
    net_profit = total_income - j_cost - d_cost
    share = net_profit / 2
    
    j_total = share + j_cost
    d_total = share + d_cost
    
    st.markdown("---")
    st.success(f"每人平分淨利: {share:,.0f} 元")
    
    st.markdown(f"### 家豪最終總計: {j_total:,.0f} 元")
    st.write(f"(總人天數: {j_total_man_days}, 淨利分紅 {share:,.0f} + 支出成本 {j_cost:,.0f})")
    
    st.markdown(f"### 定暘最終總計: {d_total:,.0f} 元")
    st.write(f"(總天數: {d_days}, 淨利分紅 {share:,.0f} + 支出成本 {d_cost:,.0f})")

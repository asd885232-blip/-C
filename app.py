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
    # 1. 計算各自支出的成本
    j_cost = (j_days * j_wage) + j_mat + j_lun
    d_cost = (d_days * d_wage) + d_mat + d_lun
    
    # 2. 計算剩餘淨利，並平分
    net_profit = total_income - j_cost - d_cost
    share = net_profit / 2
    
    # 3. 計算每人最終總金額 (分紅 + 各自墊付的成本)
    j_total = share + j_cost
    d_total = share + d_cost
    
    # 顯示結果
    st.success(f"每人平分淨利: {share}")
    
    st.write("---")
    st.write(f"**家豪最終總計:** {j_total} (淨利分紅 {share} + 支出成本 {j_cost})")
    st.write(f"**定暘最終總計:** {d_total} (淨利分紅 {share} + 支出成本 {d_cost})")

import streamlit as st

st.title("帳務計算機")

# 使用 value=None 和 placeholder 解決 0 的問題
total_income = st.number_input("總收入", value=None, placeholder="請輸入總收入", format="%d")

st.subheader("家豪")
j_days = st.number_input("家豪工作天數", value=None, placeholder="輸入天數", format="%d")
j_wage = st.number_input("家豪工資", value=None, placeholder="輸入工資", format="%d")
j_mat = st.number_input("家豪材料費", value=None, placeholder="輸入材料費", format="%d")
j_lun = st.number_input("家豪中餐費", value=None, placeholder="輸入中餐費", format="%d")

st.subheader("定暘")
d_days = st.number_input("定暘工作天數", value=None, placeholder="輸入天數", format="%d")
d_wage = st.number_input("定暘工資", value=None, placeholder="輸入工資", format="%d")
d_mat = st.number_input("定暘材料費", value=None, placeholder="輸入材料費", format="%d")
d_lun = st.number_input("定暘中餐費", value=None, placeholder="輸入中餐費", format="%d")

if st.button("計算", use_container_width=True):
    # 將 None 轉為 0
    j_days = j_days or 0
    j_wage = j_wage or 0
    j_mat = j_mat or 0
    j_lun = j_lun or 0
    d_days = d_days or 0
    d_wage = d_wage or 0
    d_mat = d_mat or 0
    d_lun = d_lun or 0
    total_income = total_income or 0
    
    # 計算邏輯
    j_cost = (j_days * j_wage) + j_mat + j_lun
    d_cost = (d_days * d_wage) + d_mat + d_lun
    net_profit = total_income - j_cost - d_cost
    share = net_profit / 2
    
    j_total = share + j_cost
    d_total = share + d_cost
    
    # 顯示結果
    st.markdown("---")
    st.success(f"每人平分淨利: {share:,.0f}")
    
    st.markdown(f"### 家豪最終總計: {j_total:,.0f} 元")
    st.write(f"（淨利分紅 {share:,.0f} + 支出成本 {j_cost:,.0f}）")
    
    st.markdown(f"### 定暘最終總計: {d_total:,.0f} 元")
    st.write(f"（淨利分紅 {share:,.0f} + 支出成本 {d_cost:,.0f}）")

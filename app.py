import streamlit as st

# 設定頁面標題
st.title("帳務計算機")

# 使用 step 和 format 參數，讓輸入時更順手
# key 參數可以幫助 Streamlit 更好管理這些輸入框
total_income = st.number_input("總收入", value=0, step=100, format="%d")

st.subheader("家豪")
j_days = st.number_input("家豪工作天數", value=0, step=1, format="%d")
j_wage = st.number_input("家豪工資", value=0, step=100, format="%d")
j_mat = st.number_input("家豪材料費", value=0, step=100, format="%d")
j_lun = st.number_input("家豪中餐費", value=0, step=50, format="%d")

st.subheader("定暘")
d_days = st.number_input("定暘工作天數", value=0, step=1, format="%d")
d_wage = st.number_input("定暘工資", value=0, step=100, format="%d")
d_mat = st.number_input("定暘材料費", value=0, step=100, format="%d")
d_lun = st.number_input("定暘中餐費", value=0, step=50, format="%d")

if st.button("計算", use_container_width=True):
    # 計算邏輯
    j_cost = (j_days * j_wage) + j_mat + j_lun
    d_cost = (d_days * d_wage) + d_mat + d_lun
    net_profit = total_income - j_cost - d_cost
    share = net_profit / 2
    
    j_total = share + j_cost
    d_total = share + d_cost
    
    # 顯示結果並放大字體
    st.markdown("---")
    st.success(f"每人平分淨利: {share:,.0f}")
    
    # 使用 Markdown 語法 # 讓字體變大
    st.markdown(f"### 家豪最終總計: {j_total:,.0f} 元")
    st.write(f"（淨利分紅 {share:,.0f} + 支出成本 {j_cost:,.0f}）")
    
    st.markdown(f"### 定暘最終總計: {d_total:,.0f} 元")
    st.write(f"（淨利分紅 {share:,.0f} + 支出成本 {d_cost:,.0f}）")

import streamlit as st

st.title("帳務計算機")

# 使用 0 作為預設值，但利用 text_input 或透過邏輯處理，
# 這裡維持 number_input 但設定 value=0，確保程式永遠有數字運作
total_income = st.number_input("總收入", value=0, format="%d")

st.subheader("家豪")
j_days = st.number_input("家豪工作天數", value=0, format="%d")
j_wage = st.number_input("家豪工資", value=0, format="%d")
j_mat = st.number_input("家豪材料費", value=0, format="%d")
j_lun = st.number_input("家豪中餐費", value=0, format="%d")

st.subheader("定暘")
d_days = st.number_input("定暘工作天數", value=0, format="%d")
d_wage = st.number_input("定暘工資", value=0, format="%d")
d_mat = st.number_input("定暘材料費", value=0, format="%d")
d_lun = st.number_input("定暘中餐費", value=0, format="%d")

if st.button("計算", use_container_width=True):
    # 進行計算 (因為上面設了 value=0，這裡就不會再出現 None 的錯誤)
    j_cost = (j_days * j_wage) + j_mat + j_lun
    d_cost = (d_days * d_wage) + d_mat + d_lun
    
    net_profit = total_income - j_cost - d_cost
    share = net_profit / 2
    
    j_total = share + j_cost
    d_total = share + d_cost
    
    # 顯示結果
    st.markdown("---")
    st.success(f"每人平分淨利: {share:,.0f} 元")
    
    st.markdown(f"### 家豪最終總計: {j_total:,.0f} 元")
    st.write(f"（淨利分紅 {share:,.0f} + 支出成本 {j_cost:,.0f}）")
    
    st.markdown(f"### 定暘最終總計: {d_total:,.0f} 元")
    st.write(f"（淨利分紅 {share:,.0f} + 支出成本 {d_cost:,.0f}）")

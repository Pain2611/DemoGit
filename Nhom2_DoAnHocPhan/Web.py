import pickle
import streamlit as st

Than_model = pickle.load(open('ThanManTinh_Reg.sav', 'rb'))

st.title('Chuẩn đoán thận mãn tính')

col1, col2 = st.columns(2)
with col1:
    age = st.number_input('Nhập tuổi của bạn')
with col2:
    bp = st.number_input('Nhập bp của bạn')
with col1:
    sg = st.number_input('Nhập sg của bạn')
with col2:
    al = st.number_input('Nhập al của bạn')
with col1:
    su = st.number_input('Nhập su của bạn')
with col2:
    rbc = st.number_input('Nhập rbc của bạn')
with col1:
    pc = st.number_input('Nhập pc của bạn')
with col2:
    pcc = st.number_input('Nhập pcc của bạn')
with col1:
    ba = st.number_input('Nhập ba của bạn')
with col2:
    bgr = st.number_input('Nhập bgr của bạn')
with col1:
    bu = st.number_input('Nhập bu của bạn')
with col2:
    sc = st.number_input('Nhập sc của bạn')
with col1:
    sod = st.number_input('Nhập sod của bạn')
with col2:
    pot = st.number_input('Nhập pot của bạn')
with col1:
    hemo = st.number_input('Nhập hemo của bạn')
with col2:
    pcv = st.number_input('Nhập pcv của bạn')
with col1:
    wc = st.number_input('Nhập wc của bạn')
with col2:
    rc = st.number_input('Nhập rc của bạn')
with col1:
    htn = st.number_input('Nhập htn của bạn')
with col2:
    dm = st.number_input('Nhập dm của bạn')
with col1:
    cad = st.number_input('Nhập cad của bạn')
with col2:
    appet = st.number_input('Nhập appet của bạn')
with col1:
    pe = st.number_input('Nhập pe của bạn')
with col2:
    ane = st.number_input('Nhập ane của bạn')

Than_diagnosis = ''

if st.button('Du doan'):
    Than_prediction = Than_model.predict(
        [[age, bp, sg, al, su, rbc, pc, pcc, ba, bgr, bu, sc, sod, pot, hemo, pcv, wc, rc, htn, dm, cad, appet, pe, ane]])
    if(Than_prediction[0] == 1):
        Than_diagnosis = 'Bệnh nhân được chuẩn đoán bị thận mãn tính'
    else:
        Than_diagnosis = 'Bệnh nhân được chuẩn đoán không bị thận mãn tính'

    st.success(Than_diagnosis)
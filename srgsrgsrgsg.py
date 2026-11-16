import streamlit as st

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Thai:wght@400;500;600;700&display=swap');

html, body, [class*="css"], .stApp, h1, h2, h3, p, div, span, button {
    font-family: 'IBM Plex Sans Thai', sans-serif !important;
}
</style>
""", unsafe_allow_html=True)

st.title("ยินดีต้อนรับสู่โปรไฟล์ของฉัน ✨")
st.write("นี่คือเว็บแอปพลิเคชันแรกในชีวิตของผม/ดิฉัน เขียนด้วยภาษา Python ครับ/ค่ะ")

st.divider()

st.header("👤 ข้อมูลส่วนตัว")
st.write("**ชื่อ-นามสกุล:** นาย/นางสาว เรียนดี มีความรู้")
st.write("**ชั้น** ม.4/5 เลขที่ 16")
st.write("**โรงเรียน:** ยุพราชวิทยาลัย")

if st.button("คลิกบอกความรู้สึกกับการเขียนเว็บครั้งแรก"):
    st.success("ว้าว! สนุกและง่ายกว่าที่คิดมาก ๆ! 🎉")
```[cite: 2]

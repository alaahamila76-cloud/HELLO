import streamlit as st

# تهيئة الصفحة الافتراضية
if "page" not in st.session_state:
    st.session_state.page = "home"

# =========================
# الصفحة الرئيسية
# =========================
def home_page():
    st.title("🏠 الصفحة الرئيسية")
    st.write("مرحبا بك في الموقع")

    if st.button("➡️ اذهب إلى الصفحة الثانية"):
        st.session_state.page = "page2"
        st.rerun()

# =========================
# الصفحة الثانية
# =========================
def page_two():
    st.title("📄 الصفحة الثانية")
    st.write("أنت الآن في الصفحة الثانية")

    if st.button("⬅️ الرجوع للرئيسية"):
        st.session_state.page = "home"
        st.rerun()

# =========================
# اختيار الصفحة
# =========================
if st.session_state.page == "home":
    home_page()
elif st.session_state.page == "page2":
    page_two()


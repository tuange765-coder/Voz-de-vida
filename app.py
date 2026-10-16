import streamlit as st
from streamlit_supabase_auth_ui.widgets import __login__

st.set_page_config(page_title="La Palabra", page_icon="🙏")

# Componente de login
login_obj = __login__(
    auth_token=st.secrets["courier_auth_token"],
    company_name="La Palabra",
    width=200,
    height=250
)

LOGGED_IN = login_obj.build_login_ui()

if LOGGED_IN:
    st.title("🙏 La Palabra")
    st.success("Bienvenido a la Palabra de Dios")

    st.header("🙏 Oración Diaria")
    st.write("Señor, gracias por este nuevo día. Guía mis pasos y dame sabiduría para caminar en tu verdad.")

    st.header("❤️ Muro de Miembros")
    st.markdown("""
    Estas son las personas que con su donación apoyan esta obra:

    - **Juan P.** — Octubre 2026
    - **María G.** — Octubre 2026
    - **Un hermano anónimo** — Septiembre 2026
    """)

    st.markdown("---")
    st.markdown("[☕ Apoyar esta obra](https://ko-fi.com/tu-usuario)")

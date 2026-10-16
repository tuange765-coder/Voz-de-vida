import streamlit as st
from streamlit_supabase_auth_ui.widgets import __login__

# ============================================
# CONFIGURACIÓN
# ============================================
st.set_page_config(
    page_title="La Palabra",
    page_icon="🙏",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ============================================
# ESTILOS PROFESIONALES
# ============================================
st.markdown("""
<style>
    /* Fondo general */
    .stApp {
        background: linear-gradient(180deg, #FAF7F2 0%, #F5EFE6 100%);
    }
    
    /* Ocultar menú por defecto */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Tipografía */
    html, body, [class*="css"] {
        font-family: 'Georgia', 'Times New Roman', serif;
        color: #2C2C2C;
    }
    
    /* Título principal */
    .main-title {
        font-size: 2.2rem;
        font-weight: 700;
        color: #1E3A5F;
        text-align: center;
        margin-bottom: 0.2rem;
        letter-spacing: -0.5px;
    }
    .main-subtitle {
        text-align: center;
        color: #8B7355;
        font-size: 0.95rem;
        margin-bottom: 1.5rem;
        font-style: italic;
    }
    
    /* Tarjeta de oración */
    .prayer-card {
        background: #FFFFFF;
        border-left: 4px solid #C9A961;
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 4px 20px rgba(30, 58, 95, 0.08);
    }
    .prayer-card h3 {
        color: #1E3A5F;
        font-size: 1rem;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        margin-bottom: 0.5rem;
        font-family: 'Helvetica', sans-serif;
    }
    .prayer-card p {
        font-size: 1.05rem;
        line-height: 1.7;
        color: #3A3A3A;
        margin: 0;
    }
    
    /* Tarjeta de versículo */
    .verse-card {
        background: linear-gradient(135deg, #1E3A5F 0%, #2C5178 100%);
        color: #FFFFFF;
        border-radius: 16px;
        padding: 1.8rem;
        margin: 1rem 0;
        text-align: center;
        box-shadow: 0 8px 24px rgba(30, 58, 95, 0.25);
    }
    .verse-card .verse-text {
        font-size: 1.15rem;
        font-style: italic;
        line-height: 1.6;
        color: #FAF7F2;
        margin-bottom: 0.8rem;
    }
    .verse-card .verse-ref {
        font-size: 0.85rem;
        letter-spacing: 2px;
        text-transform: uppercase;
        color: #C9A961;
        font-weight: 600;
    }
    
    /* Botones de acceso rápido */
    .quick-btn {
        display: block;
        background: #FFFFFF;
        border: 1px solid #E8DFD0;
        border-radius: 12px;
        padding: 1rem;
        text-align: center;
        text-decoration: none;
        color: #1E3A5F;
        font-weight: 600;
        font-size: 0.9rem;
        transition: all 0.2s ease;
        margin-bottom: 0.5rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.03);
    }
    .quick-btn:hover {
        border-color: #C9A961;
        box-shadow: 0 4px 16px rgba(201, 169, 97, 0.2);
        transform: translateY(-2px);
    }
    .quick-btn .icon {
        font-size: 1.5rem;
        display: block;
        margin-bottom: 0.3rem;
    }
    
    /* Muro de miembros */
    .member-item {
        background: #FFFFFF;
        border-radius: 10px;
        padding: 0.8rem 1rem;
        margin-bottom: 0.5rem;
        border-left: 3px solid #C9A961;
        font-size: 0.9rem;
        color: #3A3A3A;
        box-shadow: 0 2px 6px rgba(0,0,0,0.04);
    }
    .member-item strong {
        color: #1E3A5F;
    }
    
    /* Sección títulos */
    .section-title {
        font-family: 'Helvetica', sans-serif;
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 2px;
        color: #8B7355;
        margin-top: 2rem;
        margin-bottom: 1rem;
        font-weight: 600;
    }
    
    /* Botón donar */
    .donate-btn {
        display: block;
        background: linear-gradient(135deg, #C9A961 0%, #B8944F 100%);
        color: #FFFFFF !important;
        text-align: center;
        padding: 0.9rem;
        border-radius: 12px;
        text-decoration: none !important;
        font-weight: 600;
        font-size: 0.95rem;
        letter-spacing: 0.5px;
        margin-top: 1rem;
        box-shadow: 0 4px 14px rgba(201, 169, 97, 0.35);
        transition: all 0.2s ease;
    }
    .donate-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(201, 169, 97, 0.45);
    }
    
    /* Saludo superior */
    .greeting {
        text-align: center;
        font-size: 0.9rem;
        color: #8B7355;
        margin-bottom: 0.3rem;
        font-family: 'Helvetica', sans-serif;
    }
</style>
""", unsafe_allow_html=True)

# ============================================
# LOGIN
# ============================================
login_obj = __login__(
    auth_token=st.secrets["courier_auth_token"],
    company_name="La Palabra",
    width=200,
    height=250
)

LOGGED_IN = login_obj.build_login_ui()

# ============================================
# CONTENIDO PRINCIPAL
# ============================================
if LOGGED_IN:
    # Encabezado
    st.markdown('<p class="greeting">Bienvenido a</p>', unsafe_allow_html=True)
    st.markdown('<h1 class="main-title">La Palabra</h1>', unsafe_allow_html=True)
    st.markdown('<p class="main-subtitle">"Lámpara es a mis pies tu palabra" — Salmos 119:105</p>', unsafe_allow_html=True)
    
    # Versículo del día (tarjeta azul)
    st.markdown("""
    <div class="verse-card">
        <div class="verse-text">"Porque de tal manera amó Dios al mundo, que ha dado a su Hijo unigénito, para que todo aquel que en él cree, no se pierda, mas tenga vida eterna."</div>
        <div class="verse-ref">Juan 3:16</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Oración del día (tarjeta crema)
    st.markdown('<p class="section-title">🙏 Oración del día</p>', unsafe_allow_html=True)
    st.markdown("""
    <div class="prayer-card">
        <h3>Oración de la mañana</h3>
        <p>Señor, gracias por este nuevo día que me regalas. Guía mis pasos, ilumina mi mente y guarda mi corazón en tu verdad. Que cada palabra que salga de mi boca sea agradable a ti, y que cada acción refleje tu amor. Amén.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Accesos rápidos
    st.markdown('<p class="section-title">📖 Explora</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <a href="#" class="quick-btn">
            <span class="icon">📖</span>
            La Palabra
        </a>
        """, unsafe_allow_html=True)
        st.markdown("""
        <a href="#" class="quick-btn">
            <span class="icon">💭</span>
            Reflexiones
        </a>
        """, unsafe_allow_html=True)
        st.markdown("""
        <a href="#" class="quick-btn">
            <span class="icon">🔍</span>
            Curiosidades
        </a>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <a href="#" class="quick-btn">
            <span class="icon">🙋</span>
            Pregúntale al Pastor
        </a>
        """, unsafe_allow_html=True)
        st.markdown("""
        <a href="#" class="quick-btn">
            <span class="icon">⚠️</span>
            Mitos y Falsas Doctrinas
        </a>
        """, unsafe_allow_html=True)
        st.markdown("""
        <a href="#" class="quick-btn">
            <span class="icon">❤️</span>
            Favoritos
        </a>
        """, unsafe_allow_html=True)
    
    # Muro de miembros
    st.markdown('<p class="section-title">❤️ Muro de Miembros</p>', unsafe_allow_html=True)
    st.markdown("""
    <p style="font-size: 0.85rem; color: #8B7355; margin-bottom: 0.8rem;">
    Estas son las personas que con su donación apoyan esta obra:
    </p>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="member-item"><strong>Juan P.</strong> — Octubre 2026</div>
    <div class="member-item"><strong>María G.</strong> — Octubre 2026</div>
    <div class="member-item"><strong>Un hermano anónimo</strong> — Septiembre 2026</div>
    """, unsafe_allow_html=True)
    
    # Botón donar
    st.markdown("""
    <a href="https://ko-fi.com/tu-usuario" target="_blank" class="donate-btn">
        ☕ Apoyar esta obra
    </a>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(
        '<p style="text-align:center; font-size:0.75rem; color:#B0A090;">Hecho con ❤️ para la gloria de Dios</p>',
        unsafe_allow_html=True
    )

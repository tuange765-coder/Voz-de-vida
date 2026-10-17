import streamlit as st
from streamlit_supabase_auth_ui.widgets import __login__

# ============================================
# CONFIGURACIÓN
# ============================================
st.set_page_config(
    page_title="La Palabra | App Cristiana",
    page_icon="✝️",
    layout="wide", # Usamos todo el ancho de la pantalla
    initial_sidebar_state="collapsed"
)

# ============================================
# ESTILOS PROFESIONALES (DARK MODE PREMIUM)
# ============================================
st.markdown("""
<style>
    /* 1. IMPORTAR FUENTE PROFESIONAL */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&family=Playfair+Display:ital,wght@0,600;1,400&display=swap');

    /* 2. FONDO GENERAL (Degradado oscuro elegante) */
    .stApp {
        background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%);
        color: #F8FAFC;
    }

    /* 3. OCULTAR ELEMENTOS DE STREAMLIT */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* 4. TIPOGRAFÍA BASE */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    h1, h2, h3 {
        font-family: 'Playfair Display', serif;
        color: #F8FAFC !important;
    }
    p, span, div {
        color: #CBD5E1;
    }

    /* 5. ENCABEZADO PRINCIPAL */
    .hero-title {
        font-family: 'Playfair Display', serif;
        font-size: 3.5rem;
        font-weight: 600;
        background: -webkit-linear-gradient(45deg, #FDE047, #D4AF37);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0;
        line-height: 1.1;
    }
    .hero-subtitle {
        font-size: 1.1rem;
        color: #94A3B8;
        margin-top: 10px;
        font-weight: 300;
        letter-spacing: 1px;
    }

    /* 6. TARJETAS (Glassmorphism sutil) */
    .premium-card {
        background: rgba(30, 41, 59, 0.7);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 20px;
        box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.5);
    }

    /* Tarjeta de Versículo Destacada */
    .verse-highlight {
        background: linear-gradient(135deg, rgba(212, 175, 55, 0.1) 0%, rgba(212, 175, 55, 0.02) 100%);
        border-left: 4px solid #D4AF37;
        border-radius: 12px;
        padding: 30px;
        margin: 20px 0;
    }
    .verse-text {
        font-family: 'Playfair Display', serif;
        font-size: 1.5rem;
        font-style: italic;
        line-height: 1.6;
        color: #F8FAFC !important;
    }
    .verse-ref {
        display: block;
        margin-top: 15px;
        font-family: 'Inter', sans-serif;
        font-size: 0.85rem;
        letter-spacing: 2px;
        text-transform: uppercase;
        color: #D4AF37 !important;
        font-weight: 600;
    }

    /* Títulos de sección */
    .section-header {
        font-size: 1.2rem;
        font-weight: 600;
        color: #F8FAFC;
        margin-bottom: 15px;
        display: flex;
        align-items: center;
        gap: 10px;
    }

    /* 7. PERSONALIZAR BOTONES NATIVOS DE STREAMLIT */
    .stButton>button {
        background: rgba(255, 255, 255, 0.03);
        color: #F8FAFC;
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 15px 20px;
        font-weight: 400;
        font-size: 1rem;
        transition: all 0.3s ease;
        width: 100%;
        text-align: left;
        display: flex;
        justify-content: flex-start;
    }
    .stButton>button:hover {
        background: rgba(212, 175, 55, 0.15);
        border-color: #D4AF37;
        color: #D4AF37;
        transform: translateY(-2px);
    }
    /* Ocultar el texto del botón nativo para reemplazarlo con HTML */
    .stButton>button p {
        font-size: 1rem;
        margin: 0;
    }

    /* 8. MURO DE MIEMBROS */
    .member-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 12px 0;
        border-bottom: 1px solid rgba(255, 255, 255, 0.05);
    }
    .member-row:last-child {
        border-bottom: none;
    }
    .member-name {
        font-weight: 600;
        color: #F8FAFC;
    }
    .member-date {
        font-size: 0.8rem;
        color: #64748B;
        background: rgba(255,255,255,0.05);
        padding: 4px 10px;
        border-radius: 20px;
    }

    /* 9. BOTÓN DE DONACIÓN ESPECIAL */
    .stButton>button[kind="primary"] {
        background: linear-gradient(135deg, #D4AF37 0%, #FDE047 100%);
        color: #0F172A;
        border: none;
        font-weight: 600;
        text-align: center;
        justify-content: center;
        box-shadow: 0 10px 20px -5px rgba(212, 175, 55, 0.4);
    }
    .stButton>button[kind="primary"]:hover {
        transform: translateY(-2px) scale(1.02);
        box-shadow: 0 15px 25px -5px rgba(212, 175, 55, 0.6);
        color: #0F172A;
    }
</style>
""", unsafe_allow_html=True)

# ============================================
# LOGIN
# ============================================
login_obj = __login__(
    auth_token=st.secrets["courier_auth_token"],
    company_name="La Palabra",
    width=250,
    height=300
)

LOGGED_IN = login_obj.build_login_ui()

# ============================================
# CONTENIDO PRINCIPAL
# ============================================
if LOGGED_IN:
    # --- ENCABEZADO ---
    st.markdown('<h1 class="hero-title">La Palabra</h1>', unsafe_allow_html=True)
    st.markdown('<p class="hero-subtitle">Lámpara es a mis pies tu palabra, y lumbrera a mi camino.</p>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    # --- DISTRIBUCIÓN EN DOS COLUMNAS ---
    # Columna Izquierda (70% del ancho)
    col_izq, col_der = st.columns([2.2, 1], gap="large")

    with col_izq:
        # 1. Versículo del Día
        st.markdown("""
        <div class="verse-highlight">
            <div class="verse-text">"Porque de tal manera amó Dios al mundo, que ha dado a su Hijo unigénito, para que todo aquel que en él cree, no se pierda, mas tenga vida eterna."</div>
            <span class="verse-ref">Juan 3:16 — Versículo del día</span>
        </div>
        """, unsafe_allow_html=True)

        # 2. Oración del Día
        st.markdown('<div class="section-header">🙏 Oración de la Mañana</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="premium-card">
            <p style="font-size: 1.1rem; line-height: 1.8; margin: 0; font-weight: 300;">
            Señor, gracias por este nuevo día que me regalas. Guía mis pasos, ilumina mi mente y guarda mi corazón en tu verdad. Que cada palabra que salga de mi boca sea agradable a ti, y que cada acción refleje tu amor. Amén.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)

        # 3. Secciones de la App
        st.markdown('<div class="section-header">📖 Explora la Palabra</div>', unsafe_allow_html=True)
        
        # Usamos botones nativos en columnas para que se vean como una app real
        b1, b2, b3 = st.columns(3)
        with b1:
            if st.button("📖 La Biblia", use_container_width=True):
                st.toast("Abriendo la Biblia...")
        with b2:
            if st.button("💭 Reflexiones", use_container_width=True):
                st.toast("Cargando reflexiones...")
        with b3:
            if st.button("🔍 Curiosidades", use_container_width=True):
                st.toast("Cargando curiosidades...")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        b4, b5, b6 = st.columns(3)
        with b4:
            if st.button("🙋 Pregúntale al Pastor", use_container_width=True):
                st.toast("Abriendo chat con el pastor...")
        with b5:
            if st.button("⚠️ Mitos y Doctrinas", use_container_width=True):
                st.toast("Cargando aclaraciones...")
        with b6:
            if st.button("❤️ Favoritos", use_container_width=True):
                st.toast("Cargando tus favoritos...")

    # Columna Derecha (30% del ancho)
    with col_der:
        # Muro de miembros
        st.markdown('<div class="section-header">🤝 Muro de Miembros</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="premium-card" style="padding: 20px;">
            <p style="font-size: 0.85rem; color: #94A3B8; margin-bottom: 15px;">
                Personas que con su donación apoyan esta obra:
            </p>
            <div class="member-row">
                <span class="member-name">Juan P.</span>
                <span class="member-date">Oct 2026</span>
            </div>
            <div class="member-row">
                <span class="member-name">María G.</span>
                <span class="member-date">Oct 2026</span>
            </div>
            <div class="member-row">
                <span class="member-name">Un hermano anónimo</span>
                <span class="member-date">Sep 2026</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Botón de donación (usamos type="primary" para que herede el estilo dorado)
        if st.button("☕ Apoyar esta obra", type="primary", use_container_width=True):
            st.info("Redirigiendo a Ko-fi... (Aquí irá tu enlace)")

        st.markdown("<br>", unsafe_allow_html=True)
        
        # Estado del proyecto (da un toque muy profesional de transparencia)
        st.markdown("""
        <div style="background: rgba(16, 185, 129, 0.1); border: 1px solid rgba(16, 185, 129, 0.2); border-radius: 12px; padding: 15px; text-align: center;">
            <p style="color: #10B981; font-size: 0.8rem; margin: 0; font-weight: 600;">✅ App 100% Gratuita</p>
            <p style="color: #64748B; font-size: 0.75rem; margin-top: 5px;">Mantenida por donaciones</p>
        </div>
        """, unsafe_allow_html=True)

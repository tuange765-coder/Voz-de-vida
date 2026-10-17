
import streamlit as st
from streamlit_supabase_auth_ui.widgets import __login__

# ============================================
# CONFIGURACIÓN
# ============================================
st.set_page_config(
    page_title="La Palabra | App Cristiana",
    page_icon="✝️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================
# ESTILOS PROFESIONALES (CÁLIDO Y ESPIRITUAL)
# ============================================
# Imagen de fondo: Atardecer con cruz (cálida y espiritual)
IMG_URL = "https://images.unsplash.com/photo-1504052434569-70ad5836ab65?q=80&w=2070&auto=format&fit=crop"

st.markdown(f"""
<style>
    /* 1. FUENTES PREMIUM */
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,400&family=Montserrat:wght@400;500;600&display=swap');

    /* 2. FONDO CON IMAGEN Y FILTRO CÁLIDO */
    .stApp {{
        background-image: 
            linear-gradient(rgba(40, 20, 10, 0.65), rgba(20, 10, 5, 0.85)), 
            url("{IMG_URL}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        font-family: 'Montserrat', sans-serif;
    }}

    /* 3. OCULTAR ELEMENTOS DE STREAMLIT */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}

    /* 4. TIPOGRAFÍA Y COLORES */
    h1, h2, h3 {{
        font-family: 'Cormorant Garamond', serif;
        color: #FDFBF7 !important; /* Blanco perla */
    }}
    p, span, div {{
        color: #E6D5C3; /* Crema suave */
    }}

    /* 5. ENCABEZADO PRINCIPAL */
    .hero-title {{
        font-family: 'Cormorant Garamond', serif;
        font-size: 4.5rem;
        font-weight: 700;
        color: #FDFBF7 !important;
        text-align: center;
        margin-bottom: 0;
        line-height: 1.1;
        text-shadow: 2px 2px 8px rgba(0,0,0,0.6);
    }}
    .hero-subtitle {{
        text-align: center;
        font-size: 1.2rem;
        color: #D4AF37 !important; /* Dorado */
        margin-top: 10px;
        font-weight: 500;
        letter-spacing: 2px;
        text-shadow: 1px 1px 4px rgba(0,0,0,0.8);
    }}

    /* 6. TARJETAS DE CRISTAL CÁLIDO (Glassmorphism) */
    .premium-card {{
        background: rgba(45, 30, 20, 0.55); /* Marrón cálido transparente */
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(212, 175, 55, 0.25); /* Borde dorado sutil */
        border-radius: 20px;
        padding: 30px;
        margin-bottom: 25px;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.4);
    }}

    /* Tarjeta de Versículo */
    .verse-highlight {{
        background: linear-gradient(135deg, rgba(212, 175, 55, 0.15) 0%, rgba(45, 30, 20, 0.6) 100%);
        border-left: 5px solid #D4AF37;
        border-radius: 16px;
        padding: 40px;
        margin: 20px 0 40px 0;
        backdrop-filter: blur(10px);
    }}
    .verse-text {{
        font-family: 'Cormorant Garamond', serif;
        font-size: 1.8rem;
        font-style: italic;
        line-height: 1.5;
        color: #FDFBF7 !important;
        text-align: center;
        text-shadow: 1px 1px 5px rgba(0,0,0,0.5);
    }}
    .verse-ref {{
        display: block;
        margin-top: 20px;
        font-family: 'Montserrat', sans-serif;
        font-size: 0.9rem;
        letter-spacing: 3px;
        text-transform: uppercase;
        color: #D4AF37 !important;
        font-weight: 600;
        text-align: center;
    }}

    /* Títulos de sección */
    .section-header {{
        font-size: 1.4rem;
        font-weight: 600;
        color: #FDFBF7 !important;
        margin-bottom: 20px;
        display: flex;
        align-items: center;
        gap: 12px;
        text-shadow: 1px 1px 4px rgba(0,0,0,0.7);
    }}

    /* 7. BOTONES NATIVOS ESTILIZADOS */
    .stButton>button {{
        background: rgba(30, 20, 15, 0.6);
        color: #FDFBF7;
        border: 1px solid rgba(212, 175, 55, 0.3);
        border-radius: 12px;
        padding: 18px 20px;
        font-weight: 500;
        font-family: 'Montserrat', sans-serif;
        font-size: 0.95rem;
        transition: all 0.3s ease;
        width: 100%;
        text-align: left;
        backdrop-filter: blur(5px);
    }}
    .stButton>button:hover {{
        background: rgba(212, 175, 55, 0.2);
        border-color: #D4AF37;
        color: #D4AF37;
        transform: translateY(-3px);
        box-shadow: 0 10px 20px rgba(0,0,0,0.4);
    }}
    .stButton>button p {{
        font-size: 0.95rem;
        margin: 0;
    }}

    /* 8. MURO DE MIEMBROS */
    .member-row {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 15px 0;
        border-bottom: 1px solid rgba(212, 175, 55, 0.15);
    }}
    .member-row:last-child {{
        border-bottom: none;
    }}
    .member-name {{
        font-weight: 600;
        color: #FDFBF7;
        font-size: 1.05rem;
    }}
    .member-date {{
        font-size: 0.8rem;
        color: #D4AF37;
        background: rgba(212, 175, 55, 0.1);
        padding: 5px 12px;
        border-radius: 20px;
        border: 1px solid rgba(212, 175, 55, 0.3);
    }}

    /* 9. BOTÓN DE DONACIÓN ESPECIAL */
    .stButton>button[kind="primary"] {{
        background: linear-gradient(135deg, #D4AF37 0%, #F3E5AB 100%);
        color: #1A0F0A;
        border: none;
        font-weight: 700;
        text-align: center;
        justify-content: center;
        box-shadow: 0 10px 25px -5px rgba(212, 175, 55, 0.6);
        font-size: 1.1rem;
        padding: 20px;
    }}
    .stButton>button[kind="primary"]:hover {{
        transform: translateY(-3px) scale(1.02);
        box-shadow: 0 15px 30px -5px rgba(212, 175, 55, 0.8);
        color: #1A0F0A;
    }}
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
    st.markdown('<p class="hero-subtitle">LÁMPARA ES A MIS PIES TU PALABRA</p>', unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)

    # --- DISTRIBUCIÓN EN DOS COLUMNAS ---
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
            <p style="font-size: 1.15rem; line-height: 1.8; margin: 0; font-weight: 400; font-style: italic;">
            Señor, gracias por este nuevo día que me regalas. Guía mis pasos, ilumina mi mente y guarda mi corazón en tu verdad. Que cada palabra que salga de mi boca sea agradable a ti, y que cada acción refleje tu amor. Amén.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)

        # 3. Secciones de la App
        st.markdown('<div class="section-header">📖 Explora la Palabra</div>', unsafe_allow_html=True)
        
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

    # Columna Derecha
    with col_der:
        # Muro de miembros
        st.markdown('<div class="section-header">🤝 Muro de Miembros</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="premium-card" style="padding: 25px;">
            <p style="font-size: 0.9rem; color: #E6D5C3; margin-bottom: 15px; font-style: italic;">
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

        # Botón de donación
        if st.button("☕ Apoyar esta obra", type="primary", use_container_width=True):
            st.info("Redirigiendo a Ko-fi... (Aquí irá tu enlace)")

        st.markdown("<br>", unsafe_allow_html=True)
        
        # Estado del proyecto
        st.markdown("""
        <div style="background: rgba(212, 175, 55, 0.1); border: 1px solid rgba(212, 175, 55, 0.3); border-radius: 12px; padding: 20px; text-align: center; backdrop-filter: blur(5px);">
            <p style="color: #D4AF37; font-size: 0.9rem; margin: 0; font-weight: 600; letter-spacing: 1px;">✅ APP 100% GRATUITA</p>
            <p style="color: #E6D5C3; font-size: 0.8rem; margin-top: 8px;">Mantenida por donaciones</p>
        </div>
        """, unsafe_allow_html=True)

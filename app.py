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
# ESTILOS CON IMAGEN DE FONDO (GLASSMORPHISM)
# ============================================
# URL de una imagen impresionante de amanecer con cruz (puedes cambiarla si quieres)
IMG_URL = "https://images.unsplash.com/photo-1499209974431-9dac3ada00d7?q=80&w=2070&auto=format&fit=crop"

st.markdown(f"""
<style>
    /* Ocultar menú por defecto */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}
    
    /* Fondo con imagen y capa oscura para que el texto resalte */
    .stApp {{
        background-image: linear-gradient(rgba(10, 25, 45, 0.75), rgba(10, 25, 45, 0.85)), url("{IMG_URL}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        font-family: 'Helvetica Neue', Arial, sans-serif;
    }}
    
    /* Tipografía general en blanco */
    h1, h2, h3, p, span, div {{
        color: #FFFFFF !important;
    }}
    
    /* Título principal */
    .main-title {{
        font-family: 'Georgia', serif;
        font-size: 3rem;
        font-weight: 400;
        text-align: center;
        margin-bottom: 0rem;
        letter-spacing: 2px;
        text-shadow: 2px 2px 8px rgba(0,0,0,0.8);
    }}
    .main-subtitle {{
        text-align: center;
        color: #D4AF37 !important; /* Dorado */
        font-size: 1.1rem;
        margin-bottom: 2.5rem;
        font-style: italic;
        text-shadow: 1px 1px 4px rgba(0,0,0,0.8);
    }}
    
    /* Tarjetas efecto Cristal (Glassmorphism) */
    .glass-card {{
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 16px;
        padding: 2rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
    }}
    
    /* Tarjeta de versículo destacada */
    .verse-card {{
        background: rgba(212, 175, 55, 0.15); /* Dorado translúcido */
        border: 1px solid rgba(212, 175, 55, 0.4);
        border-radius: 16px;
        padding: 2rem;
        margin-bottom: 2rem;
        text-align: center;
        backdrop-filter: blur(10px);
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.4);
    }}
    .verse-text {{
        font-size: 1.3rem;
        font-style: italic;
        line-height: 1.6;
        margin-bottom: 1rem;
        text-shadow: 1px 1px 4px rgba(0,0,0,0.5);
    }}
    .verse-ref {{
        font-size: 0.9rem;
        letter-spacing: 3px;
        text-transform: uppercase;
        color: #D4AF37 !important;
        font-weight: bold;
    }}
    
    /* Botones de acceso rápido */
    .quick-btn {{
        display: flex;
        align-items: center;
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.15);
        border-radius: 12px;
        padding: 1.2rem;
        text-decoration: none !important;
        transition: all 0.3s ease;
        margin-bottom: 0.8rem;
        backdrop-filter: blur(5px);
    }}
    .quick-btn:hover {{
        background: rgba(255, 255, 255, 0.15);
        border-color: #D4AF37;
        transform: translateY(-3px);
        box-shadow: 0 10px 20px rgba(0,0,0,0.3);
    }}
    .quick-btn .icon {{
        font-size: 1.8rem;
        margin-right: 1rem;
    }}
    .quick-btn .text {{
        font-size: 1rem;
        font-weight: 600;
        letter-spacing: 0.5px;
    }}
    
    /* Muro de miembros */
    .member-item {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        background: rgba(0, 0, 0, 0.2);
        border-radius: 8px;
        padding: 0.8rem 1.2rem;
        margin-bottom: 0.6rem;
        border-left: 3px solid #D4AF37;
    }}
    .member-name {{
        font-weight: bold;
        font-size: 1rem;
    }}
    .member-date {{
        font-size: 0.8rem;
        color: #CCCCCC !important;
    }}
    
    /* Botón donar espectacular */
    .donate-btn {{
        display: block;
        background: linear-gradient(135deg, #D4AF37 0%, #F3E5AB 100%);
        color: #1A1A1A !important;
        text-align: center;
        padding: 1.2rem;
        border-radius: 50px;
        text-decoration: none !important;
        font-weight: bold;
        font-size: 1.1rem;
        letter-spacing: 1px;
        margin-top: 2rem;
        box-shadow: 0 10px 20px rgba(212, 175, 55, 0.3);
        transition: all 0.3s ease;
    }}
    .donate-btn:hover {{
        transform: scale(1.02);
        box-shadow: 0 15px 25px rgba(212, 175, 55, 0.5);
    }}
    
    /* Títulos de sección */
    .section-title {{
        font-size: 1.2rem;
        font-weight: bold;
        color: #FFFFFF !important;
        margin-top: 2.5rem;
        margin-bottom: 1rem;
        border-bottom: 1px solid rgba(255,255,255,0.2);
        padding-bottom: 0.5rem;
        text-shadow: 1px 1px 4px rgba(0,0,0,0.5);
    }}
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
    st.markdown('<h1 class="main-title">LA PALABRA</h1>', unsafe_allow_html=True)
    st.markdown('<p class="main-subtitle">"Lámpara es a mis pies tu palabra, y lumbrera a mi camino" — Salmos 119:105</p>', unsafe_allow_html=True)
    
    # Versículo del día
    st.markdown("""
    <div class="verse-card">
        <div class="verse-text">"Porque de tal manera amó Dios al mundo, que ha dado a su Hijo unigénito, para que todo aquel que en él cree, no se pierda, mas tenga vida eterna."</div>
        <div class="verse-ref">Juan 3:16</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Oración del día
    st.markdown('<p class="section-title">🙏 Oración del día</p>', unsafe_allow_html=True)
    st.markdown("""
    <div class="glass-card">
        <p style="font-size: 1.1rem; line-height: 1.8; margin: 0;">
        Señor, gracias por este nuevo día que me regalas. Guía mis pasos, ilumina mi mente y guarda mi corazón en tu verdad. Que cada palabra que salga de mi boca sea agradable a ti, y que cada acción refleje tu amor. Amén.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Accesos rápidos
    st.markdown('<p class="section-title">📖 Explora la App</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<a href="#" class="quick-btn"><span class="icon">📖</span><span class="text">La Palabra</span></a>', unsafe_allow_html=True)
        st.markdown('<a href="#" class="quick-btn"><span class="icon">💭</span><span class="text">Reflexiones</span></a>', unsafe_allow_html=True)
        st.markdown('<a href="#" class="quick-btn"><span class="icon">🔍</span><span class="text">Curiosidades</span></a>', unsafe_allow_html=True)
    with col2:
        st.markdown('<a href="#" class="quick-btn"><span class="icon">🙋</span><span class="text">Pregúntale al Pastor</span></a>', unsafe_allow_html=True)
        st.markdown('<a href="#" class="quick-btn"><span class="icon">⚠️</span><span class="text">Mitos y Falsas Doctrinas</span></a>', unsafe_allow_html=True)
        st.markdown('<a href="#" class="quick-btn"><span class="icon">❤️</span><span class="text">Favoritos</span></a>', unsafe_allow_html=True)
    
    # Muro de miembros
    st.markdown('<p class="section-title">❤️ Muro de Miembros</p>', unsafe_allow_html=True)
    st.markdown("""
    <div class="glass-card" style="padding: 1.5rem;">
        <p style="font-size: 0.9rem; margin-bottom: 1rem;">Estas son las personas que con su donación apoyan esta obra:</p>
        <div class="member-item">
            <span class="member-name">Juan P.</span>
            <span class="member-date">Octubre 2026</span>
        </div>
        <div class="member-item">
            <span class="member-name">María G.</span>
            <span class="member-date">Octubre 2026</span>
        </div>
        <div class="member-item">
            <span class="member-name">Un hermano anónimo</span>
            <span class="member-date">Septiembre 2026</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Botón donar
    st.markdown("""
    <a href="https://ko-fi.com/tu-usuario" target="_blank" class="donate-btn">
        ☕ APOYAR ESTA OBRA
    </a>
    """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown(
        '<p style="text-align:center; font-size:0.8rem; color:rgba(255,255,255,0.5) !important;">Hecho con ❤️ para la gloria de Dios</p>',
        unsafe_allow_html=True
    )

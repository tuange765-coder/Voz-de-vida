import streamlit as st
import requests
import random
import urllib.parse
import streamlit.components.v1 as components

# ============================================
# 1. CONFIGURACIÓN DE PÁGINA (DEBE SER LO PRIMERO)
# ============================================
st.set_page_config(
    page_title="Palabra de Vida | App Cristiana",
    page_icon="palabra-de-vida.png",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================
# 2. CONFIGURACIÓN DE BASE DE DATOS (SUPABASE)
# ============================================
MODO_DEMO = False

if not MODO_DEMO:
    try:
        from st_supabase_connection import SupabaseConnection, execute_query
        conn = st.connection("supabase", type=SupabaseConnection)
    except Exception as e:
        st.error(f"Error al conectar con Supabase. Revisa tus Secrets. Detalle: {e}")
        st.stop()

# ============================================
# 3. ESTILOS PROFESIONALES Y LÓGICA DE ADMIN
# ============================================
IMG_URL = "https://images.unsplash.com/photo-1504052434569-70ad5836ab65?q=80&w=2070&auto=format&fit=crop"

# Verificamos si el administrador quiere entrar usando el truco de la URL
query_params = st.query_params
es_admin_url = query_params.get("admin") == "true"

st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,400&family=Montserrat:wght@400;500;600&display=swap');

    .stApp {{
        background-image: linear-gradient(rgba(20, 10, 5, 0.8), rgba(10, 5, 0, 0.95)), url("{IMG_URL}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        font-family: 'Montserrat', sans-serif;
    }}

    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}

    /* OCULTAR LA BARRA LATERAL POR DEFECTO */
    [data-testid="collapsedControl"] {{display: none;}}
    section[data-testid="stSidebar"] {{display: none;}}

    /* MOSTRARLA SOLO SI SE USA EL TRUCO ?admin=true */
    {'section[data-testid="stSidebar"] {display: block !important;}' if es_admin_url else ''}

    h1, h2, h3 {{
        font-family: 'Cormorant Garamond', serif;
        color: #FDFBF7 !important;
    }}

    .hero-title {{
        font-family: 'Cormorant Garamond', serif;
        font-size: 4.5rem;
        font-weight: 700;
        color: #FDFBF7 !important;
        text-align: center;
        margin-bottom: 0;
        line-height: 1.1;
        text-shadow: 2px 2px 10px rgba(0,0,0,0.8);
    }}
    .hero-subtitle {{
        text-align: center;
        font-size: 1.2rem;
        color: #D4AF37 !important;
        margin-top: 10px;
        font-weight: 500;
        letter-spacing: 3px;
        text-shadow: 1px 1px 5px rgba(0,0,0,0.9);
        font-style: italic;
    }}

    /* ==========================================
       TARJETAS PREMIUM ESTILO PERGAMINO ELEGANTE
       ========================================== */
    .card-light {{
        background: #FDFBF7;
        background-image: url('https://www.transparenttextures.com/patterns/cream-paper.png');
        border: 2px solid #C9A961; /* Borde dorado sutil */
        border-radius: 8px; /* Bordes ligeramente suavizados */
        padding: 30px;
        margin-bottom: 25px;
        box-shadow: 
            0 10px 25px rgba(0, 0, 0, 0.5),
            inset 0 0 15px rgba(201, 169, 97, 0.1); /* Brillo interior dorado */
        color: #2C1A0F !important;
        position: relative;
        overflow: hidden;
    }}
    
    /* Decoración de esquina para darle un toque de libro antiguo */
    .card-light::before {{
        content: "";
        position: absolute;
        top: 10px; left: 10px; right: 10px; bottom: 10px;
        border: 1px solid rgba(201, 169, 97, 0.3);
        border-radius: 4px;
        pointer-events: none;
    }}

    .card-light *, 
    .card-light p, .card-light span, .card-light div, .card-light strong, .card-light li,
    .card-light h1, .card-light h2, .card-light h3, .card-light h4 {{
        color: #2C1A0F !important;
        font-family: 'Montserrat', sans-serif;
    }}

    .verse-light {{
        background: #FDFBF7 !important;
        background-image: url('https://www.transparenttextures.com/patterns/cream-paper.png');
        border-left: 6px solid #D4AF37;
        border-radius: 8px;
        padding: 40px;
        margin: 20px 0 40px 0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.4);
    }}
    .verse-light * {{
        color: #1A1A1A !important;
    }}
    .verse-light .verse-text {{
        font-family: 'Cormorant Garamond', serif;
        font-size: 1.9rem;
        font-style: italic;
        line-height: 1.5;
        text-align: center;
        color: #2C1A0F !important;
    }}
    .verse-light .verse-ref {{
        display: block;
        margin-top: 20px;
        font-family: 'Montserrat', sans-serif;
        font-size: 0.9rem;
        letter-spacing: 3px;
        text-transform: uppercase;
        color: #D4AF37 !important;
        font-weight: 700;
        text-align: center;
    }}

    /* ==========================================
       TARJETAS OSCURAS (Muro de miembros, etc)
       ========================================== */
    .card-dark {{
        background: rgba(30, 20, 15, 0.95) !important;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(212, 175, 55, 0.4);
        border-radius: 8px;
        padding: 30px;
        margin-bottom: 25px;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.6);
    }}
    .card-dark p, .card-dark span, .card-dark div, .card-dark li, .card-dark strong {{
        color: #FDFBF7 !important;
    }}

    .section-header {{
        font-family: 'Cormorant Garamond', serif;
        font-size: 1.6rem;
        font-weight: 600;
        color: #FDFBF7 !important;
        margin-bottom: 20px;
        display: flex;
        align-items: center;
        gap: 12px;
        text-shadow: 1px 1px 4px rgba(0,0,0,0.8);
        border-bottom: 1px solid rgba(212, 175, 55, 0.4);
        padding-bottom: 10px;
    }}

    /* Botones estándar de Streamlit (formularios, volver) */
    .stButton>button {{
        background: #FDFBF7 !important;
        background-image: url('https://www.transparenttextures.com/patterns/cream-paper.png') !important;
        color: #2C1A0F !important;
        border: 2px solid #C9A961 !important;
        border-radius: 8px !important;
        padding: 15px 20px !important;
        font-weight: 700 !important;
        font-family: 'Cormorant Garamond', serif !important;
        font-size: 1.2rem !important;
        transition: all 0.3s ease !important;
        width: 100% !important;
        text-align: center !important;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3) !important;
    }}
    .stButton>button:hover {{
        background: #FFF3E0 !important;
        border-color: #D4AF37 !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 15px rgba(212, 175, 55, 0.4) !important;
        color: #1A0F0A !important;
    }}
    .stButton>button p {{
        color: #2C1A0F !important;
        font-size: 1.2rem !important;
        margin: 0 !important;
    }}

    .member-row {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 15px 0;
        border-bottom: 1px solid rgba(212, 175, 55, 0.3);
    }}
    .member-row:last-child {{
        border-bottom: none;
    }}
    .member-name {{
        font-weight: 600;
        color: #FDFBF7 !important;
        font-size: 1.1rem;
    }}
    .member-date {{
        font-size: 0.9rem;
        color: #D4AF37 !important;
        font-style: italic;
    }}

    .stSelectbox label, .stNumberInput label {{
        color: #FDFBF7 !important;
        font-family: 'Montserrat', sans-serif;
        font-size: 1.1rem;
    }}
    .stSelectbox div[data-baseweb="select"] > div,
    .stNumberInput input {{
        background-color: #FDFBF7 !important;
        color: #2C1A0F !important;
        border-radius: 8px;
        border: 1px solid #C9A961;
    }}
    .stSelectbox div[data-baseweb="select"] *,
    .stNumberInput input {{
        color: #2C1A0F !important;
    }}

    details {{
        background: #FDFBF7 !important;
        background-image: url('https://www.transparenttextures.com/patterns/cream-paper.png');
        border: 2px solid #C9A961;
        border-radius: 8px;
        padding: 15px 20px;
        margin-bottom: 15px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.3);
    }}
    summary {{
        font-weight: 700;
        color: #2C1A0F !important;
        font-size: 1.2rem;
        cursor: pointer;
        outline: none;
        font-family: 'Cormorant Garamond', serif;
    }}
    details[open] summary {{
        margin-bottom: 15px;
        border-bottom: 1px solid rgba(201, 169, 97, 0.3);
        padding-bottom: 10px;
    }}
    details p, details strong, details div {{
        color: #2C1A0F !important;
        line-height: 1.6;
    }}
</style>
""", unsafe_allow_html=True)

# ============================================
# 4. INICIALIZAR ESTADO DE NAVEGACIÓN Y DATOS
# ============================================
if 'pagina_actual' not in st.session_state:
    st.session_state.pagina_actual = 'inicio'

if 'admin_logged' not in st.session_state:
    st.session_state.admin_logged = False

def cambiar_pagina(nombre_pagina):
    st.session_state.pagina_actual = nombre_pagina
    st.rerun()

# ============================================
# 5. LÓGICA DE MÚSICA CON YOUTUBE
# ============================================
URLS_YOUTUBE = [
    "https://www.youtube.com/watch?v=W14mg_zQpZc", 
    "https://www.youtube.com/watch?v=emVLPHouen4", 
    "https://www.youtube.com/watch?v=zuSdkh45_L4",
    "https://www.youtube.com/watch?v=AB2x_DII3W0",
    "https://www.youtube.com/watch?v=gx_4F3NQzCE",
    "https://www.youtube.com/watch?v=oT-vdtizfHo"
]

if 'indice_video' not in st.session_state:
    st.session_state.indice_video = 0

def obtener_video_id(url):
    """Extrae el ID del video de un enlace de YouTube."""
    if "v=" in url:
        return url.split("v=")[1].split("&")[0]
    elif "youtu.be/" in url:
        return url.split("youtu.be/")[1].split("?")[0]
    return url

# La barra lateral solo se muestra si se usa el truco ?admin=true
with st.sidebar:
    st.markdown("### 🔐 Acceso Administrador")
    if not st.session_state.admin_logged:
        pass_admin = st.text_input("Contraseña", type="password", key="pass_admin_input")
        if st.button("Entrar como Admin", use_container_width=True):
            if pass_admin == "Juan*316*":
                st.session_state.admin_logged = True
                st.success("¡Bienvenido, Admin!")
                st.rerun()
            else:
                st.error("Contraseña incorrecta")
    else:
        st.success("Sesión de Admin activa")
        if st.button("Cerrar Sesión Admin", use_container_width=True):
            st.session_state.admin_logged = False
            st.rerun()
        if st.button("Ir al Panel de Administrador", use_container_width=True):
            cambiar_pagina("admin")

# ============================================
# 6. FUNCIONES DE LAS PÁGINAS
# ============================================

def mostrar_inicio():
    st.markdown('<h1 class="hero-title">Palabra de Vida</h1>', unsafe_allow_html=True)
    st.markdown('<p class="hero-subtitle">LÁMPARA ES A MIS PIES TU PALABRA</p>', unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)

    col_izq, col_der = st.columns([2.2, 1], gap="large")

    with col_izq:
        # 1. Versículo del día
        st.markdown("""
        <div class="verse-light">
            <div class="verse-text">"Porque de tal manera amó Dios al mundo, que ha dado a su Hijo unigénito, para que todo aquel que en él cree, no se pierda, mas tenga vida eterna."</div>
            <span class="verse-ref">Juan 3:16 — Versículo del día</span>
        </div>
        """, unsafe_allow_html=True)

        # 2. Oración de la mañana
        st.markdown('<div class="section-header">🙏 Oración de la Mañana</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="card-light">
            <p style="font-size: 1.15rem; line-height: 1.8; margin: 0; font-weight: 400; font-style: italic;">
            Señor, gracias por este nuevo día que me regalas. Guía mis pasos, ilumina mi mente y guarda mi corazón en tu verdad. Que cada palabra que salga de mi boca sea agradable a ti, y que cada acción refleje tu amor. Amén.
            </p>
        </div>
        """, unsafe_allow_html=True)

        # 3. APOYAR LA OBRA
        st.markdown('<div class="section-header">☕ Apoyar la Obra</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="card-light" style="padding: 25px;">
            <p style="font-size: 0.95rem; line-height: 1.6; margin-bottom: 15px; text-align: justify;">
                <strong>Si crees que mi trabajo es edificante, haz tu donación para seguir adelante.</strong> Esta contribución no es un diezmo ni una ofrenda mensual. Es un aporte voluntario y único, destinado a mantener esta herramienta gratuita para todos.
            </p>
            <p style="font-size: 1rem; line-height: 1.6; margin-bottom: 20px;">
                Si ud quiere hacer una donación voluntaria, comuníquese vía WhatsApp por el <strong>04242004015</strong>.
            </p>
            <a href="https://wa.me/584242004015" target="_blank" style="text-decoration: none;">
                <div style="background: #25D366; color: white; text-align: center; padding: 15px; border-radius: 8px; font-weight: 700; font-size: 1rem; box-shadow: 0 4px 10px rgba(37, 211, 102, 0.4); cursor: pointer; display: flex; align-items: center; justify-content: center; gap: 10px;">
                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="white">
                        <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z"/>
                    </svg>
                    Contactar por WhatsApp
                </div>
            </a>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # 4. REPRODUCTOR DE MÚSICA
        st.markdown('<div class="section-header">🎵 Música Cristiana</div>', unsafe_allow_html=True)
        st.markdown('<div class="card-light" style="padding: 25px;">', unsafe_allow_html=True)
        
        if URLS_YOUTUBE:
            url_actual = URLS_YOUTUBE[st.session_state.indice_video]
            video_id = obtener_video_id(url_actual)
            
            youtube_iframe = f"""
            <div style="display: flex; justify-content: center; border: 2px solid #C9A961; padding: 5px; background: #000; border-radius: 8px;">
                <iframe width="50%" height="250" 
                        src="https://www.youtube.com/embed/{video_id}?autoplay=0&rel=0" 
                        frameborder="0" 
                        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
                        allowfullscreen>
                </iframe>
            </div>
            """
            components.html(youtube_iframe, height=270)
            
            if st.button("⏭️ Siguiente Canción", use_container_width=True):
                st.session_state.indice_video = (st.session_state.indice_video + 1) % len(URLS_YOUTUBE)
                st.rerun()
            
            st.caption(f"Canción {st.session_state.indice_video + 1} de {len(URLS_YOUTUBE)}")
        else:
            st.info("No hay canciones configuradas.")
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)

        # 5. BOTONES DE EXPLORACIÓN (Diseño Papiro en Iframe)
        st.markdown('<div class="section-header">📖 Explora la Palabra</div>', unsafe_allow_html=True)
        
        html_botones = """
        <!DOCTYPE html>
        <html>
        <head>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@700&display=swap');
            
            body {
                margin: 0;
                padding: 0;
                background: transparent;
            }
            
            .papiro-grid {
                display: grid;
                grid-template-columns: repeat(3, 1fr);
                gap: 15px;
                padding: 10px;
            }
            
            .papiro-btn {
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                background: #EFE3C3;
                background-image: 
                    radial-gradient(circle at 10% 20%, rgba(139, 69, 19, 0.1) 0%, transparent 20%),
                    radial-gradient(circle at 90% 80%, rgba(139, 69, 19, 0.1) 0%, transparent 20%),
                    url('https://www.transparenttextures.com/patterns/paper-fibers.png');
                border: 2px solid #A67B5B;
                border-radius: 4px;
                padding: 20px 10px;
                text-decoration: none;
                color: #2C1A0F;
                font-family: 'Cormorant Garamond', serif;
                font-weight: 700;
                font-size: 1.1rem;
                text-align: center;
                box-shadow: 
                    4px 4px 10px rgba(0, 0, 0, 0.5),
                    inset 0 0 15px rgba(139, 69, 19, 0.2),
                    inset 0 0 3px rgba(255, 255, 255, 0.5);
                transition: all 0.3s ease;
                cursor: pointer;
                position: relative;
                overflow: hidden;
                min-height: 110px;
                text-shadow: 1px 1px 0px rgba(255,255,255,0.4);
            }
            
            .papiro-btn::before {
                content: "";
                position: absolute;
                top: 5px; left: 5px; right: 5px; bottom: 5px;
                border: 1px dashed rgba(166, 123, 91, 0.5);
                pointer-events: none;
            }

            .papiro-btn:hover {
                background: #FFF3E0;
                border-color: #D4AF37;
                transform: translateY(-4px) scale(1.02);
                box-shadow: 
                    6px 8px 15px rgba(0, 0, 0, 0.6),
                    inset 0 0 20px rgba(212, 175, 55, 0.3),
                    inset 0 0 3px rgba(255, 255, 255, 0.9);
                color: #1A0F0A;
            }
            
            .papiro-btn .icono {
                font-size: 1.8rem;
                margin-bottom: 8px;
                position: relative;
                z-index: 2;
                color: #8B4513;
                text-shadow: 1px 1px 1px rgba(255,255,255,0.5);
            }
            
            .papiro-btn .texto {
                position: relative;
                z-index: 2;
                font-size: 0.95rem;
                letter-spacing: 1px;
                text-transform: uppercase;
            }
        </style>
        </head>
        <body>
            <div class="papiro-grid">
                <a href="?pagina=biblia" target="_self" class="papiro-btn">
                    <span class="icono">📖</span>
                    <div class="texto">La Biblia</div>
                </a>
                <a href="?pagina=reflexiones" target="_self" class="papiro-btn">
                    <span class="icono">💭</span>
                    <div class="texto">Reflexiones</div>
                </a>
                <a href="?pagina=curiosidades" target="_self" class="papiro-btn">
                    <span class="icono">🔍</span>
                    <div class="texto">Curiosidades</div>
                </a>
                <a href="?pagina=pastor" target="_self" class="papiro-btn">
                    <span class="icono">🙋</span>
                    <div class="texto">Pregúntale al Pastor</div>
                </a>
                <a href="?pagina=mitos" target="_self" class="papiro-btn">
                    <span class="icono">⚠️</span>
                    <div class="texto">Mitos y Doctrinas</div>
                </a>
                <a href="?pagina=suenos" target="_self" class="papiro-btn">
                    <span class="icono">💭</span>
                    <div class="texto">Tus sueños</div>
                </a>
            </div>
        </body>
        </html>
        """
        components.html(html_botones, height=380, scrolling=False)

    with col_der:
        # 6. MURO DE MIEMBROS
        st.markdown('<div class="section-header">🤝 Muro de Miembros</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="card-light" style="padding: 25px;">
            <p style="font-size: 0.95rem; margin-bottom: 20px; font-style: italic; border-bottom: 1px solid rgba(201, 169, 97, 0.3); padding-bottom: 10px;">
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

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("""
        <div class="card-dark" style="padding: 25px; text-align: center;">
            <p style="color: #D4AF37 !important; font-size: 1rem; margin: 0; font-weight: 700; letter-spacing: 1px;">✅ APP 100% GRATUITA</p>
            <p style="font-size: 0.9rem; margin-top: 8px; margin-bottom: 15px;">Mantenida por donaciones</p>
            <hr style="border-color: rgba(212, 175, 55, 0.3); margin: 15px 0;">
            <p style="font-size: 0.85rem; margin: 0; color: #FDFBF7 !important;">Esta app fue creada por <strong>Willian Almenar</strong>.</p>
            <p style="font-size: 0.8rem; margin: 5px 0 0 0; color: #B0A090 !important; font-style: italic;">Todos los derechos reservados. Octubre 2026.</p>
        </div>
        """, unsafe_allow_html=True)

# --- PÁGINA: BIBLIA ---
def mostrar_biblia():
    if st.button("⬅️ Volver al Inicio"):
        cambiar_pagina("inicio")
    
    st.markdown('<h1 class="hero-title" style="font-size: 3rem;">📖 La Biblia</h1>', unsafe_allow_html=True)
    st.markdown('<p class="hero-subtitle">Reina-Valera 1960</p>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    libros = [
        "Génesis", "Éxodo", "Levítico", "Números", "Deuteronomio", "Josué", "Jueces", "Rut",
        "1 Samuel", "2 Samuel", "1 Reyes", "2 Reyes", "1 Crónicas", "2 Crónicas", "Esdras",
        "Nehemías", "Ester", "Job", "Salmos", "Proverbios", "Eclesiastés", "Cantares",
        "Isaías", "Jeremías", "Lamentaciones", "Ezequiel", "Daniel", "Oseas", "Joel", "Amós",
        "Obadías", "Jonás", "Miqueas", "Nahúm", "Habacuc", "Sofonías", "Hageo", "Zacarías", "Malaquías",
        "Mateo", "Marcos", "Lucas", "Juan", "Hechos", "Romanos", "1 Corintios", "2 Corintios",
        "Gálatas", "Efesios", "Filipenses", "Colosenses", "1 Tesalonicenses", "2 Tesalonicenses",
        "1 Timoteo", "2 Timoteo", "Tito", "Filemón", "Hebreos", "Santiago", "1 Pedro", "2 Pedro",
        "1 Juan", "2 Juan", "3 Juan", "Judas", "Apocalipsis"
    ]
    
    slugs = {
        "Génesis": "genesis", "Éxodo": "exodus", "Levítico": "leviticus", "Números": "numbers",
        "Deuteronomio": "deuteronomy", "Josué": "joshua", "Jueces": "judges", "Rut": "ruth",
        "1 Samuel": "1-samuel", "2 Samuel": "2-samuel", "1 Reyes": "1-kings", "2 Reyes": "2-kings",
        "Salmos": "psalms", "Proverbios": "proverbs", "Isaías": "isaiah", "Jeremías": "jeremiah",
        "Mateo": "matthew", "Marcos": "mark", "Lucas": "luke", "Juan": "john", "Hechos": "acts",
        "Romanos": "romans", "1 Corintios": "1-corinthians", "2 Corintios": "2-corinthians",
        "Gálatas": "galatians", "Efesios": "ephesians", "Filipenses": "philippians",
        "Colosenses": "colossians", "Apocalipsis": "revelation"
    }
    
    col_libro, col_capitulo = st.columns([2, 1])
    with col_libro:
        libro_sel = st.selectbox("Selecciona un libro", libros, index=42)
    with col_capitulo:
        capitulo_sel = st.number_input("Capítulo", min_value=1, max_value=150, value=3)
    
    slug = slugs.get(libro_sel, "john")
    url = f"https://api.midvash.com/v1/rvr1960/{slug}/{capitulo_sel}"
    
    try:
        with st.spinner("Cargando la Palabra..."):
            respuesta = requests.get(url)
            respuesta.raise_for_status()
            datos = respuesta.json()
            versiculos_texto = datos.get("data", {}).get("verses", [])
            
            if not versiculos_texto:
                st.warning("No se encontraron versículos para esta selección.")
            else:
                st.markdown(f'<div class="section-header">📖 {libro_sel} {capitulo_sel}</div>', unsafe_allow_html=True)
                texto_html = ""
                for i, texto in enumerate(versiculos_texto, start=1):
                    texto_html += f'<p style="text-align: justify; text-indent: 20px;"><strong style="color: #8B5A2B !important;">{i}.</strong> {texto}</p>'
                
                st.markdown(f"""
                <div class="card-light" style="max-height: 600px; overflow-y: auto;">
                    {texto_html}
                </div>
                """, unsafe_allow_html=True)
    except Exception as e:
        st.error(f"No se pudo cargar el capítulo. Verifica tu conexión o intenta con otro capítulo. (Error: {e})")


# --- PÁGINA: CURIOSIDADES ---
def mostrar_curiosidades():
    if st.button("⬅️ Volver al Inicio"):
        cambiar_pagina("inicio")
    
    st.markdown('<h1 class="hero-title" style="font-size: 3rem;">🔍 Curiosidades Bíblicas</h1>', unsafe_allow_html=True)
    st.markdown('<p class="hero-subtitle">Datos históricos y arqueológicos que confirman las Escrituras</p>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    res = execute_query(conn.table("curiosidades").select("*").order("created_at", desc=True), ttl="1m")
    data_curiosidades = res.data

    if not data_curiosidades:
        st.info("Aún no hay curiosidades publicadas. El administrador las agregará pronto.")
    else:
        for c in data_curiosidades:
            st.markdown(f"""
            <details>
                <summary>{c['titulo']}</summary>
                <div>
                    <p><strong>¿Qué es?</strong> {c['que_es']}</p>
                    <p><strong>¿Por qué es importante?</strong> {c['importancia']}</p>
                    <p><strong>Referencia bíblica:</strong> {c['referencia']}</p>
                </div>
            </details>
            """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="section-header">💡 Sabías que...</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card-dark">
        <p>La arqueología no prueba la fe, pero sí <strong>ilumina y confirma</strong> el contexto histórico de las Escrituras.</p>
    </div>
    """, unsafe_allow_html=True)


# --- PÁGINA: PREGÚNTALE AL PASTOR ---
def mostrar_pastor():
    if st.button("⬅️ Volver al Inicio"):
        cambiar_pagina("inicio")
    
    st.markdown('<h1 class="hero-title" style="font-size: 3rem;">🙋 Pregúntale al Pastor</h1>', unsafe_allow_html=True)
    st.markdown('<p class="hero-subtitle">Envía tu duda y recibe una respuesta bíblica</p>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown('<div class="section-header">📝 Envía tu pregunta</div>', unsafe_allow_html=True)
    with st.expander("Haz clic aquí para escribir tu pregunta", expanded=True):
        with st.form("form_pregunta"):
            nombre = st.text_input("Tu nombre (opcional)", placeholder="Ej: Juan Pérez")
            pregunta = st.text_area("Escribe tu pregunta aquí", placeholder="¿Qué significa...?", height=150)
            
            submitted = st.form_submit_button("Enviar Pregunta", type="primary", use_container_width=True)
            
            if submitted:
                if not pregunta.strip():
                    st.warning("Por favor, escribe una pregunta antes de enviar.")
                else:
                    conn.table("respuestas_pastor").insert({
                        "pregunta": pregunta,
                        "respuesta": "PENDIENTE",
                        "fecha": "Hoy",
                        "nombre_usuario": nombre if nombre else "Anónimo",
                        "estado": "pendiente"
                    }).execute()
                    
                    st.success("¡Pregunta enviada! El pastor la revisará y publicará una respuesta pronto.")
                    st.rerun()

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown('<div class="section-header">💬 Respuestas del Pastor</div>', unsafe_allow_html=True)
    
    res = execute_query(conn.table("respuestas_pastor").select("*").eq("estado", "respondido").order("created_at", desc=True), ttl="1m")
    data_pastor = res.data
    
    if not data_pastor:
        st.info("Aún no hay respuestas publicadas. ¡Vuelve pronto!")
    else:
        for r in data_pastor:
            st.markdown(f"""
            <div class="card-light">
                <p style="font-weight: 600; color: #8B5A2B !important; margin-bottom: 5px;">Pregunta: {r['pregunta']}</p>
                <p style="font-size: 0.9rem; color: #5C3A21 !important; margin-bottom: 10px; font-style: italic;">{r.get('fecha', '')}</p>
                <p><strong>Respuesta:</strong> {r['respuesta']}</p>
            </div>
            """, unsafe_allow_html=True)


# --- PÁGINA: SUEÑOS ---
def mostrar_suenos():
    if st.button("⬅️ Volver al Inicio"):
        cambiar_pagina("inicio")
    
    st.markdown('<h1 class="hero-title" style="font-size: 3rem;">💭 Tus sueños significan algo</h1>', unsafe_allow_html=True)
    st.markdown('<p class="hero-subtitle">Comparte tu sueño y recibe una interpretación bíblica</p>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown('<div class="section-header">📝 Envía tu sueño</div>', unsafe_allow_html=True)
    with st.expander("Haz clic aquí para escribir tu sueño", expanded=True):
        with st.form("form_sueno"):
            nombre_sueno = st.text_input("Tu nombre (opcional)", placeholder="Ej: Juan Pérez")
            sueno = st.text_area("Describe tu sueño aquí", placeholder="Soñé que...", height=150)
            
            submitted_sueno = st.form_submit_button("Enviar Sueño", type="primary", use_container_width=True)
            
            if submitted_sueno:
                if not sueno.strip():
                    st.warning("Por favor, describe tu sueño antes de enviar.")
                else:
                    conn.table("suenos").insert({
                        "sueno": sueno,
                        "interpretacion": "PENDIENTE",
                        "fecha": "Hoy",
                        "nombre_usuario": nombre_sueno if nombre_sueno else "Anónimo",
                        "estado": "pendiente"
                    }).execute()
                    
                    st.success("¡Sueño enviado! El pastor lo revisará y publicará una respuesta pronto.")
                    st.rerun()

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown('<div class="section-header">💬 Interpretaciones publicadas</div>', unsafe_allow_html=True)
    
    res = execute_query(conn.table("suenos").select("*").eq("estado", "respondido").order("created_at", desc=True), ttl="1m")
    data_suenos = res.data
    
    if not data_suenos:
        st.info("Aún no hay interpretaciones publicadas. ¡Vuelve pronto!")
    else:
        for s in data_suenos:
            st.markdown(f"""
            <div class="card-light">
                <p style="font-weight: 600; color: #8B5A2B !important; margin-bottom: 5px;">Sueño: {s['sueno']}</p>
                <p style="font-size: 0.9rem; color: #5C3A21 !important; margin-bottom: 10px; font-style: italic;">{s.get('fecha', '')}</p>
                <p><strong>Interpretación:</strong> {s['interpretacion']}</p>
            </div>
            """, unsafe_allow_html=True)


# --- PÁGINA: REFLEXIONES ---
def mostrar_reflexiones():
    if st.button("⬅️ Volver al Inicio"):
        cambiar_pagina("inicio")
    st.markdown('<h1 class="hero-title" style="font-size: 3rem;">💭 Reflexiones</h1>', unsafe_allow_html=True)
    
    res = execute_query(conn.table("reflexiones").select("*").order("created_at", desc=True), ttl="1m")
    data_ref = res.data
    
    if not data_ref:
        st.info("Próximamente: Devocionales diarios.")
    else:
        for r in data_ref:
            st.markdown(f"""
            <div class="card-light">
                <h3 style="color: #8B5A2B !important; border-bottom: 1px solid rgba(139, 90, 43, 0.3); padding-bottom: 10px;">{r['titulo']}</h3>
                <p style="text-align: justify;">{r['contenido']}</p>
            </div>
            """, unsafe_allow_html=True)


# --- PÁGINA: MITOS ---
def mostrar_mitos():
    if st.button("⬅️ Volver al Inicio"):
        cambiar_pagina("inicio")
    st.markdown('<h1 class="hero-title" style="font-size: 3rem;">⚠️ Mitos y Doctrinas</h1>', unsafe_allow_html=True)
    
    res = execute_query(conn.table("mitos").select("*").order("created_at", desc=True), ttl="1m")
    data_mitos = res.data
    
    if not data_mitos:
        st.info("Próximamente: Aclaraciones bíblicas.")
    else:
        for m in data_mitos:
            st.markdown(f"""
            <div class="card-light">
                <h3 style="color: #8B5A2B !important; border-bottom: 1px solid rgba(139, 90, 43, 0.3); padding-bottom: 10px;">{m['titulo']}</h3>
                <p style="text-align: justify;">{m['explicacion']}</p>
            </div>
            """, unsafe_allow_html=True)


# --- PÁGINA: ADMIN ---
def mostrar_admin():
    if not st.session_state.admin_logged:
        st.error("Debes iniciar sesión como administrador para acceder a esta página.")
        if st.button("Volver al Inicio"):
            cambiar_pagina("inicio")
        return

    if st.button("⬅️ Volver al Inicio"):
        cambiar_pagina("inicio")
    
    st.markdown('<h1 class="hero-title" style="font-size: 3rem;">🔐 Panel de Administrador</h1>', unsafe_allow_html=True)
    st.markdown('<p class="hero-subtitle">Gestiona el contenido de la app</p>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    tab1, tab2, tab3, tab4, tab5 = st.tabs(["🙋 Pastor", "💭 Reflexiones", "🔍 Curiosidades", "⚠️ Mitos", "💭 Sueños"])

    with tab1:
        st.markdown("### Preguntas Pendientes")
        pendientes = execute_query(conn.table("respuestas_pastor").select("*").eq("estado", "pendiente"), ttl="0").data
        if not pendientes:
            st.info("No hay preguntas pendientes.")
        else:
            for p in pendientes:
                with st.expander(f"Pregunta de {p.get('nombre_usuario', 'Anónimo')}: {p['pregunta'][:50]}..."):
                    st.write(f"**Pregunta:** {p['pregunta']}")
                    respuesta = st.text_area("Tu respuesta", key=f"resp_{p['id']}")
                    if st.button("Publicar Respuesta", key=f"btn_pub_{p['id']}"):
                        if respuesta.strip():
                            conn.table("respuestas_pastor").update({
                                "respuesta": respuesta,
                                "estado": "respondido"
                            }).eq("id", p['id']).execute()
                            st.success("¡Respuesta publicada!")
                            st.rerun()
                        else:
                            st.warning("Escribe una respuesta antes de publicar.")

        st.markdown("---")
        st.markdown("### Agregar Respuesta Manual")
        with st.form("admin_pastor"):
            pregunta = st.text_area("Pregunta del usuario", height=80)
            respuesta = st.text_area("Tu respuesta", height=150)
            fecha = st.text_input("Fecha", value="Hoy")
            
            if st.form_submit_button("Publicar Respuesta", type="primary", use_container_width=True):
                if pregunta and respuesta:
                    conn.table("respuestas_pastor").insert({
                        "pregunta": pregunta, 
                        "respuesta": respuesta, 
                        "fecha": fecha,
                        "estado": "respondido"
                    }).execute()
                    st.success("¡Respuesta publicada!")
                    st.rerun()
                else:
                    st.warning("Completa todos los campos.")

        data = execute_query(conn.table("respuestas_pastor").select("*").eq("estado", "respondido").order("created_at", desc=True), ttl="0").data
        st.markdown("### Respuestas Publicadas")
        if not data:
            st.info("No hay respuestas publicadas aún.")
        else:
            for r in data:
                with st.expander(f"Pregunta: {r['pregunta'][:50]}..."):
                    st.write(f"**Respuesta:** {r['respuesta']}")
                    if st.button(f"Eliminar", key=f"del_p_{r['id']}"):
                        conn.table("respuestas_pastor").delete().eq("id", r['id']).execute()
                        st.rerun()

    with tab2:
        st.markdown("### Agregar Reflexión")
        with st.form("admin_reflexion"):
            titulo_ref = st.text_input("Título")
            contenido_ref = st.text_area("Contenido", height=200)
            
            if st.form_submit_button("Publicar Reflexión", type="primary", use_container_width=True):
                if titulo_ref and contenido_ref:
                    conn.table("reflexiones").insert({"titulo": titulo_ref, "contenido": contenido_ref}).execute()
                    st.success("¡Reflexión publicada!")
                    st.rerun()
                else:
                    st.warning("Completa todos los campos.")

        data = execute_query(conn.table("reflexiones").select("*").order("created_at", desc=True), ttl="0").data
        st.markdown("### Reflexiones Publicadas")
        if not data:
            st.info("No hay reflexiones publicadas aún.")
        else:
            for r in data:
                with st.expander(f"Reflexión: {r['titulo']}"):
                    st.write(r['contenido'])
                    if st.button(f"Eliminar", key=f"del_r_{r['id']}"):
                        conn.table("reflexiones").delete().eq("id", r['id']).execute()
                        st.rerun()

    with tab3:
        st.markdown("### Agregar Curiosidad")
        with st.form("admin_curiosidad"):
            titulo_cur = st.text_input("Título")
            que_es = st.text_area("¿Qué es?", height=100)
            importancia = st.text_area("¿Por qué es importante?", height=100)
            referencia = st.text_input("Referencia bíblica")
            
            if st.form_submit_button("Publicar Curiosidad", type="primary", use_container_width=True):
                if titulo_cur and que_es:
                    conn.table("curiosidades").insert({"titulo": titulo_cur, "que_es": que_es, "importancia": importancia, "referencia": referencia}).execute()
                    st.success("¡Curiosidad publicada!")
                    st.rerun()
                else:
                    st.warning("Completa los campos obligatorios.")

        data = execute_query(conn.table("curiosidades").select("*").order("created_at", desc=True), ttl="0").data
        st.markdown("### Curiosidades Publicadas")
        if not data:
            st.info("No hay curiosidades publicadas aún.")
        else:
            for c in data:
                with st.expander(f"{c['titulo']}"):
                    st.write(f"**¿Qué es?** {c['que_es']}")
                    st.write(f"**Importancia:** {c['importancia']}")
                    st.write(f"**Referencia:** {c['referencia']}")
                    if st.button(f"Eliminar", key=f"del_c_{c['id']}"):
                        conn.table("curiosidades").delete().eq("id", c['id']).execute()
                        st.rerun()

    with tab4:
        st.markdown("### Agregar Mito o Falsa Doctrina")
        with st.form("admin_mito"):
            titulo_mito = st.text_input("Título del mito")
            explicacion = st.text_area("Explicación bíblica", height=200)
            
            if st.form_submit_button("Publicar Mito", type="primary", use_container_width=True):
                if titulo_mito and explicacion:
                    conn.table("mitos").insert({"titulo": titulo_mito, "explicacion": explicacion}).execute()
                    st.success("¡Mito publicado!")
                    st.rerun()
                else:
                    st.warning("Completa todos los campos.")

        data = execute_query(conn.table("mitos").select("*").order("created_at", desc=True), ttl="0").data
        st.markdown("### Mitos Publicados")
        if not data:
            st.info("No hay mitos publicados aún.")
        else:
            for m in data:
                with st.expander(f"Mito: {m['titulo']}"):
                    st.write(m['explicacion'])
                    if st.button(f"Eliminar", key=f"del_m_{m['id']}"):
                        conn.table("mitos").delete().eq("id", m['id']).execute()
                        st.rerun()

    with tab5:
        st.markdown("### Sueños Pendientes")
        pendientes_suenos = execute_query(conn.table("suenos").select("*").eq("estado", "pendiente"), ttl="0").data
        if not pendientes_suenos:
            st.info("No hay sueños pendientes.")
        else:
            for s in pendientes_suenos:
                with st.expander(f"Sueño de {s.get('nombre_usuario', 'Anónimo')}: {s['sueno'][:50]}..."):
                    st.write(f"**Sueño:** {s['sueno']}")
                    interpretacion = st.text_area("Interpretación", key=f"interp_{s['id']}")
                    if st.button("Publicar Interpretación", key=f"btn_interp_{s['id']}"):
                        if interpretacion.strip():
                            conn.table("suenos").update({
                                "interpretacion": interpretacion,
                                "estado": "respondido"
                            }).eq("id", s['id']).execute()
                            st.success("¡Interpretación publicada!")
                            st.rerun()
                        else:
                            st.warning("Escribe una interpretación antes de publicar.")

        st.markdown("---")
        st.markdown("### Agregar Interpretación Manual")
        with st.form("admin_sueno"):
            sueno = st.text_area("Sueño del usuario", height=100)
            interpretacion = st.text_area("Interpretación bíblica", height=150)
            fecha_sueno = st.text_input("Fecha", value="Hoy")
            
            if st.form_submit_button("Publicar Interpretación", type="primary", use_container_width=True):
                if sueno and interpretacion:
                    conn.table("suenos").insert({
                        "sueno": sueno, 
                        "interpretacion": interpretacion, 
                        "fecha": fecha_sueno,
                        "estado": "respondido"
                    }).execute()
                    st.success("¡Interpretación publicada!")
                    st.rerun()
                else:
                    st.warning("Completa todos los campos.")

        data = execute_query(conn.table("suenos").select("*").eq("estado", "respondido").order("created_at", desc=True), ttl="0").data
        st.markdown("### Interpretaciones Publicadas")
        if not data:
            st.info("No hay interpretaciones publicadas aún.")
        else:
            for s in data:
                with st.expander(f"Sueño: {s['sueno'][:50]}..."):
                    st.write(f"**Interpretación:** {s['interpretacion']}")
                    if st.button(f"Eliminar", key=f"del_s_{s['id']}"):
                        conn.table("suenos").delete().eq("id", s['id']).execute()
                        st.rerun()


# ============================================
# 8. ENRUTADOR PRINCIPAL
# ============================================
# Lógica para manejar los botones HTML de las pestañas
if "pagina" in st.query_params:
    pagina_solicitada = st.query_params["pagina"]
    if pagina_solicitada != st.session_state.pagina_actual:
        st.session_state.pagina_actual = pagina_solicitada
        st.query_params.clear() # Limpiamos la URL
        st.rerun()

# Enrutador principal
if st.session_state.pagina_actual == 'inicio':
    mostrar_inicio()
elif st.session_state.pagina_actual == 'biblia':
    mostrar_biblia()
elif st.session_state.pagina_actual == 'curiosidades':
    mostrar_curiosidades()
elif st.session_state.pagina_actual == 'pastor':
    mostrar_pastor()
elif st.session_state.pagina_actual == 'suenos':
    mostrar_suenos()
elif st.session_state.pagina_actual == 'reflexiones':
    mostrar_reflexiones()
elif st.session_state.pagina_actual == 'mitos':
    mostrar_mitos()
elif st.session_state.pagina_actual == 'admin':
    mostrar_admin()

import streamlit as st
from streamlit_supabase_auth_ui.widgets import __login__
import requests

# ============================================
# CONFIGURACIÓN
# ============================================
st.set_page_config(
    page_title="Palabra de Vida | App Cristiana",
    page_icon="✝️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================
# ESTILOS PROFESIONALES (CÁLIDO Y ESPIRITUAL)
# ============================================
IMG_URL = "https://images.unsplash.com/photo-1504052434569-70ad5836ab65?q=80&w=2070&auto=format&fit=crop"

st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,400&family=Montserrat:wght@400;500;600&display=swap');

    .stApp {{
        background-image: linear-gradient(rgba(40, 20, 10, 0.65), rgba(20, 10, 5, 0.85)), url("{IMG_URL}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        font-family: 'Montserrat', sans-serif;
    }}

    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}

    h1, h2, h3 {{
        font-family: 'Cormorant Garamond', serif;
        color: #FDFBF7 !important;
    }}
    p, span, div {{
        color: #E6D5C3;
    }}

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
        color: #D4AF37 !important;
        margin-top: 10px;
        font-weight: 500;
        letter-spacing: 2px;
        text-shadow: 1px 1px 4px rgba(0,0,0,0.8);
    }}

    .premium-card {{
        background: rgba(45, 30, 20, 0.55);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(212, 175, 55, 0.25);
        border-radius: 20px;
        padding: 30px;
        margin-bottom: 25px;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.4);
    }}

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
# INICIALIZAR ESTADO DE NAVEGACIÓN
# ============================================
if 'pagina_actual' not in st.session_state:
    st.session_state.pagina_actual = 'inicio'

def cambiar_pagina(nombre_pagina):
    st.session_state.pagina_actual = nombre_pagina
    st.rerun()

# ============================================
# LOGIN
# ============================================
login_obj = __login__(
    auth_token=st.secrets["courier_auth_token"],
    company_name="Palabra de Vida",
    width=250,
    height=300
)
LOGGED_IN = login_obj.build_login_ui()

# ============================================
# FUNCIONES DE LAS PÁGINAS
# ============================================

def mostrar_inicio():
    st.markdown('<h1 class="hero-title">Palabra de Vida</h1>', unsafe_allow_html=True)
    st.markdown('<p class="hero-subtitle">LÁMPARA ES A MIS PIES TU PALABRA</p>', unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)

    col_izq, col_der = st.columns([2.2, 1], gap="large")

    with col_izq:
        st.markdown("""
        <div class="verse-highlight">
            <div class="verse-text">"Porque de tal manera amó Dios al mundo, que ha dado a su Hijo unigénito, para que todo aquel que en él cree, no se pierda, mas tenga vida eterna."</div>
            <span class="verse-ref">Juan 3:16 — Versículo del día</span>
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="section-header">🙏 Oración de la Mañana</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="premium-card">
            <p style="font-size: 1.15rem; line-height: 1.8; margin: 0; font-weight: 400; font-style: italic;">
            Señor, gracias por este nuevo día que me regalas. Guía mis pasos, ilumina mi mente y guarda mi corazón en tu verdad. Que cada palabra que salga de mi boca sea agradable a ti, y que cada acción refleje tu amor. Amén.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown('<div class="section-header">📖 Explora la Palabra</div>', unsafe_allow_html=True)
        
        b1, b2, b3 = st.columns(3)
        with b1:
            if st.button("📖 La Biblia", use_container_width=True):
                cambiar_pagina("biblia")
        with b2:
            if st.button("💭 Reflexiones", use_container_width=True):
                cambiar_pagina("reflexiones")
        with b3:
            if st.button("🔍 Curiosidades", use_container_width=True):
                cambiar_pagina("curiosidades")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        b4, b5, b6 = st.columns(3)
        with b4:
            if st.button("🙋 Pregúntale al Pastor", use_container_width=True):
                cambiar_pagina("pastor")
        with b5:
            if st.button("⚠️ Mitos y Doctrinas", use_container_width=True):
                cambiar_pagina("mitos")
        with b6:
            if st.button("❤️ Favoritos", use_container_width=True):
                cambiar_pagina("favoritos")

    with col_der:
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

        if st.button("☕ Apoyar esta obra", type="primary", use_container_width=True):
            st.info("Redirigiendo a Ko-fi... (Aquí irá tu enlace)")

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("""
        <div style="background: rgba(212, 175, 55, 0.1); border: 1px solid rgba(212, 175, 55, 0.3); border-radius: 12px; padding: 20px; text-align: center; backdrop-filter: blur(5px);">
            <p style="color: #D4AF37; font-size: 0.9rem; margin: 0; font-weight: 600; letter-spacing: 1px;">✅ APP 100% GRATUITA</p>
            <p style="color: #E6D5C3; font-size: 0.8rem; margin-top: 8px;">Mantenida por donaciones</p>
        </div>
        """, unsafe_allow_html=True)

# --- PÁGINA: BIBLIA (Midvash API - RVR1960) ---
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
    # Midvash API con RVR1960
    url = f"https://api.midvash.com/v1/rvr1960/{slug}/{capitulo_sel}"
    
    try:
        with st.spinner("Cargando la Palabra..."):
            respuesta = requests.get(url)
            respuesta.raise_for_status()
            datos = respuesta.json()
            # Midvash devuelve los versículos en data.verses
            versiculos = datos.get("data", {}).get("verses", [])
            
            if not versiculos:
                st.warning("No se encontraron versículos para esta selección.")
            else:
                st.markdown(f'<div class="section-header">📖 {libro_sel} {capitulo_sel}</div>', unsafe_allow_html=True)
                texto_html = ""
                for v in versiculos:
                    num = v.get("verse", "")
                    texto = v.get("text", "")
                    # Forzamos el color negro para que resalte en la tarjeta clara
                    texto_html += f'<p style="margin-bottom: 12px; color: #1A1A1A !important; font-family: \'Montserrat\', sans-serif;"><strong style="color: #D4AF37;">{num}.</strong> {texto}</p>'
                
                st.markdown(f"""
                <div class="premium-card" style="max-height: 600px; overflow-y: auto; background: #FDFBF7;">
                    {texto_html}
                </div>
                """, unsafe_allow_html=True)
    except Exception as e:
        st.error(f"No se pudo cargar el capítulo. Verifica tu conexión o intenta con otro capítulo. (Error: {e})")


# --- OTRAS PÁGINAS (Placeholders) ---
def mostrar_reflexiones():
    if st.button("⬅️ Volver al Inicio"):
        cambiar_pagina("inicio")
    st.markdown('<h1 class="hero-title" style="font-size: 3rem;">💭 Reflexiones</h1>', unsafe_allow_html=True)
    st.markdown('<div class="premium-card"><p>Próximamente: Devocionales diarios.</p></div>', unsafe_allow_html=True)

def mostrar_curiosidades():
    if st.button("⬅️ Volver al Inicio"):
        cambiar_pagina("inicio")
    st.markdown('<h1 class="hero-title" style="font-size: 3rem;">🔍 Curiosidades</h1>', unsafe_allow_html=True)
    st.markdown('<div class="premium-card"><p>Próximamente: Datos históricos y arqueológicos.</p></div>', unsafe_allow_html=True)

def mostrar_pastor():
    if st.button("⬅️ Volver al Inicio"):
        cambiar_pagina("inicio")
    st.markdown('<h1 class="hero-title" style="font-size: 3rem;">🙋 Pregúntale al Pastor</h1>', unsafe_allow_html=True)
    st.markdown('<div class="premium-card"><p>Próximamente: Formulario de contacto.</p></div>', unsafe_allow_html=True)

def mostrar_mitos():
    if st.button("⬅️ Volver al Inicio"):
        cambiar_pagina("inicio")
    st.markdown('<h1 class="hero-title" style="font-size: 3rem;">⚠️ Mitos y Doctrinas</h1>', unsafe_allow_html=True)
    st.markdown('<div class="premium-card"><p>Próximamente: Aclaraciones bíblicas.</p></div>', unsafe_allow_html=True)

def mostrar_favoritos():
    if st.button("⬅️ Volver al Inicio"):
        cambiar_pagina("inicio")
    st.markdown('<h1 class="hero-title" style="font-size: 3rem;">❤️ Favoritos</h1>', unsafe_allow_html=True)
    st.markdown('<div class="premium-card"><p>Próximamente: Tus versículos guardados.</p></div>', unsafe_allow_html=True)


# ============================================
# ENRUTADOR PRINCIPAL
# ============================================
if LOGGED_IN:
    if st.session_state.pagina_actual == 'inicio':
        mostrar_inicio()
    elif st.session_state.pagina_actual == 'biblia':
        mostrar_biblia()
    elif st.session_state.pagina_actual == 'reflexiones':
        mostrar_reflexiones()
    elif st.session_state.pagina_actual == 'curiosidades':
        mostrar_curiosidades()
    elif st.session_state.pagina_actual == 'pastor':
        mostrar_pastor()
    elif st.session_state.pagina_actual == 'mitos':
        mostrar_mitos()
    elif st.session_state.pagina_actual == 'favoritos':
        mostrar_favoritos()

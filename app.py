import streamlit as st
from streamlit_supabase_auth_ui.widgets import __login__
import requests
import random
import urllib.parse

# ============================================
# 1. CONFIGURACIÓN DE PÁGINA (DEBE SER LO PRIMERO)
# ============================================
st.set_page_config(
    page_title="Palabra de Vida | App Cristiana",
    page_icon="✝️",
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
# 3. ESTILOS PROFESIONALES (CONTRASTE INTELIGENTE)
# ============================================
IMG_URL = "https://images.unsplash.com/photo-1504052434569-70ad5836ab65?q=80&w=2070&auto=format&fit=crop"

st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,400&family=Montserrat:wght@400;500;600&display=swap');

    .stApp {{
        background-image: linear-gradient(rgba(40, 20, 10, 0.7), rgba(20, 10, 5, 0.9)), url("{IMG_URL}");
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

    .card-light {{
        background: #FDFBF7 !important;
        border: 1px solid rgba(212, 175, 55, 0.4);
        border-radius: 20px;
        padding: 30px;
        margin-bottom: 25px;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.4);
    }}
    .card-light *, 
    .card-light p, .card-light span, .card-light div, .card-light strong, .card-light li,
    .card-light h1, .card-light h2, .card-light h3, .card-light h4 {{
        color: #1A1A1A !important;
    }}

    .verse-light {{
        background: #FDFBF7 !important;
        border-left: 5px solid #D4AF37;
        border-radius: 16px;
        padding: 40px;
        margin: 20px 0 40px 0;
        box-shadow: 0 10px 25px rgba(0,0,0,0.3);
    }}
    .verse-light * {{
        color: #1A1A1A !important;
    }}
    .verse-light .verse-text {{
        font-family: 'Cormorant Garamond', serif;
        font-size: 1.8rem;
        font-style: italic;
        line-height: 1.5;
        text-align: center;
    }}
    .verse-light .verse-ref {{
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

    .card-dark {{
        background: rgba(30, 20, 15, 0.85) !important;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(212, 175, 55, 0.3);
        border-radius: 20px;
        padding: 30px;
        margin-bottom: 25px;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.5);
    }}
    .card-dark p, .card-dark span, .card-dark div, .card-dark li {{
        color: #FDFBF7 !important;
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
        background: #FDFBF7 !important;
        color: #1A1A1A !important;
        border: 1px solid rgba(212, 175, 55, 0.5);
        border-radius: 12px;
        padding: 18px 20px;
        font-weight: 600;
        font-family: 'Montserrat', sans-serif;
        font-size: 0.95rem;
        transition: all 0.3s ease;
        width: 100%;
        text-align: left;
    }}
    .stButton>button:hover {{
        background: #F3E5AB !important;
        border-color: #D4AF37;
        color: #1A1A1A !important;
        transform: translateY(-3px);
        box-shadow: 0 10px 20px rgba(0,0,0,0.2);
    }}
    .stButton>button p {{
        color: #1A1A1A !important;
        font-size: 0.95rem;
        margin: 0;
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
        color: #1A1A1A !important;
        font-size: 1.05rem;
    }}
    .member-date {{
        font-size: 0.8rem;
        color: #1A1A1A !important;
        background: rgba(212, 175, 55, 0.2);
        padding: 5px 12px;
        border-radius: 20px;
        border: 1px solid rgba(212, 175, 55, 0.4);
    }}

    .stButton>button[kind="primary"] {{
        background: linear-gradient(135deg, #D4AF37 0%, #F3E5AB 100%) !important;
        color: #1A0F0A !important;
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
        color: #1A0F0A !important;
    }}
    
    .stSelectbox label, .stNumberInput label {{
        color: #FDFBF7 !important;
    }}
    .stSelectbox div[data-baseweb="select"] > div,
    .stNumberInput input {{
        background-color: #FDFBF7 !important;
        color: #1A1A1A !important;
        border-radius: 8px;
    }}
    .stSelectbox div[data-baseweb="select"] *,
    .stNumberInput input {{
        color: #1A1A1A !important;
    }}

    details {{
        background: #FDFBF7 !important;
        border: 1px solid rgba(212, 175, 55, 0.5);
        border-radius: 12px;
        padding: 15px 20px;
        margin-bottom: 15px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }}
    summary {{
        font-weight: 600;
        color: #1A1A1A !important;
        font-size: 1.1rem;
        cursor: pointer;
        outline: none;
    }}
    details[open] summary {{
        margin-bottom: 15px;
        border-bottom: 1px solid rgba(212, 175, 55, 0.3);
        padding-bottom: 10px;
    }}
    details p, details strong, details div {{
        color: #1A1A1A !important;
        line-height: 1.6;
    }}
</style>
""", unsafe_allow_html=True)

# ============================================
# 4. INICIALIZAR ESTADO DE NAVEGACIÓN Y DATOS
# ============================================
if 'pagina_actual' not in st.session_state:
    st.session_state.pagina_actual = 'inicio'

if 'respuestas_pastor' not in st.session_state:
    st.session_state.respuestas_pastor = []
if 'reflexiones' not in st.session_state:
    st.session_state.reflexiones = []
if 'curiosidades' not in st.session_state:
    st.session_state.curiosidades = []
if 'mitos' not in st.session_state:
    st.session_state.mitos = []
if 'suenos' not in st.session_state:
    st.session_state.suenos = []
if 'admin_logged' not in st.session_state:
    st.session_state.admin_logged = False

def cambiar_pagina(nombre_pagina):
    st.session_state.pagina_actual = nombre_pagina
    st.rerun()

# ============================================
# 5. LOGIN
# ============================================
login_obj = __login__(
    auth_token=st.secrets["courier_auth_token"],
    company_name="Palabra de Vida",
    width=250,
    height=300
)
LOGGED_IN = login_obj.build_login_ui()

# ============================================
# 6. LÓGICA DE MÚSICA POR URL (EN BARRA LATERAL)
# ============================================
URLS_CANCIONES = [
    "https://TU_ENLACE_1.mp3",
    "https://TU_ENLACE_2.mp3",
]

if LOGGED_IN:
    if 'canciones_url' not in st.session_state:
        canciones = URLS_CANCIONES.copy()
        random.shuffle(canciones)
        st.session_state.canciones_url = canciones
        st.session_state.indice_url = 0

    with st.sidebar:
        st.markdown("### 🎵 Música Cristiana")
        st.markdown("---")
        if st.session_state.canciones_url:
            url_actual = st.session_state.canciones_url[st.session_state.indice_url]
            st.audio(url_actual, format="audio/mpeg")
            if st.button("⏭️ Siguiente Canción", use_container_width=True):
                st.session_state.indice_url = (st.session_state.indice_url + 1) % len(st.session_state.canciones_url)
                st.rerun()
            st.caption(f"Canción {st.session_state.indice_url + 1} de {len(st.session_state.canciones_url)}")
        else:
            st.info("No hay canciones configuradas.")
        
        st.markdown("---")
        st.markdown("### 🔐 Acceso Administrador")
        if not st.session_state.admin_logged:
            pass_admin = st.text_input("Contraseña", type="password", key="pass_admin_input")
            if st.button("Entrar como Admin", use_container_width=True):
                if pass_admin == "Willian2026": # Cambia esta contraseña
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
# 7. FUNCIONES DE LAS PÁGINAS
# ============================================

def mostrar_inicio():
    st.markdown('<h1 class="hero-title">Palabra de Vida</h1>', unsafe_allow_html=True)
    st.markdown('<p class="hero-subtitle">LÁMPARA ES A MIS PIES TU PALABRA</p>', unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)

    col_izq, col_der = st.columns([2.2, 1], gap="large")

    with col_izq:
        st.markdown("""
        <div class="verse-light">
            <div class="verse-text">"Porque de tal manera amó Dios al mundo, que ha dado a su Hijo unigénito, para que todo aquel que en él cree, no se pierda, mas tenga vida eterna."</div>
            <span class="verse-ref">Juan 3:16 — Versículo del día</span>
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="section-header">🙏 Oración de la Mañana</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="card-light">
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
            if st.button("💭 Tus sueños significan algo", use_container_width=True):
                cambiar_pagina("suenos")

    with col_der:
        st.markdown('<div class="section-header">🤝 Muro de Miembros</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="card-light" style="padding: 25px;">
            <p style="font-size: 0.9rem; margin-bottom: 15px; font-style: italic;">
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

        st.markdown('<div class="section-header">☕ Apoyar la Obra</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="card-light" style="padding: 20px; margin-bottom: 15px;">
            <p style="font-size: 0.85rem; line-height: 1.6; margin-bottom: 15px;">
                <strong>Aclaración importante:</strong> Esta contribución no es un diezmo ni una ofrenda mensual. Es un aporte voluntario y único, destinado a seguir creciendo en el trabajo del Señor. Tu generosidad nos permite mantener esta herramienta gratuita para todos.
            </p>
            <a href="https://ko-fi.com/TU_USUARIO" target="_blank" style="text-decoration: none;">
                <div style="background: linear-gradient(135deg, #D4AF37 0%, #F3E5AB 100%); color: #1A0F0A; text-align: center; padding: 15px; border-radius: 12px; font-weight: 700; font-size: 1rem; box-shadow: 0 10px 25px -5px rgba(212, 175, 55, 0.6); cursor: pointer;">
                    Realizar Contribución Única
                </div>
            </a>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("""
        <div class="card-dark" style="padding: 25px; text-align: center;">
            <p style="color: #D4AF37 !important; font-size: 1rem; margin: 0; font-weight: 600; letter-spacing: 1px;">✅ APP 100% GRATUITA</p>
            <p style="font-size: 0.85rem; margin-top: 8px; margin-bottom: 15px;">Mantenida por donaciones</p>
            <hr style="border-color: rgba(212, 175, 55, 0.3); margin: 15px 0;">
            <p style="font-size: 0.8rem; margin: 0; color: #FDFBF7 !important;">Esta app fue creada por <strong>Willian Almenar</strong>.</p>
            <p style="font-size: 0.75rem; margin: 5px 0 0 0; color: #B0A090 !important;">Todos los derechos reservados. Octubre 2026.</p>
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
                    texto_html += f'<p><strong style="color: #D4AF37 !important;">{i}.</strong> {texto}</p>'
                
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
            
            submitted = st.form_submit_button("Enviar Pregunta por WhatsApp", type="primary", use_container_width=True)
            
            if submitted:
                if not pregunta.strip():
                    st.warning("Por favor, escribe una pregunta antes de enviar.")
                else:
                    mensaje = f"Hola Pastor, mi nombre es {nombre if nombre else 'un hermano/a'}. Tengo una pregunta: {pregunta}"
                    mensaje_codificado = urllib.parse.quote(mensaje)
                    numero_whatsapp = "584242004015"
                    url_whatsapp = f"https://wa.me/{numero_whatsapp}?text={mensaje_codificado}"
                    
                    st.success("¡Pregunta lista! Haz clic en el botón de abajo para enviarla por WhatsApp.")
                    st.markdown(f"""
                    <a href="{url_whatsapp}" target="_blank" style="text-decoration: none;">
                        <div style="background: #25D366; color: white; text-align: center; padding: 15px; border-radius: 12px; font-weight: 700; font-size: 1.1rem; margin-top: 15px; box-shadow: 0 4px 15px rgba(37, 211, 102, 0.4); cursor: pointer;">
                            📲 Abrir WhatsApp y Enviar
                        </div>
                    </a>
                    """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown('<div class="section-header">💬 Respuestas del Pastor</div>', unsafe_allow_html=True)
    
    res = execute_query(conn.table("respuestas_pastor").select("*").order("created_at", desc=True), ttl="1m")
    data_pastor = res.data
    
    if not data_pastor:
        st.info("Aún no hay respuestas publicadas. ¡Vuelve pronto!")
    else:
        for r in data_pastor:
            st.markdown(f"""
            <div class="card-light" style="margin-bottom: 15px;">
                <p style="font-weight: 600; color: #D4AF37 !important; margin-bottom: 5px;">Pregunta: {r['pregunta']}</p>
                <p style="font-size: 0.9rem; color: #666 !important; margin-bottom: 10px;">{r.get('fecha', '')}</p>
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
                    st.success("¡Sueño recibido! El pastor lo revisará y publicará una respuesta pronto.")

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown('<div class="section-header">💬 Interpretaciones publicadas</div>', unsafe_allow_html=True)
    
    res = execute_query(conn.table("suenos").select("*").order("created_at", desc=True), ttl="1m")
    data_suenos = res.data
    
    if not data_suenos:
        st.info("Aún no hay interpretaciones publicadas. ¡Vuelve pronto!")
    else:
        for s in data_suenos:
            st.markdown(f"""
            <div class="card-light" style="margin-bottom: 15px;">
                <p style="font-weight: 600; color: #D4AF37 !important; margin-bottom: 5px;">Sueño: {s['sueno']}</p>
                <p style="font-size: 0.9rem; color: #666 !important; margin-bottom: 10px;">{s.get('fecha', '')}</p>
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
            <div class="card-light" style="margin-bottom: 15px;">
                <h3 style="color: #D4AF37 !important;">{r['titulo']}</h3>
                <p>{r['contenido']}</p>
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
            <div class="card-light" style="margin-bottom: 15px;">
                <h3 style="color: #D4AF37 !important;">{m['titulo']}</h3>
                <p>{m['explicacion']}</p>
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
        st.markdown("### Agregar Respuesta")
        with st.form("admin_pastor"):
            pregunta = st.text_area("Pregunta del usuario", height=80)
            respuesta = st.text_area("Tu respuesta", height=150)
            fecha = st.text_input("Fecha", value="Hoy")
            
            if st.form_submit_button("Publicar Respuesta", type="primary", use_container_width=True):
                if pregunta and respuesta:
                    conn.table("respuestas_pastor").insert({"pregunta": pregunta, "respuesta": respuesta, "fecha": fecha}).execute()
                    st.success("¡Respuesta publicada!")
                    st.rerun()
                else:
                    st.warning("Completa todos los campos.")

        data = execute_query(conn.table("respuestas_pastor").select("*").order("created_at", desc=True), ttl="0").data
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
        st.markdown("### Agregar Interpretación de Sueño")
        with st.form("admin_sueno"):
            sueno = st.text_area("Sueño del usuario", height=100)
            interpretacion = st.text_area("Interpretación bíblica", height=150)
            fecha_sueno = st.text_input("Fecha", value="Hoy")
            
            if st.form_submit_button("Publicar Interpretación", type="primary", use_container_width=True):
                if sueno and interpretacion:
                    conn.table("suenos").insert({"sueno": sueno, "interpretacion": interpretacion, "fecha": fecha_sueno}).execute()
                    st.success("¡Interpretación publicada!")
                    st.rerun()
                else:
                    st.warning("Completa todos los campos.")

        data = execute_query(conn.table("suenos").select("*").order("created_at", desc=True), ttl="0").data
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
if LOGGED_IN:
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

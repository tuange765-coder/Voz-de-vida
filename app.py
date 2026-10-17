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
# ESTILOS PROFESIONALES (CONTRASTE INTELIGENTE FORZADO)
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
            if st.button("❤️ Favoritos", use_container_width=True):
                cambiar_pagina("favoritos")

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
        # SECCIÓN DE CRÉDITOS ACTUALIZADA
        st.markdown("""
        <div class="card-dark" style="padding: 25px; text-align: center;">
            <p style="color: #D4AF37 !important; font-size: 1rem; margin: 0; font-weight: 600; letter-spacing: 1px;">✅ APP 100% GRATUITA</p>
            <p style="font-size: 0.85rem; margin-top: 8px; margin-bottom: 15px;">Mantenida por donaciones</p>
            <hr style="border-color: rgba(212, 175, 55, 0.3); margin: 15px 0;">
            <p style="font-size: 0.8rem; margin: 0; color: #FDFBF7 !important;">Esta app fue creada por <strong>Willian Almenar</strong>.</p>
            <p style="font-size: 0.75rem; margin: 5px 0 0 0; color: #B0A090 !important;">Todos los derechos reservados. Octubre 2026.</p>
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


# --- PÁGINA: CURIOSIDADES (Pestañas HTML Desplegables) ---
def mostrar_curiosidades():
    if st.button("⬅️ Volver al Inicio"):
        cambiar_pagina("inicio")
    
    st.markdown('<h1 class="hero-title" style="font-size: 3rem;">🔍 Curiosidades Bíblicas</h1>', unsafe_allow_html=True)
    st.markdown('<p class="hero-subtitle">Datos históricos y arqueológicos que confirman las Escrituras</p>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    curiosidades = [
        {
            "titulo": "📜 La Estela de Merneptah (Primera mención de Israel)",
            "que_es": "Una losa de granito negro descubierta en 1896 en Tebas, Egipto. Data aproximadamente del 1205 a.C.",
            "importancia": "Contiene la primera mención conocida de 'Israel' fuera de la Biblia. El faraón Merneptah se jacta de haber derrotado a Israel, lo que confirma que el pueblo ya estaba establecido en Canaán en esa época.",
            "referencia": "Éxodo y Josué (la conquista de la Tierra Prometida)."
        },
        {
            "titulo": "🏺 El Cilindro de Ciro (El decreto de repatriación)",
            "que_es": "Un cilindro de arcilla con inscripciones en acadio, encontrado en Sippar, cerca de Bagdad (Irak).",
            "importancia": "Documenta la conquista de Babilonia por Ciro el Grande y su política de permitir a los pueblos deportados regresar a sus tierras. Esto coincide exactamente con el relato bíblico del decreto que permitió a los judíos volver a Jerusalén.",
            "referencia": "Esdras 1:1-4; Isaías 44:28–45:1."
        },
        {
            "titulo": "📜 Los Rollos del Mar Muerto (Los manuscritos más antiguos)",
            "que_es": "Miles de fragmentos de manuscritos descubiertos en cuevas cerca de Qumrán, a orillas del Mar Muerto, a partir de 1947.",
            "importancia": "Son los manuscritos bíblicos más antiguos conocidos (copiados entre el siglo III a.C. y el siglo I d.C.). Incluyen fragmentos de casi todos los libros del Antiguo Testamento y demuestran la fidelidad con la que el texto bíblico fue transmitido durante más de mil años.",
            "referencia": "Dato curioso: El fragmento más antiguo de Génesis 1:1 fue encontrado entre estos rollos."
        },
        {
            "titulo": "💧 El Túnel de Ezequías (Piscina de Siloé)",
            "que_es": "Un túnel de 533 metros excavado en roca sólida bajo Jerusalén hace más de 2.700 años.",
            "importancia": "Fue construido por el rey Ezequías para asegurar el suministro de agua de la ciudad ante el asedio asirio. La Inscripción de Siloé, encontrada dentro, describe cómo dos equipos de excavadores se encontraron en el medio. Esto confirma el relato bíblico de los preparativos de Ezequías.",
            "referencia": "2 Reyes 20:20; 2 Crónicas 32:30."
        },
        {
            "titulo": "👑 La Estela de Tel Dan (La Casa de David)",
            "que_es": "Fragmentos de una estela de basalto encontrados en el norte de Israel en 1993 y 1994.",
            "importancia": "Contiene la frase 'Casa de David' (Beit David), escrita por un rey arameo en el siglo IX a.C. Es la primera evidencia arqueológica directa de la existencia de la dinastía del rey David, fuera de la Biblia.",
            "referencia": "1 Samuel 16–2 Samuel 5."
        },
        {
            "titulo": "🗿 La Estela de Mesa (Piedra Moabita)",
            "que_es": "Una losa de basalto negro de 1,15 m de altura, descubierta en 1868 en Jordania. Se conserva en el Museo del Louvre.",
            "importancia": "El rey Mesa de Moab narra su rebelión contra Israel, coincidiendo con el relato bíblico de 2 Reyes 3. Menciona el nombre de Yahvé y la 'Casa de David', confirmando detalles históricos sobre la ocupación israelita de Moab.",
            "referencia": "2 Reyes 1:1; 3:4-27."
        },
        {
            "titulo": "🏛️ Las Tablillas de Ebla (El mundo de los patriarcas)",
            "que_es": "Miles de tablillas de arcilla con escritura cuneiforme encontradas en la antigua ciudad de Ebla, Siria, en la década de 1970.",
            "importancia": "Contienen nombres y costumbres que se mencionan en Génesis (como las ciudades de Ur y Sodoma), demostrando que el mundo patriarcal descrito en la Biblia era históricamente real y no una invención posterior.",
            "referencia": "Génesis 11–50."
        },
        {
            "titulo": "🏺 El Rey Belsasar (Daniel 5)",
            "que_es": "Durante mucho tiempo, los críticos negaron la existencia de Belsasar porque no aparecía en fuentes fuera de la Biblia.",
            "importancia": "Hallazgos posteriores en tablillas babilónicas demostraron que Belsasar era el hijo de Nabonido y corregente de Babilonia, exactamente como lo describe Daniel 5. Esto explica por qué Daniel fue ofrecido como 'tercer gobernante' del reino.",
            "referencia": "Daniel 5:16, 29-31."
        },
        {
            "titulo": "📜 Las Cartas de Lachis (La caída de Judá)",
            "que_es": "Fragmentos de cerámica (ostraca) con inscripciones en hebreo antiguo, encontrados en las ruinas de Lachis, una ciudad fortificada de Judá.",
            "importancia": "Son una correspondencia militar de la época del profeta Jeremías. En una de ellas se lee: 'No podemos ver las señales de Azeca', lo que coincide con el avance de Nabucodonosor descrito en Jeremías 34:7.",
            "referencia": "Jeremías 34:7."
        },
        {
            "titulo": "🏛️ El Sello del Rey Ezequías",
            "que_es": "Una impresión de arcilla (bula) de solo 1 cm de diámetro, encontrada en 2015 en Jerusalén.",
            "importancia": "Lleva la inscripción: 'Perteneciente a Ezequías, hijo de Acaz, rey de Judá', con un símbolo solar con alas. Es prueba física del reinado de uno de los reyes más importantes del Antiguo Testamento.",
            "referencia": "2 Reyes 18-20; Isaías 36-39."
        },
        {
            "titulo": "🏺 Los Heteos (Un pueblo que se creía legendario)",
            "que_es": "Los hititas son mencionados en varios libros del Antiguo Testamento, pero los críticos los consideraban una 'leyenda bíblica'.",
            "importancia": "Los arqueólogos encontraron la capital hitita en Bogazkoy, Turquía, repleta de registros de su pueblo. Esto confirmó que los hititas fueron una civilización real y poderosa, tal como la Biblia los describe.",
            "referencia": "Génesis 23; 2 Samuel 11; 1 Reyes 10."
        },
        {
            "titulo": "🌿 El Jardín bajo el Santo Sepulcro (Descubrimiento 2025)",
            "que_es": "Excavaciones recientes bajo la Basílica del Santo Sepulcro en Jerusalén han revelado un antiguo jardín con restos de trigo, uvas e higos.",
            "importancia": "El Evangelio de Juan dice que Jesús fue crucificado y sepultado en un huerto. Los análisis arqueobotánicos confirman la existencia de un área cultivada entre el Calvario y la tumba, coincidiendo con el relato bíblico.",
            "referencia": "Juan 19:41-42."
        },
        {
            "titulo": "🏛️ La Inscripción de Poncio Pilato",
            "que_es": "Una piedra caliza con una inscripción en latín, encontrada en Cesarea Marítima en 1961.",
            "importancia": "Contiene el nombre de 'Poncio Pilato, prefecto de Judea'. Es la única evidencia arqueológica directa de la existencia del gobernador romano que condenó a Jesús.",
            "referencia": "Mateo 27; Marcos 15; Lucas 23; Juan 18-19."
        },
        {
            "titulo": "🦴 El Osario de Caifás",
            "que_es": "Un osario de piedra caliza con la inscripción 'José, hijo de Caifás', encontrado en Jerusalén en 1990.",
            "importancia": "Es la primera evidencia arqueológica del sumo sacerdote Caifás, quien presidió el juicio contra Jesús.",
            "referencia": "Mateo 26:57; Juan 18:13."
        },
        {
            "titulo": "📜 El Papiro 52 (El fragmento más antiguo del Nuevo Testamento)",
            "que_es": "Un pequeño fragmento de papiro del Evangelio de Juan, datado alrededor del año 125 d.C.",
            "importancia": "Es el fragmento más antiguo conocido del Nuevo Testamento. Contiene partes de Juan 18:31-33 y 37-38.",
            "referencia": "Juan 18."
        }
    ]

    html_expanders = ""
    for c in curiosidades:
        html_expanders += f"""
        <details>
            <summary>{c['titulo']}</summary>
            <div>
                <p><strong>¿Qué es?</strong> {c['que_es']}</p>
                <p><strong>¿Por qué es importante?</strong> {c['importancia']}</p>
                <p><strong>Referencia bíblica:</strong> {c['referencia']}</p>
            </div>
        </details>
        """
    
    st.markdown(html_expanders, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="section-header">💡 Sabías que...</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card-dark">
        <p>La arqueología no prueba la fe, pero sí <strong>ilumina y confirma</strong> el contexto histórico de las Escrituras. Como dijo el arqueólogo Joseph Free: "La arqueología ha confirmado incontables pasajes que los críticos habían rechazado como no históricos".</p>
    </div>
    """, unsafe_allow_html=True)


# --- OTRAS PÁGINAS (Placeholders) ---
def mostrar_reflexiones():
    if st.button("⬅️ Volver al Inicio"):
        cambiar_pagina("inicio")
    st.markdown('<h1 class="hero-title" style="font-size: 3rem;">💭 Reflexiones</h1>', unsafe_allow_html=True)
    st.markdown('<div class="card-light"><p>Próximamente: Devocionales diarios.</p></div>', unsafe_allow_html=True)

def mostrar_pastor():
    if st.button("⬅️ Volver al Inicio"):
        cambiar_pagina("inicio")
    st.markdown('<h1 class="hero-title" style="font-size: 3rem;">🙋 Pregúntale al Pastor</h1>', unsafe_allow_html=True)
    st.markdown('<div class="card-light"><p>Próximamente: Formulario de contacto.</p></div>', unsafe_allow_html=True)

def mostrar_mitos():
    if st.button("⬅️ Volver al Inicio"):
        cambiar_pagina("inicio")
    st.markdown('<h1 class="hero-title" style="font-size: 3rem;">⚠️ Mitos y Doctrinas</h1>', unsafe_allow_html=True)
    st.markdown('<div class="card-light"><p>Próximamente: Aclaraciones bíblicas.</p></div>', unsafe_allow_html=True)

def mostrar_favoritos():
    if st.button("⬅️ Volver al Inicio"):
        cambiar_pagina("inicio")
    st.markdown('<h1 class="hero-title" style="font-size: 3rem;">❤️ Favoritos</h1>', unsafe_allow_html=True)
    st.markdown('<div class="card-light"><p>Próximamente: Tus versículos guardados.</p></div>', unsafe_allow_html=True)


# ============================================
# ENRUTADOR PRINCIPAL
# ============================================
if LOGGED_IN:
    if st.session_state.pagina_actual == 'inicio':
        mostrar_inicio()
    elif st.session_state.pagina_actual == 'biblia':
        mostrar_biblia()
    elif st.session_state.pagina_actual == 'curiosidades':
        mostrar_curiosidades()
    elif st.session_state.pagina_actual == 'reflexiones':
        mostrar_reflexiones()
    elif st.session_state.pagina_actual == 'pastor':
        mostrar_pastor()
    elif st.session_state.pagina_actual == 'mitos':
        mostrar_mitos()
    elif st.session_state.pagina_actual == 'favoritos':
        mostrar_favoritos()

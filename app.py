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
# ESTILOS PROFESIONALES (CONTRASTE INTELIGENTE)
# ============================================
IMG_URL = "https://images.unsplash.com/photo-1504052434569-70ad5836ab65?q=80&w=2070&auto=format&fit=crop"

st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,400&family=Montserrat:wght@400;500;600&display=swap');

    /* Fondo general */
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

    /* Títulos principales (siempre blancos porque van sobre la imagen) */
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
        color: #D4AF37 !important; /* Dorado */
        margin-top: 10px;
        font-weight: 500;
        letter-spacing: 2px;
        text-shadow: 1px 1px 4px rgba(0,0,0,0.8);
    }}

    /* ==========================================
       TARJETAS CLARAS (Fondo claro, texto negro)
       ========================================== */
    .card-light {{
        background: #FDFBF7 !important;
        border: 1px solid rgba(212, 175, 55, 0.4);
        border-radius: 20px;
        padding: 30px;
        margin-bottom: 25px;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.4);
    }}
    /* Forzar texto negro dentro de tarjetas claras */
    .card-light p, .card-light span, .card-light div, .card-light strong, .card-light li {{
        color: #1A1A1A !important;
    }}

    /* Tarjeta especial para el versículo del inicio */
    .verse-light {{
        background: #FDFBF7 !important;
        border-left: 5px solid #D4AF37;
        border-radius: 16px;
        padding: 40px;
        margin: 20px 0 40px 0;
        box-shadow: 0 10px 25px rgba(0,0,0,0.3);
    }}
    .verse-light .verse-text {{
        font-family: 'Cormorant Garamond', serif;
        font-size: 1.8rem;
        font-style: italic;
        line-height: 1.5;
        color: #1A1A1A !important; /* Texto negro */
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

    /* ==========================================
       TARJETAS OSCURAS (Fondo oscuro, texto blanco)
       ========================================== */
    .card-dark {{
        background: rgba(30, 20, 15, 0.85) !important;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(212, 175, 55, 0.3);
        border-radius: 20px;
        padding: 30px;
        margin-bottom: 25px;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.5);
    }}
    /* Forzar texto blanco dentro de tarjetas oscuras */
    .card-dark p, .card-dark span, .card-dark div, .card-dark li {{
        color: #FDFBF7 !important;
    }}

    /* Títulos de sección */
    .section-header {{
        font-size: 1.4rem;
        font-weight: 600;
        color: #FDFBF7 !important; /* Blanco sobre el fondo */
        margin-bottom: 20px;
        display: flex;
        align-items: center;
        gap: 12px;
        text-shadow: 1px 1px 4px rgba(0,0,0,0.7);
    }}

    /* Botones del menú principal */
    .stButton>button {{
        background: #FDFBF7 !important; /* Fondo claro */
        color: #1A1A1A !important; /* Texto negro */
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

    /* Muro de miembros (dentro de tarjeta clara) */
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

    /* Botón de donación */
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
    
    /* Estilo para listas dentro de tarjetas */
    .card-light ul, .card-dark ul {{
        margin-top: 10px;
        padding-left: 20px;
    }}
    .card-light li, .card-dark li {{
        margin-bottom: 10px;
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
        # Versículo del día (Tarjeta Clara)
        st.markdown("""
        <div class="verse-light">
            <div class="verse-text">"Porque de tal manera amó Dios al mundo, que ha dado a su Hijo unigénito, para que todo aquel que en él cree, no se pierda, mas tenga vida eterna."</div>
            <span class="verse-ref">Juan 3:16 — Versículo del día</span>
        </div>
        """, unsafe_allow_html=True)

        # Oración (Tarjeta Clara)
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
        # Muro de miembros (Tarjeta Clara)
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

        if st.button("☕ Apoyar esta obra", type="primary", use_container_width=True):
            st.info("Redirigiendo a Ko-fi... (Aquí irá tu enlace)")

        st.markdown("<br>", unsafe_allow_html=True)
        # Mensaje final (Tarjeta Oscura para contraste)
        st.markdown("""
        <div class="card-dark" style="padding: 20px; text-align: center;">
            <p style="color: #D4AF37 !important; font-size: 0.9rem; margin: 0; font-weight: 600; letter-spacing: 1px;">✅ APP 100% GRATUITA</p>
            <p style="font-size: 0.8rem; margin-top: 8px;">Mantenida por donaciones</p>
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
                
                # Usamos la tarjeta clara para la Biblia
                st.markdown(f"""
                <div class="card-light" style="max-height: 600px; overflow-y: auto;">
                    {texto_html}
                </div>
                """, unsafe_allow_html=True)
    except Exception as e:
        st.error(f"No se pudo cargar el capítulo. Verifica tu conexión o intenta con otro capítulo. (Error: {e})")


# --- PÁGINA: CURIOSIDADES (Datos Históricos y Arqueológicos) ---
def mostrar_curiosidades():
    if st.button("⬅️ Volver al Inicio"):
        cambiar_pagina("inicio")
    
    st.markdown('<h1 class="hero-title" style="font-size: 3rem;">🔍 Curiosidades Bíblicas</h1>', unsafe_allow_html=True)
    st.markdown('<p class="hero-subtitle">Datos históricos y arqueológicos que confirman las Escrituras</p>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    # 1. Estela de Merneptah
    st.markdown("""
    <div class="card-light">
        <h3 style="font-family: 'Cormorant Garamond', serif; font-size: 1.6rem; color: #1A1A1A !important; margin-bottom: 10px;">📜 La Estela de Merneptah</h3>
        <p><strong>¿Qué es?</strong> Una losa de granito negro descubierta en 1896 en Tebas, Egipto.</p>
        <p><strong>¿Por qué es importante?</strong> Contiene la <strong>primera mención conocida de "Israel"</strong> fuera de la Biblia. El faraón Merneptah (c. 1209 a.C.) se jacta de haber derrotado a Israel, lo que confirma que el pueblo ya estaba establecido en Canaán en esa época.</p>
        <p><strong>Referencia bíblica:</strong> Éxodo y Josué (la conquista de la Tierra Prometida).</p>
    </div>
    """, unsafe_allow_html=True)

    # 2. Cilindro de Ciro
    st.markdown("""
    <div class="card-light">
        <h3 style="font-family: 'Cormorant Garamond', serif; font-size: 1.6rem; color: #1A1A1A !important; margin-bottom: 10px;">🏺 El Cilindro de Ciro</h3>
        <p><strong>¿Qué es?</strong> Un cilindro de arcilla con inscripciones en acadio, encontrado en Babilonia (actual Irak).</p>
        <p><strong>¿Por qué es importante?</strong> Documenta la conquista de Babilonia por Ciro el Grande y su política de <strong>permitir a los pueblos deportados regresar a sus tierras</strong>. Esto coincide exactamente con el relato bíblico del decreto que permitió a los judíos volver a Jerusalén.</p>
        <p><strong>Referencia bíblica:</strong> Esdras 1:1-4; Isaías 44:28–45:1.</p>
    </div>
    """, unsafe_allow_html=True)

    # 3. Rollos del Mar Muerto
    st.markdown("""
    <div class="card-light">
        <h3 style="font-family: 'Cormorant Garamond', serif; font-size: 1.6rem; color: #1A1A1A !important; margin-bottom: 10px;">📜 Los Rollos del Mar Muerto</h3>
        <p><strong>¿Qué son?</strong> Miles de fragmentos de manuscritos descubiertos en cuevas cerca de Qumrán, a orillas del Mar Muerto, a partir de 1947.</p>
        <p><strong>¿Por qué son importantes?</strong> Son los <strong>manuscritos bíblicos más antiguos conocidos</strong> (copiados entre el siglo III a.C. y el siglo I d.C.). Incluyen fragmentos de casi todos los libros del Antiguo Testamento y demuestran la fidelidad con la que el texto bíblico fue transmitido durante más de mil años.</p>
        <p><strong>Dato curioso:</strong> El fragmento más antiguo de Génesis 1:1 fue encontrado entre estos rollos.</p>
    </div>
    """, unsafe_allow_html=True)

    # 4. El Túnel de Ezequías (o Siloé)
    st.markdown("""
    <div class="card-light">
        <h3 style="font-family: 'Cormorant Garamond', serif; font-size: 1.6rem; color: #1A1A1A !important; margin-bottom: 10px;">💧 El Túnel de Ezequías</h3>
        <p><strong>¿Qué es?</strong> Un túnel de 533 metros excavado en roca sólida bajo Jerusalén.</p>
        <p><strong>¿Por qué es importante?</strong> Fue construido por el rey Ezequías para asegurar el suministro de agua de la ciudad ante el asedio asirio. Una inscripción antigua (la Inscripción de Siloé) describe cómo dos equipos de excavadores se encontraron en el medio. Esto confirma el relato bíblico de los preparativos de Ezequías.</p>
        <p><strong>Referencia bíblica:</strong> 2 Reyes 20:20; 2 Crónicas 32:30.</p>
    </div>
    """, unsafe_allow_html=True)

    # 5. La Casa de David (Estela de Tel Dan)
    st.markdown("""
    <div class="card-light">
        <h3 style="font-family: 'Cormorant Garamond', serif; font-size: 1.6rem; color: #1A1A1A !important; margin-bottom: 10px;">👑 La Estela de Tel Dan</h3>
        <p><strong>¿Qué es?</strong> Fragmentos de una estela de basalto encontrados en el norte de Israel en 1993 y 1994.</p>
        <p><strong>¿Por qué es importante?</strong> Contiene la frase <strong>"Casa de David"</strong> (Beit David), escrita por un rey arameo en el siglo IX a.C. Es la primera evidencia arqueológica directa de la existencia de la dinastía del rey David, fuera de la Biblia.</p>
        <p><strong>Referencia bíblica:</strong> 1 Samuel 16–2 Samuel 5.</p>
    </div>
    """, unsafe_allow_html=True)
    
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

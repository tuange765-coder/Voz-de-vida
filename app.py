import streamlit as st
from supabase import create_client
import streamlit_supabase_auth_ui.utils as sb_utils
from streamlit_supabase_auth_ui.widgets import __login__

# ============================================================
# 1. PARCHE PARA EL ERROR 42501 (MANTENIDO)
# ============================================================
def _register_new_usr_patched(name, email, username, password):
    """Versión parcheada que evita el RETURNING * problemático."""
    url = st.secrets["supa_url"]
    key = st.secrets["supa_key"]
    supabase = create_client(url, key)
    
    new_usr_data = {
        "name": name,
        "email": email,
        "username": username,
        "password": password,
    }
    
    supabase.table("user_authentication").insert(
        new_usr_data, returning="minimal"
    ).execute()

sb_utils.register_new_usr = _register_new_usr_patched
# ============================================================


# ============================================================
# 2. CONFIGURACIÓN DE LA PÁGINA
# ============================================================
st.set_page_config(
    page_title="Voz de Vida - Auditoría Epidemiológica",
    page_icon="🩺",
    layout="wide"
)


# ============================================================
# 3. INICIALIZAR LOGIN
# ============================================================
# Usamos las mismas variables que tienes en tu secrets.toml
SUPABASE_URL = st.secrets["supa_url"]
SUPABASE_KEY = st.secrets["supa_key"]

login_obj = __login__(
    auth_token=SUPABASE_KEY,
    company_name="Voz de Vida",
    width=400,
    height=400,
)

LOGGED_IN = login_obj.build_login_ui()


# ============================================================
# 4. CONTENIDO DE LA APP
# ============================================================
if LOGGED_IN:
    st.success("✅ Has iniciado sesión correctamente.")
    st.title("🩺 Generador de Prompts de Auditoría Epidemiológica")
    
    st.markdown("Ingrese los datos de cada informe en las pestañas correspondientes.")
    
    # --- Pestañas de entrada ---
    tab1, tab2, tab3, tab4 = st.tabs([
        "📄 SISPRO",
        "📅 EPI-12 (Semanal)",
        "📆 EPI-14 / EPI-15 (Mensual)",
        "🖼️ Nota de Imágenes"
    ])
    
    with tab1:
        datos_sispro = st.text_area(
            "Datos del reporte SISPRO:",
            height=200,
            placeholder="Pega aquí el texto o la referencia a la imagen del SISPRO..."
        )
    
    with tab2:
        datos_epi12 = st.text_area(
            "Datos del reporte EPI-12 (semanal):",
            height=200,
            placeholder="Pega aquí el texto o la referencia a la imagen del EPI-12..."
        )
    
    with tab3:
        datos_epi15 = st.text_area(
            "Datos del reporte EPI-14 / EPI-15 (mensual):",
            height=200,
            placeholder="Pega aquí el texto o la referencia a la imagen del EPI-14/15..."
        )
    
    with tab4:
        nota_imagenes = st.text_area(
            "Descripción de las imágenes adjuntas:",
            height=200,
            placeholder="Ej: Foto 1 = EPI-12 semanal, Foto 2 = SISPRO mensual..."
        )
    
    
    # --- Lógica de generación del prompt ---
    def generar_prompt_auditoria(datos_sispro="", datos_epi12="", datos_epi15_epi14="", nota_imagenes=""):
        if not any([datos_sispro, datos_epi12, datos_epi15_epi14, nota_imagenes]):
            return None
    
        secciones = []
        if nota_imagenes.strip():
            secciones.append("[NOTAS / INSTRUCCIONES DE IMÁGENES ADJUNTAS]\n" + nota_imagenes.strip())
        if datos_sispro.strip():
            secciones.append("[REPORTE SISPRO]\n" + datos_sispro.strip())
        if datos_epi12.strip():
            secciones.append("[REPORTE EPI-12 (SEMANAL)]\n" + datos_epi12.strip())
        if datos_epi15_epi14.strip():
            secciones.append("[REPORTE EPI-14 / EPI-15 (MENSUAL)]\n" + datos_epi15_epi14.strip())
    
        bloque_datos = "\n\n".join(secciones)
    
        prompt_base = (
            "Actúa como un experto auditor de estadísticas de salud pública y "
            "analista de datos epidemiológicos. Tu objetivo es procesar, auditar y "
            "cruzar los datos de los formatos oficiales que te proporcionaré a "
            "continuación (SISPRO, Epi-12 y Epi-14 / Epi-15)...\n\n"
            "==================================================\n"
            "DATOS E IMÁGENES INGRESADAS PARA AUDITORÍA\n"
            "==================================================\n\n"
        )
        return prompt_base + bloque_datos
    
    
    # --- Botón y salida ---
    col1, col2 = st.columns([1, 3])
    
    with col1:
        generar = st.button("⚡ Generar Prompt", type="primary", use_container_width=True)
    
    with col2:
        if generar:
            resultado = generar_prompt_auditoria(
                datos_sispro=datos_sispro,
                datos_epi12=datos_epi12,
                datos_epi15_epi14=datos_epi15,
                nota_imagenes=nota_imagenes
            )
    
            if resultado is None:
                st.warning("⚠️ Debes ingresar al menos un dato o nota de imagen.")
            else:
                st.success("✅ Prompt generado correctamente.")
                st.subheader("📤 Prompt listo para copiar")
                st.code(resultado, language="text")
                st.caption(f"Longitud total: {len(resultado):,} caracteres")

else:
    # ESTO ES LO QUE FALTABA: mostrar algo cuando NO se ha iniciado sesión
    st.info("👋 Por favor, inicia sesión o regístrate para continuar.")

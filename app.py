import streamlit as st
from supabase import create_client

# --- PARCHE para el error 42501 ---
import streamlit_supabase_auth_ui.utils as sb_utils

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
    
    # returning="minimal" evita el SELECT implícito que causa el error
    supabase.table("user_authentication").insert(
        new_usr_data, returning="minimal"
    ).execute()

# Reemplazar la función original por la parcheada
sb_utils.register_new_usr = _register_new_usr_patched
# --- FIN DEL PARCHE ---

# A partir de aquí, tu código normal con la librería
from streamlit_supabase_auth_ui.widgets import __login__
# ... el resto de tu app

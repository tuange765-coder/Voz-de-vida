# --- PARCHE: evitar el error 42501 en el registro ---
import streamlit_supabase_auth_ui.utils as sb_utils
from supabase import create_client
import os

def _register_new_usr_patched(name, email, username, password):
    """Versión parcheada que usa returning='minimal' para evitar RLS en el RETURNING."""
    url = os.environ.get("SUPABASE_URL") or st.secrets.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_KEY") or st.secrets.get("SUPABASE_KEY")
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

# Reemplazar la función original por la parcheada
sb_utils.register_new_usr = _register_new_usr_patched
# ------------------------------------------------------

import streamlit_supabase_auth_ui as sbui
# ... el resto de tu código

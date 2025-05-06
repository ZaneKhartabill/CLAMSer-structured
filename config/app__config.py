
import streamlit as st

def setup_page():
    st.set_page_config(
        page_title="CLAMSer",
        page_icon="🧬",
        layout="wide",
        initial_sidebar_state="expanded"
    )

def apply_global_styles():
    st.markdown("""
        <style>
        [data-testid="stSidebar"] {
            background-color: #1a1f2e;
            padding: 1rem;
            border-right: 1px solid #2d3648;
        }
        [data-testid="stSidebar"] .stRadio {
            background-color: #262d3d;
            padding: 1rem;
            border-radius: 5px;
            margin: 0.5rem 0;
        }
        .uploadedFile {
            background-color: #262d3d;
            padding: 1rem;
            border-radius: 5px;
            margin: 0.5rem 0;
        }
        </style>
        """, unsafe_allow_html=True)

import streamlit as st
import os
import sys
from importlib import import_module
import base64

# Add the parent directory to sys.path to allow imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import utility functions
from utils import add_custom_css, add_navbar, add_bg_from_file, create_enhanced_sidebar_navigation, force_dark_mode

# Import authentication functions
from utils import authenticate_user, check_authentication
from pages.login import show_login_page

# Initialize authentication session state variables
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "username" not in st.session_state:
    st.session_state.username = None

# Page configuration with custom icon
st.set_page_config(
    page_title="ESTK",
    page_icon="C:/Users/surface/Desktop/app/images/estk2.png",  # Add your icon path here
    layout="wide",
    initial_sidebar_state="expanded"
)

# FORCE DARK MODE - This should be called first, before any other styling
force_dark_mode()

# Function to add animated particles background
def add_animated_particles_background():
    st.markdown(
        """
        <style>
        /* Main app background with animated particles */
        .stApp {
            background: linear-gradient(135deg, 
                #0f0f23 0%, 
                #1a1a3e 25%, 
                #2d2d5f 50%, 
                #1a1a3e 75%, 
                #0f0f23 100%) !important;
            background-attachment: fixed !important;
            color: white !important;
        }
        
        /* Create animated particles */
        .stApp::before {
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: -1;
            background-image: 
                radial-gradient(circle at 20% 80%, rgba(120, 119, 198, 0.4) 0%, transparent 50%),
                radial-gradient(circle at 80% 20%, rgba(255, 119, 198, 0.3) 0%, transparent 50%),
                radial-gradient(circle at 40% 40%, rgba(120, 219, 255, 0.25) 0%, transparent 50%),
                radial-gradient(circle at 70% 70%, rgba(255, 200, 87, 0.3) 0%, transparent 50%),
                radial-gradient(circle at 30% 60%, rgba(134, 255, 119, 0.2) 0%, transparent 50%),
                radial-gradient(circle at 85% 30%, rgba(188, 119, 255, 0.15) 0%, transparent 50%);
            animation: floatParticles 20s ease-in-out infinite;
        }
        
        @keyframes floatParticles {
            0%, 100% {
                transform: translateY(0px) rotate(0deg);
                opacity: 1;
            }
            25% {
                transform: translateY(-20px) rotate(90deg);
                opacity: 0.8;
            }
            50% {
                transform: translateY(-40px) rotate(180deg);
                opacity: 0.6;
            }
            75% {
                transform: translateY(-20px) rotate(270deg);
                opacity: 0.8;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

# Function to set custom logo in the sidebar
def set_custom_logo():
    logo_path = ""  # Add your logo path here
    if os.path.exists(logo_path):
        with open(logo_path, "rb") as f:
            logo_data = f.read()
            logo_base64 = base64.b64encode(logo_data).decode("utf-8")
            
        # Custom CSS to replace the Streamlit logo
        st.markdown(
            f"""
            <style>
            [data-testid="stSidebarNav"] {{
                background-image: url("data:image/png;base64,{logo_base64}");
                background-repeat: no-repeat;
                background-position: 20px 20px;
                background-size: 140px auto;
                padding-top: 120px;
            }}
            [data-testid="stSidebarNav"]::before {{
                content: "";
                margin-left: 20px;
                margin-top: 20px;
                font-size: 30px;
                position: relative;
                top: 100px;
            }}
            </style>
            """,
            unsafe_allow_html=True,
        )

# Check if user is authenticated
if not check_authentication():
    show_login_page()
else:
    # User is authenticated, continue with normal app flow
    
    # Add animated particles background
    add_animated_particles_background()
    
    # Add custom logo
    set_custom_logo()
    
    # Add custom CSS and navbar
    add_custom_css()
    add_navbar()
    
    # Comment out the old background since we're using animated particles now
    # try:
    #     add_bg_from_file("C:/Users/surface/Desktop/app/images/black_background.svg")
    # except:
    #     st.warning("Background image not found. Please update the path.")
    
    # Initialize session state variables
    if "df" not in st.session_state:
        st.session_state["df"] = None
    if "df_filtered" not in st.session_state:
        st.session_state["df_filtered"] = None
    if "db_path" not in st.session_state:
        st.session_state["db_path"] = None
    if "tables" not in st.session_state:
        st.session_state["tables"] = []
    if "show_cleaning" not in st.session_state:
        st.session_state["show_cleaning"] = False
    if "show_filtering" not in st.session_state:
        st.session_state["show_filtering"] = False
    if "show_filter_category" not in st.session_state:
        st.session_state["show_filter_category"] = False
    if "show_filter_numeric" not in st.session_state:
        st.session_state["show_filter_numeric"] = False
    if "current_page" not in st.session_state:
        st.session_state["current_page"] = "🏠 Accueil"
    
    # Create enhanced sidebar navigation with logout option
    sidebar_container = st.sidebar.container()
    with sidebar_container:
        st.write(f"**Connecté en tant que:** {st.session_state.username}")
        if st.button("🚪 Déconnexion", key="logout_btn"):
            st.session_state.authenticated = False
            st.session_state.username = None
            st.rerun()
        
        st.markdown("---")  # Add a separator
        
    # Create enhanced sidebar navigation
    page = create_enhanced_sidebar_navigation()
    
    # Import and display the selected page module
    if page == "🏠 Accueil":
        from pages.home import show_page
    elif page == "🔀 Fusion":
        from pages.merge import show_page
    elif page == "📊 Visualisation":
        from pages.visualization import show_page
    elif page == "Analyse stratégique":
        from pages.strategic import show_page
    elif page == "🤖 Prédiction":
        from pages.prediction import show_page
    elif page == "dashboard":
        from pages.dashboard import show_page
        
    
    # Call the show_page function from the selected module
    show_page()

import base64
import json
import os
from datetime import datetime
import streamlit as st

# Define the path for the users database
USERS_DB_PATH = "users.json"

def get_users():
    """Load the users database from JSON file"""
    if os.path.exists(USERS_DB_PATH):
        try:
            with open(USERS_DB_PATH, "r") as f:
                return json.load(f)
        except:
            return {}
    else:
        return {}

def save_users(users):
    """Save the users database to JSON file"""
    with open(USERS_DB_PATH, "w") as f:
        json.dump(users, f, indent=4)

def authenticate_user(username, password):
    """
    Authenticate a user with username and password.
    Checks against the JSON file.
    """
    users = get_users()
    return username in users and users[username]["password"] == password

def register_user(username, password, email=""):
    """
    Register a new user.
    Returns:
    - "success" if registration successful
    - "exists" if username already exists
    - "error" on other errors
    """
    try:
        users = get_users()
        
        # Check if username already exists
        if username in users:
            return "exists"
        
        # Add new user
        users[username] = {
            "password": password,
            "email": email,
            "created_at": str(datetime.now())
        }
        
        # Save updated users database
        save_users(users)
        return "success"
    except Exception as e:
        print(f"Error registering user: {e}")
        return "error"

def check_authentication():
    """
    Check if the user is authenticated.
    """
    return "authenticated" in st.session_state and st.session_state.authenticated

# Function to add background image
def add_bg_from_file(image_file):
    with open(image_file, "rb") as f:
        encoded_string = base64.b64encode(f.read()).decode()

    # CSS to set the background image
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded_string}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

# Function to add custom CSS that hides the sidebar only for login page
# Add this function to your utils.py file

def force_dark_mode():
    """
    Force dark mode for all users regardless of their Streamlit theme settings
    """
    st.markdown("""
    <style>
    /* Force dark mode - Override all Streamlit theme settings */
    .stApp {
        background-color: #0f0f23 !important;
        color: white !important;
    }
    
    /* Force dark background for all containers */
    .main .block-container,
    .stApp > div,
    [data-testid="stAppViewContainer"],
    [data-testid="stHeader"],
    [data-testid="stToolbar"],
    [data-testid="stDecoration"],
    [data-testid="stStatusWidget"],
    section[data-testid="stSidebar"],
    .css-1d391kg,
    .css-1lcbmhc {
        background-color: transparent !important;
        color: white !important;
    }
    
    /* Force all text elements to be white */
    .stApp h1, .stApp h2, .stApp h3, .stApp h4, .stApp h5, .stApp h6,
    .stApp p, .stApp div, .stApp span, .stApp label,
    .stMarkdown, .stText, .stCaption {
        color: white !important;
    }
    
    /* Force input fields to have dark background and white text */
    .stTextInput input,
    .stNumberInput input,
    .stTextArea textarea,
    .stSelectbox select,
    .stMultiSelect > div,
    .stSlider > div,
    .stDateInput input,
    .stTimeInput input {
        background-color: rgba(255, 255, 255, 0.1) !important;
        color: white !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
    }
    
    /* Force labels to be white */
    .stTextInput label,
    .stNumberInput label,
    .stTextArea label,
    .stSelectbox label,
    .stMultiSelect label,
    .stSlider label,
    .stDateInput label,
    .stTimeInput label,
    .stCheckbox label,
    .stRadio label {
        color: white !important;
    }
    
    /* Force selectbox and multiselect dropdown to be dark */
    .stSelectbox > div > div,
    .stMultiSelect > div > div,
    .stSelectbox [data-baseweb="select"],
    .stMultiSelect [data-baseweb="select"] {
        background-color: rgba(0, 0, 0, 0.8) !important;
        color: white !important;
    }
    
    /* Force dropdown options to be dark */
    [data-baseweb="menu"] {
        background-color: rgba(0, 0, 0, 0.9) !important;
    }
    
    [data-baseweb="menu"] li {
        background-color: rgba(0, 0, 0, 0.9) !important;
        color: white !important;
    }
    
    [data-baseweb="menu"] li:hover {
        background-color: rgba(255, 255, 255, 0.1) !important;
    }
    
    /* Force dataframe/table styling to be dark */
    .stDataFrame,
    [data-testid="stDataFrame"],
    .dataframe,
    table {
        background-color: rgba(0, 0, 0, 0.8) !important;
        color: white !important;
    }
    
    .stDataFrame th,
    .stDataFrame td,
    [data-testid="stDataFrame"] th,
    [data-testid="stDataFrame"] td,
    table th,
    table td {
        background-color: rgba(0, 0, 0, 0.6) !important;
        color: white !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
    }
    
    /* Force metrics to be dark */
    [data-testid="metric-container"] {
        background-color: rgba(0, 0, 0, 0.3) !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        color: white !important;
    }
    
    [data-testid="metric-container"] [data-testid="stMetricValue"] {
        color: white !important;
    }
    
    [data-testid="metric-container"] [data-testid="stMetricLabel"] {
        color: rgba(255, 255, 255, 0.8) !important;
    }
    
    /* Force alerts/notifications to have proper contrast */
    .stAlert,
    .stSuccess,
    .stError,
    .stWarning,
    .stInfo {
        color: white !important;
    }
    
    .stAlert > div,
    .stSuccess > div,
    .stError > div,
    .stWarning > div,
    .stInfo > div {
        color: white !important;
    }
    
    /* Force chart backgrounds to be transparent or dark */
    .stPlotlyChart,
    .stAltairChart,
    .stPydeckChart,
    .stGraphvizChart {
        background-color: transparent !important;
    }
    
    /* Force progress bars to be visible */
    .stProgress > div > div {
        background-color: rgba(255, 255, 255, 0.2) !important;
    }
    
    /* Force tabs to be dark */
    .stTabs [data-baseweb="tab-list"] {
        background-color: rgba(0, 0, 0, 0.5) !important;
    }
    
    .stTabs [data-baseweb="tab"] {
        background-color: rgba(0, 0, 0, 0.3) !important;
        color: white !important;
    }
    
    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        background-color: rgba(0, 0, 0, 0.7) !important;
        color: white !important;
    }
    
    /* Force expander to be dark */
    .streamlit-expanderHeader {
        background-color: rgba(0, 0, 0, 0.3) !important;
        color: white !important;
    }
    
    .streamlit-expanderContent {
        background-color: rgba(0, 0, 0, 0.1) !important;
        color: white !important;
    }
    
    /* Force columns background */
    .element-container,
    .stColumn > div {
        background-color: transparent !important;
        color: white !important;
    }
    
    /* Override any remaining light mode artifacts */
    * {
        scrollbar-color: rgba(255, 255, 255, 0.3) transparent !important;
    }
    
    ::-webkit-scrollbar {
        background-color: transparent !important;
    }
    
    ::-webkit-scrollbar-thumb {
        background-color: rgba(255, 255, 255, 0.3) !important;
        border-radius: 4px !important;
    }
    
    ::-webkit-scrollbar-track {
        background-color: transparent !important;
    }
    
    /* Force any missed text elements */
    [data-testid] {
        color: white !important;
    }
    
    /* Special override for stubborn elements */
    .css-1629p8f, .css-6n58uw, .css-17eq0hr, .css-1d391kg,
    .css-1lcbmhc, .css-12oz5g7, .css-1cpxqw2 {
        background-color: transparent !important;
        color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)
def add_login_page_css():
    st.markdown("""
    <style>
        /* Hide sidebar ONLY for login page */
        [data-testid="stSidebar"] {
            display: none !important;
        }
        
        /* Hide default elements */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* 
    </style>
    """, unsafe_allow_html=True)

# Function to restore sidebar (if needed in other parts of your application)
def remove_sidebar_hiding():
    st.markdown("""
    <style>
        /* Remove the hiding of sidebar */
        [data-testid="stSidebar"] {
            display: block !important;
        }
    </style>
    """, unsafe_allow_html=True)

# Function to add custom CSS for the main app
# Function to add custom CSS for the main app
def add_custom_css():
    st.markdown("""
    <style>
/* Hide default navbar and elements */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Hide the default sidebar navigation titles */
[data-testid="stSidebarNavTitle"] {display: none !important;}
[data-testid="stSidebarNavItems"] {display: none !important;}
[data-baseweb="tab-list"] {display: none !important;}

/* Custom navbar styles - full width and fixed at top */
.custom-navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 15px 25px; /* Increased padding to make navbar bigger */
    background-color: var(--navbar-bg);
    color: var(--navbar-text);
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    z-index: 1000; /* Increased z-index to ensure it stays above sidebar */
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    width: 100%;
    height: auto; /* Allow height to adjust based on content */
    min-height: 60px; /* Set minimum height for navbar */
}

/* Change sidebar background color */
[data-testid="stSidebar"] {
    background-color: rgba(255,255,255,0.25) !important;
    color: white !important;
    margin-top: 60px; /* Add margin to push sidebar content below navbar */
    padding-top: 10px;
    z-index: 999; /* Lower than navbar */
}

/* Make sidebar text white for better contrast */
[data-testid="stSidebar"] .st-bq {
    color: white !important;
}

/* Make radio buttons text white */
[data-testid="stSidebar"] .st-cj {
    color: white !important;
}

/* Navigation title color */
[data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 {
    color: white !important;
}

/* Navigation styles */
.custom-navigation {
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 8px 15px;
    background-color: var(--navigation-bg);
    color: var(--navbar-text);
    margin: 10px 0;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.nav-item {
    padding: 8px 15px;
    margin: 0 5px;
    border-radius: 6px;
    cursor: pointer;
    transition: all 0.3s ease;
    font-weight: 500;
}

.nav-item:hover {
    background-color: rgba(255,255,255,0.2);
}

.nav-item.active {
    background-color: rgba(255,255,255,0.3);
    font-weight: bold;
}

/* Add padding to the top of content to account for fixed navbar */
.main-content {
    padding-top: 80px; /* Increased to account for larger navbar */
}

/* Style form buttons in main app */
div.stButton button {
    background: linear-gradient(45deg, #2b5876, #4e4376);
    color: white !important;
    font-weight: bold;
    border: none;
    padding: 12px 15px;
    width: 100%;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    transition: all 0.3s ease;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    margin: 10px 0;
    cursor: pointer;
    position: relative;
    overflow: hidden;
}

div.stButton button:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 12px rgba(0,0,0,0.15);
    background: linear-gradient(45deg, #3a7bd5, #5d46a3);
}

/* Set fixed colors - CHANGED TO BLACK */
:root {
    --navbar-bg: #000000;  /* Changed from #1E3A8A to black */
    --navbar-text: white;
    --navigation-bg: #000000;  /* Changed from #2563EB to black */
}
.social-icons {
            display: flex;
            gap: 10px;
        }
.social-icon {
            font-size: 20px;
            color: var(--navbar-text);
            padding: 5px;
            border-radius: 5px;
            transition: all 0.3s ease;
            cursor: pointer;
        }
        
.social-icon:hover {
            transform: translateY(-2px);
            background-color: rgba(255,255,255,0.1);
        }
        
    </style>
    """, unsafe_allow_html=True)

# Function to add custom navbar with social media icons
def add_navbar():
    navbar_html = """
    <div class="custom-navbar">
        <div class="navbar-brand">
            <span>📊 DataAnalyzer Pro</span>
        </div>
        <div class="navbar-actions">
            <div class="social-icons">
                <a href="https://wa.me/qr/RJX7SXREUWZAM1" class="social-icon" title="WhatsApp" style="color: #25D366;"><i class="fab fa-whatsapp"></i></a>
                <a href="https://www.linkedin.com/in/idriss-benfanich-70231b348?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app" class="social-icon" title="LinkedIn" style="color: #ffffff;"><i class="fab fa-linkedin"></i></a>
            </div>
        </div>
    </div>
    
    <!-- Font Awesome for icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
    <!-- Add div for main content with padding to account for fixed navbar -->
    <div class="main-content">
    """
    st.markdown(navbar_html, unsafe_allow_html=True)

# Function to create enhanced sidebar navigation
def create_enhanced_sidebar_navigation():     
    # Get current page from session state or default     
    nav_options = ["🏠 Accueil", "🔀 Fusion", "📊 Visualisation", "Analyse stratégique", "🤖 Prédiction", "dashboard"]     
    current_page = st.session_state.get('current_page', nav_options[0])          
    
    # Create custom navigation that matches the design in the image     
    # Use a hidden container for the state management but don't display radio buttons     
    with st.sidebar.container():         
        # This hidden radio button maintains the state but won't be shown         
        page = st.radio(             
            "Navigation",              
            nav_options,              
            index=nav_options.index(current_page),              
            label_visibility="collapsed",             
            key="hidden_nav"         
        )                  
        
        # Update current page in session state         
        if page != current_page:             
            st.session_state['current_page'] = page          
        
        # Custom navigation items styling for card-style buttons with black theme     
        st.sidebar.markdown("""  
        <style>     
            /* Hide the default radio buttons completely */     
            div[data-testid="stRadio"] {         
                display: none !important;     
            }          
            
            /* Black sidebar background */
            .css-1d391kg {
                background-color: #000000 !important;
            }
            
            section[data-testid="stSidebar"] {
                background-color: #000000 !important;
            }
            
            section[data-testid="stSidebar"] > div {
                background-color: #000000 !important;
            }
            
            /* Card-style navigation item with black theme */     
            .card-nav-item {         
                background-color: rgba(255,255,255,0.1);         
                border-radius: 10px;         
                padding: 15px;         
                margin-bottom: 8px; /* Reduced from 15px to 8px */         
                display: flex;         
                align-items: center;         
                cursor: pointer;         
                transition: all 0.3s ease;
                border: 1px solid rgba(255,255,255,0.1);     
            }          
            
            .card-nav-item.active {         
                background-color: rgba(255,255,255,0.2);         
                border-left: 4px solid #ffffff;
                border: 1px solid rgba(255,255,255,0.3);     
            }          
            
            .card-nav-item:hover {         
                background-color: rgba(255,255,255,0.15);         
                transform: translateX(5px);
                border: 1px solid rgba(255,255,255,0.2);     
            }          
            
            .card-nav-icon {         
                margin-right: 15px;         
                font-size: 24px;         
                color: #ffffff;     
            }          
            
            .card-nav-text {         
                color: #ffffff;         
                font-size: 18px;         
                font-weight: 500;     
            }          
            
            /* Reduce spacing between buttons */     
            .stButton {         
                margin-bottom: 0px !important; /* Remove bottom margin from buttons */     
            }          
            
            /* Adjust button margins directly */     
            div.stButton > button {         
                margin-top: 2px !important;  /* Reduced top margin */         
                margin-bottom: 2px !important;  /* Reduced bottom margin */
                background-color: transparent !important;
                border: 1px solid rgba(255,255,255,0.1) !important;
                color: #ffffff !important;     
            }
            
            div.stButton > button:hover {
                background-color: rgba(255,255,255,0.1) !important;
                border: 1px solid rgba(255,255,255,0.2) !important;
            }          
            
            /* Fix for visible radio buttons that might show up despite the hide rule */     
            div[data-testid="stRadio"] > div {         
                display: none !important;     
            }
            
            /* Sidebar title and other text elements */
            .css-1d391kg h1, .css-1d391kg h2, .css-1d391kg h3, 
            .css-1d391kg p, .css-1d391kg span, .css-1d391kg div {
                color: #ffffff !important;
            }
            
            /* Streamlit sidebar container */
            .css-1lcbmhc, .css-1d391kg, .css-k1vhr4 {
                background-color: #000000 !important;
            }
            
            /* Additional selectors for different Streamlit versions */
            [data-testid="stSidebar"] [data-testid="stVerticalBlock"] {
                background-color: #000000 !important;
            }
        </style>     
        """, unsafe_allow_html=True)
    
    # Accueil item
    accueil_active = "active" if page == "🏠 Accueil" else ""
    if st.sidebar.button("🏠 Accueil", key="nav_home", use_container_width=True):
        st.session_state['current_page'] = "🏠 Accueil"
        st.rerun()
    
    # Fusion item
    fusion_active = "active" if page == "🔀 Fusion" else ""
    if st.sidebar.button("🔀 Fusion", key="nav_fusion", use_container_width=True):
        st.session_state['current_page'] = "🔀 Fusion"
        st.rerun()
    
    # Visualisation item
    visualisation_active = "active" if page == "📊 Visualisation" else ""
    if st.sidebar.button("📊 Visualisation", key="nav_viz", use_container_width=True):
        st.session_state['current_page'] = "📊 Visualisation"
        st.rerun()

    # Analyse stratégique item

    dashboard_active = "active" if page == "dashboard" else ""
    if st.sidebar.button("dashboard", key="nav_dashboard", use_container_width=True):
        st.session_state['current_page'] = "dashboard"
        st.rerun()
        
    # Prédiction item
    prediction_active = "active" if page == "🤖 Prédiction" else ""
    if st.sidebar.button("🤖 Prédiction", key="nav_pred", use_container_width=True):
        st.session_state['current_page'] = "🤖 Prédiction"
        st.rerun()
    
    return page

# Function to display enhanced filter options
def display_enhanced_filter_options():
    st.sidebar.markdown("""
    <div class="option-filtrage">
        <div class="filtrage-titre">
            Options de filtrage
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Initialize session state variables if they don't exist
    if "show_filter_category" not in st.session_state:
        st.session_state["show_filter_category"] = False
    if "show_filter_numeric" not in st.session_state:
        st.session_state["show_filter_numeric"] = False
    
    # Boutons pour le filtrage
    cat_filter_clicked = st.sidebar.button("Catégories", key="cat_filter", on_click=None)
    num_filter_clicked = st.sidebar.button("Numériques", key="num_filter", on_click=None)
    
    # Logic for filter buttons
    if cat_filter_clicked:
        st.session_state["show_filter_category"] = not st.session_state["show_filter_category"]
        st.session_state["show_filter_numeric"] = False
        st.rerun()

    if num_filter_clicked:
        st.session_state["show_filter_numeric"] = not st.session_state["show_filter_numeric"]
        st.session_state["show_filter_category"] = False
        st.rerun()

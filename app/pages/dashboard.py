import streamlit as st
from pages import nada_page, othmane_page, belghiti_page
from pages.pages_yahya import yahya_page

def show_page():
    """
    Main Dashboard page that orchestrates navigation between different modules
    """
    st.title("📊 Tableau de Bord ")
    
    # Sidebar with 4 buttons
    st.sidebar.header("Navigation")
    
    # Button 1: Décrochage scolaire (G Yahya)
    if st.sidebar.button("G Yahya: Décrochage scolaire", use_container_width=True):
        st.session_state.dashboard_view = "yahya"
    
    # Button 2: Inégalités Scolaires (G Nada)
    if st.sidebar.button("G Nada: Inégalités Scolaires", use_container_width=True):
        st.session_state.dashboard_view = "nada"
    
    # Button 3: Optimisation des Ressources (G Othmane)
    if st.sidebar.button("G Othmane: Optimisation des Ressources", use_container_width=True):
        st.session_state.dashboard_view = "othmane"
    
    # Button 4: Suivi personnalisé des ICSE (G Belghiti)
    if st.sidebar.button("G Belghiti: Suivi personnalisé des ICSE", use_container_width=True):
        st.session_state.dashboard_view = "belghiti"
    
    # Initialize session state if not exists
    if 'dashboard_view' not in st.session_state:
        st.session_state.dashboard_view = "yahya"
    
    # Main content area based on selected button
    if st.session_state.dashboard_view == "yahya":
       yahya_page.show_page()
    elif st.session_state.dashboard_view == "nada":
        nada_page.show_page()
    elif st.session_state.dashboard_view == "othmane":
        othmane_page.show_page()
    elif st.session_state.dashboard_view == "belghiti":
        belghiti_page.show_page()
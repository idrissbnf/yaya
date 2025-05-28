import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def show_page():
    """
    Nada's page for analyzing educational inequalities
    """
    st.header("📊 Analyse des Inégalités Scolaires")
    
    st.markdown("""
    ### 🎯 Objectifs de l'analyse
    - Identifier les disparités dans l'accès à l'éducation
    - Analyser les écarts de performance entre différents groupes
    - Évaluer l'impact des facteurs socio-économiques
    - Proposer des solutions pour réduire les inégalités
    """)
    
    # Key indicators
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="Écart de performance",
            value="18.5%",
            delta="-3.2%"
        )
    
    with col2:
        st.metric(
            label="Accès aux ressources",
            value="67.3%",
            delta="5.1%"
        )
    
    with col3:
        st.metric(
            label="Taux de réussite équitable",
            value="72.1%",
            delta="2.8%"
        )
    
    with col4:
        st.metric(
            label="Indices d'égalité",
            value="0.76",
            delta="0.04"
        )
    
    # Analysis sections
    st.subheader("📈 Analyse des disparités")
    
    # Sample data for demonstration
    inequality_data = pd.DataFrame({
        'Région': ['Nord', 'Sud', 'Est', 'Ouest', 'Centre'],
        'Taux_réussite': [85, 72, 78, 81, 88],
        'Accès_internet': [92, 65, 78, 85, 95],
        'Niveau_socioeco': ['Élevé', 'Faible', 'Moyen', 'Élevé', 'Très élevé']
    })
    
    # Bar chart comparing regions
    fig = px.bar(inequality_data, x='Région', y=['Taux_réussite', 'Accès_internet'],
                 title="Comparaison régionale des indicateurs éducatifs",
                 barmode='group')
    st.plotly_chart(fig, use_container_width=True)
    
    # Detailed analysis tabs
    tab1, tab2, tab3, tab4 = st.tabs(["Disparités régionales", "Facteurs socio-économiques", "Solutions proposées", "Suivi des progrès"])
    
    with tab1:
        st.markdown("""
        #### Analyse régionale
        - **Nord**: Performance élevée, bonnes infrastructures
        - **Sud**: Défis importants, manque de ressources
        - **Est**: Progrès modérés, potentiel d'amélioration
        - **Ouest**: Bonne performance globale
        - **Centre**: Excellente performance, référence
        """)
        
        # Scatter plot
        fig_scatter = px.scatter(inequality_data, x='Accès_internet', y='Taux_réussite',
                                color='Niveau_socioeco', size_max=60,
                                title="Corrélation accès internet vs taux de réussite")
        st.plotly_chart(fig_scatter, use_container_width=True)
    
    with tab2:
        st.markdown("""
        #### Facteurs socio-économiques identifiés
        - Revenus familiaux
        - Niveau d'éducation des parents
        - Accès aux technologies
        - Infrastructure scolaire locale
        - Disponibilité des transports
        
        #### Impact mesuré
        - Corrélation forte entre niveau socio-économique et réussite scolaire
        - Écart de 23% entre quartiles extrêmes
        - Influence significative de l'environnement familial
        """)
    
    with tab3:
        st.markdown("""
        #### Solutions recommandées
        
        **Court terme:**
        - Programme de bourses ciblées
        - Distribution d'équipements numériques
        - Renforcement du transport scolaire
        
        **Moyen terme:**
        - Amélioration des infrastructures
        - Formation des enseignants
        - Programmes de soutien parental
        
        **Long terme:**
        - Réforme structurelle du système
        - Développement économique régional
        - Politique d'égalité des chances
        """)
    
    with tab4:
        st.markdown("""
        #### Indicateurs de suivi
        - Indice de Gini éducatif
        - Taux de scolarisation par quartile
        - Écart de performance standardisé
        - Progression annuelle des groupes défavorisés
        
        #### Objectifs 2025
        - Réduction de 30% de l'écart de performance
        - Amélioration de 15% de l'accès aux ressources
        - Atteinte d'un indice d'égalité de 0.85
        """)
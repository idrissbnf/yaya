import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def show_page():
    """
    Othmane's page for resource optimization analysis
    """
    st.header("🔧 Optimisation des Ressources")
    
    st.markdown("""
    ### 🎯 Objectifs de l'optimisation
    - Analyser l'allocation actuelle des ressources
    - Identifier les inefficacités dans le système
    - Proposer des stratégies d'optimisation
    - Évaluer l'impact des améliorations proposées
    """)
    
    # Key performance indicators
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="Efficacité budgétaire",
            value="78.5%",
            delta="12.3%"
        )
    
    with col2:
        st.metric(
            label="Utilisation des ressources",
            value="85.2%",
            delta="7.8%"
        )
    
    with col3:
        st.metric(
            label="Économies réalisées",
            value="€2.3M",
            delta="€450K"
        )
    
    with col4:
        st.metric(
            label="ROI éducatif",
            value="3.2x",
            delta="0.8x"
        )
    
    # Resource allocation analysis
    st.subheader("📊 Analyse de l'allocation des ressources")
    
    # Sample resource data
    resource_data = pd.DataFrame({
        'Catégorie': ['Personnel', 'Infrastructure', 'Matériel pédagogique', 'Technologies', 'Maintenance'],
        'Budget_actuel': [12000000, 8500000, 3200000, 2800000, 1500000],
        'Budget_optimal': [11500000, 9200000, 3800000, 3500000, 1200000],
        'Utilisation': [92, 75, 88, 65, 82]
    })
    
    # Budget comparison chart
    fig_budget = go.Figure(data=[
        go.Bar(name='Budget Actuel', x=resource_data['Catégorie'], y=resource_data['Budget_actuel']),
        go.Bar(name='Budget Optimal', x=resource_data['Catégorie'], y=resource_data['Budget_optimal'])
    ])
    fig_budget.update_layout(title='Comparaison Budget Actuel vs Optimal', barmode='group')
    st.plotly_chart(fig_budget, use_container_width=True)
    
    # Detailed analysis tabs
    tab1, tab2, tab3, tab4 = st.tabs(["Analyse actuelle", "Optimisations identifiées", "Plan d'action", "Monitoring"])
    
    with tab1:
        st.markdown("""
        #### État actuel des ressources
        
        **Forces identifiées:**
        - Bonne utilisation du personnel enseignant
        - Matériel pédagogique bien géré
        - Processus de maintenance efficace
        
        **Défis identifiés:**
        - Sous-utilisation des technologies (65%)
        - Infrastructure vieillissante
        - Répartition inégale entre établissements
        """)
        
        # Efficiency radar chart
        categories = ['Personnel', 'Infrastructure', 'Matériel', 'Technologies', 'Maintenance']
        efficiency_scores = [92, 75, 88, 65, 82]
        
        fig_radar = go.Figure()
        fig_radar.add_trace(go.Scatterpolar(
            r=efficiency_scores,
            theta=categories,
            fill='toself',
            name='Efficacité actuelle'
        ))
        fig_radar.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 100]
                )),
            title="Radar d'efficacité par catégorie de ressources"
        )
        st.plotly_chart(fig_radar, use_container_width=True)
    
    with tab2:
        st.markdown("""
        #### Optimisations recommandées
        
        **1. Redistribution budgétaire**
        - Réduire le budget personnel de 4.3% (€500K)
        - Augmenter l'investissement infrastructure de 8.2% (€700K)
        - Renforcer le budget technologique de 25% (€700K)
        
        **2. Amélioration de l'utilisation**
        - Formation du personnel aux nouvelles technologies
        - Mutualisation des ressources entre établissements
        - Maintenance préventive plutôt que corrective
        
        **3. Innovations proposées**
        - Système de gestion intégrée des ressources
        - Plateforme de partage inter-établissements
        - Tableaux de bord temps réel
        """)
        
        # Savings potential chart
        savings_data = pd.DataFrame({
            'Optimisation': ['Redistribution', 'Mutualisation', 'Digitalisation', 'Maintenance préventive'],
            'Économies_potentielles': [500000, 320000, 450000, 180000]
        })
        
        fig_savings = px.bar(savings_data, x='Optimisation', y='Économies_potentielles',
                            title='Potentiel d\'économies par type d\'optimisation')
        st.plotly_chart(fig_savings, use_container_width=True)
    
    with tab3:
        st.markdown("""
        #### Plan d'implémentation
        
        **Phase 1 (0-6 mois) - Fondations**
        - Audit complet des ressources existantes
        - Mise en place du système de monitoring
        - Formation des équipes de gestion
        
        **Phase 2 (6-12 mois) - Optimisation**
        - Redistribution budgétaire progressive
        - Lancement des projets de mutualisation
        - Implémentation des nouvelles technologies
        
        **Phase 3 (12-18 mois) - Consolidation**
        - Évaluation des résultats
        - Ajustements et améliorations
        - Extension à tous les établissements
        
        **Ressources nécessaires:**
        - Équipe projet: 5 personnes
        - Budget d'implémentation: €800K
        - Formation: 200 heures
        """)
    
    with tab4:
        st.markdown("""
        #### Indicateurs de suivi
        
        **KPIs opérationnels:**
        - Taux d'utilisation des ressources
        - Temps de résolution des demandes
        - Satisfaction des utilisateurs
        - Coût par élève
        
        **KPIs financiers:**
        - Économies réalisées vs objectifs
        - ROI des investissements
        - Évolution des coûts unitaires
        
        **KPIs qualité:**
        - Disponibilité des équipements
        - Taux de panne des infrastructures
        - Temps de réponse maintenance
        
        #### Reporting
        - Tableau de bord hebdomadaire
        - Rapport mensuel détaillé
        - Revue trimestrielle stratégique
        """)
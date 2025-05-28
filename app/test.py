 # Always show cycle analysis if available
            if 'cycle' in filtered_data.columns and 'niveau' in filtered_data.columns:
                st.markdown('<div class="dashboard-section animated-section">', unsafe_allow_html=True)
                st.markdown('<div class="section-header">📚 Dashboard d\'Analyse par Cycle et Niveau</div>', unsafe_allow_html=True)
                
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
                    # Abandons by cycle and niveau
                    abandon_cycle_niveau = filtered_data[abandon_mask].groupby(['cycle', 'niveau']).size().reset_index(name='Abandons')
                    if not abandon_cycle_niveau.empty:
                        fig_cycle_niveau = px.bar(
                            abandon_cycle_niveau, x='niveau', y='Abandons', color='cycle',
                            title="Abandons par Cycle et Niveau",
                            barmode='group',
                            color_discrete_sequence=['#667eea', '#764ba2', '#f093fb', '#f5576c']
                        )
                        fig_cycle_niveau.update_layout(
                            plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)',
                            font={'color': '#8892b0'}, height=500,
                            title={'x': 0.5, 'xanchor': 'center', 'font': {'color': '#ccd6f6'}}
                        )
                        st.plotly_chart(fig_cycle_niveau, use_container_width=True)
                    st.markdown('</div>', unsafe_allow_html=True)
                
                with col2:
                    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
                    # Pie chart for cycle distribution
                    abandon_cycle_data = filtered_data[abandon_mask].groupby('cycle').size().reset_index(name='Abandons')
                    if not abandon_cycle_data.empty:
                        fig_pie_cycle = create_enhanced_chart(
                            abandon_cycle_data, "pie", "cycle", "Abandons", "Répartition des Abandons par Cycle"
                        )
                        st.plotly_chart(fig_pie_cycle, use_container_width=True)
                    st.markdown('</div>', unsafe_allow_html=True)
                
                # Detailed level analysis
                st.markdown('<div class="chart-container">', unsafe_allow_html=True)
                st.markdown('<div class="chart-title">📖 Analyse Détaillée par Niveau</div>', unsafe_allow_html=True)
                
                niveau_stats = filtered_data.groupby('niveau').agg({
                    'situation': ['count', lambda x: sum(x.isin([2, 5]))]
                }).round(2)
                niveau_stats.columns = ['Total_Étudiants', 'Total_Abandons']
                niveau_stats['Taux_Abandon'] = (niveau_stats['Total_Abandons'] / niveau_stats['Total_Étudiants'] * 100).round(1)
                niveau_stats = niveau_stats.reset_index().sort_values('Taux_Abandon', ascending=False)
                
                if not niveau_stats.empty:
                    fig_niveau_rate = px.bar(
                        niveau_stats, x='niveau', y='Taux_Abandon',
                        title="Taux d'Abandon par Niveau (%)",
                        text='Taux_Abandon',
                        color='Taux_Abandon',
                        color_continuous_scale=['#00f2fe', '#4facfe', '#f5576c']
                    )
                    fig_niveau_rate.update_layout(
                        plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)',
                        font={'color': '#8892b0'}, height=500,
                        title={'x': 0.5, 'xanchor': 'center', 'font': {'color': '#ccd6f6'}}
                    )
                    fig_niveau_rate.update_traces(texttemplate='%{text}%', textposition='outside')
                    st.plotly_chart(fig_niveau_rate, use_container_width=True)
                
                st.markdown('</div>', unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)

            # Social Aids Analysis Section
            st.markdown('<div class="dashboard-section animated-section">', unsafe_allow_html=True)
            st.markdown('<div class="section-header">🤝 Analyse Détaillée des Aides Sociales</div>', unsafe_allow_html=True)
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown('<div class="chart-container">', unsafe_allow_html=True)
                # Distribution of social aids
                aid_distribution = filtered_data[aides].sum().reset_index()
                aid_distribution.columns = ['Type_Aide', 'Nombre_Bénéficiaires']
                aid_distribution = aid_distribution.sort_values('Nombre_Bénéficiaires', ascending=False)
                
                fig_aid_dist = create_enhanced_chart(
                    aid_distribution, "bar", "Type_Aide", "Nombre_Bénéficiaires", 
                    "Distribution des Aides Sociales"
                )
                fig_aid_dist.update_layout(xaxis_tickangle=-45)
                st.plotly_chart(fig_aid_dist, use_container_width=True)
                st.markdown('</div>', unsafe_allow_html=True)
            
            with col2:
                st.markdown('<div class="chart-container">', unsafe_allow_html=True)
                # Pie chart of aid distribution
                fig_aid_pie = create_enhanced_chart(
                    aid_distribution, "pie", "Type_Aide", "Nombre_Bénéficiaires",
                    "Répartition des Types d'Aides"
                )
                st.plotly_chart(fig_aid_pie, use_container_width=True)
                st.markdown('</div>', unsafe_allow_html=True)
            
            # Correlation analysis between aids and abandonment
            st.markdown('<div class="chart-container">', unsafe_allow_html=True)
            st.markdown('<div class="chart-title">🔍 Analyse de Corrélation: Aides vs Abandons</div>', unsafe_allow_html=True)
            
            # Create correlation data
            correlation_data = []
            for aide in aides:
                aide_beneficiaries = filtered_data[filtered_data[aide] == 1]
                total_with_aid = len(aide_beneficiaries)
                abandons_with_aid = len(aide_beneficiaries[aide_beneficiaries['situation'].isin([2, 5])])
                abandon_rate_with_aid = (abandons_with_aid / total_with_aid * 100) if total_with_aid > 0 else 0
                
                correlation_data.append({
                    'Type_Aide': aide,
                    'Bénéficiaires': total_with_aid,
                    'Abandons': abandons_with_aid,
                    'Taux_Abandon': abandon_rate_with_aid
                })
            
            correlation_df = pd.DataFrame(correlation_data)
            
            if not correlation_df.empty:
                fig_correlation = px.scatter(
                    correlation_df, x='Bénéficiaires', y='Taux_Abandon',
                    size='Abandons', hover_name='Type_Aide',
                    title="Corrélation entre Nombre de Bénéficiaires et Taux d'Abandon",
                    color='Taux_Abandon',
                    color_continuous_scale=['#00f2fe', '#4facfe', '#f5576c']
                )
                fig_correlation.update_layout(
                    plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)',
                    font={'color': '#8892b0'}, height=500,
                    title={'x': 0.5, 'xanchor': 'center', 'font': {'color': '#ccd6f6'}}
                )
                st.plotly_chart(fig_correlation, use_container_width=True)
            
            st.markdown('</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

           

import streamlit as st
from pathlib import Path
import time

# Configuração da página
st.set_page_config(
    page_title="SQL Mystery - O Detetive de Banco de Dados",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Carregar CSS customizado
def load_css():
    css_file = Path(__file__).parent / "assets" / "styles" / "main.css"
    if css_file.exists():
        with open(css_file, encoding='utf-8') as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# Página principal ultra moderna
def main():
    # Header com tema de mistério ultra moderno
    st.markdown("""
        <div class="header-container">
            <h1 class="main-title">SQL MYSTERY</h1>
            <p class="subtitle">O Detetive de Banco de Dados</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Introdução ultra moderna
    st.markdown("""
        <div class="intro-section">
            <h2 style="text-align: center; color: var(--primary-cyan); font-family: 'Orbitron', sans-serif; margin-bottom: 2rem;">
                🕵️ Bem-vindo, Detetive Digital!
            </h2>
            <p style="text-align: center; font-size: 1.2rem; line-height: 1.8;">
                Você foi convocado para resolver <strong style="color: var(--primary-cyan);">mistérios complexos</strong> 
                usando suas habilidades em <strong style="color: var(--primary-purple);">SQL</strong>.
            </p>
            <p style="text-align: center; font-size: 1.1rem; line-height: 1.8;">
                Cada episódio apresenta um caso único que requer <strong style="color: var(--accent-green);">análise cuidadosa</strong> 
                de dados e <strong style="color: var(--accent-orange);">consultas SQL precisas</strong>.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Cards dos episódios ultra modernos
    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        st.markdown("""
            <div class="episode-card">
                <h3>📚 Episódio 1: Biblioteca</h3>
                <h4>O Livro Raro</h4>
                <p>Um livro raro desapareceu da biblioteca. Investigue os registros de empréstimos e descubra quem não devolveu o livro.</p>
                <ul>
                    <li>SELECT, WHERE, ORDER BY</li>
                    <li>GROUP BY, JOIN</li>
                    <li>Funções agregadas</li>
                    <li>Análise de datas</li>
                </ul>
                <div style="margin-top: 1.5rem; padding: 1rem; background: rgba(0, 240, 255, 0.1); border-radius: 10px; border-left: 4px solid var(--primary-cyan);">
                    <strong style="color: var(--primary-cyan);">Dificuldade:</strong> 
                    <span style="color: var(--accent-green);">⭐⭐⭐ Iniciante</span>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        if st.button("🔍 Investigar Biblioteca", key="ep1", use_container_width=True):
            with st.spinner("Iniciando investigação..."):
                time.sleep(0.5)
                st.switch_page("pages/01_📚_Biblioteca.py")
    
    with col2:
        st.markdown("""
            <div class="episode-card">
                <h3>🖥️ Episódio 2: Servidor</h3>
                <h4>Incidente na Madrugada</h4>
                <p>O servidor de dados caiu misteriosamente durante a madrugada. Analise os logs e descubra o que aconteceu.</p>
                <ul>
                    <li>JOINs complexos</li>
                    <li>Subqueries</li>
                    <li>Análise temporal</li>
                    <li>Detecção de padrões</li>
                </ul>
                <div style="margin-top: 1.5rem; padding: 1rem; background: rgba(176, 38, 255, 0.1); border-radius: 10px; border-left: 4px solid var(--primary-purple);">
                    <strong style="color: var(--primary-purple);">Dificuldade:</strong> 
                    <span style="color: var(--accent-orange);">⭐⭐⭐⭐⭐ Avançado</span>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        if st.button("🔍 Investigar Servidor", key="ep2", use_container_width=True):
            with st.spinner("Iniciando investigação..."):
                time.sleep(0.5)
                st.switch_page("pages/02_🖥️_Servidor.py")
    
    # Seção de estatísticas
    st.markdown("---")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
            <div class="metric-container">
                <div class="metric-value">0</div>
                <div class="metric-label">🎯 Puzzles Resolvidos</div>
                <div class="metric-delta">Comece agora!</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div class="metric-container">
                <div class="metric-value">--:--</div>
                <div class="metric-label">⏱️ Tempo Médio</div>
                <div class="metric-delta">Melhore seu tempo</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
            <div class="metric-container">
                <div class="metric-value">0</div>
                <div class="metric-label">🏆 Pontuação</div>
                <div class="metric-delta">Alcance 1000 pontos</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
            <div class="metric-container">
                <div class="metric-value">0/10</div>
                <div class="metric-label">🎖️ Conquistas</div>
                <div class="metric-delta">Desbloqueie todas</div>
            </div>
        """, unsafe_allow_html=True)
    
    # Footer ultra moderno
    st.markdown("""
        <div class="footer">
            <h3 style="color: var(--primary-cyan); font-family: 'Orbitron', sans-serif; margin-bottom: 1rem;">
                💡 Dicas para Detetives Iniciantes
            </h3>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem; margin-top: 2rem;">
                <div style="padding: 1rem; background: rgba(0, 240, 255, 0.1); border-radius: 10px; border-left: 4px solid var(--primary-cyan);">
                    <strong>🔍 Leia com Atenção</strong><br>
                    Cada puzzle tem pistas importantes na descrição
                </div>
                <div style="padding: 1rem; background: rgba(176, 38, 255, 0.1); border-radius: 10px; border-left: 4px solid var(--primary-purple);">
                    <strong>💡 Use as Dicas</strong><br>
                    Não hesite em pedir ajuda quando necessário
                </div>
                <div style="padding: 1rem; background: rgba(0, 255, 136, 0.1); border-radius: 10px; border-left: 4px solid var(--accent-green);">
                    <strong>🎯 Pratique</strong><br>
                    A prática leva à perfeição em SQL
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()


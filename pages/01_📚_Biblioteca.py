import streamlit as st
import sys
from pathlib import Path

# Adicionar o diretório raiz ao path
root_dir = Path(__file__).parent.parent
sys.path.insert(0, str(root_dir))

from components.puzzle_engine import PuzzleEngine
from components.database import DatabaseManager
from src.biblioteca.puzzles import puzzles_biblioteca

# Configuração da página
st.set_page_config(
    page_title="Episódio 1: Biblioteca - SQL Mystery",
    page_icon="📚",
    layout="wide"
)

# Carregar CSS
def load_css():
    css_file = root_dir / "assets" / "styles" / "main.css"
    if css_file.exists():
        with open(css_file, encoding='utf-8') as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# Inicializar estado da sessão
if 'biblioteca_puzzle_index' not in st.session_state:
    st.session_state.biblioteca_puzzle_index = 0
if 'biblioteca_hint_level' not in st.session_state:
    st.session_state.biblioteca_hint_level = 0
if 'biblioteca_completed' not in st.session_state:
    st.session_state.biblioteca_completed = []

# Inicializar banco de dados e engine
db_path = root_dir / "data" / "biblioteca.db"
db_manager = DatabaseManager(str(db_path))
puzzle_engine = PuzzleEngine(puzzles_biblioteca, db_manager)

def main():
    # Header
    st.markdown("""
        <div class="episode-header">
            <h1>📚 Episódio 1: Biblioteca</h1>
            <h2>O Livro Raro</h2>
        </div>
    """, unsafe_allow_html=True)
    
    # Sidebar ultra moderna com progresso
    with st.sidebar:
        st.markdown("""
            <div style="background: var(--glass-bg); backdrop-filter: blur(20px); padding: 1.5rem; border-radius: 15px; border: 2px solid var(--border-glow); margin-bottom: 2rem;">
                <h3 style="color: var(--primary-cyan); font-family: 'Orbitron', sans-serif; text-align: center; margin-bottom: 1rem;">
                    🎯 Progresso da Investigação
                </h3>
                <div style="text-align: center;">
                    <div style="font-size: 2rem; font-weight: bold; color: var(--primary-cyan);">
                        {completed}/{total}
                    </div>
                    <div style="color: var(--text-secondary); margin-bottom: 1rem;">
                        Puzzles Resolvidos
                    </div>
                </div>
            </div>
        """.format(
            completed=len(st.session_state.biblioteca_completed),
            total=len(puzzles_biblioteca)
        ), unsafe_allow_html=True)
        
        progress = len(st.session_state.biblioteca_completed) / len(puzzles_biblioteca)
        st.progress(progress)
        
        # Barra de experiência
        st.markdown("""
            <div style="background: var(--glass-bg); backdrop-filter: blur(20px); padding: 1rem; border-radius: 10px; border: 1px solid var(--border-glow); margin: 1rem 0;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
                    <span style="color: var(--primary-cyan); font-weight: bold;">XP</span>
                    <span style="color: var(--text-secondary);">{xp}/1000</span>
                </div>
                <div style="background: var(--darker-bg); height: 8px; border-radius: 4px; overflow: hidden;">
                    <div style="background: var(--gradient-success); height: 100%; width: {xp_percent}%; transition: width 0.3s ease;"></div>
                </div>
            </div>
        """.format(
            xp=len(st.session_state.biblioteca_completed) * 100,
            xp_percent=(len(st.session_state.biblioteca_completed) * 100) / 10
        ), unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Estrutura do banco de dados melhorada
        st.markdown("""
            <div style="background: var(--glass-bg); backdrop-filter: blur(20px); padding: 1.5rem; border-radius: 15px; border: 2px solid var(--border-glow-purple);">
                <h3 style="color: var(--primary-purple); font-family: 'Orbitron', sans-serif; text-align: center; margin-bottom: 1rem;">
                    📊 Estrutura do Banco
                </h3>
            </div>
        """, unsafe_allow_html=True)
        
        with st.expander("📋 Tabelas Disponíveis", expanded=False):
            st.markdown("""
                <div style="background: rgba(0, 240, 255, 0.05); padding: 1rem; border-radius: 10px; margin-bottom: 1rem;">
                    <strong style="color: var(--primary-cyan);">📚 leitores</strong><br>
                    <span style="color: var(--text-secondary); font-size: 0.9rem;">id, nome, email</span>
                </div>
                <div style="background: rgba(176, 38, 255, 0.05); padding: 1rem; border-radius: 10px; margin-bottom: 1rem;">
                    <strong style="color: var(--primary-purple);">📖 livros</strong><br>
                    <span style="color: var(--text-secondary); font-size: 0.9rem;">id, titulo, autor, edicao</span>
                </div>
                <div style="background: rgba(255, 0, 128, 0.05); padding: 1rem; border-radius: 10px; margin-bottom: 1rem;">
                    <strong style="color: var(--accent-pink);">📋 emprestimos</strong><br>
                    <span style="color: var(--text-secondary); font-size: 0.9rem;">id, livro_id, leitor_id, data_emprestimo, data_devolucao_plano, data_devolucao_real</span>
                </div>
                <div style="background: rgba(0, 255, 136, 0.05); padding: 1rem; border-radius: 10px;">
                    <strong style="color: var(--accent-green);">💰 multas</strong><br>
                    <span style="color: var(--text-secondary); font-size: 0.9rem;">id, emprestimo_id, valor, pago</span>
                </div>
            """, unsafe_allow_html=True)
        
        # Botões de ação
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🏠", help="Voltar ao Menu Principal", use_container_width=True):
                st.switch_page("app.py")
        
        with col2:
            if st.button("🔄", help="Reiniciar Episódio", use_container_width=True):
                st.session_state.biblioteca_puzzle_index = 0
                st.session_state.biblioteca_hint_level = 0
                st.session_state.biblioteca_completed = []
                st.rerun()
        
        # Dicas rápidas
        st.markdown("""
            <div style="background: var(--glass-bg); backdrop-filter: blur(20px); padding: 1rem; border-radius: 10px; border: 1px solid var(--border-glow); margin-top: 1rem;">
                <h4 style="color: var(--primary-cyan); font-family: 'Orbitron', sans-serif; margin-bottom: 0.5rem;">
                    💡 Dica Rápida
                </h4>
                <p style="color: var(--text-secondary); font-size: 0.9rem; margin: 0;">
                    Use JOIN para conectar tabelas relacionadas e WHERE para filtrar resultados específicos.
                </p>
            </div>
        """, unsafe_allow_html=True)
    
    # Puzzle atual
    current_puzzle_index = st.session_state.biblioteca_puzzle_index
    
    if current_puzzle_index >= len(puzzles_biblioteca):
        st.success("🎉 Parabéns! Você completou todos os puzzles do Episódio 1!")
        if st.button("🔄 Reiniciar Episódio"):
            st.session_state.biblioteca_puzzle_index = 0
            st.session_state.biblioteca_hint_level = 0
            st.session_state.biblioteca_completed = []
            st.rerun()
        return
    
    current_puzzle = puzzles_biblioteca[current_puzzle_index]
    
    # Mostrar puzzle
    st.markdown(f"""
        <div class="puzzle-container">
            <h3>🔍 Puzzle {current_puzzle_index + 1}: {current_puzzle.name}</h3>
            <p class="puzzle-description">{current_puzzle.description}</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Editor SQL
    st.markdown("### 💻 Digite sua consulta SQL:")
    user_query = st.text_area(
        "Query SQL",
        height=150,
        placeholder="SELECT * FROM ...",
        label_visibility="collapsed"
    )
    
    col1, col2, col3 = st.columns([1, 1, 3])
    
    with col1:
        execute_button = st.button("▶️ Executar Query", type="primary", use_container_width=True)
    
    with col2:
        hint_button = st.button("💡 Pedir Dica", use_container_width=True)
    
    # Processar dica
    if hint_button:
        if st.session_state.biblioteca_hint_level < 3:
            st.session_state.biblioteca_hint_level += 1
        else:
            st.info("Você já usou todas as dicas disponíveis!")
    
    # Mostrar dicas ultra modernas
    if st.session_state.biblioteca_hint_level > 0:
        st.markdown("""
            <div style="background: var(--glass-bg); backdrop-filter: blur(20px); border: 2px solid var(--border-glow-purple); border-radius: 15px; padding: 1.5rem; margin: 1rem 0;">
                <h3 style="color: var(--primary-purple); font-family: 'Orbitron', sans-serif; margin-bottom: 1rem; display: flex; align-items: center; gap: 0.5rem;">
                    💡 Dicas da Investigação
                </h3>
        """, unsafe_allow_html=True)
        
        if st.session_state.biblioteca_hint_level >= 1:
            st.markdown(f"""
                <div style="background: rgba(0, 240, 255, 0.1); border-left: 4px solid var(--primary-cyan); padding: 1rem; border-radius: 8px; margin-bottom: 1rem;">
                    <strong style="color: var(--primary-cyan);">🔍 Dica 1:</strong><br>
                    <span style="color: var(--text-primary);">{current_puzzle.hint_level_1}</span>
                </div>
            """, unsafe_allow_html=True)
        
        if st.session_state.biblioteca_hint_level >= 2:
            st.markdown(f"""
                <div style="background: rgba(176, 38, 255, 0.1); border-left: 4px solid var(--primary-purple); padding: 1rem; border-radius: 8px; margin-bottom: 1rem;">
                    <strong style="color: var(--primary-purple);">💡 Dica 2:</strong><br>
                    <span style="color: var(--text-primary);">{current_puzzle.hint_level_2}</span>
                </div>
            """, unsafe_allow_html=True)
        
        if st.session_state.biblioteca_hint_level >= 3:
            st.markdown(f"""
                <div style="background: rgba(255, 0, 128, 0.1); border-left: 4px solid var(--accent-pink); padding: 1rem; border-radius: 8px;">
                    <strong style="color: var(--accent-pink);">🎯 Dica 3:</strong><br>
                    <span style="color: var(--text-primary);">{current_puzzle.hint_level_3}</span>
                </div>
            """, unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Processar execução da query
    if execute_button and user_query.strip():
        result = puzzle_engine.execute_query(user_query, current_puzzle_index)
        
        if result['success']:
            if result['correct']:
                # Sucesso ultra moderno
                st.markdown("""
                    <div style="background: var(--glass-bg); backdrop-filter: blur(20px); border: 2px solid var(--accent-green); border-radius: 15px; padding: 2rem; margin: 1rem 0; text-align: center;">
                        <h2 style="color: var(--accent-green); font-family: 'Orbitron', sans-serif; margin-bottom: 1rem;">
                            🎉 Parabéns! Puzzle Resolvido!
                        </h2>
                        <p style="color: var(--text-primary); font-size: 1.1rem;">
                            Você desvendou o mistério com sucesso! Sua consulta SQL está correta.
                        </p>
                    </div>
                """, unsafe_allow_html=True)
                
                # Mostrar resultado
                if not result['data'].empty:
                    st.markdown("""
                        <h3 style="color: var(--primary-cyan); font-family: 'Orbitron', sans-serif; margin-bottom: 1rem;">
                            📊 Resultado da Investigação
                        </h3>
                    """, unsafe_allow_html=True)
                    st.dataframe(result['data'], use_container_width=True)
                
                # Marcar como completado
                if current_puzzle_index not in st.session_state.biblioteca_completed:
                    st.session_state.biblioteca_completed.append(current_puzzle_index)
                
                # Botão para próximo puzzle ultra moderno
                col1, col2, col3 = st.columns([1, 2, 1])
                with col2:
                    if st.button("➡️ Próximo Puzzle", use_container_width=True, type="primary"):
                        st.session_state.biblioteca_puzzle_index += 1
                        st.session_state.biblioteca_hint_level = 0
                        st.rerun()
            else:
                # Erro ultra moderno
                st.markdown("""
                    <div style="background: var(--glass-bg); backdrop-filter: blur(20px); border: 2px solid var(--error-red); border-radius: 15px; padding: 2rem; margin: 1rem 0; text-align: center;">
                        <h2 style="color: var(--error-red); font-family: 'Orbitron', sans-serif; margin-bottom: 1rem;">
                            ❌ Resultado Incorreto
                        </h2>
                        <p style="color: var(--text-primary); font-size: 1.1rem;">
                            A investigação não está completa. Analise os dados novamente e tente uma nova abordagem.
                        </p>
                    </div>
                """, unsafe_allow_html=True)
                
                # Mostrar resultado do usuário
                if not result['data'].empty:
                    st.markdown("""
                        <h3 style="color: var(--warning-yellow); font-family: 'Orbitron', sans-serif; margin-bottom: 1rem;">
                            📊 Seu Resultado Atual
                        </h3>
                    """, unsafe_allow_html=True)
                    st.dataframe(result['data'], use_container_width=True)
                
                # Mostrar resultado esperado
                expected_result = puzzle_engine.get_expected_result(current_puzzle_index)
                if not expected_result.empty:
                    st.markdown("""
                        <h3 style="color: var(--accent-green); font-family: 'Orbitron', sans-serif; margin-bottom: 1rem;">
                            ✅ Resultado Esperado
                        </h3>
                    """, unsafe_allow_html=True)
                    st.dataframe(expected_result, use_container_width=True)
        else:
            # Erro de execução ultra moderno
            st.markdown(f"""
                <div style="background: var(--glass-bg); backdrop-filter: blur(20px); border: 2px solid var(--error-red); border-radius: 15px; padding: 2rem; margin: 1rem 0;">
                    <h3 style="color: var(--error-red); font-family: 'Orbitron', sans-serif; margin-bottom: 1rem;">
                        ⚠️ Erro na Execução
                    </h3>
                    <p style="color: var(--text-primary);">
                        <strong>Detalhes do erro:</strong><br>
                        <code style="background: rgba(255, 51, 102, 0.1); padding: 0.5rem; border-radius: 5px; color: var(--error-red);">
                            {result['error']}
                        </code>
                    </p>
                    <p style="color: var(--text-secondary); margin-top: 1rem;">
                        Verifique a sintaxe da sua consulta SQL e tente novamente.
                    </p>
                </div>
            """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()


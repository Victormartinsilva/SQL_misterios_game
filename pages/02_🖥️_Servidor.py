import streamlit as st
import sys
from pathlib import Path

# Adicionar o diretório raiz ao path
root_dir = Path(__file__).parent.parent
sys.path.insert(0, str(root_dir))

from components.puzzle_engine import PuzzleEngine
from components.database import DatabaseManager
from src.server_incident.puzzles import puzzles_server_incident

# Configuração da página
st.set_page_config(
    page_title="Episódio 2: Servidor - SQL Mystery",
    page_icon="🖥️",
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
if 'servidor_puzzle_index' not in st.session_state:
    st.session_state.servidor_puzzle_index = 0
if 'servidor_hint_level' not in st.session_state:
    st.session_state.servidor_hint_level = 0
if 'servidor_completed' not in st.session_state:
    st.session_state.servidor_completed = []

# Inicializar banco de dados e engine
db_path = root_dir / "data" / "server_incident.db"
db_manager = DatabaseManager(str(db_path))
puzzle_engine = PuzzleEngine(puzzles_server_incident, db_manager)

def main():
    # Header
    st.markdown("""
        <div class="episode-header">
            <h1>🖥️ Episódio 2: Servidor</h1>
            <h2>Incidente na Madrugada</h2>
        </div>
    """, unsafe_allow_html=True)
    
    # Sidebar com progresso
    with st.sidebar:
        st.markdown("### 🎯 Progresso")
        progress = len(st.session_state.servidor_completed) / len(puzzles_server_incident)
        st.progress(progress)
        st.write(f"{len(st.session_state.servidor_completed)}/{len(puzzles_server_incident)} puzzles resolvidos")
        
        st.markdown("---")
        st.markdown("### 📊 Estrutura do Banco de Dados")
        
        with st.expander("📋 Tabelas Disponíveis"):
            st.markdown("""
            **usuarios**
            - id, username, role
            
            **acessos**
            - id, usuario_id, evento, query_text, timestamp
            
            **jobs**
            - id, nome, usuario_id, tipo, horario_cron, ultima_execucao
            
            **alerts**
            - id, nivel, mensagem, timestamp
            """)
        
        if st.button("🏠 Voltar ao Menu Principal"):
            st.switch_page("app.py")
    
    # Puzzle atual
    current_puzzle_index = st.session_state.servidor_puzzle_index
    
    if current_puzzle_index >= len(puzzles_server_incident):
        st.success("🎉 Parabéns! Você completou todos os puzzles do Episódio 2!")
        if st.button("🔄 Reiniciar Episódio"):
            st.session_state.servidor_puzzle_index = 0
            st.session_state.servidor_hint_level = 0
            st.session_state.servidor_completed = []
            st.rerun()
        return
    
    current_puzzle = puzzles_server_incident[current_puzzle_index]
    
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
        if st.session_state.servidor_hint_level < 3:
            st.session_state.servidor_hint_level += 1
        else:
            st.info("Você já usou todas as dicas disponíveis!")
    
    # Mostrar dicas
    if st.session_state.servidor_hint_level > 0:
        with st.expander("💡 Dicas", expanded=True):
            if st.session_state.servidor_hint_level >= 1:
                st.info(f"**Dica 1:** {current_puzzle.hint_level_1}")
            if st.session_state.servidor_hint_level >= 2:
                st.warning(f"**Dica 2:** {current_puzzle.hint_level_2}")
            if st.session_state.servidor_hint_level >= 3:
                st.error(f"**Dica 3:** {current_puzzle.hint_level_3}")
    
    # Processar execução da query
    if execute_button and user_query.strip():
        result = puzzle_engine.execute_query(user_query, current_puzzle_index)
        
        if result['success']:
            if result['correct']:
                st.success("✅ Correto! Você resolveu o puzzle!")
                
                # Mostrar resultado
                if not result['data'].empty:
                    st.markdown("### 📊 Resultado da Query:")
                    st.dataframe(result['data'], use_container_width=True)
                
                # Marcar como completado
                if current_puzzle_index not in st.session_state.servidor_completed:
                    st.session_state.servidor_completed.append(current_puzzle_index)
                
                # Botão para próximo puzzle
                if st.button("➡️ Próximo Puzzle"):
                    st.session_state.servidor_puzzle_index += 1
                    st.session_state.servidor_hint_level = 0
                    st.rerun()
            else:
                st.error("❌ Resultado incorreto. Tente novamente!")
                
                # Mostrar resultado do usuário
                if not result['data'].empty:
                    st.markdown("### 📊 Seu Resultado:")
                    st.dataframe(result['data'], use_container_width=True)
                
                # Mostrar resultado esperado
                expected_result = puzzle_engine.get_expected_result(current_puzzle_index)
                if not expected_result.empty:
                    st.markdown("### ✅ Resultado Esperado:")
                    st.dataframe(expected_result, use_container_width=True)
        else:
            st.error(f"❌ Erro na execução: {result['error']}")

if __name__ == "__main__":
    main()


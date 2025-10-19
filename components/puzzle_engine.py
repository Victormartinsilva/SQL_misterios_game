import pandas as pd
from typing import Dict, Any, List
from components.database import DatabaseManager

class PuzzleEngine:
    """Motor de puzzles para validar queries e gerenciar o progresso do jogo."""
    
    def __init__(self, puzzles: List, db_manager: DatabaseManager):
        """
        Inicializa o motor de puzzles.
        
        Args:
            puzzles: Lista de objetos Puzzle
            db_manager: Instância do DatabaseManager
        """
        self.puzzles = puzzles
        self.db_manager = db_manager
    
    def execute_query(self, user_query: str, puzzle_index: int) -> Dict[str, Any]:
        """
        Executa a query do usuário e valida contra a solução esperada.
        
        Args:
            user_query: Query SQL fornecida pelo usuário
            puzzle_index: Índice do puzzle atual
            
        Returns:
            Dicionário com:
            - success (bool): Se a execução foi bem-sucedida
            - correct (bool): Se a resposta está correta
            - data (pd.DataFrame): Dados retornados pela query do usuário
            - error (str ou None): Mensagem de erro, se houver
        """
        if puzzle_index >= len(self.puzzles):
            return {
                'success': False,
                'correct': False,
                'data': pd.DataFrame(),
                'error': 'Índice de puzzle inválido'
            }
        
        puzzle = self.puzzles[puzzle_index]
        
        # Executar query do usuário
        success, user_data, error = self.db_manager.execute_query(user_query)
        
        if not success:
            return {
                'success': False,
                'correct': False,
                'data': pd.DataFrame(),
                'error': error
            }
        
        # Obter resultado esperado
        expected_success, expected_data, _ = self.db_manager.execute_query(puzzle.query_solution)
        
        if not expected_success:
            return {
                'success': False,
                'correct': False,
                'data': user_data,
                'error': 'Erro ao obter resultado esperado'
            }
        
        # Validar resultado
        is_correct = self._validate_result(user_data, expected_data)
        
        return {
            'success': True,
            'correct': is_correct,
            'data': user_data,
            'error': None
        }
    
    def get_expected_result(self, puzzle_index: int) -> pd.DataFrame:
        """
        Obtém o resultado esperado para um puzzle.
        
        Args:
            puzzle_index: Índice do puzzle
            
        Returns:
            DataFrame com o resultado esperado
        """
        if puzzle_index >= len(self.puzzles):
            return pd.DataFrame()
        
        puzzle = self.puzzles[puzzle_index]
        success, data, _ = self.db_manager.execute_query(puzzle.query_solution)
        
        return data if success else pd.DataFrame()
    
    def _validate_result(self, user_df: pd.DataFrame, expected_df: pd.DataFrame) -> bool:
        """
        Valida se o resultado do usuário corresponde ao esperado.
        
        Args:
            user_df: DataFrame com resultado do usuário
            expected_df: DataFrame com resultado esperado
            
        Returns:
            True se os resultados são equivalentes, False caso contrário
        """
        # Verificar se ambos estão vazios
        if user_df.empty and expected_df.empty:
            return True
        
        # Verificar se têm a mesma forma
        if user_df.shape != expected_df.shape:
            return False
        
        # Normalizar nomes de colunas (case-insensitive)
        user_df.columns = [col.lower() for col in user_df.columns]
        expected_df.columns = [col.lower() for col in expected_df.columns]
        
        # Verificar se têm as mesmas colunas
        if set(user_df.columns) != set(expected_df.columns):
            return False
        
        # Ordenar colunas para garantir mesma ordem
        user_df = user_df[sorted(user_df.columns)]
        expected_df = expected_df[sorted(expected_df.columns)]
        
        # Ordenar linhas para comparação
        try:
            user_df_sorted = user_df.sort_values(by=list(user_df.columns)).reset_index(drop=True)
            expected_df_sorted = expected_df.sort_values(by=list(expected_df.columns)).reset_index(drop=True)
            
            return user_df_sorted.equals(expected_df_sorted)
        except Exception:
            # Se não conseguir ordenar, tentar comparação direta
            return user_df.equals(expected_df)


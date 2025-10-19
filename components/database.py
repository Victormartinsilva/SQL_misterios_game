import sqlite3
import pandas as pd
from typing import Optional, Tuple

class DatabaseManager:
    """Gerenciador de conexão e execução de queries no banco de dados SQLite."""
    
    def __init__(self, db_path: str):
        """
        Inicializa o gerenciador de banco de dados.
        
        Args:
            db_path: Caminho para o arquivo do banco de dados SQLite
        """
        self.db_path = db_path
    
    def execute_query(self, query: str) -> Tuple[bool, Optional[pd.DataFrame], Optional[str]]:
        """
        Executa uma query SQL e retorna o resultado.
        
        Args:
            query: Query SQL a ser executada
            
        Returns:
            Tupla contendo:
            - success (bool): Se a execução foi bem-sucedida
            - data (pd.DataFrame ou None): Dados retornados pela query
            - error (str ou None): Mensagem de erro, se houver
        """
        try:
            conn = sqlite3.connect(self.db_path)
            
            # Executar a query e obter resultado
            df = pd.read_sql_query(query, conn)
            
            conn.close()
            
            return True, df, None
            
        except Exception as e:
            return False, None, str(e)
    
    def get_table_schema(self, table_name: str) -> Optional[pd.DataFrame]:
        """
        Obtém o schema de uma tabela específica.
        
        Args:
            table_name: Nome da tabela
            
        Returns:
            DataFrame com informações das colunas ou None em caso de erro
        """
        try:
            conn = sqlite3.connect(self.db_path)
            query = f"PRAGMA table_info({table_name});"
            df = pd.read_sql_query(query, conn)
            conn.close()
            return df
        except Exception:
            return None
    
    def get_all_tables(self) -> list:
        """
        Obtém lista de todas as tabelas no banco de dados.
        
        Returns:
            Lista com nomes das tabelas
        """
        try:
            conn = sqlite3.connect(self.db_path)
            query = "SELECT name FROM sqlite_master WHERE type='table';"
            df = pd.read_sql_query(query, conn)
            conn.close()
            return df['name'].tolist()
        except Exception:
            return []


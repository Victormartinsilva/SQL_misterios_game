
import sqlite3
import pandas as pd
from rich.console import Console
from src.common.db import create_tables, execute_sql_from_file
from src.ui.terminal_ui import display_title, display_message, get_user_input, display_table, display_error
from src.server_incident.puzzles import puzzles_server_incident, Puzzle

console = Console()

DB_PATH = "sql-mystery/data/server_incident.db"
SEED_PATH = "sql-mystery/seeds/seed_server.sql"

def setup_database():
    create_tables(DB_PATH)
    execute_sql_from_file(DB_PATH, SEED_PATH)

def run_query(query):
    conn = None
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute(query)
        
        # Fetch column names
        columns = [description[0] for description in cursor.description]
        
        results = cursor.fetchall()
        return columns, results
    except sqlite3.Error as e:
        display_error(f"Erro ao executar a query: {e}")
        return None, None
    finally:
        if conn:
            conn.close()

def get_expected_result(query_solution):
    conn = None
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute(query_solution)
        results = cursor.fetchall()
        columns = [description[0] for description in cursor.description]
        return pd.DataFrame(results, columns=columns)
    except sqlite3.Error as e:
        display_error(f"Erro ao obter o resultado esperado: {e}")
        return pd.DataFrame()
    finally:
        if conn:
            conn.close()

def play_server_incident_game():
    display_title("SQL Mystery: O Detetive de Banco de Dados - Episódio 2: Queda do Servidor")
    display_message("Um servidor de dados caiu na madrugada! Use suas habilidades em SQL para investigar o incidente.")
    
    setup_database()

    for i, puzzle in enumerate(puzzles_server_incident):
        display_title(f"Puzzle {i+1}: {puzzle.name}")
        display_message(puzzle.description)
        
        attempts = 0
        max_attempts = 3
        
        while attempts < max_attempts:
            user_query = get_user_input("Digite sua query SQL aqui (ou 'dica' para uma dica):\n")
            
            if user_query.lower() == 'dica':
                attempts += 1
                if attempts == 1:
                    display_message(f"Dica 1: {puzzle.hint_level_1}", style="yellow")
                elif attempts == 2:
                    display_message(f"Dica 2: {puzzle.hint_level_2}", style="yellow")
                elif attempts == 3:
                    display_message(f"Dica 3: {puzzle.hint_level_3}", style="yellow")
                continue

            columns, user_query_result = run_query(user_query)
            
            if user_query_result is not None:
                display_message("Resultado da sua query:")
                display_table(user_query_result, columns)
                
                expected_df = get_expected_result(puzzle.query_solution)
                
                if puzzle.validate_query(user_query_result, expected_df):
                    display_message("Parabéns! Query correta! Você resolveu este puzzle.", style="green")
                    break
                else:
                    display_message("Query incorreta ou resultado inesperado. Tente novamente.", style="red")
            
            attempts += 1
            if attempts < max_attempts:
                display_message(f"Tentativas restantes: {max_attempts - attempts}", style="yellow")
        else:
            display_message(f"Você esgotou suas tentativas para este puzzle. A solução era:\n{puzzle.query_solution}", style="red")
            display_message("Avançando para o próximo puzzle...", style="yellow")

    display_title("Parabéns, Detetive!")
    display_message("Você resolveu todos os mistérios da Queda do Servidor!", style="bold green")

if __name__ == "__main__":
    play_server_incident_game()


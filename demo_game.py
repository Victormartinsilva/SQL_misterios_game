#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Demonstração do SQL Mystery Game
Este script mostra como o jogo funciona sem interação do usuário
"""

import sys
import os
import sqlite3
import pandas as pd

# Configurar codificação para Windows
if sys.platform == "win32":
    os.system("chcp 65001 > nul")

from src.ui.terminal_ui import display_title, display_message, display_table, clear_screen
from src.common.db import create_tables, execute_sql_from_file

def demo_biblioteca():
    """Demonstra o jogo da Biblioteca"""
    clear_screen()
    display_title("Episódio 1: Biblioteca - O Livro Raro")
    
    # Configurar banco de dados
    DB_PATH = "data/biblioteca.db"
    SEED_PATH = "seeds/seed_biblioteca.sql"
    
    display_message("Usando banco de dados existente...", style="yellow")
    # create_tables(DB_PATH)
    # execute_sql_from_file(DB_PATH, SEED_PATH)
    
    # Mostrar estrutura do banco
    display_message("\nEstrutura do Banco de Dados da Biblioteca:", style="bold blue")
    display_message("Tabelas disponíveis:", style="green")
    display_message("• leitores (id, nome, email)")
    display_message("• livros (id, titulo, autor, edicao)")
    display_message("• emprestimos (id, livro_id, leitor_id, data_emprestimo, data_devolucao_plano, data_devolucao_real)")
    display_message("• multas (id, emprestimo_id, valor, pago)")
    
    # Mostrar dados de exemplo
    conn = sqlite3.connect(DB_PATH)
    
    display_message("\nLivros disponíveis:", style="bold blue")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM livros")
    livros = cursor.fetchall()
    display_table(livros, ["ID", "Título", "Autor", "Edição"])
    
    display_message("\nLeitores cadastrados:", style="bold blue")
    cursor.execute("SELECT * FROM leitores")
    leitores = cursor.fetchall()
    display_table(leitores, ["ID", "Nome", "Email"])
    
    display_message("\nEmpréstimos:", style="bold blue")
    cursor.execute("SELECT e.id, l.nome, li.titulo, e.data_emprestimo, e.data_devolucao_plano, e.data_devolucao_real FROM emprestimos e JOIN leitores l ON e.leitor_id = l.id JOIN livros li ON e.livro_id = li.id")
    emprestimos = cursor.fetchall()
    display_table(emprestimos, ["ID", "Leitor", "Livro", "Data Empréstimo", "Devolução Plano", "Devolução Real"])
    
    # Exemplo de puzzle
    display_message("\nExemplo de Puzzle:", style="bold red")
    display_message("MISTÉRIO: Um livro raro não foi devolvido! Descubra qual livro e quem o emprestou.")
    display_message("DICA: Procure por empréstimos onde data_devolucao_real é NULL")
    
    # Solução do puzzle
    display_message("\nSolução:", style="bold green")
    cursor.execute("""
        SELECT l.nome, li.titulo, e.data_emprestimo, e.data_devolucao_plano
        FROM emprestimos e 
        JOIN leitores l ON e.leitor_id = l.id 
        JOIN livros li ON e.livro_id = li.id 
        WHERE e.data_devolucao_real IS NULL
    """)
    resultado = cursor.fetchall()
    display_table(resultado, ["Leitor", "Livro", "Data Empréstimo", "Devolução Plano"])
    
    conn.close()
    
    display_message("\n[SUCCESS] Demonstração concluída!", style="bold green")

def demo_server_incident():
    """Demonstra o jogo do Server Incident"""
    clear_screen()
    display_title("Episódio 2: Queda do Servidor - Incidente na Madrugada")
    
    # Configurar banco de dados
    DB_PATH = "data/server_incident.db"
    SEED_PATH = "seeds/seed_server.sql"
    
    display_message("Usando banco de dados existente...", style="yellow")
    # create_tables(DB_PATH)
    # execute_sql_from_file(DB_PATH, SEED_PATH)
    
    # Mostrar estrutura do banco
    display_message("\nEstrutura do Banco de Dados do Servidor:", style="bold blue")
    display_message("Tabelas disponíveis:", style="green")
    display_message("• usuarios (id, username, role)")
    display_message("• acessos (id, usuario_id, evento, query_text, timestamp)")
    display_message("• jobs (id, nome, usuario_id, tipo, horario_cron, ultima_execucao)")
    display_message("• alerts (id, nivel, mensagem, timestamp)")
    
    # Mostrar dados de exemplo
    conn = sqlite3.connect(DB_PATH)
    
    display_message("\nUsuários do sistema:", style="bold blue")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    display_table(usuarios, ["ID", "Username", "Role"])
    
    display_message("\nAcessos registrados:", style="bold blue")
    cursor.execute("SELECT a.id, u.username, a.evento, a.query_text, a.timestamp FROM acessos a JOIN usuarios u ON a.usuario_id = u.id ORDER BY a.timestamp")
    acessos = cursor.fetchall()
    display_table(acessos, ["ID", "Usuário", "Evento", "Query", "Timestamp"])
    
    display_message("\nAlertas do sistema:", style="bold blue")
    cursor.execute("SELECT * FROM alerts ORDER BY timestamp")
    alerts = cursor.fetchall()
    display_table(alerts, ["ID", "Nível", "Mensagem", "Timestamp"])
    
    # Exemplo de puzzle
    display_message("\nExemplo de Puzzle:", style="bold red")
    display_message("MISTÉRIO: O servidor caiu! Descubra quem pode ter causado o problema.")
    display_message("DICA: Procure por operações perigosas como DROP ou DELETE")
    
    # Solução do puzzle
    display_message("\nSolução:", style="bold green")
    cursor.execute("""
        SELECT u.username, u.role, a.evento, a.query_text, a.timestamp
        FROM acessos a 
        JOIN usuarios u ON a.usuario_id = u.id 
        WHERE a.evento IN ('DROP', 'DELETE')
        ORDER BY a.timestamp DESC
    """)
    resultado = cursor.fetchall()
    display_table(resultado, ["Usuário", "Role", "Evento", "Query", "Timestamp"])
    
    conn.close()
    
    display_message("\n[SUCCESS] Demonstração concluída!", style="bold green")

def main():
    clear_screen()
    display_title("SQL Mystery: Demonstração do Jogo")
    display_message("Este é um jogo educacional para aprender SQL de forma prática!")
    display_message("Você assume o papel de um detetive que resolve mistérios usando consultas SQL.")
    
    display_message("\nEscolha qual demonstração você quer ver:")
    display_message("1. Episódio 1: Biblioteca - O Livro Raro")
    display_message("2. Episódio 2: Queda do Servidor - Incidente na Madrugada")
    display_message("3. Ambos")
    
    # Para demonstração, vamos mostrar ambos
    display_message("\n[DEMO] Executando ambas as demonstrações...", style="yellow")
    
    try:
        demo_biblioteca()
        
        display_message("\n" + "="*60, style="blue")
        display_message("Continuando para o próximo episódio...", style="cyan")
        # input()  # Removido para funcionar em ambiente não-interativo
        
        demo_server_incident()
        
        display_message("\n[SUCCESS] Demonstração completa!", style="bold magenta")
        display_message("Para jogar o jogo completo com interação, execute: python main.py", style="green")
        
    except Exception as e:
        display_message(f"Erro durante a demonstração: {str(e)}", style="red")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()

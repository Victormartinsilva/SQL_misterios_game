#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script de teste para o SQL Mystery Game
Este script demonstra o funcionamento do jogo sem interação do usuário
"""

import sys
import os

# Configurar codificação para Windows
if sys.platform == "win32":
    os.system("chcp 65001 > nul")

from src.ui.terminal_ui import display_title, display_message, display_table, clear_screen
from src.biblioteca.game import play_biblioteca_game
from src.server_incident.game import play_server_incident_game

def simulate_user_input():
    """Simula entrada do usuário para demonstração"""
    return "1"  # Escolhe o Episódio 1

def main():
    clear_screen()
    display_title("Bem-vindo ao SQL Mystery: O Detetive de Banco de Dados")
    display_message("Escolha qual mistério você quer resolver:")
    display_message("1. Episódio 1: Biblioteca - O Livro Raro")
    display_message("2. Episódio 2: Queda do Servidor - Incidente na Madrugada")
    display_message("3. Sair")
    
    display_message("\n[DEMO] Executando Episódio 1: Biblioteca - O Livro Raro", style="yellow")
    display_message("=" * 60, style="blue")
    
    try:
        # Simular escolha do usuário
        choice = simulate_user_input()
        
        if choice == "1":
            clear_screen()
            display_message("Iniciando Episódio 1: Biblioteca - O Livro Raro", style="bold green")
            play_biblioteca_game()
        elif choice == "2":
            clear_screen()
            display_message("Iniciando Episódio 2: Queda do Servidor - Incidente na Madrugada", style="bold green")
            play_server_incident_game()
        elif choice == "3":
            display_message("Obrigado por jogar SQL Mystery!", style="bold magenta")
        else:
            display_message("Escolha inválida. Por favor, digite 1, 2 ou 3.", style="red")
            
    except Exception as e:
        display_message(f"Erro durante a execução: {str(e)}", style="red")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()




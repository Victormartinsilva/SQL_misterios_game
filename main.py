
from src.ui.terminal_ui import display_title, display_message, get_user_input, clear_screen
from src.biblioteca.game import play_biblioteca_game
from src.server_incident.game import play_server_incident_game

def main():
    clear_screen()
    display_title("Bem-vindo ao SQL Mystery: O Detetive de Banco de Dados")
    display_message("Escolha qual mistério você quer resolver:")
    display_message("1. Episódio 1: Biblioteca - O Livro Raro")
    display_message("2. Episódio 2: Queda do Servidor - Incidente na Madrugada")
    display_message("3. Sair")

    choice = get_user_input("Digite o número da sua escolha: ")

    if choice == "1":
        clear_screen()
        play_biblioteca_game()
    elif choice == "2":
        clear_screen()
        play_server_incident_game()
    elif choice == "3":
        display_message("Obrigado por jogar SQL Mystery!", style="bold magenta")
    else:
        display_message("Escolha inválida. Por favor, digite 1, 2 ou 3.", style="red")
        main() # Loop back to main menu

if __name__ == "__main__":
    main()


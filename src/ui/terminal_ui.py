
from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table
import sys
import os

# Configurar console para Windows com codificação UTF-8
if sys.platform == "win32":
    # Configurar codificação para Windows
    os.system("chcp 65001 > nul")
    
console = Console()

def display_title(title):
    console.print(Panel(Text(title, justify="center", style="bold magenta"), border_style="blue"))

def display_message(message, style="green"):
    console.print(Text(message, style=style))

def get_user_input(prompt_message, password=False):
    try:
        return Prompt.ask(Text(prompt_message, style="cyan"), password=password)
    except (EOFError, KeyboardInterrupt):
        # Fallback para entrada simples se Prompt.ask falhar
        console.print(Text(prompt_message, style="cyan"), end="")
        return input()

def display_table(data, headers):
    if not data:
        display_message("Nenhum resultado encontrado.", style="yellow")
        return

    table = Table(show_header=True, header_style="bold green")
    for header in headers:
        table.add_column(header)

    for row in data:
        table.add_row(*[str(item) for item in row])
    console.print(table)

def clear_screen():
    console.clear()

def display_error(message):
    console.print(Panel(Text(f"ERRO: {message}", style="bold red"), border_style="red"))



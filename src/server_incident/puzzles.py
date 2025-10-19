
import pandas as pd
from rich.console import Console

console = Console()

class Puzzle:
    def __init__(self, name, description, query_solution, hint_level_1, hint_level_2, hint_level_3):
        self.name = name
        self.description = description
        self.query_solution = query_solution
        self.hint_level_1 = hint_level_1
        self.hint_level_2 = hint_level_2
        self.hint_level_3 = hint_level_3

    def validate_query(self, user_query_result, expected_result_df):
        if user_query_result is None:
            return False
        
        user_df = pd.DataFrame(user_query_result)
        
        if user_df.empty and expected_result_df.empty:
            return True
        
        if user_df.shape != expected_result_df.shape:
            return False
            
        user_df_sorted = user_df.sort_values(by=list(user_df.columns)).reset_index(drop=True)
        expected_df_sorted = expected_result_df.sort_values(by=list(expected_result_df.columns)).reset_index(drop=True)

        return user_df_sorted.equals(expected_df_sorted)

# Puzzles para o jogo da Queda do Servidor
puzzles_server_incident = [
    Puzzle(
        name="Logs Iniciais",
        description="O servidor caiu na madrugada. Filtre os eventos de acesso que ocorreram entre 01:00 e 04:00 do dia 2025-10-10. Liste o timestamp, o evento e o ID do usuário.",
        query_solution="""
SELECT timestamp, evento, usuario_id
FROM acessos
WHERE timestamp BETWEEN '2025-10-10 01:00:00' AND '2025-10-10 04:00:00';
""",
        hint_level_1="Use a cláusula WHERE com BETWEEN para filtrar por um intervalo de tempo.",
        hint_level_2="Sua query deve selecionar as colunas timestamp, evento e usuario_id da tabela acessos. O filtro de tempo deve ser BETWEEN '2025-10-10 01:00:00' AND '2025-10-10 04:00:00'.",
        hint_level_3="A query deve ser: SELECT timestamp, evento, usuario_id FROM acessos WHERE timestamp BETWEEN '2025-10-10 01:00:00' AND '2025-10-10 04:00:00';"
    ),
    Puzzle(
        name="Atividades Suspeitas",
        description="Identifique quais usuários realizaram eventos de 'DROP' ou 'DELETE' no período crítico (entre 01:00 e 04:00 do dia 2025-10-10). Liste o nome do usuário, o evento e o timestamp.",
        query_solution="""
SELECT u.username, a.evento, a.timestamp
FROM acessos a
JOIN usuarios u ON u.id = a.usuario_id
WHERE a.evento IN ('DROP', 'DELETE')
AND a.timestamp BETWEEN '2025-10-10 01:00:00' AND '2025-10-10 04:00:00';
""",
        hint_level_1="Você precisará juntar a tabela 'acessos' com 'usuarios' e filtrar por eventos específicos e um intervalo de tempo.",
        hint_level_2="Use JOIN para conectar 'acessos' e 'usuarios'. Filtre por 'evento IN ('DROP', 'DELETE')' e o mesmo intervalo de tempo do puzzle anterior.",
        hint_level_3="A query deve ser: SELECT u.username, a.evento, a.timestamp FROM acessos a JOIN usuarios u ON u.id = a.usuario_id WHERE a.evento IN ('DROP', 'DELETE') AND a.timestamp BETWEEN '2025-10-10 01:00:00' AND '2025-10-10 04:00:00';"
    ),
    Puzzle(
        name="Jobs Agendados e Acessos",
        description="Correlacione os jobs agendados com os acessos dos usuários no período crítico. Liste o nome do usuário, o nome do job, o evento de acesso e o timestamp do acesso.",
        query_solution="""
SELECT u.username, j.nome AS job_nome, a.evento, a.timestamp
FROM acessos a
JOIN usuarios u ON u.id = a.usuario_id
LEFT JOIN jobs j ON j.usuario_id = u.id AND j.ultima_execucao BETWEEN '2025-10-10 01:00:00' AND '2025-10-10 04:00:00'
WHERE a.timestamp BETWEEN '2025-10-10 01:00:00' AND '2025-10-10 04:00:00'
ORDER BY a.timestamp;
""",
        hint_level_1="Use um LEFT JOIN para incluir os jobs mesmo que não haja correspondência direta com os acessos. Lembre-se de filtrar ambos por tempo.",
        hint_level_2="Junte 'acessos', 'usuarios' e 'jobs'. O JOIN com 'jobs' deve ser LEFT JOIN e incluir a condição de tempo para 'ultima_execucao'. Filtre os acessos pelo período crítico.",
        hint_level_3="A query deve ser: SELECT u.username, j.nome AS job_nome, a.evento, a.timestamp FROM acessos a JOIN usuarios u ON u.id = a.usuario_id LEFT JOIN jobs j ON j.usuario_id = u.id AND j.ultima_execucao BETWEEN '2025-10-10 01:00:00' AND '2025-10-10 04:00:00' WHERE a.timestamp BETWEEN '2025-10-10 01:00:00' AND '2025-10-10 04:00:00' ORDER BY a.timestamp;"
    ),
    Puzzle(
        name="O Culpado Final",
        description="Encontre o usuário que executou o maior número de eventos 'DROP' ou 'DELETE' no período crítico (entre 01:00 e 04:00 do dia 2025-10-10). Liste o nome do usuário e a contagem de eventos.",
        query_solution="""
SELECT u.username, COUNT(a.id) AS total_eventos_deletorios
FROM acessos a
JOIN usuarios u ON u.id = a.usuario_id
WHERE a.evento IN ('DROP', 'DELETE')
AND a.timestamp BETWEEN '2025-10-10 01:00:00' AND '2025-10-10 04:00:00'
GROUP BY u.username
ORDER BY total_eventos_deletorios DESC
LIMIT 1;
""",
        hint_level_1="Agrupe os resultados por usuário e conte os eventos 'DROP' ou 'DELETE'. Use ORDER BY e LIMIT para encontrar o maior.",
        hint_level_2="Junte 'acessos' e 'usuarios'. Filtre por eventos 'DROP' ou 'DELETE' e o período crítico. Use GROUP BY no nome do usuário, COUNT para os eventos, e depois ORDER BY e LIMIT 1.",
        hint_level_3="A query deve ser: SELECT u.username, COUNT(a.id) AS total_eventos_deletorios FROM acessos a JOIN usuarios u ON u.id = a.usuario_id WHERE a.evento IN ('DROP', 'DELETE') AND a.timestamp BETWEEN '2025-10-10 01:00:00' AND '2025-10-10 04:00:00' GROUP BY u.username ORDER BY total_eventos_deletorios DESC LIMIT 1;"
    )
]


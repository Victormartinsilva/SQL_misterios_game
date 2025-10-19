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

puzzles_biblioteca = [
    Puzzle(
        name="Inventário de Livros",
        description="O bibliotecário precisa de uma lista de todos os livros disponíveis. Selecione o título e o autor de todos os livros.",
        query_solution="SELECT titulo, autor FROM livros;",
        hint_level_1="Lembre-se de como selecionar colunas específicas de uma tabela.",
        hint_level_2="Use SELECT seguido dos nomes das colunas e FROM seguido do nome da tabela 'livros'.",
        hint_level_3="A query deve ser 'SELECT titulo, autor FROM livros;'"
    ),
    Puzzle(
        name="Livro Raro Desaparecido",
        description="O exemplar raro 'A História dos Bancos de Dados', 1ª edição, não foi devolvido. Descubra quem o pegou. Liste o nome do leitor e o título do livro que ele não devolveu.",
        query_solution='''
SELECT l.nome, lv.titulo
FROM emprestimos e
JOIN leitores l ON l.id = e.leitor_id
JOIN livros lv ON lv.id = e.livro_id
WHERE e.data_devolucao_real IS NULL
AND lv.titulo = 'A História dos Bancos de Dados'
AND lv.edicao = 1;
''',
        hint_level_1="Você precisará juntar informações de várias tabelas: emprestimos, leitores e livros. Pense nos JOINs.",
        hint_level_2="Use JOINs para conectar 'emprestimos' com 'leitores' e 'livros'. Filtre por 'data_devolucao_real IS NULL' e o título/edição do livro.",
        hint_level_3="A query deve ser algo como: SELECT l.nome, lv.titulo FROM emprestimos e JOIN leitores l ON l.id = e.leitor_id JOIN livros lv ON lv.id = e.livro_id WHERE e.data_devolucao_real IS NULL AND lv.titulo = 'A História dos Bancos de Dados' AND lv.edicao = 1;"
    ),
    Puzzle(
        name="Empréstimos Atrasados",
        description="Descubra quais leitores têm livros com data de devolução planejada no passado e ainda não foram devolvidos. Liste o nome do leitor, o título do livro e a data de devolução planejada.",
        query_solution='''
SELECT l.nome, lv.titulo, e.data_devolucao_plano
FROM emprestimos e
JOIN leitores l ON l.id = e.leitor_id
JOIN livros lv ON lv.id = e.livro_id
WHERE e.data_devolucao_real IS NULL
AND e.data_devolucao_plano < date('now');
''',
        hint_level_1="Combine JOINs e use a função 'date('now')' para comparar datas. Lembre-se de filtrar por livros não devolvidos.",
        hint_level_2="Sua query deve juntar 'emprestimos', 'leitores' e 'livros'. Use WHERE para 'data_devolucao_real IS NULL' e 'data_devolucao_plano < date('now')'.",
        hint_level_3="A query deve ser: SELECT l.nome, lv.titulo, e.data_devolucao_plano FROM emprestimos e JOIN leitores l ON l.id = e.leitor_id JOIN livros lv ON lv.id = e.livro_id WHERE e.data_devolucao_real IS NULL AND e.data_devolucao_plano < date('now');"
    ),
    Puzzle(
        name="Leitor Mais Inadimplente",
        description="Qual leitor tem o maior número de empréstimos não devolvidos? Liste o nome do leitor e a contagem de livros não devolvidos.",
        query_solution='''
SELECT l.nome, COUNT(e.id) AS livros_nao_devolvidos
FROM emprestimos e
JOIN leitores l ON l.id = e.leitor_id
WHERE e.data_devolucao_real IS NULL
GROUP BY l.nome
ORDER BY livros_nao_devolvidos DESC
LIMIT 1;
''',
        hint_level_1="Você precisará agrupar os resultados por leitor e contar os empréstimos não devolvidos. Pense em GROUP BY e COUNT.",
        hint_level_2="Junte 'emprestimos' e 'leitores'. Filtre por 'data_devolucao_real IS NULL'. Use GROUP BY no nome do leitor e COUNT para os empréstimos. Ordene e limite para o primeiro.",
        hint_level_3="A query deve ser: SELECT l.nome, COUNT(e.id) AS livros_nao_devolvidos FROM emprestimos e JOIN leitores l ON l.id = e.leitor_id WHERE e.data_devolucao_real IS NULL GROUP BY l.nome ORDER BY livros_nao_devolvidos DESC LIMIT 1;"
    )
]

# SQL Mystery: O Detetive de Banco de Dados

Este projeto é um jogo educacional interativo desenvolvido em Python para ensinar SQL de forma prática e divertida. O jogador assume o papel de um detetive que precisa resolver mistérios utilizando consultas SQL em um banco de dados SQLite.

## Conteúdo

1.  [Visão Geral](#visão-geral)
2.  [Estrutura do Projeto](#estrutura-do-projeto)
3.  [Instalação e Configuração](#instalação-e-configuração)
4.  [Como Jogar](#como-jogar)
5.  [Mecânica do Jogo](#mecânica-do-jogo)
6.  [Estrutura do Banco de Dados](#estrutura-do-banco-de-dados)
7.  [Manutenção e Melhorias](#manutenção-e-melhorias)
    *   [Adicionar Novos Puzzles](#adicionar-novos-puzzles)
    *   [Modificar Puzzles Existentes](#modificar-puzzles-existentes)
    *   [Gerenciar Bancos de Dados](#gerenciar-bancos-de-dados)
    *   [Melhorias na Interface](#melhorias-na-interface)
8.  [Créditos](#créditos)

## Visão Geral

O jogo `SQL Mystery` apresenta dois episódios principais, cada um com um cenário e um conjunto de puzzles que exigem diferentes habilidades em SQL:

*   **Episódio 1: Biblioteca - O Livro Raro**: Foca em `SELECT`, `WHERE`, `ORDER BY`, `GROUP BY`, `JOIN` simples e funções agregadas para descobrir quem não devolveu um livro raro.
*   **Episódio 2: Queda do Servidor - Incidente na Madrugada**: Aborda `JOINs` mais complexos, `subqueries`, `filtros`, `UNION` e análise temporal para investigar a queda de um servidor de dados.

A interface é baseada em terminal, utilizando a biblioteca `rich` para uma experiência visual aprimorada e `prompt_toolkit` para interações de usuário mais ricas.

## Estrutura do Projeto

A estrutura de diretórios do projeto é organizada da seguinte forma:

```
sql-mystery/
├── data/                 # Arquivos .db de exemplo (bancos de dados SQLite)
│   ├── biblioteca.db
│   └── server_incident.db
├── seeds/                # Scripts SQL para popular os bancos de dados
│   ├── seed_biblioteca.sql
│   └── seed_server.sql
├── src/                  # Código fonte principal do jogo
│   ├── common/           # Módulos comuns (conexão com DB, utilitários)
│   │   └── db.py
│   ├── biblioteca/       # Lógica e puzzles do Episódio 1 (Biblioteca)
│   │   ├── game.py
│   │   └── puzzles.py
│   ├── server_incident/  # Lógica e puzzles do Episódio 2 (Queda do Servidor)
│   │   ├── game.py
│   │   └── puzzles.py
│   └── ui/               # Módulos de interface de usuário (terminal)
│       └── terminal_ui.py
├── assets/               # Imagens e outros recursos visuais
├── main.py               # Ponto de entrada principal do jogo
├── README.md             # Este arquivo de documentação
└── requirements.txt      # Dependências do Python
```

## Instalação e Configuração

Para configurar e executar o jogo, siga os passos abaixo:

1.  **Clone o repositório (ou descompacte o ZIP)**:

    ```bash
    git clone https://github.com/seu-usuario/sql-mystery.git
    cd sql-mystery
    ```

2.  **Crie um ambiente virtual (recomendado)**:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    ```

3.  **Instale as dependências**: As bibliotecas necessárias estão listadas em `requirements.txt`.

    ```bash
    pip install -r requirements.txt
    ```

4.  **Inicialize os bancos de dados**: Os scripts de seed criarão e popularão os bancos de dados SQLite necessários para o jogo.

    ```bash
    python3 -c "from src.common.db import create_tables, execute_sql_from_file; create_tables(\'data/biblioteca.db\'); execute_sql_from_file(\'data/biblioteca.db\', \'seeds/seed_biblioteca.sql\'); create_tables(\'data/server_incident.db\'); execute_sql_from_file(\'data/server_incident.db\', \'seeds/seed_server.sql\')"
    ```
    *Nota: Este comando é para configuração inicial. Os arquivos `game.py` de cada episódio também chamam `setup_database()` que recria e popula o banco de dados do episódio, garantindo um estado limpo a cada nova partida.* 

## Como Jogar

Para iniciar o jogo, execute o arquivo `main.py`:

```bash
python3 main.py
```

Você será apresentado a um menu onde poderá escolher entre os dois episódios. Siga as instruções na tela, digite suas queries SQL e tente resolver os mistérios. Você pode digitar `dica` a qualquer momento para receber uma ajuda.

## Mecânica do Jogo

Cada episódio é composto por uma série de puzzles. Para cada puzzle, você receberá uma descrição do problema e deverá escrever uma consulta SQL para resolvê-lo. O jogo validará sua query comparando o resultado com a solução esperada. Se sua query estiver incorreta, você terá mais tentativas e poderá pedir dicas.

*   **Validação de Queries**: O sistema compara o `DataFrame` resultante da sua query com o `DataFrame` da query de solução esperada. A ordem das linhas e colunas é normalizada para permitir flexibilidade nas suas respostas, desde que o conjunto de dados final seja o mesmo.
*   **Sistema de Dicas**: Você tem até 3 níveis de dicas para cada puzzle. Basta digitar `dica` no prompt da query para recebê-las. As dicas se tornam progressivamente mais explícitas.

## Estrutura do Banco de Dados

### Episódio 1: Biblioteca

**Tabelas:**

*   `leitores`: `id`, `nome`, `email`
*   `livros`: `id`, `titulo`, `autor`, `edicao`
*   `emprestimos`: `id`, `livro_id`, `leitor_id`, `data_emprestimo`, `data_devolucao_plano`, `data_devolucao_real`
*   `multas`: `id`, `emprestimo_id`, `valor`, `pago`

### Episódio 2: Queda do Servidor

**Tabelas:**

*   `usuarios`: `id`, `username`, `role`
*   `acessos`: `id`, `usuario_id`, `evento`, `query_text`, `timestamp`
*   `jobs`: `id`, `nome`, `usuario_id`, `tipo`, `horario_cron`, `ultima_execucao`
*   `alerts`: `id`, `nivel`, `mensagem`, `timestamp`

## Manutenção e Melhorias

### Adicionar Novos Puzzles

Para adicionar um novo puzzle a um episódio existente:

1.  **Edite o arquivo `puzzles.py`** correspondente (`src/biblioteca/puzzles.py` ou `src/server_incident/puzzles.py`).
2.  **Crie uma nova instância da classe `Puzzle`**, fornecendo:
    *   `name`: Nome do puzzle.
    *   `description`: Descrição detalhada do problema.
    *   `query_solution`: A query SQL correta que resolve o puzzle.
    *   `hint_level_1`, `hint_level_2`, `hint_level_3`: Dicas para ajudar o jogador.
3.  **Adicione a nova instância à lista `puzzles_biblioteca` ou `puzzles_server_incident`**.

Exemplo:

```python
# Em src/biblioteca/puzzles.py
puzzles_biblioteca = [
    # ... puzzles existentes ...
    Puzzle(
        name="Novo Desafio",
        description="Descrição do novo desafio SQL.",
        query_solution="SELECT * FROM alguma_tabela;",
        hint_level_1="Primeira dica.",
        hint_level_2="Segunda dica.",
        hint_level_3="Terceira dica."
    ),
]
```

### Modificar Puzzles Existentes

Para modificar um puzzle existente, basta editar os atributos da instância `Puzzle` correspondente no arquivo `puzzles.py` do episódio.

### Gerenciar Bancos de Dados

Os bancos de dados são criados e populados a partir dos scripts em `seeds/`. Para modificar os dados iniciais ou o schema:

1.  **Edite os arquivos `.sql`** em `seeds/` para alterar os dados de inserção.
2.  **Edite a função `create_tables`** em `src/common/db.py` para alterar o schema das tabelas.
3.  **Execute o `main.py`** ou o comando de inicialização do banco de dados para aplicar as mudanças.

### Melhorias na Interface

A interface atual é baseada em terminal com `rich`. Para melhorias:

*   **Estilos `rich`**: Explore mais opções de estilo e formatação da biblioteca `rich` em `src/ui/terminal_ui.py`.
*   **Interface Web (Streamlit/Flask)**: O protótipo original mencionou a possibilidade de uma interface web. Isso exigiria a criação de um novo módulo `web_ui.py` em `src/ui/` e a adaptação da lógica do jogo para interagir com um framework web (e.g., Flask ou Streamlit).

## Créditos

Desenvolvido por Manus AI.

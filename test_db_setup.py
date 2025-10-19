import os
from src.common.db import create_tables, execute_sql_from_file

# Remove bancos de dados existentes se existirem
if os.path.exists('data/biblioteca.db'):
    os.remove('data/biblioteca.db')
    print('Banco de dados da Biblioteca removido.')

if os.path.exists('data/server_incident.db'):
    os.remove('data/server_incident.db')
    print('Banco de dados do Server Incident removido.')

# Cria diretório data se não existir
os.makedirs('data', exist_ok=True)

# Teste para Biblioteca
create_tables('data/biblioteca.db')
execute_sql_from_file('data/biblioteca.db', 'seeds/seed_biblioteca.sql')
print('Banco de dados da Biblioteca criado com sucesso!')

# Teste para Server Incident
create_tables('data/server_incident.db')
execute_sql_from_file('data/server_incident.db', 'seeds/seed_server.sql')
print('Banco de dados do Server Incident criado com sucesso!')

print('\n[SUCCESS] Todos os bancos de dados foram configurados com sucesso!')


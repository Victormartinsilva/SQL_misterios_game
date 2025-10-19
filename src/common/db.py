
import sqlite3
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./sql-mystery.db"

# SQLAlchemy setup
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_tables(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Schema para o jogo da Biblioteca
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS leitores (
            id INTEGER PRIMARY KEY,
            nome TEXT,
            email TEXT
        );
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS livros (
            id INTEGER PRIMARY KEY,
            titulo TEXT,
            autor TEXT,
            edicao INTEGER
        );
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS emprestimos (
            id INTEGER PRIMARY KEY,
            livro_id INTEGER,
            leitor_id INTEGER,
            data_emprestimo DATE,
            data_devolucao_plano DATE,
            data_devolucao_real DATE, -- pode ser NULL
            FOREIGN KEY(livro_id) REFERENCES livros(id),
            FOREIGN KEY(leitor_id) REFERENCES leitores(id)
        );
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS multas (
            id INTEGER PRIMARY KEY,
            emprestimo_id INTEGER,
            valor REAL,
            pago BOOLEAN,
            FOREIGN KEY(emprestimo_id) REFERENCES emprestimos(id)
        );
    ''')

    # Schema para o jogo da Queda do Servidor
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY,
            username TEXT,
            role TEXT -- ex: admin, analyst, db_maintainer
        );
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS acessos (
            id INTEGER PRIMARY KEY,
            usuario_id INTEGER,
            evento TEXT, -- ex: LOGIN, QUERY, DROP, DELETE
            query_text TEXT,
            timestamp DATETIME,
            FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
        );
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY,
            nome TEXT,
            usuario_id INTEGER,
            tipo TEXT, -- ex: ETL, VACUUM
            horario_cron TEXT,
            ultima_execucao DATETIME,
            FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
        );
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS alerts (
            id INTEGER PRIMARY KEY,
            nivel TEXT,
            mensagem TEXT,
            timestamp DATETIME
        );
    ''')
    
    conn.commit()
    conn.close()

def execute_sql_from_file(db_path, sql_file_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    with open(sql_file_path, 'r') as f:
        sql_script = f.read()
        cursor.executescript(sql_script)
    conn.commit()
    conn.close()




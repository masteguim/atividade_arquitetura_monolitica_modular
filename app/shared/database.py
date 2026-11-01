"""Conexão SQLite e criação do esquema compartilhado do monólito."""
import os
import sqlite3
from contextlib import contextmanager
from pathlib import Path

DB_PATH = Path(os.getenv('DATABASE_PATH', str(Path(__file__).resolve().parents[2] / 'livraria.db')))


def connect():
    conn = sqlite3.connect(str(DB_PATH), timeout=10)
    conn.row_factory = sqlite3.Row
    conn.execute('PRAGMA foreign_keys = ON')
    return conn


@contextmanager
def transaction():
    conn = connect()
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def initialize():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    with transaction() as db:
        db.executescript('''
            CREATE TABLE IF NOT EXISTS livros (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL, autor TEXT NOT NULL,
                isbn TEXT UNIQUE NOT NULL, categoria TEXT NOT NULL DEFAULT '',
                preco REAL NOT NULL CHECK(preco >= 0),
                estoque INTEGER NOT NULL CHECK(estoque >= 0),
                imagem_url TEXT NOT NULL DEFAULT '', descricao TEXT NOT NULL DEFAULT ''
            );
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL, email TEXT NOT NULL UNIQUE, telefone TEXT NOT NULL DEFAULT ''
            );
            CREATE TABLE IF NOT EXISTS carrinho_itens (
                cliente_id INTEGER NOT NULL REFERENCES clientes(id) ON DELETE CASCADE,
                livro_id INTEGER NOT NULL REFERENCES livros(id) ON DELETE CASCADE,
                quantidade INTEGER NOT NULL CHECK(quantidade > 0),
                PRIMARY KEY(cliente_id, livro_id)
            );
            CREATE TABLE IF NOT EXISTS pedidos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cliente_id INTEGER NOT NULL REFERENCES clientes(id),
                criado_em TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                status TEXT NOT NULL DEFAULT 'confirmado',
                total REAL NOT NULL CHECK(total >= 0)
            );
            CREATE TABLE IF NOT EXISTS pedido_itens (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                pedido_id INTEGER NOT NULL REFERENCES pedidos(id),
                livro_id INTEGER REFERENCES livros(id) ON DELETE SET NULL,
                titulo TEXT NOT NULL, quantidade INTEGER NOT NULL,
                preco_unitario REAL NOT NULL
            );
        ''')

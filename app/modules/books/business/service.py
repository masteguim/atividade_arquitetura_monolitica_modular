import sqlite3
from app.modules.books.data import repository as repo
from app.shared.errors import not_found, conflict


def listar(busca=None):
    return repo.all_books(busca)


def buscar(livro_id):
    return repo.get(livro_id) or not_found('Livro')


def criar(dados):
    try:
        id_ = repo.insert(dados)
    except sqlite3.IntegrityError:
        conflict('ISBN já cadastrado.')
    return buscar(id_)


def atualizar(livro_id, dados):
    buscar(livro_id)
    try:
        repo.update(livro_id, dados)
    except sqlite3.IntegrityError:
        conflict('ISBN já cadastrado.')
    return buscar(livro_id)


def excluir(livro_id):
    if not repo.delete(livro_id):
        not_found('Livro')

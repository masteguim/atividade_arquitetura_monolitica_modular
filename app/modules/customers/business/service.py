import sqlite3
from app.modules.customers.data import repository as repo
from app.shared.errors import not_found, conflict


def listar():
    return repo.all_customers()


def buscar(id_):
    return repo.get(id_) or not_found('Cliente')


def criar(data):
    try:
        id_ = repo.insert(data)
    except sqlite3.IntegrityError:
        conflict('E-mail já cadastrado.')
    return buscar(id_)


def atualizar(id_, data):
    buscar(id_)
    try:
        repo.update(id_, data)
    except sqlite3.IntegrityError:
        conflict('E-mail já cadastrado.')
    return buscar(id_)


def excluir(id_):
    buscar(id_)
    try:
        repo.delete(id_)
    except sqlite3.IntegrityError:
        conflict('Cliente possui pedidos e não pode ser excluído.')

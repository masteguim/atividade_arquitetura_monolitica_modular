from app.modules.cart.data import repository as repo
from app.modules.books.business.service import buscar as buscar_livro
from app.modules.customers.business.service import buscar as buscar_cliente
from app.shared.errors import bad_request


def listar(cliente_id):
    buscar_cliente(cliente_id)
    itens = repo.items(cliente_id)
    return {'cliente_id': cliente_id, 'itens': itens, 'total': round(sum(x['subtotal'] for x in itens), 2)}


def adicionar(cliente_id, livro_id, quantidade):
    buscar_cliente(cliente_id)
    livro = buscar_livro(livro_id)
    novo_total = repo.quantity(cliente_id, livro_id) + quantidade
    if novo_total > livro['estoque']:
        bad_request('Quantidade solicitada supera o estoque.')
    repo.set_quantity(cliente_id, livro_id, novo_total)
    return listar(cliente_id)


def alterar(cliente_id, livro_id, quantidade):
    buscar_cliente(cliente_id)
    livro = buscar_livro(livro_id)
    if quantidade > livro['estoque']:
        bad_request('Quantidade solicitada supera o estoque.')
    repo.set_quantity(cliente_id, livro_id, quantidade)
    return listar(cliente_id)


def remover(cliente_id, livro_id):
    buscar_cliente(cliente_id)
    repo.set_quantity(cliente_id, livro_id, 0)
    return listar(cliente_id)


def limpar(cliente_id):
    buscar_cliente(cliente_id)
    repo.clear(cliente_id)
    return listar(cliente_id)

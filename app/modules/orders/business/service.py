from app.modules.orders.data import repository as repo
from app.shared.errors import bad_request, not_found


def listar():
    return repo.all_orders()


def buscar(id_):
    return repo.get(id_) or not_found('Pedido')


def finalizar(cliente_id):
    pedido_id, erro = repo.checkout(cliente_id)
    if erro == 'cliente':
        not_found('Cliente')
    if erro == 'vazio':
        bad_request('O carrinho está vazio.')
    if erro == 'estoque':
        bad_request('Estoque insuficiente para um ou mais livros.')
    return buscar(pedido_id)


def alterar_status(id_, status):
    buscar(id_)
    if status not in ('pendente', 'confirmado', 'cancelado'):
        bad_request('Status inválido.')
    # Cancelamento altera o status, mas não repõe estoque automaticamente.
    repo.change_status(id_, status)
    return buscar(id_)

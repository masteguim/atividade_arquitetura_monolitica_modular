from modulos.carrinho.dados import repositorio
from modulos.livros.negocio import servico as livros

def listar():
    return [{**item, "livro": livros.obter(item["livro_id"])} for item in repositorio.listar() if livros.obter(item["livro_id"])]

def adicionar(id_livro):
    if not livros.obter(id_livro):
        raise ValueError("Livro não encontrado.")
    itens = repositorio.listar()
    encontrado = next((item for item in itens if item["livro_id"] == id_livro), None)
    if encontrado:
        encontrado["quantidade"] += 1
    else:
        itens.append({"livro_id": id_livro, "quantidade": 1})
    repositorio.guardar(itens)

def remover(id_livro):
    repositorio.guardar([i for i in repositorio.listar() if i["livro_id"] != id_livro])

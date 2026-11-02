from modulos.favoritos.dados import repositorio
from modulos.livros.negocio import servico as livros

def listar():
    return [livros.obter(i["livro_id"]) for i in repositorio.listar() if livros.obter(i["livro_id"])]

def alternar(id_livro):
    if not livros.obter(id_livro):
        raise ValueError("Livro não encontrado.")
    itens = repositorio.listar()
    if any(i["livro_id"] == id_livro for i in itens):
        itens = [i for i in itens if i["livro_id"] != id_livro]
    else:
        itens.append({"livro_id": id_livro})
    repositorio.guardar(itens)

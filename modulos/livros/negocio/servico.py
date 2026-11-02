from modulos.livros.dados import repositorio

def listar(termo=""):
    livros = repositorio.listar()
    return [livro for livro in livros if termo.casefold() in (livro["titulo"] + " " + livro["autor"]).casefold()]

def obter(id_livro):
    return next((l for l in repositorio.listar() if l["id"] == id_livro), None)

def cadastrar(titulo, autor):
    titulo, autor = titulo.strip(), autor.strip()
    if not titulo or not autor:
        raise ValueError("Informe título e autor.")
    livros = repositorio.listar()
    novo = {"id": max((l["id"] for l in livros), default=0)+1, "titulo": titulo, "autor": autor}
    livros.append(novo)
    repositorio.guardar(livros)
    return novo

def excluir(id_livro):
    livros = repositorio.listar()
    restantes = [l for l in livros if l["id"] != id_livro]
    if len(livros) == len(restantes):
        raise ValueError("Livro não encontrado.")
    repositorio.guardar(restantes)

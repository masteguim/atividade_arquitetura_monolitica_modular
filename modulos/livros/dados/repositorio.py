from modulos.compartilhado.armazenamento import ler, salvar
ARQUIVO = "livros.txt"

def listar():
    return ler(ARQUIVO)

def guardar(livros):
    salvar(ARQUIVO, livros)

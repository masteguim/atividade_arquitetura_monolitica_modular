from modulos.compartilhado.armazenamento import ler, salvar
ARQUIVO = "favoritos.txt"

def listar():
    return ler(ARQUIVO)

def guardar(itens):
    salvar(ARQUIVO, itens)

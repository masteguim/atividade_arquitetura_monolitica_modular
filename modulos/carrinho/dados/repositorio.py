from modulos.compartilhado.armazenamento import ler, salvar
ARQUIVO = "carrinho.txt"

def listar():
    return ler(ARQUIVO)

def guardar(itens):
    salvar(ARQUIVO, itens)

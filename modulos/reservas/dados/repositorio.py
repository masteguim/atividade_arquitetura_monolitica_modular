from modulos.compartilhado.armazenamento import ler, salvar
ARQUIVO = "reservas.txt"

def listar():
    return ler(ARQUIVO)

def guardar(reservas):
    salvar(ARQUIVO, reservas)

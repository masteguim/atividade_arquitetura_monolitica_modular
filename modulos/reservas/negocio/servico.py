from modulos.reservas.dados import repositorio
from modulos.livros.negocio import servico as livros

def listar():
    return [{**reserva, "livro": livros.obter(reserva["livro_id"])} for reserva in repositorio.listar()]

def criar(id_livro, nome):
    nome = nome.strip()
    if not nome:
        raise ValueError("Informe seu nome para reservar.")
    if not livros.obter(id_livro):
        raise ValueError("Livro não encontrado.")
    reservas = repositorio.listar()
    reservas.append({"id": max((r["id"] for r in reservas), default=0)+1, "livro_id": id_livro, "nome": nome, "status": "Pendente"})
    repositorio.guardar(reservas)

def cancelar(id_reserva):
    reservas = repositorio.listar()
    repositorio.guardar([r for r in reservas if r["id"] != id_reserva])

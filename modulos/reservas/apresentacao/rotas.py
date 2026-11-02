from flask import Blueprint, render_template, request, redirect, url_for, flash
from modulos.reservas.negocio import servico
from modulos.livros.negocio import servico as livros
rotas_reservas = Blueprint("reservas", __name__, url_prefix="/reservas")

@rotas_reservas.get("")
def pagina():
    return render_template("reservas.html", reservas=servico.listar(), livros=livros.listar())

@rotas_reservas.post("")
def criar():
    try:
        servico.criar(int(request.form.get("livro_id", "0")), request.form.get("nome", ""))
        flash("Reserva registrada.", "ok")
    except ValueError as erro:
        flash(str(erro), "erro")
    return redirect(url_for("reservas.pagina"))

@rotas_reservas.post("/<int:id_reserva>/cancelar")
def cancelar(id_reserva):
    servico.cancelar(id_reserva)
    return redirect(url_for("reservas.pagina"))

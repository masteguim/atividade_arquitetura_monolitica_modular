from flask import Blueprint, render_template, redirect, url_for, flash
from modulos.favoritos.negocio import servico
rotas_favoritos = Blueprint("favoritos", __name__, url_prefix="/favoritos")

@rotas_favoritos.get("")
def pagina():
    return render_template("favoritos.html", livros=servico.listar())

@rotas_favoritos.post("/alternar/<int:id_livro>")
def alternar(id_livro):
    try:
        servico.alternar(id_livro)
    except ValueError as erro:
        flash(str(erro), "erro")
    return redirect(url_for("livros.inicio"))

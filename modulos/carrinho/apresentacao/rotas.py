from flask import Blueprint, render_template, redirect, url_for, flash
from modulos.carrinho.negocio import servico
rotas_carrinho = Blueprint("carrinho", __name__, url_prefix="/carrinho")

@rotas_carrinho.get("")
def pagina():
    return render_template("carrinho.html", itens=servico.listar())

@rotas_carrinho.post("/adicionar/<int:id_livro>")
def adicionar(id_livro):
    try:
        servico.adicionar(id_livro)
        flash("Livro adicionado ao carrinho.", "ok")
    except ValueError as erro:
        flash(str(erro), "erro")
    return redirect(url_for("livros.inicio"))

@rotas_carrinho.post("/remover/<int:id_livro>")
def remover(id_livro):
    servico.remover(id_livro)
    return redirect(url_for("carrinho.pagina"))

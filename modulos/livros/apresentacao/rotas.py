from flask import Blueprint, render_template, request, redirect, url_for, flash
from modulos.livros.negocio import servico

rotas_livros = Blueprint("livros", __name__)

@rotas_livros.get("/")
def inicio():
    return render_template("livros.html", livros=servico.listar(request.args.get("busca", "")))

@rotas_livros.post("/livros")
def cadastrar():
    try:
        servico.cadastrar(request.form.get("titulo", ""), request.form.get("autor", ""))
        flash("Livro cadastrado.", "ok")
    except ValueError as erro:
        flash(str(erro), "erro")
    return redirect(url_for("livros.inicio"))

@rotas_livros.post("/livros/<int:id_livro>/excluir")
def excluir(id_livro):
    try:
        servico.excluir(id_livro)
        flash("Livro excluído.", "ok")
    except ValueError as erro:
        flash(str(erro), "erro")
    return redirect(url_for("livros.inicio"))

from flask import Flask
from pathlib import Path
from modulos.livros.apresentacao.rotas import rotas_livros
from modulos.carrinho.apresentacao.rotas import rotas_carrinho
from modulos.favoritos.apresentacao.rotas import rotas_favoritos
from modulos.reservas.apresentacao.rotas import rotas_reservas

app = Flask(__name__, template_folder="modelos_html", static_folder="estaticos")
app.secret_key = "exercicio-academico-livraria-local"
for rotas in (rotas_livros, rotas_carrinho, rotas_favoritos, rotas_reservas):
    app.register_blueprint(rotas)

if __name__ == "__main__":
    app.run(debug=True)

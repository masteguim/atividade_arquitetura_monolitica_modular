import os
import tempfile
from pathlib import Path

# O banco de teste é isolado e definido antes de importar a aplicação.
_tmp = tempfile.TemporaryDirectory()
os.environ['DATABASE_PATH'] = str(Path(_tmp.name) / 'test.db')

from fastapi.testclient import TestClient  # noqa: E402
from app.main import app  # noqa: E402


def test_fluxo_completo():
    with TestClient(app) as client:
        assert client.get('/health').json()['status'] == 'ok'
        livro = client.post('/livros', json={
            'titulo': 'Dom Casmurro', 'autor': 'Machado de Assis', 'isbn': '9780000000001',
            'categoria': 'Romance', 'preco': 29.90, 'estoque': 5,
        })
        assert livro.status_code == 201
        lid = livro.json()['id']
        cli = client.post('/clientes', json={'nome': 'Ana', 'email': 'ana@example.com', 'telefone': '11999999999'})
        assert cli.status_code == 201
        cid = cli.json()['id']
        carrinho = client.post(f'/carrinho/{cid}/itens', json={'livro_id': lid, 'quantidade': 2})
        assert carrinho.status_code == 200
        assert carrinho.json()['total'] == 59.8
        pedido = client.post('/pedidos', json={'cliente_id': cid})
        assert pedido.status_code == 201
        assert pedido.json()['total'] == 59.8
        assert client.get(f'/livros/{lid}').json()['estoque'] == 3
        assert client.get(f'/carrinho/{cid}').json()['itens'] == []
        assert client.get('/dashboard/resumo').json()['total_pedidos'] == 1
        assert client.post('/pedidos', json={'cliente_id': cid}).status_code == 400
        assert client.post('/livros', json={
            'titulo': 'Outro', 'autor': 'Autor', 'isbn': '9780000000001', 'preco': 2, 'estoque': 1
        }).status_code == 409

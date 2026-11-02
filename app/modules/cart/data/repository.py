from app.shared.database import connect, transaction

SQL = '''SELECT ci.livro_id, l.titulo, l.preco, l.estoque, ci.quantidade,
                ROUND(l.preco * ci.quantidade, 2) AS subtotal
         FROM carrinho_itens ci JOIN livros l ON l.id=ci.livro_id
         WHERE ci.cliente_id=? ORDER BY ci.livro_id'''


def items(cliente_id):
    with connect() as db:
        return [dict(row) for row in db.execute(SQL, (cliente_id,))]


def quantity(cliente_id, livro_id):
    with connect() as db:
        row = db.execute('SELECT quantidade FROM carrinho_itens WHERE cliente_id=? AND livro_id=?', (cliente_id, livro_id)).fetchone()
        return row['quantidade'] if row else 0


def set_quantity(cliente_id, livro_id, quantidade):
    with transaction() as db:
        if quantidade == 0:
            db.execute('DELETE FROM carrinho_itens WHERE cliente_id=? AND livro_id=?', (cliente_id, livro_id))
        else:
            db.execute('''INSERT INTO carrinho_itens(cliente_id,livro_id,quantidade) VALUES(?,?,?)
                          ON CONFLICT(cliente_id,livro_id) DO UPDATE SET quantidade=excluded.quantidade''',
                       (cliente_id, livro_id, quantidade))


def clear(cliente_id):
    with transaction() as db:
        db.execute('DELETE FROM carrinho_itens WHERE cliente_id=?', (cliente_id,))

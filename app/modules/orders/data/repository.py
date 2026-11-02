from app.shared.database import connect, transaction


def all_orders():
    with connect() as db:
        return [dict(row) for row in db.execute('SELECT * FROM pedidos ORDER BY id DESC')]


def get(id_):
    with connect() as db:
        pedido = db.execute('SELECT * FROM pedidos WHERE id=?', (id_,)).fetchone()
        if not pedido:
            return None
        output = dict(pedido)
        output['itens'] = [dict(row) for row in db.execute('SELECT livro_id,titulo,quantidade,preco_unitario FROM pedido_itens WHERE pedido_id=? ORDER BY id', (id_,))]
        return output


def change_status(id_, status):
    with transaction() as db:
        return db.execute('UPDATE pedidos SET status=? WHERE id=?', (status, id_)).rowcount


def checkout(cliente_id):
    # Operação atômica: estoque, pedido e carrinho são atualizados juntos.
    # BEGIN IMMEDIATE serializa escritas concorrentes no SQLite.
    with transaction() as db:
        db.execute('BEGIN IMMEDIATE')
        cliente = db.execute('SELECT id FROM clientes WHERE id=?', (cliente_id,)).fetchone()
        if not cliente:
            return None, 'cliente'
        itens = db.execute('''SELECT ci.livro_id, ci.quantidade, l.titulo, l.preco, l.estoque
                              FROM carrinho_itens ci JOIN livros l ON l.id=ci.livro_id
                              WHERE ci.cliente_id=?''', (cliente_id,)).fetchall()
        if not itens:
            return None, 'vazio'
        for item in itens:
            if item['quantidade'] > item['estoque']:
                return None, 'estoque'
        total = round(sum(round(item['preco'] * item['quantidade'], 2) for item in itens), 2)
        cursor = db.execute('INSERT INTO pedidos(cliente_id,total) VALUES (?,?)', (cliente_id, total))
        pedido_id = cursor.lastrowid
        for item in itens:
            db.execute('UPDATE livros SET estoque=estoque-? WHERE id=?', (item['quantidade'], item['livro_id']))
            db.execute('''INSERT INTO pedido_itens(pedido_id,livro_id,titulo,quantidade,preco_unitario)
                          VALUES(?,?,?,?,?)''', (pedido_id, item['livro_id'], item['titulo'], item['quantidade'], item['preco']))
        db.execute('DELETE FROM carrinho_itens WHERE cliente_id=?', (cliente_id,))
        return pedido_id, None

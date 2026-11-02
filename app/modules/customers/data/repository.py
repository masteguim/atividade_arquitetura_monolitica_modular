from app.shared.database import connect, transaction


def all_customers():
    with connect() as db:
        return [dict(r) for r in db.execute('SELECT * FROM clientes ORDER BY id')]


def get(id_):
    with connect() as db:
        row = db.execute('SELECT * FROM clientes WHERE id=?', (id_,)).fetchone()
        return dict(row) if row else None


def insert(data):
    with transaction() as db:
        return db.execute('INSERT INTO clientes(nome,email,telefone) VALUES (?,?,?)', (data['nome'], data['email'], data['telefone'])).lastrowid


def update(id_, data):
    with transaction() as db:
        return db.execute('UPDATE clientes SET nome=?, email=?, telefone=? WHERE id=?', (data['nome'], data['email'], data['telefone'], id_)).rowcount


def delete(id_):
    with transaction() as db:
        return db.execute('DELETE FROM clientes WHERE id=?', (id_,)).rowcount

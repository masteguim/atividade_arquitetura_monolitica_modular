from app.shared.database import connect, transaction


def all_books(search=None):
    with connect() as db:
        if search:
            return [dict(x) for x in db.execute('SELECT * FROM livros WHERE titulo LIKE ? OR autor LIKE ? ORDER BY id', (f'%{search}%', f'%{search}%'))]
        return [dict(x) for x in db.execute('SELECT * FROM livros ORDER BY id')]


def get(book_id):
    with connect() as db:
        row = db.execute('SELECT * FROM livros WHERE id=?', (book_id,)).fetchone()
        return dict(row) if row else None


def insert(data):
    with transaction() as db:
        fields = list(data)
        cursor = db.execute(f"INSERT INTO livros ({','.join(fields)}) VALUES ({','.join('?' for _ in fields)})", tuple(data.values()))
        return cursor.lastrowid


def update(book_id, data):
    with transaction() as db:
        fields = list(data)
        cursor = db.execute(f"UPDATE livros SET {','.join(f'{key}=?' for key in fields)} WHERE id=?", (*data.values(), book_id))
        return cursor.rowcount


def delete(book_id):
    with transaction() as db:
        return db.execute('DELETE FROM livros WHERE id=?', (book_id,)).rowcount

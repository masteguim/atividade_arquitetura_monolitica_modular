from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.shared.database import initialize, connect
from app.modules.books.presentation.routes import router as books_router
from app.modules.customers.presentation.routes import router as customers_router
from app.modules.cart.presentation.routes import router as cart_router
from app.modules.orders.presentation.routes import router as orders_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    initialize()
    yield


app = FastAPI(title='Livraria Nexus — Monólito Modular', version='1.0.0', lifespan=lifespan)
app.add_middleware(CORSMiddleware, allow_origins=['http://localhost:5173', 'http://127.0.0.1:5173'], allow_credentials=True, allow_methods=['*'], allow_headers=['*'])
app.include_router(books_router)
app.include_router(customers_router)
app.include_router(cart_router)
app.include_router(orders_router)


@app.get('/health', tags=['Sistema'])
def health():
    return {'status': 'ok'}


@app.get('/dashboard/resumo', tags=['Dashboard'])
def dashboard():
    with connect() as db:
        livros = db.execute('SELECT COUNT(*) AS n, COALESCE(SUM(estoque),0) AS estoque FROM livros').fetchone()
        clientes = db.execute('SELECT COUNT(*) FROM clientes').fetchone()[0]
        pedidos = db.execute('SELECT COUNT(*) AS n, COALESCE(SUM(total),0) AS vendas FROM pedidos WHERE status != ?', ('cancelado',)).fetchone()
        return {'total_livros': livros['n'], 'livros_em_estoque': livros['estoque'], 'total_clientes': clientes, 'total_pedidos': pedidos['n'], 'total_vendas': round(pedidos['vendas'], 2)}

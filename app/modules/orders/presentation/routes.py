from fastapi import APIRouter
from pydantic import BaseModel
from typing import Literal
from app.modules.orders.business import service

router = APIRouter(prefix='/pedidos', tags=['Pedidos'])


class PedidoEntrada(BaseModel):
    cliente_id: int


class StatusEntrada(BaseModel):
    status: Literal['pendente', 'confirmado', 'cancelado']


@router.get('')
def listar():
    return service.listar()


@router.get('/{pedido_id}')
def detalhar(pedido_id: int):
    return service.buscar(pedido_id)


@router.post('', status_code=201)
def criar(dados: PedidoEntrada):
    return service.finalizar(dados.cliente_id)


@router.patch('/{pedido_id}/status')
def alterar_status(pedido_id: int, dados: StatusEntrada):
    return service.alterar_status(pedido_id, dados.status)

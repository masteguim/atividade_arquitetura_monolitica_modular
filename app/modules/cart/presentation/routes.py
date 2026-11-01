from fastapi import APIRouter
from pydantic import BaseModel, Field
from app.modules.cart.business import service

router = APIRouter(prefix='/carrinho', tags=['Carrinho'])


class ItemAdicionar(BaseModel):
    livro_id: int = Field(gt=0)
    quantidade: int = Field(gt=0)


class QuantidadeAtualizar(BaseModel):
    quantidade: int = Field(ge=0)


@router.get('/{cliente_id}')
def listar(cliente_id: int):
    return service.listar(cliente_id)


@router.post('/{cliente_id}/itens')
def adicionar(cliente_id: int, dados: ItemAdicionar):
    return service.adicionar(cliente_id, dados.livro_id, dados.quantidade)


@router.put('/{cliente_id}/itens/{livro_id}')
def alterar(cliente_id: int, livro_id: int, dados: QuantidadeAtualizar):
    return service.alterar(cliente_id, livro_id, dados.quantidade)


@router.delete('/{cliente_id}/itens/{livro_id}')
def remover(cliente_id: int, livro_id: int):
    return service.remover(cliente_id, livro_id)


@router.delete('/{cliente_id}')
def limpar(cliente_id: int):
    return service.limpar(cliente_id)

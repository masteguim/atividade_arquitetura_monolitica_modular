from fastapi import APIRouter
from pydantic import BaseModel, EmailStr, Field
from app.modules.customers.business import service

router = APIRouter(prefix='/clientes', tags=['Clientes'])


class ClienteEntrada(BaseModel):
    nome: str = Field(min_length=1)
    email: EmailStr
    telefone: str = ''


@router.get('')
def listar():
    return service.listar()


@router.get('/{cliente_id}')
def detalhar(cliente_id: int):
    return service.buscar(cliente_id)


@router.post('', status_code=201)
def cadastrar(dados: ClienteEntrada):
    return service.criar(dados.model_dump())


@router.put('/{cliente_id}')
def atualizar(cliente_id: int, dados: ClienteEntrada):
    return service.atualizar(cliente_id, dados.model_dump())


@router.delete('/{cliente_id}', status_code=204)
def excluir(cliente_id: int):
    service.excluir(cliente_id)

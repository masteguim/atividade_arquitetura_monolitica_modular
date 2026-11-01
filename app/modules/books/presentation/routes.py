from fastapi import APIRouter
from pydantic import BaseModel, Field
from app.modules.books.business import service

router = APIRouter(prefix='/livros', tags=['Livros'])


class LivroEntrada(BaseModel):
    titulo: str = Field(min_length=1)
    autor: str = Field(min_length=1)
    isbn: str = Field(min_length=1)
    categoria: str = ''
    preco: float = Field(ge=0)
    estoque: int = Field(ge=0)
    imagem_url: str = ''
    descricao: str = ''


@router.get('')
def listar(busca: str | None = None):
    return service.listar(busca)


@router.get('/{livro_id}')
def detalhar(livro_id: int):
    return service.buscar(livro_id)


@router.post('', status_code=201)
def cadastrar(dados: LivroEntrada):
    return service.criar(dados.model_dump())


@router.put('/{livro_id}')
def atualizar(livro_id: int, dados: LivroEntrada):
    return service.atualizar(livro_id, dados.model_dump())


@router.delete('/{livro_id}', status_code=204)
def excluir(livro_id: int):
    service.excluir(livro_id)

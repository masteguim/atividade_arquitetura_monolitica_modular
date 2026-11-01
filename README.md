# Livraria Nexus — Exercício 8.3

Refatoração do MVP de livraria para **monólito modular** com **FastAPI + SQLite**.

## Arquitetura

Uma única aplicação FastAPI, um único banco SQLite e quatro módulos de negócio:

- `books`: cadastro, atualização, consulta, exclusão de livros e estoque
- `customers`: cadastro, edição, consulta e exclusão de clientes
- `cart`: carrinho persistido por cliente
- `orders`: finalização de compra, histórico e status de pedidos

Cada módulo possui **presentation** (rotas HTTP), **business** (regras de negócio) e **data** (repositório SQL). A pasta `shared` contém infraestrutura compartilhada. **Não são microsserviços independentes**: todos executam juntos em um processo.

## Execução

Requer Python 3.10+ (recomendado 3.12).

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

No Windows, ative o ambiente com `.venv\\Scripts\\activate`.

- Documentação interativa: http://127.0.0.1:8000/docs
- Verificação: http://127.0.0.1:8000/health
- Dashboard: http://127.0.0.1:8000/dashboard/resumo

O banco de dados `livraria.db` é criado automaticamente na primeira inicialização. É possível definir outro arquivo via variável de ambiente `DATABASE_PATH`.

## Exemplo de uso

1. `POST /livros` — cadastrar livro
2. `POST /clientes` — cadastrar cliente
3. `POST /carrinho/{cliente_id}/itens` — adicionar livro ao carrinho
4. `POST /pedidos` com `{ "cliente_id": 1 }` — finalizar compra
5. `GET /pedidos` — conferir pedidos

A compra cria o pedido, registra os itens com o preço do momento, reduz estoque e limpa o carrinho **em uma transação SQLite**. O status inicial é `confirmado`. Alterar o status para `cancelado` não repõe estoque automaticamente.

## Rotas

| Método | Rota | Objetivo |
|---|---|---|
| GET | `/livros` | Listar; aceita `?busca=` |
| GET | `/livros/{id}` | Buscar |
| POST | `/livros` | Criar |
| PUT | `/livros/{id}` | Atualizar |
| DELETE | `/livros/{id}` | Excluir |
| GET/POST | `/clientes` | Listar/criar |
| GET/PUT/DELETE | `/clientes/{id}` | Consultar/editar/excluir |
| GET/DELETE | `/carrinho/{cliente_id}` | Listar/limpar |
| POST | `/carrinho/{cliente_id}/itens` | Adicionar |
| PUT/DELETE | `/carrinho/{cliente_id}/itens/{livro_id}` | Alterar/remover |
| GET/POST | `/pedidos` | Listar/finalizar compra |
| GET | `/pedidos/{id}` | Detalhar |
| PATCH | `/pedidos/{id}/status` | Alterar status |
| GET | `/dashboard/resumo` | Indicadores |
| GET | `/health` | Saúde da aplicação |

## Testes

```bash
pip install -r requirements-dev.txt
pytest -q
```

## Frontend React

CORS permite `http://localhost:5173` e `http://127.0.0.1:5173`. No React use `VITE_API_URL=http://127.0.0.1:8000` e `VITE_USE_MOCKS=false`. A compatibilidade dos payloads e rotas com o frontend exportado do Figma deve ser verificada.

## Limitações do MVP

Não possui autenticação, pagamentos reais, multiusuário administrativo nem APIs independentes. Valores monetários são armazenados como REAL por simplicidade acadêmica; em produção recomenda-se centavos inteiros ou NUMERIC/Decimal. Para o exercício 8.4, preparar o deploy deste monólito em servidor.
# atividade_arquitetura_monolitica_modular

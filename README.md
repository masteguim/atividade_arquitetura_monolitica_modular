# Livraria — Arquitetura Monolítica Modular

Refatoração simplificada baseada na estrutura da atividade Clean Architecture: livros, carrinho, favoritos e reservas para retirada. Um único processo Python, com módulos por domínio e três camadas em português: `apresentacao`, `negocio` e `dados`. A persistência permanece simples, em arquivos TXT. O frontend é HTML/CSS renderizado pelo Flask; não utiliza React, Node nem npm.

> Esta versão foi reconstruída a partir das funcionalidades conhecidas da atividade Clean; para um refactor arquivo a arquivo do código original, é necessário fornecer os arquivos da implementação Clean.

## Executar no Linux

```bash
cd biblioteca_monolitica_modular_simples
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Abra http://127.0.0.1:5000

## Estrutura

- `app.py`: único ponto de inicialização (monólito)
- `modulos/livros/`: cadastro, pesquisa e exclusão de livros
- `modulos/carrinho/`: adição, remoção e quantidade de itens
- `modulos/favoritos/`: marcar/desmarcar favoritos
- `modulos/reservas/`: reservar livros para retirada e cancelar reservas
- `apresentacao/`: rotas e recebimento das requisições
- `negocio/`: regras de negócio
- `dados/`: repositório para persistência TXT
- `modelos_html/`: páginas HTML
- `estaticos/estilo.css`: estilos
- `dados_txt/`: registros armazenados em TXT

## Verificar

1. Cadastre um livro em **Livros**.
2. Adicione o livro ao carrinho.
3. Marque-o como favorito.
4. Faça uma reserva para retirada.
5. Reinicie o servidor e confirme que os dados permanecem salvos.

É um protótipo acadêmico local: os dados são compartilhados entre os usuários, sem login ou controle de concorrência. Não se destina a produção.

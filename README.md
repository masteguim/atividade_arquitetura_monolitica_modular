# Livraria — Arquitetura Monolítica Modular

Refatoração simplificada baseada na estrutura da atividade Clean Architecture: livros, carrinho, favoritos e reservas para retirada. Um único processo Python, com módulos por domínio e três camadas em português: `apresentacao`, `negocio` e `dados`. A persistência permanece simples, em arquivos TXT. O frontend é HTML/CSS renderizado pelo Flask; não utiliza React, Node nem npm.

> Esta versão foi reconstruída a partir das funcionalidades conhecidas da atividade Clean; para um refactor arquivo a arquivo do código original, é necessário fornecer os arquivos da implementação Clean.

## Verificar

1. Cadastre um livro em **Livros**.
2. Adicione o livro ao carrinho.
3. Marque-o como favorito.
4. Faça uma reserva para retirada.
5. Reinicie o servidor e confirme que os dados permanecem salvos.


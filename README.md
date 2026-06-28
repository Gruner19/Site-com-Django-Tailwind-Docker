# Parte 1 — Estrutura inicial do Django + Tailwind + Docker

## Resultados obtidos

### Página inicial (`http://localhost:8000`)

A página principal exibe o cabeçalho "Olá, Django + Tailwind!" com três cards
explicativos sobre Django, Tailwind CSS e Docker Compose.

A seção "Mensagens do banco de dados" aparece vazia com a mensagem
"Nenhuma mensagem ainda", pois ainda não há registros no banco.

**PDF da página inicial:** [capturas/parte1-index.pdf](capturas/parte1-index.pdf)
**HTML:** [capturas/parte1-index.html](capturas/parte1-index.html)

### Painel administrativo (`http://localhost:8000/admin/`)

O admin do Django exibe a tela de login.

**PDF do admin:** [capturas/parte1-admin.pdf](capturas/parte1-admin.pdf)
**HTML:** [capturas/parte1-admin.html](capturas/parte1-admin.html)

## Funcionalidades implementadas

- Projeto Django configurado com Docker
- Tailwind CSS via CDN
- Modelo `Mensagem` definido (titulo, conteudo, criada_em)
- View `index` que lista mensagens
- Admin básico registrado
- `/admin/` funcional

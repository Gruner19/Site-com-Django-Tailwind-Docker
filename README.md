# Site com Django + Tailwind + Docker

Projeto de demonstração com Django, Tailwind via CDN, SQLite e Docker Compose.

## Funcionalidades implementadas

- Modelo `Mensagem` (título, conteúdo, autor, categoria, tags, data de criação)
- Modelo `Categoria` (nome único, relacionamento FK com Mensagem)
- Modelo `Tag` (slug único, relacionamento M2M com Mensagem)
- Página inicial com listagem de mensagens, categorias e tags
- Página `/sobre/`
- Painel administrativo `/admin/` com filtros, busca e `filter_horizontal` para tags

## Como executar

```bash
docker compose run --rm web python manage.py makemigrations
docker compose up --build
```

Depois, abra `http://localhost:8000`.

## Resultados obtidos

> Para capturar as imagens manualmente, execute o projeto e tire os prints das
> páginas abaixo. As imagens devem ser salvas em `capturas/` no formato PNG.

### Página inicial (`http://localhost:8000`)

![Página inicial](capturas/parte4-index.png)

### Página /sobre/ (`http://localhost:8000/sobre/`)

![Página sobre](capturas/parte4-sobre.png)

### Painel administrativo (`http://localhost:8000/admin/`)

![Admin](capturas/parte4-admin.png)

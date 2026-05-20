# Site-com-Django-Tailwind-Docker

Projeto de demonstração com Django, Tailwind via CDN, SQLite e Docker Compose.

## Como executar

```bash
docker compose run --rm web python manage.py makemigrations
docker compose up --build
```

Depois, abra `http://localhost:8000`.

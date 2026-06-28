# Parte 2 — Adicionando campo `autor` e página `/sobre/`

## Resultados obtidos

### Página inicial (`http://localhost:8000`)

![Página inicial](capturas/parte2-pagina-inicial.png)

### Página /sobre/ (`http://localhost:8000/sobre/`)

![Página sobre](capturas/parte2-pagina-sobre.png)

### Painel administrativo (`http://localhost:8000/admin/`)

![Admin](capturas/parte2-admin.png)

## Funcionalidades implementadas

- Campo `autor` adicionado ao model `Mensagem` (default: "Anônimo")
- Migration `0001_initial.py` gerada
- View `sobre` criada
- Rota `/sobre/` registrada
- Template `templates/home/sobre.html` criado
- Link `/sobre` no menu de navegação
- Gradiente do fundo alterado

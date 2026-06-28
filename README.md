# Parte 2 — Adicionando campo `autor` e página `/sobre/`

## Resultados obtidos

### Página inicial (`http://localhost:8000`)

A página principal agora exibe:
- Gradiente alterado para `from-emerald-950 via-teal-950`
- Link de navegação `/sobre` no cabeçalho
- Mensagens exibem `por {{ m.autor }}` quando cadastradas

**PDF:** [capturas/parte2-index.pdf](capturas/parte2-index.pdf)
**HTML:** [capturas/parte2-index.html](capturas/parte2-index.html)

### Página /sobre/ (`http://localhost:8000/sobre/`)

Nova página criada com informações sobre o projeto, link "← voltar"
para retornar à página inicial.

**PDF:** [capturas/parte2-sobre.pdf](capturas/parte2-sobre.pdf)
**HTML:** [capturas/parte2-sobre.html](capturas/parte2-sobre.html)

### Painel administrativo (`http://localhost:8000/admin/`)

Admin agora exibe o campo `autor` no formulário de Mensagens.

**PDF:** [capturas/parte2-admin.pdf](capturas/parte2-admin.pdf)
**HTML:** [capturas/parte2-admin.html](capturas/parte2-admin.html)

## Funcionalidades implementadas

- Campo `autor` adicionado ao model `Mensagem` (default: "Anônimo")
- Migration `0001_initial.py` gerada
- View `sobre` criada
- Rota `/sobre/` registrada
- Template `templates/home/sobre.html` criado
- Link `/sobre` no menu de navegação
- Gradiente do fundo alterado

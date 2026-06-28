# Parte 3 — Relacionamento um-para-muitos (Categoria → Mensagem)

## Resultados obtidos

### Página inicial (`http://localhost:8000`)

A página principal agora exibe um selo de categoria ao lado do título
da mensagem quando uma categoria está associada (`{{ m.categoria.nome }}`).

**PDF:** [capturas/parte3-index.pdf](capturas/parte3-index.pdf)
**HTML:** [capturas/parte3-index.html](capturas/parte3-index.html)

### Página /sobre/ (`http://localhost:8000/sobre/`)

Página sobre mantida da Parte 2.

**PDF:** [capturas/parte3-sobre.pdf](capturas/parte3-sobre.pdf)
**HTML:** [capturas/parte3-sobre.html](capturas/parte3-sobre.html)

### Painel administrativo (`http://localhost:8000/admin/`)

O admin agora exibe:
- Modelo `Categoria` cadastrável com campo `nome`
- Formulário de `Mensagem` com campo `Categoria` (dropdown)
- Coluna `categoria` na listagem de mensagens
- Filtro lateral por categoria

**PDF:** [capturas/parte3-admin.pdf](capturas/parte3-admin.pdf)
**HTML:** [capturas/parte3-admin.html](capturas/parte3-admin.html)

## Funcionalidades implementadas

- Modelo `Categoria` (nome único)
- Campo `categoria` (ForeignKey) em `Mensagem`
- `related_name="mensagens"` para acesso reverso `categoria.mensagens.all()`
- `on_delete=models.SET_NULL` para preservar mensagens ao apagar categoria
- Migration `0002_categoria_mensagem_categoria.py`
- Template exibe badge da categoria quando presente
- Admin com `list_filter` por categoria

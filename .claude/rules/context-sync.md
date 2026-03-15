# Context Sync — CLAUDE.md e CLAUDE-MARIANA.md

Dois arquivos coexistem. Detecte e aplique o contexto correto automaticamente.

## Regra de Detecção

| Sinal | Contexto | Arquivo Primário |
|-------|----------|-----------------|
| "Como faz X?", "O que é Y?", módulos E1-E5, dúvidas conceituais | Educacional | CLAUDE-MARIANA.md |
| Story, agentes (@dev, @qa), workflow, epic, desenvolvimento | Técnico | CLAUDE.md |
| Ambíguo | Pedir clarificação | — |

## Comportamento na Transição

Ao detectar mudança de contexto, emitir:

```
[CONTEXTO ALTERADO: <origem> → <destino>]
Modo: <EDUCACIONAL|DESENVOLVIMENTO AIOX>
```

## Regras por Contexto

- **Educacional:** Português simples, passo a passo, sem jargão, comandos Windows (não Linux)
- **Técnico:** Rigor AIOX, padrões de framework, agent-authority.md, execução eficiente

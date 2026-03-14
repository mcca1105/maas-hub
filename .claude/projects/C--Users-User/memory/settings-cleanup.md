---
name: Limpeza de Configurações Claude Code
description: Remoção de statusLine que exibia dados de consumo de tokens
type: feedback
---

# Limpeza de Configurações — StatusLine Removida

**Data:** 2026-03-14
**Commit:** 15616e0 — `chore: Remove statusLine configuration from Claude Code settings`

## O que foi feito

Removida completamente a configuração `statusLine` do arquivo `.claude/settings.json`.

### Antes
```json
"statusLine": {
  "type": "command",
  "command": "echo ''"
}
```

### Depois
Propriedade removida completamente.

## Resultado

A barra de status que exibia estas informações foi eliminada:
- 🤖 Modelo: Claude Haiku 4.5
- ⚡ Consumo: X tokens
- 💰 Gastos: R$ X
- 📁 Pasta: /c/Users/User
- 👤 Usuário: Mariana

## Como aplicar

Essa configuração está permanentemente removida. A statusLine não reaparecerá em futuras sessões do Claude Code.

**Arquivo modificado:** `.claude/settings.json`
**Status:** ✅ Finalizado e commitado

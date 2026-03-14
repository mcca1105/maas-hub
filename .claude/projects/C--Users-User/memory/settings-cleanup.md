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

A barra de status que exibia estas informações foi **completamente eliminada de todos os terminais**:
- 🤖 Modelo: Claude Haiku 4.5
- ⚡ Consumo: X tokens
- 💰 Gastos: R$ X
- 📁 Pasta: /c/Users/User
- 👤 Usuário: Mariana

## Arquivos removidos

| Arquivo | Tipo | Status |
|---------|------|--------|
| `C:\Users\User\Show-StatusBar.ps1` | PowerShell | 🗑️ Deletado |
| `C:\Users\User\show-statusbar.sh` | Bash/Shell | 🗑️ Deletado |

## Arquivos modificados

| Arquivo | Modificação | Status |
|---------|------------|--------|
| `.claude/settings.json` | Removida prop. statusLine | ✅ Commitado |
| `Documents/PowerShell/profile.ps1` | Removida referência Show-StatusBar.ps1 | ✅ Commitado |
| `.bashrc` | Removida referência show-statusbar.sh | ✅ Commitado |

## Commits

- `15616e0` — Remove statusLine from Claude Code settings
- `34c73ca` — Remove statusLine reference from PowerShell profile
- `c775836` — Remove statusLine reference from .bashrc

## Como aplicar

Essas configurações estão **permanentemente removidas**:
- ✅ Claude Code: Sem statusLine
- ✅ PowerShell: Sem carregamento de Show-StatusBar.ps1
- ✅ Git Bash: Sem carregamento de show-statusbar.sh
- ✅ Todos os terminais: A barra NÃO reaparecerá

**Status:** ✅ FINALIZADO — Completamente removido de todos os terminais

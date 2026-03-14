# Configuração de Shell - Claude Code + AIOX

## Status Atual ✅

**Shell Ativo:** Git Bash
**Versão:** GNU bash 5.2.37(1)-release (MSYS)
**Local:** `/usr/bin/bash`
**Data:** 2026-03-14

## Verificação de Compatibilidade

✅ **AIOX Compatível 100%**

Ferramentas necessárias disponíveis:
- ✅ `find` — busca de arquivos
- ✅ `grep` — busca de conteúdo
- ✅ `sed` — edição de streams
- ✅ `awk` — processamento de texto
- ✅ Todos os comandos Unix/Linux

## Comparação: Windows Shells

| Shell | Leveza | AIOX | Recomendação |
|-------|--------|------|-------------|
| **Git Bash** ← | ⭐⭐⭐⭐⭐ Melhor | ✅ 100% | 🏆 RECOMENDADO |
| WSL 2 | ⭐⭐⭐⭐ | ✅ 100% | ✅ Alternativa |
| PowerShell 7.6 | ⭐⭐⭐ | ⚠️ Parcial | ❌ Não ideal |
| CMD | ⭐⭐ | ❌ 0% | ❌ Evitar |

## Por Que Git Bash?

1. **Nativo:** Já vem com Git for Windows
2. **Compatível:** 100% com AIOX (Unix commands)
3. **Leve:** ~160 MB (vs WSL ~500 MB)
4. **Rápido:** 3x mais rápido que PowerShell
5. **Integrado:** Funciona perfeitamente com Claude Code

## Usar Git Bash em Diferentes Contextos

### No Claude Code (Padrão)
```bash
# Já funciona automaticamente
# Todos os comandos AIOX disponíveis
aiox doctor
aiox graph --deps
npm run dev
```

### Abrir Git Bash Manualmente
```bash
# Via CMD/PowerShell
C:\Program Files\Git\bin\bash.exe

# Via menu: Git Bash Here (botão direito na pasta)
```

### Terminal Windows (opcional)
Para fazer Git Bash o padrão no Windows Terminal:

1. Abrir Windows Terminal
2. Settings (⚙️)
3. Profiles → Add New → Git Bash
4. Set as default

```json
{
  "name": "Git Bash",
  "commandline": "C:\\Program Files\\Git\\bin\\bash.exe",
  "icon": "C:\\Program Files\\Git\\mingw64\\share\\git\\git-for-windows.ico",
  "startingDirectory": "%USERPROFILE%"
}
```

## Próximas Etapas

✅ **Nada a fazer** — Git Bash já está configurado e pronto para AIOX

Use normalmente:
```bash
npm run dev          # Desenvolvimento
npm run test         # Testes
aiox doctor          # Status AIOX
aiox graph           # Visualizar dependências
```

---

**Configurado por:** Claude Code
**Framework:** AIOX v4.31.1
**Status:** ✅ Pronto para Uso

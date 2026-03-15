---
name: Context Synchronization Status
description: Sincronização automática entre CLAUDE.md (técnico) e CLAUDE-MARIANA.md (educacional)
type: project
---

> ⚠️ ARQUIVADO 2026-03-15: Sistema reorganizado. Regras consolidadas em
> `.claude/rules/context-sync.md`. Este arquivo mantido por histórico.

# 🔄 Sincronização de Contexto — Status Operacional

**Status:** ✅ ATIVADA em 2026-03-14

## O que foi Sincronizado

Claude Code agora possui **sincronização automática de contexto** entre dois arquivos de configuração:

| Arquivo | Tipo | Propósito |
|---------|------|----------|
| `CLAUDE.md` | Técnico | Framework AIOX, agentes, desenvolvimento profissional |
| `CLAUDE-MARIANA.md` | Educacional | Seu perfil pessoal, módulos E1-E5, aprendizado |

**Por quê:** Você é iniciante em programação, mas precisa de um framework técnico robusto para projetos complexos. A sincronização garante que Claude mude automaticamente entre "modo simples" e "modo técnico" conforme você pedirá.

## Como Funciona

Claude **detecta automaticamente:**
- ✅ Quando você faz pergunta educacional → ativa CLAUDE-MARIANA.md
- ✅ Quando você pede tarefa técnica → ativa CLAUDE.md
- ✅ Quando há transição → avisa com `[CONTEXTO ALTERADO]`

**Você não precisa fazer nada** — é automático.

## Documentação

3 arquivos de referência foram criados:

1. **CONTEXT-SYNC-GUIDE.md** — Guia completo de como funciona
2. **CONTEXT-SYNC-EXAMPLES.md** — Exemplos práticos de detecção
3. Ambos `CLAUDE.md` e `CLAUDE-MARIANA.md` têm seções marcadas `<!-- CONTEXT-SYNC-* -->`

## Detecção de Contexto

### 📚 EDUCACIONAL (CLAUDE-MARIANA.md)
```
Triggers:
- "Como faz X?"
- "O que é Y?"
- "Por que...?"
- Dúvidas sobre conceitos
- Módulos E1-E5
```

### 🛠️ TÉCNICO (CLAUDE.md)
```
Triggers:
- "Implemente a story..."
- "@dev faz isso"
- "Execute o workflow"
- Desenvolvimento direto
- Referência a agentes
```

### 🔀 TRANSIÇÃO
```
Detecção:
- Pergunta educacional → tarefa técnica
- Evolução notável de nível
- Mistura de contextos
→ Claude avisa: [CONTEXTO ALTERADO]
```

## Impacto para Você

| Antes | Depois |
|-------|--------|
| Claude sempre técnico | Claude é **adaptativo** |
| Você pedia "explique simples" | Claude já faz automaticamente |
| Sem avisos de transição | **Avisos claros quando contexto muda** |

## Próxima Revisão

Recomendado rever em 2026-03-21 (1 semana) para confirmar que:
- Detecção está funcionando bem
- Avisos são claros
- Nenhum contexto está sendo confundido

**Why:** Detecção pode evoluir conforme seu perfil muda (você continua aprendendo).

---

**Ativado por:** Claude Code (versão com sincronização)
**Data:** 2026-03-14
**Status:** ✅ Operacional

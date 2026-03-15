# 🚀 Próxima Sessão — Comandos de Retomada

**Última atualização:** 2026-03-15
**Estado:** ✅ Limpo e pronto para retomada

---

## Estado ao Encerrar (2026-03-15)

### Commits Finais ✅
```
.aiox-core:        3c17f2d (CLAUDE.md otimizado + Project Guides + MCP Delegation)
prospect-hunter:   5eaae18 (Story 4.1 + Project Configuration)
squad-vendas:      (aguardando push para GitHub + Vercel)
```

### Status de Cada Projeto
| Projeto | Status | Próximo Passo | Esforço |
|---------|--------|---------------|---------|
| **squad-vendas** | ✅ Landing completa (490 linhas) | Push GitHub + Vercel | 2 min |
| **prospect-hunter** | ✅ Story 4.1 committed (5eaae18) | Corrigir ESLint no-explicit-any | 2-3h |
| **zona-genialidade** | ⏸️ Assessment Bloco 3 (14-16 pendentes) | `/zona-genialidade start` | 1h |
| **dashboard-central** | ✅ MVP stories criadas (13pt) | Phase 1 implementação | 6-8h |

---

## ⚡ Pendências em Ordem de Prioridade

### 1️⃣ Deploy Squad Vendas (2 min)
```bash
cd C:\Users\User\squad-vendas

# Checklist:
[ ] git status (deve estar limpo)
[ ] git push origin master
[ ] Conectar no Vercel → Deploy automático
[ ] Testar: https://squad-vendas.vercel.app (ou seu domínio)
```

### 2️⃣ MCPs Phase 3 — @oalanicolas (2-3h)
**Contexto:** Delegado em 2026-03-15
**Agente ID:** `ae651578aec12aed4`
**Escopo:**
- [ ] Gmail API integration
- [ ] Google Calendar API integration
- [ ] Notion API integration

**Bloqueador:** Aguardando credenciais OAuth de Mariana
**Ação quando tiver credenciais:** `@oalanicolas *mcp-phase-3-execute`

### 3️⃣ Zona Genialidade Assessment — Bloco 3 (1h)
**Status:** Pausado em Bloco 2 (6/6 completos)
**Próximo:** Bloco 3 - Unique Ability (perguntas 14-16)

```bash
# Retomar:
/zona-genialidade start
→ Responder perguntas 14-16
→ Continuar com Blocos 4-7 (Wealth Dynamics, Value Eq, Kolbe, Fascination)
```

### 4️⃣ Story 4.1 — ESLint Fixes (2-3h)
**Projeto:** prospect-hunter
**Status:** Scaffold commitada (5eaae18), código sem tipagem
**Problema:** ESLint `--no-explicit-any` em 5 arquivos
**Arquivos a corrigir:**
- `src/services/messaging-bridge.ts`
- `src/integration/whatsapp-handler.ts`
- `src/integration/telegram-handler.ts`
- `src/integration/viber-handler.ts`
- `src/api/messaging-endpoints.ts`

```bash
cd C:\Users\User\prospect-hunter

# Ver erros:
npm run lint

# Corrigir tipos (use Type Guard patterns, não `any`):
npm run lint -- --fix

# Testar:
npm run typecheck
npm test

# Commit:
git add .
git commit -m "fix(story-4.1): Type safety — replace any with proper types"
```

### 5️⃣ Story 4.2 — Analytics (6-8h)
**Próximo:** Criar story para implementar analytics backend
**Precedentes:** Story 4.1 deve estar com ESLint ✅

```bash
@sm *create-story

# Template:
Title: "Story 4.2 — Analytics & Engagement Metrics"
Epic: prospect-hunter
Scope: Backend analytics, event tracking, dashboard API
AC: [ ] Event schema, [ ] Tracking endpoints, [ ] Admin dashboard
Estimate: 13 points
```

---

## 📋 Checklist de Retomada

Ao iniciar a próxima sessão:

```
[ ] Lê MEMORY.md → Entender o contexto
[ ] git status → Confirmar limpeza (sem mudanças pendentes)
[ ] Primeiro passo: Deploy Squad Vendas (2 min)
[ ] Próximo: Escolher entre MCPs (delegado), ESLint (2-3h), ou Assessment (1h)
[ ] Toda sessão: npm test antes de commit
```

---

## 🔗 Comandos Rápidos

```bash
# Verificar status de TODOS os projetos
cd C:\Users\User\.aiox-core && git status
cd C:\Users\User\prospect-hunter && git status
cd C:\Users\User\squad-vendas && git status
cd C:\Users\User\.squads\zona-genialidade && git status

# Iniciar desenvolvimento
@dev *help           # Ver comandos disponíveis
@sm *create-story    # Criar nova story
@qa *qa-gate         # Rodar QA

# Monitorar tokens (próxima sessão)
# STATUS: `/fast` está ativo
# Ativar statusline se necessário: `/statusline`
```

---

## 📚 Referências Importantes

| Arquivo | Propósito |
|---------|----------|
| `.claude/CLAUDE.md` | Framework técnico, agentes, workflows |
| `.claude/CLAUDE-MARIANA.md` | Contexto educacional (se Mariana fazer perguntas) |
| `.claude/rules/` | 13 arquivos com regras contextuais |
| `.claude/projects/C--Users-User/memory/MEMORY.md` | Índice de memoria para futuras sessões |
| `.claude/governance-decision-log.md` | Histórico de decisões (2026-03-07, 2026-03-15) |

---

## ✨ Otimizações Ativas

- ✅ CLAUDE.md modularizado (-36% tokens)
- ✅ Project CLAUDE.md em 4 repos (prospect-hunter, squad-vendas, zona-genialidade, dashboard-central)
- ✅ Statusline v2.0 desabilitado (economiza 50% de tokens)
- ✅ Voice mode desabilitado (economiza 30%)
- ✅ MCP Phase 1 & 2 completadas; Phase 3 delegado

---

**Criado por:** @aiox-master (Orion)
**Data:** 2026-03-15
**Próxima revisão:** 2026-03-16

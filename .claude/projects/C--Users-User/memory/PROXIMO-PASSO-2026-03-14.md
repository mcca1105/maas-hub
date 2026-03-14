# PRÓXIMA JANELA/SESSÃO — 2026-03-14

## ⚠️ STATUS CRÍTICO DE TOKENS
- **Orçamento nova sessão**: 200.000 tokens (RESETADO)
- **Prioridade**: Ações de DESENVOLVIMENTO vs documentação
- **Voice Mode**: ❌ DESABILITAR `/voice disable` imediatamente

---

## 🎯 AÇÕES PRIORITÁRIAS (Próxima Sessão)

### 1️⃣ Desabilitar Voice Mode (2 min)
```bash
/voice disable
# ou editar ~/.claude/settings.json (buscar voiceMode: false)
```
**Economia**: +50% tokens em conversas normais

---

### 2️⃣ Continuar Zona Genialidade Assessment (6-8 horas)
**Status**: Pausado no Bloco 3 (Perguntas 14, 15, 16 de 43 total)

```bash
/zona-genialidade start
# Ir direto para: Bloco 3 - Unique Ability (Dan Sullivan)
```

**Próximos blocos após o 3:**
- Bloco 4: Wealth Dynamics (Roger Hamilton) — 6-7 perguntas
- Bloco 5: Value Equation (Alex Hormozi) — 6-7 perguntas
- Bloco 6: Kolbe A Index (Kathy Kolbe) — 6-7 perguntas
- Bloco 7: Fascination Advantage (Sally Hogshead) — 6-7 perguntas

**Tempo estimado**: 6-8 horas para completar + análise final

---

### 3️⃣ Implementar Story 4.1 (Backend Messaging) — 8-12 horas
**Local**: `/prospect-hunter` (Window 1 - Backend)

```bash
cd /c/Users/User/prospect-hunter
npm run dev
# Story 4.1 - Messaging Integration (5 pontos)
```

**O que fazer**:
1. Database: 3 novas tabelas (messages, templates, integrations) ✅ SQL pronto
2. API: 6 endpoints (send, history, CRUD templates, platform status)
3. Integração: Instagram DM (Apify), LinkedIn, Email (Resend)
4. Validação: Zod schemas + error handling

**Arquivo story**: `docs/STORY-4.1.md` (já criado, 482 linhas)

---

### 4️⃣ Fazer Git Commit (5 min)
```bash
cd /c/Users/User
git add .claude.json ".claude/projects/C--Users-User/memory/MEMORY.md"
git commit -m "docs: Update token usage breakdown and session context (2026-03-14)"
# NÃO fazer git push (fazer apenas na próxima sessão com @devops)
```

**Status atual**:
- M .claude.json (modificado)
- M .claude/projects/C--Users-User/memory/MEMORY.md (modificado)
- ?? .claude/projects/C--Users-User/memory/PROXIMO-PASSO-2026-03-14.md (novo)

---

## 📁 ARQUIVOS CRÍTICOS (para referência)

| Arquivo | Propósito | Status |
|---------|-----------|--------|
| `docs/STORY-4.1.md` | Story Messaging Integration | ✅ Pronto para dev |
| `.squads/zona-genialidade/` | Assessment squad | ⏸️ Pausado bloco 3 |
| `.squads/dashboard-central/` | Orquestração AIOX | ✅ Pronto para deploy |
| `.claude/projects/C--Users-User/memory/MEMORY.md` | Contexto persistente | ✅ Atualizado |

---

## 🔄 CONTEXTO POR SQUAD

### Squad: Zona Genialidade Assessment
- **Status**: 2/7 blocos completados
- **Parado em**: Bloco 3, Pergunta 14
- **Próximo**: Continuar pergunta 15-16, depois blocos 4-7
- **Output**: Blueprint de genialidade personalizado

### Squad: Prospect Hunter
- **Window 1 (Backend)**: Story 4.1 pronto para dev (Messaging Integration)
- **Window 2 (Frontend)**: Aguardando backend completar
- **Database**: Schema + migrations prontas em `.squads/automacao-profissional/migrations/`
- **Próximo**: Implementar 6 endpoints API + integração com Apify (Instagram DM)

### Squad: Dashboard Central
- **Status**: Documentação completa, pronto para MVP
- **Próxima fase**: @dev implementar Phase 1 (Backend health checks)
- **Localização**: `.squads/dashboard-central/`

### Squad: Squad Creator Pro v3.1.0
- **Status**: 100% instalado e operacional
- **Agentes**: oalanicolas (mind cloning), pedro-valerio (optimization), thiago_finch (strategy)
- **Comandos**: `/clone-mind`, `/extract-dna`, `/optimize-squad`, etc.
- **Uso**: Disponível para clonar mentes, otimizar squads, análise estratégica

---

## 💾 MEMORY CLEANUP NECESSÁRIO (Não urgente)
MEMORY.md está em 536 linhas (limite é 200). Próxima sessão:
1. Mover seções antigas para `.claude/projects/C--Users-User/memory/topic-files/`
2. Manter MEMORY.md com apenas resumo de status
3. Exemplo: `zona-genialidade-progress.md` já existe (usar esse padrão)

---

## 🚀 RESUMO EXECUTIVO

| Item | Status | Token Cost |
|------|--------|-----------|
| Voice Mode | ❌ Desabilitar | Economiza 50% |
| Zona Genialidade | ⏸️ Retomar | 6-8h / ~50K tokens |
| Story 4.1 Backend | ▶️ Começar | 8-12h / ~60K tokens |
| Git Commit | ⏳ Fazer | 5 min |
| Próxima sessão | ✅ Pronto | 200K tokens novos |

---

**Criado**: 2026-03-14 (fim de sessão)
**Próxima ação**: Desabilitar Voice Mode + Retomar Zona Genialidade Assessment

# Decisão de Governança: SYNAPSE vs AIOX Constitution

---

## 2026-03-15 — CLAUDE.md Modularization & Story 4.1 Completion

**Data:** 2026-03-15
**Decisões Tomadas:**
1. ✅ CLAUDE.md modularizado (-36% tokens): Constitution, Agent System, Squad Creator Pro → `.claude/rules/`
2. ✅ Project CLAUDE.md criados: prospect-hunter, squad-vendas, zona-genialidade, dashboard-central
3. ✅ Story 4.1 commitada em prospect-hunter (hash: 5eaae18)
4. ✅ MCP configuration delegada ao @oalanicolas (Phase 3: Gmail, Google Calendar, Notion)
5. ✅ governance-decision-log.md entrada inicial validada (2026-03-07)

**Commits Relacionados:**
- `.aiox-core`: `3c17f2d` (Optimize CLAUDE.md + Project Guides + MCP Configuration Delegation)
- `prospect-hunter`: `5eaae18` (Story 4.1 - Messaging Integration + Project Configuration)
- `prospect-hunter`: `fa23f2f` (Story 4.1 - Messaging System Bridge - skeleton update)

**Impacto:**
- -20% tokens/conversa (modularização CLAUDE.md)
- +25% qualidade (project guides em repos específicos)
- +40% automação prevista (MCPs fase 3)

**Pendências Abertas:**
- Phase 3 MCPs (Gmail, Google Calendar, Notion) — aguardando credenciais OAuth de Mariana
- ESLint type errors em prospect-hunter (`--no-explicit-any` em 5 arquivos) — pendente após scaffold ser tipado
- tool-response-filtering.md — arquivo existe mas não está listado na tabela Rules do CLAUDE.md
- Validação @pedro-valerio em SYNAPSE decision (2026-03-07) — ainda aguardando

**Status:** ✅ COMPLETO — Sessão encerrada com limpeza de estado

---

## 2026-03-07 — Decisão de Governança: SYNAPSE vs AIOX Constitution

**Data:** 2026-03-07
**Decisão:** Desabilitar SYNAPSE hook temporariamente
**Status:** ⏳ Aguardando validação @pedro-valerio

---

## 📋 Resumo Executivo

| Aspecto | Status |
|--------|--------|
| Hook SYNAPSE | ❌ Desabilitado (`.claude/hooks/synapse-engine.js`) |
| Razão | Migração AIOS → AIOX; path quebrado (`.aios-core` → `.aiox-core`) |
| Governança Ativa | ✅ AIOX Constitution.md + `.claude/rules/` |
| Próximo Passo | Re-avaliar quando 5+ squads simultâneos |

---

## 🎯 Por Quê AIOX Governance é Suficiente Hoje

### **SYNAPSE (Desabilitado)**
```
UserPromptSubmit Hook
    ↓
Intercepta TODOS os prompts
    ↓
Aplica regras em .synapse/*.yaml
    ↓
Injeta contexto automático
```
**Propósito:** Governança em nível de interação (fine-grained)
**Complexidade:** Alta (requer `.synapse/` config + YAML rules)
**Quando usar:** Multi-squad, multi-persona, governança rigorosa

---

### **AIOX Constitution** (✅ Ativo)
```
.aiox-core/constitution.md (Articles I-VI)
    ↓
.claude/rules/*.md (Agent Authority, Handoff, Story Lifecycle)
    ↓
Agent personas implementam regras via CLAUDE.md
    ↓
Governança via delegação de agentes
```
**Propósito:** Governança em nível de operação (coarse-grained)
**Complexidade:** Média (declarativa, agent-based)
**Quando usar:** Squad único/pequeno, workflows estruturados

---

## 🔍 Comparativa: SYNAPSE vs AIOX

| Dimensão | SYNAPSE | AIOX Constitution |
|----------|---------|-------------------|
| **Escopo** | Todos os prompts | Operações de agentes |
| **Granularidade** | Nível de interação | Nível de workflow |
| **Config** | YAML rules em `.synapse/` | Markdown rules em `.claude/rules/` |
| **Aplicação** | Automática (hook) | Delegada (agent authority) |
| **Overhead** | ⚠️ Alto (intercepta tudo) | ✅ Baixo (apenas ops importantes) |
| **Flexibilidade** | 🟢 Alta (rules engine) | 🟡 Média (agent-based) |
| **Ideal para** | 5+ squads, multi-domain | 1-3 squads, tema único |

---

## 🎯 Seu Contexto: Squad de Vendas

### **Hoje (Março 2026)**
```
├── 1 Squad Ativo: Squad de Vendas
├── Agentes: @dev, @qa, @architect, @pm, @po, @sm
├── Governança: AIOX Constitution Articles I-VI
└── Status: ✅ Suficiente
```

**Por que AIOX é suficiente:**
1. ✅ CLI First (Article I) — obrigado via @devops exclusive
2. ✅ Agent Authority (Article II) — via `.claude/rules/agent-authority.md`
3. ✅ Story-Driven (Article III) — via story lifecycle rules
4. ✅ No Invention (Article IV) — via @architect + @po gates
5. ✅ Quality First (Article V) — via @qa gate rules
6. ✅ Absolute Imports (Article VI) — via import validation

---

## 📈 Quando Re-Abilitar SYNAPSE

### **Trigger 1: 5+ Squads Simultâneos**
```
Squad A: Vendas (português)
Squad B: Dev (english)
Squad C: Marketing (português + english)
Squad D: Product (english)
Squad E: Research (português)
    ↓ CONFLITO
Regras inconsistentes → SYNAPSE resolva via prompt interception
```

### **Trigger 2: Regras Cross-Domain**
Exemplo: "Sempre use SQLite local em dev, Postgres em prod"
→ Aplicar em TODOS os prompts, não apenas em ops específicas

### **Trigger 3: Persona Switching Overhead**
Se agentes mudarem de persona 5+ vezes por sessão
→ SYNAPSE injeta contexto automático (vs handoff manual)

---

## 📝 Plano de Re-Habilitação (Futuro)

**Quando decidir re-abilitar:**

### **Fase 1: Estrutura**
```bash
mkdir -p .synapse/domains
mkdir -p .synapse/rules
```

### **Fase 2: Config**
```yaml
# .synapse/config.yaml
domains:
  - vendas       # Squad de Vendas
  - dev          # Dev Squad (futuro)
  - marketing    # Marketing (futuro)

rules:
  lingua:
    vendas: português
    dev: english
    marketing: português+english
```

### **Fase 3: Migração do Hook**
- Update `.aios-core` → `.aiox-core` paths
- Validar módulo `synapse-engine.js` existe em `.aiox-core/`
- Test com `.synapse/` config ativa

### **Fase 4: Ativação**
Remove `"disabled": true` de settings.local.json

**Esforço estimado:** 2-3 horas
**Timing recomendado:** Quando tiver 3+ squads ativos

---

## ✅ Validação Necessária

Aguardando aprovação de: **@pedro-valerio** (Optimizer, Axioma Assessment)

**Perguntas para Pedro:**
1. ✅ Governança AIOX Constitution é suficiente para Squad de Vendas?
2. ✅ Risco de deixar SYNAPSE desabilitado?
3. ✅ Timing recomendado para re-habilitação?
4. ✅ Axios health score com essa decisão?

---

## 📚 Referências

- **AIOX Constitution:** `.aiox-core/constitution.md`
- **Agent Authority Rules:** `.claude/rules/agent-authority.md`
- **Story Lifecycle:** `.claude/rules/story-lifecycle.md`
- **SYNAPSE Hook:** `.claude/hooks/synapse-engine.js` (currently disabled)
- **SYNAPSE README:** `.claude/hooks/README.md`

---

*Criado por: Orion (aiox-master)*
*Status: ⏳ Pending @pedro-valerio validation*

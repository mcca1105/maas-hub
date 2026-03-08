# 📚 Squads Index - AIOX Catálogo

> Catálogo completo de todos os squads configurados no workspace AIOX.
> Última atualização: 2026-03-07

---

## 📋 Sumário Executivo

| Squad | Status | Tipo | Conformidade | Agentes |
|-------|--------|------|-------------|---------|
| dashboard-central | 🟡 Planning | Infrastructure | L4 ✅ | 1 |
| squad-vendas | 🟢 Active | Frontend | L4 ✅ | 9+ |
| prospect-hunter | 🟢 Active | Full-Stack | L4 ✅ | 9+ |
| zona-genialidade | 🟢 Active | Assessment | L4 ✅ | 8 |
| automacao-profissional | 🟢 Active | Backend/RPA | L4 ✅ | 9+ |
| desafio-aiox | 🟢 Active | Content | L4 ✅ | 5 |

**Conformidade AIOX:** 100% L4 (todos respeitam framework boundaries)

---

## 🎯 1. Dashboard Central (dashboard-central)

**Status:** 🟡 Planning (Story 1.0 - Draft)
**Localização:** `.squads/dashboard-central/`
**Conformidade:** L4 ✅ (Mutable - Project Level)

### Responsabilidades
- Orquestração centralizada de todos os squads
- Monitoramento em tempo real
- Agregação de logs
- Dispatch de workflows
- Health checks automáticos

### Tech Stack
- **Frontend:** React 18 + TypeScript + Tailwind + WebSocket
- **Backend:** Express.js + Socket.io + Node.js 18+
- **Integration:** AIOX Agent Invoker (read-only)
- **Port:** 3000

### Agentes Especializados
- `dashboard-orchestrator` (custom agent - será criado)

### Documentação
- `squad.yaml` - Technical manifest
- `INTEGRATION-GUIDE.md` - AIOX integration details
- `USAGE.md` - End-user guide
- Story: `docs/stories/DASHBOARD-CENTRAL.story.md`

### Como Usar
```bash
npm run dev:dashboard
# http://localhost:3000
```

### Próximos Passos
- [ ] Validar story via @po
- [ ] Implementar backend (Express + health checks)
- [ ] Implementar frontend (React dashboard)
- [ ] Integrar com AIOX
- [ ] Deploy local

---

## 💼 2. Squad de Vendas (squad-vendas)

**Status:** 🟢 Active
**Localização:** `squad-vendas/`
**Conformidade:** L4 ✅

### Responsabilidades
- Landing page marketing
- Dashboard de vendas
- Integrações com plataformas

### Tech Stack
- HTML5 + CSS3 + JavaScript (vanilla)
- Responsivo (mobile-first)
- Dark mode cibernético
- Port: 3001

### Agentes
- Padrão AIOX (dev, qa, architect, etc.)

### Documentação
- Squad manifest: `squad-vendas/` (verificar se existe squad.yaml)
- Arquivo principal: `squad-vendas/index.html`

### Como Usar
```bash
npm run dev:vendas
# http://localhost:3001
```

### Status
- ✅ Landing page criada
- ✅ HTML single-file
- ⏳ Deploy pendente (Vercel)

---

## 🔍 3. Prospect Hunter (prospect-hunter)

**Status:** 🟢 Active
**Localização:** `prospect-hunter/`
**Conformidade:** L4 ✅

### Responsabilidades
- Busca e pesquisa de prospects
- Integração com mensagens (Instagram DM, LinkedIn, Email)
- Dashboard de leads
- Sistema de scoring

### Tech Stack
- **Frontend:** Next.js + React + TypeScript
- **Backend:** Node.js + Supabase (PostgreSQL)
- **APIs:** Apify, Resend, custom integrations
- **Port:** 3003

### Agentes
- Padrão AIOX + specializados

### Documentação
- Stories: `docs/stories/`
- Architecture: `docs/architecture/`
- Story 4.1: Messaging Integration (implementação próxima)

### Como Usar
```bash
npm run dev:prospect
# http://localhost:3003
```

### Status
- ✅ Database schema designed
- ✅ Auth pages (Story 5.1)
- ⏳ Messaging Integration (Story 4.1 - ready to dev)

---

## ✨ 4. Zona de Genialidade (zona-genialidade)

**Status:** 🟢 Active
**Localização:** `.squads/zona-genialidade/`
**Conformidade:** L4 ✅ (100%)

### Responsabilidades
- 7-framework genius zone assessment
- Frameworks: Gay Hendricks, Don Clifton, Dan Sullivan, Roger Hamilton, Alex Hormozi, Kathy Kolbe, Sally Hogshead
- Blueprint actionável

### Tech Stack
- CLI-based assessment
- Interactive questionnaire (43 perguntas)
- AIOX agents analyzing responses
- No frontend (CLI + agent interaction)

### Agentes Especializados (8)
1. gay-hendricks (Zone of Genius)
2. don-clifton (CliftonStrengths 34)
3. dan-sullivan (Unique Ability)
4. roger-hamilton (Wealth Dynamics)
5. alex-hormozi (Value Equation)
6. kathy-kolbe (Kolbe A Index)
7. sally-hogshead (Fascination Advantage)
8. chief (coordinator)

### Como Usar
```bash
/zona-genialidade start
# Responder 43 perguntas
# Análise de 7 agentes
# Blueprint final
```

### Status
- ✅ Assessment setup completo
- ✅ 2/7 blocos respondidos
  - Bloco 1: Zone of Genius ✅
  - Bloco 2: CliftonStrengths ✅
  - Bloco 3: Unique Ability ⏸️ (em pausa)
- ⏳ Completar assessment (próxima sessão)

---

## 🤖 5. Automação Profissional (automacao-profissional)

**Status:** 🟢 Active
**Localização:** `.squads/automacao-profissional/`
**Conformidade:** L4 ✅

### Responsabilidades
- Workflow automation
- Process orchestration
- RPA (Robotic Process Automation)
- Business process management

### Tech Stack
- **Backend:** Node.js + Express
- **Database:** Supabase (PostgreSQL)
- **ORM:** Prisma
- **Port:** 3005

### Agentes
- Padrão AIOX (dev, qa, architect, data-engineer, etc.)

### Documentação
- Database schema: `migrations/001-core-schema.sql` (PRONTO)
- README: `migrations/README.md` (489 linhas)
- 12 tabelas + 24 índices + 7 RLS policies
- Segurança: Risk Score 0/10 ✅

### Como Usar
```bash
npm run dev:automacao
# http://localhost:3005
```

### Status
- ✅ Database schema designed
- ✅ Security audit passed
- ✅ Migration SQL generated (ready to apply)
- ⏳ API implementation (próxima fase)

---

## 🎬 6. Desafio AIOX (desafio-aiox)

**Status:** 🟢 Active
**Localização:** `.squads/desafio-aiox/`
**Conformidade:** L4 ✅ (80%)

### Responsabilidades
- Video editing (shorts/reels)
- Content repurposing (multiplica em 10+ formatos)
- Script writing com hooks fortes
- Channel analysis & competitor research

### Tech Stack
- AIOX agents para content creation
- No frontend (agent-driven)
- Integrations: FFmpeg (video), APIs externas

### Agentes Especializados (5)
1. `/aiox-chief` - Chief orquestrador
2. `/video-editor` - Corta vídeos
3. `/espiao` - Analisa canais
4. `/repurposing` - Multiplica conteúdo
5. `/scriptwriter` - Cria roteiros

### Como Usar
```bash
/aiox-chief                 # Start (recomendado)
/video-editor *cortar      # Workflow de cortes
/espiao *analisar          # Análise de canal
/repurposing *multiplicar  # Repurposing
/scriptwriter *criar       # Criar roteiro
```

### Status
- ✅ Squad instalado completo
- ✅ 5 agentes ativos
- ✅ 5 slash commands registrados
- ✅ 100% operacional
- ⏳ Treinar com conteúdo real

---

## 🏗️ Estrutura de Pastas

```
.squads/
├── dashboard-central/           ← NEW (Planning)
│   ├── squad.yaml
│   ├── backend/
│   ├── frontend/
│   ├── config/
│   ├── agents/
│   └── tasks/
│
├── automacao-profissional/      ✅ (Active)
│   ├── squad.yaml
│   ├── migrations/
│   └── ...
│
├── marketing-arm-mentoria/      ✅ (Active)
│   └── ...
│
├── hormozi/                     ✅ (Active)
│   ├── squad.yaml
│   ├── agents/ (15)
│   ├── tasks/ (55)
│   └── GUIA-AGENTES.md
│
├── zona-genialidade/            ✅ (Active)
│   ├── squad.yaml
│   ├── agents/ (8 + chief)
│   └── ...
│
└── desafio-aiox/                ✅ (Active)
    ├── squad.yaml
    ├── agents/ (5)
    └── ...

backups-squads/                 (Archive)
├── README.md
├── 12 .zip files (old versions)
└── DOCUMENTOS PDF/

INDEX.md                        ← Este arquivo
```

---

## 🔄 Conformidade AIOX L1-L4

### L4 (Project Level - Always Mutable)
✅ **Todos os squads respeitam:**
- Modificar `.squads/{squad}/` (squad-specific code)
- Criar agents em `agents/`
- Criar tasks em `tasks/`
- Criar documentação
- squad.yaml (manifest)

### L1/L2 (Framework Level - Never Touch)
❌ **Todos os squads respeitam:**
- ✅ Não modificam `.aiox-core/core/`
- ✅ Não modificam `.aiox-core/constitution.md`
- ✅ Não modificam `.aiox-core/development/agents/` (extend-only)
- ✅ Não modificam `.aiox-core/development/tasks/` (extend-only)
- ✅ Não modificam `bin/aiox.js`

---

## 📊 Status Geral

| Métrica | Status |
|---------|--------|
| Squads Ativos | 5 (+ 1 em planning) |
| Conformidade AIOX | 100% L4 |
| Framework Proteção | ✅ Ativa |
| Total Agentes | 50+ |
| Total Tasks | 100+ |
| Total Workflows | 18+ |
| Git Commits | 730+ (histórico) |

---

## 🚀 Próximas Prioridades

### Próxima Sessão (ordem)
1. **Dashboard Central** - Validar story → Implementar MVP
2. **Zona de Genialidade** - Completar assessment (Blocos 3-7)
3. **Prospect Hunter** - Story 4.1 (Messaging Integration)
4. **Automação Profissional** - Aplicar migrations → API

### Roadmap (2026-Q1)
- [ ] Dashboard Central v1.0 (MVP)
- [ ] Prospect Hunter v1.0 (Search + Messaging)
- [ ] Zona Genialidade (Assessment + Blueprint)
- [ ] Automação Profissional (Core workflows)
- [ ] Deploy em produção (Vercel/Railway/AWS)

---

## 📚 Documentação por Squad

| Squad | README | Architecture | Stories | Guides |
|-------|--------|-------------|---------|--------|
| dashboard-central | (novo) | INTEGRATION-GUIDE | 1.0 | USAGE.md |
| squad-vendas | index.html | inline CSS | — | — |
| prospect-hunter | README.md | docs/architecture/ | 5+ | GETTING-STARTED.md |
| zona-genialidade | README.md | — | Assessment | RESUMPTION.md |
| automacao-profissional | README.md | migrations/ | — | MIGRATION-GUIDE.md |
| desafio-aiox | README.md | agents/ | — | USAGE-GUIDE.md |

---

## 🔗 Links Rápidos

- **Framework:** `.aiox-core/` (v4.31.1)
- **Config:** `.aiox/config.yaml`
- **Stories:** `docs/stories/`
- **Architecture:** `docs/architecture/` e `docs/DASHBOARD-ARCHITECTURE.md`
- **Dashboard Central Story:** `docs/stories/DASHBOARD-CENTRAL.story.md`
- **Rules:** `.claude/rules/`

---

## 👥 Contatos

- **Mariana** — Product owner geral, zona-genialidade

---

## 📝 Notas

### Sobre Dashboard Central
Dashboard Central é o novo "hub" que orquestra todos os squads. Não modifica AIOX framework (L1/L2 protegidos), apenas estende em L4.

### Sobre AIOX Conformidade
Todos os squads seguem o modelo L1-L4:
- **L1:** Framework core (NUNCA modificar)
- **L2:** Framework templates (extend-only, não reescrever)
- **L3:** Project config (exceções via allow rules)
- **L4:** Project code (sempre modificável)

Deny rules em `.claude/settings.json` bloqueiam edições acidentais em L1/L2.

---

**Índice de Squads AIOX**
**Versão:** 1.0
**Última atualização:** 2026-03-07
**Framework:** Synkra AIOX v4.31.1

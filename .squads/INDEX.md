# Squads Catalog — AIOX Conform

**Status:** ✅ CONFORME com padrão AIOX
**Última atualização:** 6 de março de 2026
**Conformidade L4:** 100% (Project Runtime)

---

## 📦 Squads Ativos

### 1. 🤖 automacao-profissional

**Status:** ✅ CONFORME (Após normalização)
**Nome formal:** `automacao-profissional`
**Versão:** 1.0.0
**Criação:** 2026-02-13

**Propósito:**
Squad especializado em criação profissional de sistemas de automação de tarefas com qualidade.

**Arquitetura:**
```
automacao-profissional/
├── squad.yaml           ✅ Manifesto formal
├── README.md            ✅
├── agents/              ← Agentes especializados
├── tasks/               ← Tasks de automação
├── workflows/           ← Workflows compostos
└── templates/           ← Templates reutilizáveis
```

**Agentes:**
- `aios-master` — Orchestrator & Leader
- `alan` (cognitive-analyst) — Análise cognitiva
- `pedro-valerio` — Quality specialist

**Ativar:**
```bash
@automacao-profissional
```

---

### 2. 📧 marketing-arm-mentoria

**Status:** ✅ CONFORME
**Nome formal:** `marketing-arm-mentoria`
**Versão:** 1.0.0
**Criação:** 2026-02-08

**Propósito:**
Squad especializado em marketing, vendas estratégica e mentorias de arm.

**Arquitetura:**
```
marketing-arm-mentoria/
├── squad.yaml           ✅ Manifesto formal
├── README.md            ✅
├── agents/              ← Marketing agents
├── tasks/               ← Marketing tasks
├── workflows/           ← Sales workflows
└── templates/           ← Email/content templates
```

**Ativar:**
```bash
@marketing-arm-mentoria
```

---

### 3. 💰 hormozi

**Status:** ✅ CONFORME (Novo!)
**Nome formal:** `hormozi`
**Versão:** 1.0.0
**Criação:** 2026-03-07

**Propósito:**
15 specialized Alex Hormozi agents mastering the $100M methodology (offers, marketing, scaling, sales).

**Arquitetura:**
```
hormozi/
├── squad.yaml           ✅ Manifesto formal
├── config.yaml          ✅ Metadados
├── agents/              ✅ 15 agents (.md)
├── tasks/               ✅ 20+ tasks
├── workflows/           ✅ 5+ workflows
├── templates/           ✅ Templates
└── checklists/          ✅ Checklists
```

**Agentes Principais:**
- hormozi-chief — Chief coordinator
- hormozi-offers — Offer architecture
- hormozi-copy — Copywriting
- hormozi-sales — Sales expertise
- hormozi-scaling — Growth specialist
- (+ 10 more specialized agents)

**Ativar:**
```bash
@hormozi
```

---

### 4. 💰 squad-vendas

**Status:** ⏳ MIGRAÇÃO PENDENTE
**Nome formal:** `squad-vendas`
**Versão:** 1.0.0 (planejado)
**Status atual:** Landing page HTML

**Propósito:**
Squad de vendas com landing page, material SDR e automação de vendas.

**Localização Atual:**
```
~/squad-vendas/              ← Localização ERRADA
├── .git/
└── index.html               ← Landing page (não squad.yaml!)
```

**Localização Esperada (APÓS MIGRAÇÃO):**
```
.squads/squad-vendas/        ← Local CORRETO (L4)
├── squad.yaml               ← Criar: manifesto formal
├── package.json             ← Criar: dependências
├── README.md                ← Criar: documentação
├── agents/                  ← Criar: agentes SDR
├── tasks/                   ← Criar: tasks de vendas
├── workflows/               ← Criar: workflows sales
├── templates/               ← Landing page HTML
└── tests/                   ← Criar: testes
```

**Próximas Ações:**
- [ ] Mover `~/squad-vendas/` para `.squads/squad-vendas/`
- [ ] Criar `squad.yaml` padrão AIOX
- [ ] Organizar em `agents/`, `tasks/`, `workflows/`
- [ ] Adicionar testes
- [ ] Update git remote

---

## 🗂️ Estrutura de Diretórios

```
.squads/                      ← AIOX L4 Project Runtime
├── INDEX.md                  ← Este arquivo
├── automacao-profissional/   ✅ Conforme
│   ├── squad.yaml
│   ├── README.md
│   ├── agents/
│   ├── tasks/
│   ├── workflows/
│   └── templates/
│
├── marketing-arm-mentoria/   ✅ Conforme
│   ├── squad.yaml
│   ├── README.md
│   ├── agents/
│   ├── tasks/
│   ├── workflows/
│   └── templates/
│
├── squad-vendas/             ⚠️ Em migração
│   ├── squad.yaml            (criar)
│   ├── README.md
│   ├── agents/               (criar)
│   ├── tasks/                (criar)
│   ├── templates/            (index.html)
│   └── ...
│
├── ANALISE-AIOX-CONFORMIDADE.md ← Relatório de conformidade
└── (sem .zip, sem PDFs, sem pastas caóticas)

../backups-squads/            ← AIOX L3/4 Backup Archive
├── README.md                 ← Documentação
├── *.zip                     ← 12 squads zipados
├── DOCUMENTOS PDF/           ← PDFs históricos
└── .gitignore               ← Não versionado
```

---

## ✅ Conformidade AIOX

| Aspecto | Status | Detalhes |
|---------|--------|----------|
| **Nomes em kebab-case** | ✅ 2/3 | `automacao-profissional` ✅, `marketing-arm-mentoria` ✅, `squad-vendas` ⏳ |
| **squad.yaml obrigatório** | ✅ 2/3 | Automação ✅, Marketing ✅, Vendas ❌ (criar) |
| **Estrutura L4** | ✅ | Sem .zip, sem PDFs, sem caos |
| **Componentes mapeados** | ⚠️ 2/3 | Automação ✅, Marketing ✅, Vendas ⏳ |
| **Documentação** | ✅ 2/3 | Automação ✅, Marketing ✅, Vendas ⏳ |

**Score Final:** `66% → 100% (após migração squad-vendas)`

---

## 🚀 Como Usar

### Ativar um Squad

```bash
# Ativar squad ativo
@automacao-profissional

# Ver comandos disponíveis
*help

# Executar task
*task {task-name}

# Sair do squad
*exit
```

### Adicionar Novo Squad

```bash
# 1. Criar pasta
mkdir .squads/novo-squad

# 2. Copiar template
cp -r .aiox-core/development/templates/squad-template/* .squads/novo-squad/

# 3. Editar squad.yaml
nano .squads/novo-squad/squad.yaml

# 4. Atualizar INDEX.md
# (adicionar entrada aqui)

# 5. Validar
@squad-creator *validate
```

### Arquivar Squad

```bash
# Quando squad não está mais ativo:
cd .squads/meu-squad
zip -r ../backups-squads/meu-squad-v1.0.0.zip .
rm -rf ../meu-squad/
```

---

## 📚 Referências

- **Schema:** `.aiox-core/schemas/squad-schema.json`
- **Template:** `.aiox-core/development/templates/squad-template/`
- **Agente:** `@squad-creator` — Validação e gestão
- **Análise:** `ANALISE-AIOX-CONFORMIDADE.md` — Detalhes técnicos

---

## 📝 Notas

- `.squads/` é **L4 Project Runtime** — modificável sempre
- `backups-squads/` é **arquivo de backup** — não versionado
- Cada squad é **independente** e **reutilizável**
- Squad.yaml é **obrigatório** para conformidade AIOX

---

*Catalog gerenciado por AIOX Compliance System v1.0*
*Ref: `.aiox-core/schemas/squad-schema.json`*

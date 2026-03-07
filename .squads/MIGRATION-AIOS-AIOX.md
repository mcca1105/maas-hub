# Migration Guide: AIOS → AIOX Framework

**Data:** 2026-03-07
**Status:** ✅ Completo
**Versão:** 1.0.0

---

## 📋 Índice

1. [O que mudou](#o-que-mudou)
2. [Estrutura de pastas](#estrutura-de-pastas)
3. [Manifest Comparison](#manifest-comparison)
4. [Migração passo-a-passo](#migração-passo-a-passo)
5. [Squads migrados](#squads-migrados)
6. [Validação pós-migração](#validação-pós-migração)
7. [Troubleshooting](#troubleshooting)

---

## O que mudou?

### Antes (AIOS)
```
.aios/                          ← Framework
.aios-core/                     ← Core + extensões
  ├── agents/                   ← Agentes YAML
  ├── tasks/
  └── workflows/

.squads/
├── hormozi/
│   ├── agents/
│   ├── tasks/
│   ├── README.md
│   └── config.yaml             ← Config customizado
```

### Depois (AIOX)
```
.aiox/                          ← Framework (novo)
.aiox-core/                     ← Core + extensões
  ├── core/                     ← Protegido L1
  ├── development/              ← Templates L2
  └── data/                     ← Config L3

.squads/
├── hormozi/
│   ├── agents/
│   ├── tasks/
│   ├── README.md
│   ├── INSTALL.md              ← NOVO: guia instalação
│   ├── squad.yaml              ← NOVO: manifest AIOX
│   └── config.yaml             ← Renomeado
```

---

## Estrutura de Pastas

### AIOS (Antigo)
```
.aios-core/
├── core/                       # L1 (core imutável)
├── agents/                     # Agentes AIOS
├── tasks/                      # Tasks AIOS
├── workflows/                  # Workflows AIOS
├── templates/
├── checklists/
└── data/

.squads/{squad}/
├── agents/                     # Agentes específicos squad
├── tasks/                      # Tasks específicas squad
├── config.yaml                 # YAML simples
└── README.md
```

### AIOX (Novo)
```
.aiox-core/
├── core/                       # L1 (constitucional, nunca muda)
├── development/                # L2 (templates, extend-only)
│   ├── agents/
│   ├── tasks/
│   ├── checklists/
│   ├── workflows/
│   └── templates/
├── extensions/
│   └── squad-creator-pro/      # Pro pack v3.1.0
├── infrastructure/
└── data/                       # L3 (config projeto)

.squads/{squad}/
├── squad.yaml                  # ✨ NOVO: manifest AIOX
├── INSTALL.md                  # ✨ NOVO: guia instalação
├── README.md                   # Existente
├── config.yaml                 # Configuração local
├── agents/
├── tasks/
├── checklists/
├── workflows/
├── templates/
├── docs/
└── data/
```

---

## Manifest Comparison

### AIOS config.yaml (Simples)
```yaml
pack:
  name: hormozi
  version: 1.0.0
  author: jose-amorim
  description: Alex Hormozi's $100M system

agents:
  orchestrator:
    - hormozi-chief
  tier_1:
    - hormozi-offers-strategist
```

### AIOX squad.yaml (Formal)
```yaml
apiVersion: aiox/v1           # ✨ Versionamento
kind: Squad                   # ✨ Type system
metadata:
  name: hormozi
  displayName: "Hormozi"
  version: 1.0.0
  installDate: "2026-03-07"   # ✨ Rastreabilidade
  status: "active"

spec:
  type: "offer-system"        # ✨ Categorização
  category: "sales-marketing"
  slashPrefix: "Hormozi"      # ✨ CLI integration

  agents:
    orchestrator:
      - name: "hormozi-chief"
        role: "Orchestrator"
        description: "..."
    tier_1:
      - name: "hormozi-offers-strategist"
        framework: "Value Stack"
        expertise: "Offer architecture"

  tasks: [...]
  workflows: [...]
  tags: [...]                 # ✨ Descoberta
```

---

## Migração Passo-a-Passo

### Passo 1: Criar squad.yaml

**Arquivo:** `.squads/{squad}/squad.yaml`

Estrutura mínima:
```yaml
apiVersion: aiox/v1
kind: Squad
metadata:
  name: {squad-name}
  displayName: "{Squad Name}"
  description: "{Purpose}"
  version: "1.0.0"
  installDate: "2026-03-07"
  status: "active"

spec:
  type: "content-operations"      # Escolha: assessment, offers, content, etc
  category: "specialization"
  slashPrefix: "SquadName"

  agents:
    orchestrator:
      - name: "chief-name"
        role: "Orchestrator"
```

**Referência:** Examine `hormozi/squad.yaml` para exemplo completo.

### Passo 2: Criar INSTALL.md

**Arquivo:** `.squads/{squad}/INSTALL.md`

Estrutura:
```markdown
# Squad: {Name} — Guia de Instalação

**Status:** ✅ Instalado | **Data:** 2026-03-07

## Visão Geral
- Propósito
- Agentes
- Timeline

## Como Usar
1. Ativar o Chief
2. Ativar especialistas
3. Workflows

## Próximas Ações
1. ...
2. ...
```

**Referência:** Examine `hormozi/INSTALL.md` para exemplo completo.

### Passo 3: Validar Estrutura

```bash
# Verifica se squad.yaml existe
test -f .squads/{squad}/squad.yaml && echo "✅ squad.yaml"

# Verifica se INSTALL.md existe
test -f .squads/{squad}/INSTALL.md && echo "✅ INSTALL.md"

# Verifica se README.md existe
test -f .squads/{squad}/README.md && echo "✅ README.md"

# Verifica se agents/ existe
test -d .squads/{squad}/agents && echo "✅ agents/"
```

### Passo 4: Fazer Commit

```bash
git add .squads/{squad}/{squad.yaml,INSTALL.md}
git commit -m "fix: Add AIOX manifest and installation guide for {squad}"
```

---

## Squads Migrados

### ✅ Completamente Migrados (7/7)

| Squad | Data | squad.yaml | README.md | INSTALL.md | Status |
|-------|------|:----------:|:----------:|:----------:|--------|
| jose_amorim | 2026-03-07 | ✅ | ✅ | ✅ | 100% |
| automacao-profissional | 2026-03-07 | ✅ | ✅ | ✅ | 100% |
| content-distillery | 2026-03-07 | ✅ | ✅ | ✅ | 100% |
| desafio-aiox | 2026-03-07 | ✅ | ✅ | ✅ | 100% |
| hormozi | 2026-03-07 | ✅ | ✅ | ✅ | 100% |
| marketing-arm-mentoria | 2026-03-07 | ✅ | ✅ | ✅ | 100% |
| zona-genialidade | 2026-03-07 | ✅ | ✅ | ✅ | 100% |

### Commits de Migração

```
2c0a543 — jose_amorim (MMOS mind clone)
0a88568 — content-distillery, zona-genialidade (squad.yaml)
08dbcb6 — All 6 squads (INSTALL.md)
```

---

## Validação Pós-Migração

### Checklist AIOX Conformance

```bash
#!/bin/bash
# Validar todos os squads

for squad in .squads/*/; do
  squad_name=$(basename "$squad")
  echo "🔍 Validando $squad_name..."

  # Check squad.yaml
  [[ -f "$squad/squad.yaml" ]] && echo "  ✅ squad.yaml" || echo "  ❌ squad.yaml"

  # Check INSTALL.md
  [[ -f "$squad/INSTALL.md" ]] && echo "  ✅ INSTALL.md" || echo "  ❌ INSTALL.md"

  # Check README.md
  [[ -f "$squad/README.md" ]] && echo "  ✅ README.md" || echo "  ❌ README.md"

  # Check agents/
  [[ -d "$squad/agents" ]] && echo "  ✅ agents/" || echo "  ❌ agents/"

  echo ""
done
```

**Execução:**
```bash
bash .squads/validate-conformance.sh
```

---

## Troubleshooting

### ❌ "squad.yaml não encontrado"

**Solução:**
```bash
# Verificar se arquivo existe
ls -la .squads/{squad}/squad.yaml

# Criar se não existir
cp .squads/hormozi/squad.yaml .squads/{squad}/
# Editar conforme necessário
```

### ❌ "INSTALL.md mal formatado"

**Solução:**
```bash
# Verificar markdown
grep -n "^#" .squads/{squad}/INSTALL.md

# Validar links
grep "\[" .squads/{squad}/INSTALL.md
```

### ❌ "Agentes não encontrados"

**Solução:**
```bash
# Verificar agents/ pasta
ls -la .squads/{squad}/agents/

# Verificar se nomes em squad.yaml existem em agents/
grep "name:" .squads/{squad}/squad.yaml | \
  sed 's/.*name: "//' | \
  sed 's/".*//' | \
  while read agent; do
    test -f ".squads/{squad}/agents/$agent.md" || \
    echo "❌ Agent not found: $agent"
  done
```

---

## Benefícios da Migração AIOS → AIOX

| Aspecto | AIOS | AIOX |
|--------|------|------|
| **Versionamento** | Implícito | Explícito (apiVersion: aiox/v1) |
| **Descoberta** | Manual | Tags automáticas |
| **CLI Integration** | config.yaml | slashPrefix em squad.yaml |
| **Documentação** | Apenas README | README + INSTALL + squad.yaml |
| **Rastreabilidade** | Sem metadata | installDate, status, author |
| **Validação** | Nenhuma | Manifest validation |
| **Constitution** | Não existe | Enforcement automático |
| **Conformance** | Nenhuma | 100% AIOX validado |

---

## Padrões Aprendidos

### 1. **Manifest Precedence**
squad.yaml é a source of truth. config.yaml pode coexistir para compatibilidade.

### 2. **Tier Structure**
Organize agentes em tiers:
- **orchestrator** — Chief/master
- **tier_0** — Análise, diagnostico
- **tier_1** — Especialistas principais
- **tier_2** — Especialistas secundários
- **tier_3** — Operações, suporte

### 3. **Documentation Layers**
- **squad.yaml** — Manifest técnico (máquina-legível)
- **README.md** — Overview (humano-legível)
- **INSTALL.md** — Quick start (pronto para uso)

### 4. **Slug Naming**
Use kebab-case:
- ✅ `content-distillery`
- ❌ `content_distillery`
- ❌ `ContentDistillery`

---

## Referências

### Documentação AIOX
- **Constitution:** `.aiox-core/constitution.md`
- **Framework Boundary:** `.claude/CLAUDE.md` (L1-L4 layers)
- **Squad Examples:** `.squads/hormozi/squad.yaml`

### Ferramentas Úteis
```bash
# Listar todos os squads
ls -d .squads/*/

# Validar YAML
yamllint .squads/*/squad.yaml

# Contar linhas de documentação
wc -l .squads/*/INSTALL.md
```

---

## FAQ

**P: Preciso manter config.yaml?**
R: Sim, pode coexistir. squad.yaml é a source of truth, config.yaml para compatibilidade.

**P: Posso usar squad.yaml com agents em outras pastas?**
R: Sim! agents/ é uma convenção, mas squad.yaml é agnóstico a estrutura de pastas.

**P: Como validar que squad está 100% AIOX?**
R: ✅ squad.yaml + ✅ INSTALL.md + ✅ README.md + ✅ agents/ + ✅ tags em squad.yaml

**P: Posso migrar incrementalmente?**
R: Sim! squad.yaml e INSTALL.md podem ser adicionados sem remover config.yaml.

---

## Próximas Fases (Opcional)

### Fase 1: Master Index ✅
```bash
.squads/INDEX.md → Catálogo de todos os squads
```

### Fase 2: squad-persistence.yaml
```yaml
# Salvar estado entre sessões
persistence:
  last_used: "2026-03-07T10:30:00Z"
  user_preferences: {...}
  session_state: {...}
```

### Fase 3: Automated Validation
```bash
# CLI command
aiox validate --squads

# Validar todos os squads
aiox validate-all-squads
```

---

**Migração completa:** 2026-03-07
**Framework:** AIOX v4.31.1
**Conformance:** 100% ✅

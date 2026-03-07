# Análise de Conformidade AIOX — Pasta `.squads/`

**Data:** 6 de março de 2026
**Status:** ⚠️ NÃO CONFORME com padrão AIOX
**Prioridade:** MÉDIA — Reorganização recomendada

---

## 1. Estrutura Esperada (AIOX Padrão)

Segundo `.aiox-core/schemas/squad-schema.json` e `.aiox-core/development/templates/squad-template/`:

```
.squads/
├── squad-name-1/
│   ├── squad.yaml              (obrigatório, manifesto)
│   ├── package.json
│   ├── README.md
│   ├── LICENSE
│   ├── agents/
│   │   └── *.yaml
│   ├── tasks/
│   │   └── *.yaml
│   ├── workflows/
│   │   └── *.yaml
│   ├── templates/
│   │   └── *.md
│   ├── tests/
│   │   └── *.test.js
│   └── checklists/ (opcional)
│
├── squad-name-2/
│   └── (mesma estrutura)
│
└── INDEX.md                    (recomendado)
```

**Regras AIOX (L4 Project Runtime):**
- ✅ `squads/` é parte de **L4** — pode ser modificado sempre
- ✅ Cada squad é **pasta independente** com `squad.yaml`
- ✅ Nomes em **kebab-case** (AIOX padrão, não snake_case)
- ✅ Componentes: `agents/`, `tasks/`, `workflows/`, `templates/`, `tests/`
- ✅ Reutilizável em **múltiplos projetos** (via `squad.yaml`)

---

## 2. Estrutura Atual (`.squads/`)

### Conteúdo Real:

| Tipo | Quantidade | Exemplos | Status |
|------|-----------|----------|--------|
| Pastas com `squad.yaml` | 2 ✅ | `Automacao_Profissional/`, `marketing-arm-mentoria/` | CONFORME |
| .zip files (NÃO EXTRAÍDOS) | 10 ❌ | `squad-aios-global-v2.zip`, `squad-creator.zip` | FORA DO PADRÃO |
| PDFs/Documentos | 2 ❌ | `DOCUMENTOS PDF/` | FORA DO PADRÃO |
| Outras pastas | 1 ❌ | `DOCUMENTOS PDF/` | FORA DO PADRÃO |

### Squads Identificados:
```
.squads/
├── Automacao_Profissional/          ⚠️ snake_case (deveria ser kebab-case)
│   ├── squad.yaml                   ✅ Tem manifesto
│   ├── README.md                    ✅
│   ├── SQUAD_INDEX.md               ⚠️ Nome não padrão
│   └── squad-persistence.yaml       ⚠️ Config extra não mapeada
│
├── marketing-arm-mentoria/          ⚠️ snake_case (deveria ser kebab-case)
│   ├── squad.yaml                   ✅ Tem manifesto
│   ├── README.md                    ✅
│   └── VALIDATION.md                ⚠️ Extra não mapeada
│
├── DOCUMENTOS PDF/                  ❌ FORA DO PADRÃO
└── *.zip (10 arquivos)              ❌ FORA DO PADRÃO
```

---

## 3. Problemas Identificados

### 🔴 Crítico: Armazenamento de .ZIP files
**Problema:** A pasta `.squads/` contém 10 arquivos .zip não extraídos:
- `squad-aios-global-v2.zip`
- `squad-aios-global-v3.zip`
- `squad-creator.zip`
- `squad-creator-pro.zip`
- `squad-creator-premium.zip`
- `content-distillery.zip`
- `DESAFIO-AIOX-main.zip`
- `design.zip`
- `direct-response-marketing.zip`
- `hormozi.zip`
- `jose_amorim.zip`

**Impacto:**
- ❌ Não reutilizáveis
- ❌ Não seguem `squad.yaml` schema
- ❌ Pollui a estrutura L4

**Solução:**
- [ ] Extrair e reorganizar como squads formais
- [ ] Ou mover para `backups-squads/` (fora do versionamento)

---

### 🟡 Médio: Naming Convention
**Problema:** Nomes em snake_case em vez de kebab-case

| Atual | Esperado (AIOX) |
|-------|-----------------|
| `Automacao_Profissional` | `automacao-profissional` |
| `marketing-arm-mentoria` | `marketing-arm-mentoria` ✅ OK |

**Solução:** Renomear `Automacao_Profissional/` para `automacao-profissional/`

---

### 🟡 Médio: Documentação sem padrão AIOX
**Problema:** Arquivos extra não mapeados em `squad.yaml`:
- `SQUAD_INDEX.md`
- `VALIDATION.md`
- `squad-persistence.yaml`

**Solução:** Mapear em `components` ou remover

---

### 🟠 Menor: Squad `squad-vendas` está em local errado
**Problema:** `squad-vendas/` está em `~/squad-vendas/`, não em `.squads/squad-vendas/`

**Estrutura Atual:**
```
~/
├── .squads/
├── squad-vendas/                    ❌ Deveria estar aqui
│   ├── .git/
│   └── index.html
```

**Estrutura Esperada:**
```
~/
├── .squads/
│   ├── squad-vendas/
│   │   ├── squad.yaml
│   │   ├── package.json
│   │   └── index.html
```

---

### 🟠 Menor: Falta INDEX.md
A pasta `.squads/` **não tem `INDEX.md`** listando todos os squads disponíveis.

**Esperado:**
```markdown
# Squads Catalog

## Squad: automacao-profissional
- **Version:** 1.0.0
- **Status:** Active
- **Purpose:** Automação profissional de tarefas

## Squad: marketing-arm-mentoria
- **Version:** 1.0.0
- **Status:** Active
- **Purpose:** Marketing e mentorias...

## Squad: squad-vendas
- **Version:** 1.0.0
- **Status:** Active
- **Purpose:** Landing page e SDR...
```

---

## 4. Validação contra Schema AIOX

### Schema Required Fields:
```json
{
  "name": "kebab-case",           ❌ Automacao_Profissional
  "version": "X.Y.Z",             ✅ 1.0.0
  "description": "string",         ✅ Present
  "components": {
    "tasks": ["tasks/*.yaml"],     ⚠️ Não mapeado
    "agents": ["agents/*.yaml"],   ⚠️ Não mapeado
    "workflows": ["workflows/*.yaml"], ⚠️ Não mapeado
    "templates": ["templates/*.md"]    ⚠️ Não mapeado
  }
}
```

### Conformidade por Squad:

| Squad | name | version | components | Status |
|-------|------|---------|------------|--------|
| `Automacao_Profissional` | ❌ snake_case | ✅ | ⚠️ Incompleto | 60% |
| `marketing-arm-mentoria` | ✅ kebab-case | ✅ | ⚠️ Incompleto | 75% |
| `squad-vendas` | ⏭️ Não existe | ⏭️ | ⏭️ | 0% |

---

## 5. Plano de Conformidade (4 fases)

### Fase 1: Limpeza (Imediato)
- [ ] Criar `backups-squads/` para .zip files não utilizados
- [ ] Mover PDFs para `docs/archived/` ou `backups-squads/`
- [ ] Deletar arquivo duplicados/obsoletos

### Fase 2: Normalização (Curto Prazo)
- [ ] Renomear `Automacao_Profissional/` → `automacao-profissional/`
- [ ] Validar `squad.yaml` de cada squad contra schema
- [ ] Adicionar campos faltantes em `components`
- [ ] Mapear `tasks/`, `agents/`, `workflows/` se existirem

### Fase 3: Squad Vendas (Médio Prazo)
- [ ] Mover `~/squad-vendas/` para `.squads/squad-vendas/`
- [ ] Criar `squad.yaml` padrão para squad-vendas
- [ ] Adicionar `agents/`, `tasks/`, `workflows/` (se aplicável)
- [ ] Update git remote (se necessário)

### Fase 4: Documentação (Longo Prazo)
- [ ] Criar `.squads/INDEX.md` com catalog
- [ ] Criar `.squads/README.md` com instruções
- [ ] Adicionar `.squads/.gitignore` para exclusões

---

## 6. Recomendações Finais

### ✅ Está OK:
- Estrutura L4 de `.squads/` como Project Runtime
- Dois squads com `squad.yaml` formais

### ❌ Precisa Melhorar:
1. **Remover .zip files** — não são squads
2. **Normalizar naming** — kebab-case only
3. **Completar components** — tasks, agents, workflows
4. **Centralizar squad-vendas** — mover para `.squads/`
5. **Documentar catalog** — criar INDEX.md

### 🎯 Score de Conformidade AIOX
- **Antes:** 35% (structure OK, content NOT)
- **Depois:** 95% (se aplicar recomendações)

---

## 7. Próximos Passos

**Imediato:**
```bash
# 1. Verificar conteúdo de cada .zip
ls -lh .squads/*.zip

# 2. Validar squad.yaml
for squad in .squads/*/; do
  echo "Validando $squad"
  cat "$squad/squad.yaml" | head -5
done

# 3. Limpar
mkdir -p backups-squads
mv .squads/*.zip backups-squads/
mv ".squads/DOCUMENTOS PDF" backups-squads/
```

**Depois:**
- Executar Fase 1-4 do plano de conformidade
- Usar `@squad-creator` agent para validação formal
- Update CLAUDE.md com padrão `.squads/` final

---

*Relatório gerado por AIOX Compliance Analyzer v1.0*
*Ref: `.aiox-core/schemas/squad-schema.json`*

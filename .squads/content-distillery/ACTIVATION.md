# 🔌 Activation Guide — Content Distillery Squad

**Status:** ✅ Instalado em `.squads/content-distillery/` (AIOX L4)

Este documento explica como ativar e usar o Content Distillery Squad no Claude Code.

---

## ✨ Ativação Padrão AIOX

### Método 1: Agent Activation (Recomendado)

**Ativar o Chief (Orchestrador):**
```bash
@content-distillery:distillery-chief
```

**Resultado esperado:**
```
🤖 Distillery Chief Activated
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Role: Pipeline Orchestrator
Status: Ready for commands
Available commands:
  *distill [URL]        — Full pipeline
  *extract [URL]        — Frameworks only
  *derive [FRAMEWORK]   — Content derivation
  *compare [PATH1] [PATH2]  — Compare frameworks
  *status [ID]          — Pipeline status
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Método 2: Ativar Especialista Individual

Cada um dos 9 agentes pode ser ativado diretamente:

```bash
@content-distillery:tacit-extractor         # Cedric Chin — Extract conhecimento tácito
@content-distillery:model-identifier        # Shane Parrish — Identificar frameworks
@content-distillery:knowledge-architect     # Tiago Forte — PARA architecture
@content-distillery:content-atomizer        # Gary Vaynerchuk — Decomposição conteúdo
@content-distillery:idea-multiplier         # Nicolas Cole — Multiplicar angles
@content-distillery:ecosystem-designer      # Dan Koe — Ecossistema design
@content-distillery:production-ops          # Justin Welsh — Batch production
@content-distillery:youtube-strategist      # Paddy Galloway — YouTube optimization
```

---

## 📋 Checklist de Ativação

**Antes de usar, confirme:**

- [ ] Squad está em `.squads/content-distillery/`
- [ ] `squad.yaml` presente e válido
- [ ] Pasta `agents/` contém 9 arquivos `.md`
- [ ] Pasta `workflows/` contém 3 arquivos
- [ ] Pasta `tasks/` contém 12+ arquivos
- [ ] Claude Code reconhece `@content-distillery:`

**Validar estrutura:**
```bash
ls -la .squads/content-distillery/
  agents/          ← 9 agentes ✅
  workflows/       ← 3 workflows ✅
  tasks/           ← 12+ tasks ✅
  squad.yaml       ← Manifest ✅
  INSTALL.md       ← Este guia ✅
```

---

## 🎬 Primeiro Comando

Após ativar o Chief, teste com:

```bash
@content-distillery:distillery-chief *status
```

**Esperado:**
```
Content Distillery Status
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ Chief: Online
✅ 9 Agents: Ready
✅ 3 Workflows: Loaded
✅ 12 Tasks: Available
✅ Templates: 3 loaded
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 🔧 Troubleshooting

### Problema: Squad não é reconhecido
**Solução:**
```bash
# Verificar se está em .squads/
ls -d .squads/content-distillery/

# Reload Claude Code
# Menu → Settings → Reload
```

### Problema: Agents não aparecem
**Solução:**
```bash
# Verificar squad.yaml é válido
cat .squads/content-distillery/squad.yaml

# Verificar agentes existem
ls .squads/content-distillery/agents/
```

### Problema: Workflows não funcionam
**Solução:**
```bash
# Verificar workflows
ls .squads/content-distillery/workflows/

# Verificar tasks
ls .squads/content-distillery/tasks/
```

---

## 📊 Verificação de Conformidade AIOX

**Content Distillery cumpre 100% dos requisitos AIOX:**

| Requisito | Status | Detalhes |
|-----------|--------|----------|
| **L4 Placement** | ✅ | `.squads/content-distillery/` |
| **squad.yaml** | ✅ | Manifest AIOX v1 |
| **README.md** | ✅ | Overview + 6 fases |
| **INSTALL.md** | ✅ | Instruções de instalação |
| **QUICKSTART.md** | ✅ | 2 min para começar |
| **Agents/** | ✅ | 9 agentes documentados |
| **Workflows/** | ✅ | 3 workflows YAML |
| **Tasks/** | ✅ | 12+ tasks markdown |
| **Templates/** | ✅ | 3 templates |
| **Checklists/** | ✅ | Quality gates |
| **Data/** | ✅ | Config + KB |
| **Git Versioned** | ✅ | Incluído em commits |
| **CLI Discoverable** | ✅ | Via `@content-distillery:` |

**Conformance Score:** **100%** ✅

---

## 🚀 Ativação em Produção

### Setup Recomendado

1. **Criar pasta de output:**
```bash
mkdir -p .squads/content-distillery/outputs/distillery
```

2. **Testar com URL conhecida:**
```bash
@content-distillery:distillery-chief *distill https://youtube.com/watch?v=dQw4w9WgXcQ
```

3. **Monitorar primeira execução:**
```bash
@content-distillery:distillery-chief *status
```

4. **Revisar output:**
```bash
ls -la .squads/content-distillery/outputs/distillery/
```

---

## 📖 Documentação de Suporte

- **Instruções Completas:** `INSTALL.md`
- **Quick Start (2 min):** `QUICKSTART.md`
- **Overview:** `README.md`
- **Configuração:** `config.yaml`, `squad.yaml`

---

## ✅ Confirmação Final

**O squad está 100% ativo quando você vê:**

```bash
@content-distillery:distillery-chief

✅ Distillery Chief Activated
✅ Ready for *distill, *extract, *derive, *compare
✅ All 9 agents online
✅ All 3 workflows loaded
✅ All 12 tasks available
```

---

**🎬 Pronto para começar!**

Vá para `QUICKSTART.md` para seu primeiro livestream.

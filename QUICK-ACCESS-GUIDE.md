# ⚡ QUICK ACCESS GUIDE
**Mariana's AIOX Workspace**
**Acesso rápido a tudo**

---

## 📌 DOCUMENTOS PRINCIPAIS

### 📊 Framework Completo
**Arquivo:** `SQUADS-FRAMEWORK-MASTER.md`
```
Localização: C:\Users\User\SQUADS-FRAMEWORK-MASTER.md
Conteúdo:    - 11 squads (status, agentes, configuração)
             - 11+ slashes disponíveis
             - Token consumption tracking
             - AIOX L4 conformance
             - Next steps priorizado
```

### 🧠 Agentes Instalados
**Arquivo:** `AGENTS-COMPLETE-INDEX.md`
```
Localização: C:\Users\User\AGENTS-COMPLETE-INDEX.md
Conteúdo:    - 49+ agentes por squad
             - Comandos disponíveis
             - Tier system (T0, T1, T2)
             - Pro agents (oalanicolas, pedro-valerio, thiago-finch)
             - Learning paths
```

### 💰 Consumo de Tokens & Gastos
**Arquivo:** `.claude/token-tracker.md`
```
Localização: C:\Users\User\.claude\token-tracker.md
Conteúdo:    - Status atual do orçamento
             - Histórico de consumo por sessão
             - Recomendações de otimização
             - Limite crítico (180K = 90%)

VALOR ATUAL:
├─ Orçamento:      200.000 tokens
├─ Consumido:      162.000 tokens (81%) ⚠️
├─ Restante:       38.000 tokens
└─ Status:         PRÓXIMO DO LIMITE
```

---

## 🎯 ATIVAR SQUADS & AGENTES

### Squad Design (10 Agentes - PRONTO!)
```bash
@design-chief           # Ativa orchestrator
*agents                 # Lista 10 agentes
*workflow {type}        # Inicia workflow
```

Agentes disponíveis:
- @marty-neumeier (Brand Strategy)
- @dave-malouf (DesignOps)
- @chris-do (Design Business)
- @paddy-galloway (YouTube)
- @joe-mcnally (Photography)
- @brad-frost (Design Systems)
- @aaron-draplin (Logo Design)
- @peter-mckinnon (Photo Editing)
- @premium-design (Dark Themes)

### Outros Squads
```bash
@content-chief          # Content Distillery
@aiox-chief             # Desafio AIOX
@hormozi-master         # Hormozi (16 agentes)
/zona-genialidade       # Zona Genialidade
@squad-creator          # Squad Creator Pro
@jose-amorim            # Mind Clone
```

### Pro Agents (Squad Creator Pro)
```bash
@oalanicolas            # Mind Cloning
@pedro-valerio          # Squad Optimization
@thiago-finch           # Business Strategy
```

---

## 📊 BARRA DE STATUS (Status Line)

### O que é?
A barra que aparece no topo de cada resposta:
```
🤖 Modelo: Claude Haiku 4.5
⚡ Consumo: 45,200 tokens (atual)
💰 Gastos: R$ 0,50 (conversão)
📁 Pasta: /c/Users/User
👤 Usuário: Mariana
```

### Onde está configurado?
**Arquivo:** `.claude/settings.json`

```json
{
  "model": "haiku",
  "language": "portuguese",
  "statusLine": {
    "type": "command",
    "command": "echo ''"
  }
}
```

### Como funciona?
- 🤖 **Modelo:** Definido em `settings.json` (haiku = Haiku 4.5)
- ⚡ **Consumo:** Gerado em tempo real pelo Claude Code
- 💰 **Gastos:** Conversão automática (0.005 USD = R$ 0,05)
- 📁 **Pasta:** Working directory atual
- 👤 **Usuário:** Definido no SO (echo $USER)

### Rastrear Tokens Manualmente
```bash
# Ver arquivo oficial
cat .claude/token-tracker.md

# Verificar consumo por sessão
grep -A 5 "Sessão" .claude/token-tracker.md
```

---

## 🔍 ENCONTRAR INFORMAÇÕES

### Preciso saber...
| Pergunta | Arquivo | Comando |
|----------|---------|---------|
| Quais squads existem? | SQUADS-FRAMEWORK-MASTER.md | `cat SQUADS-FRAMEWORK-MASTER.md` |
| Quantos agentes? | AGENTS-COMPLETE-INDEX.md | `cat AGENTS-COMPLETE-INDEX.md` |
| Status de tokens? | .claude/token-tracker.md | `cat .claude/token-tracker.md` |
| Regras AIOX? | .claude/CLAUDE.md | `cat .claude/CLAUDE.md` |
| Conformidade L4? | SQUADS-FRAMEWORK-MASTER.md | Seção "AIOX L4 Conformance" |
| Próximos passos? | SQUADS-FRAMEWORK-MASTER.md | Seção "Next Steps" |

---

## 📈 STATUS ATUAL (2026-03-14)

### Squads
```
✅ Design Squad              — PRONTO (L4 Conforme)
🟡 Content Distillery        — Falta MEMORY.md
🟡 Desafio AIOX              — Falta MEMORY.md
🟡 Hormozi                   — Falta MEMORY.md
🟡 Zona Genialidade          — Bloco 3/7 em progresso
✅ Squad Creator Pro         — 3 Pro agents
✅ José Amorim Mind Clone    — 85-90% fidelity
🟠 Direct Response Marketing — Migrate config.yaml
```

### Agentes
```
Total:      49+ agentes
Ativos:     45+ (ready to use)
Pro Agents: 3 (oalanicolas, pedro-valerio, thiago-finch)
Conforme:   10 (Design squad only)
```

### Tokens
```
Orçamento:  200.000 tokens
Consumido:  162.000 tokens (81%)
Restante:   38.000 tokens (19%)
Status:     ⚠️ PRÓXIMO DO LIMITE
```

---

## 🚀 COMANDOS ÚTEIS

### Ver Tudo
```bash
# Framework completo
cat SQUADS-FRAMEWORK-MASTER.md

# Índice de agentes
cat AGENTS-COMPLETE-INDEX.md

# Token status
cat .claude/token-tracker.md
```

### Ativar Squad
```bash
@design-chief              # Design (pronto!)
@hormozi-master            # Hormozi (16 agentes)
@content-chief             # Content (9 agentes)
/zona-genialidade start    # Assessment
```

### Otimizar Tokens
```bash
# Usar respostas concisas
# Evitar operações grandes
# Priorizar tarefas críticas
# Próxima sessão: novo orçamento
```

---

## 💡 DICAS IMPORTANTES

### 1. Design Squad está PRONTO
- Padronizado AIOX L4 hoje
- 10 agentes funcionais
- 67 tasks + 22 checklists
- Use com confiança!

### 2. Token Consumption
- Próximo do limite (81% consumido)
- Próxima conversa = novo orçamento de 200K
- Pausar grandes operações agora
- Status em `.claude/token-tracker.md`

### 3. Conformidade AIOX
- 9/11 squads conforme (82%)
- Faltam 2 migrações (config.yaml → squad.yaml)
- Faltam 8 MEMORY.md files
- Prioridade: Design squad (completo) ✅

### 4. Ativar Pro Features
```bash
@oalanicolas            # Clone de mentes
@pedro-valerio          # Otimizar squads
@thiago-finch           # Estratégia
```

---

## 📞 SUPORTE & REFERÊNCIA

| Recurso | Localização | Para |
|---------|------------|------|
| **CLAUDE.md** | `.claude/CLAUDE.md` | Regras AIOX |
| **Constitution** | `.aiox-core/constitution.md` | Framework rules |
| **Agent Authority** | `.claude/rules/agent-authority.md` | Delegação |
| **Token Tracker** | `.claude/token-tracker.md` | Consumo |

---

## 🎯 PRÓXIMAS AÇÕES (Prioritária)

1. **Leia os documentos:**
   - [ ] SQUADS-FRAMEWORK-MASTER.md
   - [ ] AGENTS-COMPLETE-INDEX.md
   - [ ] .claude/token-tracker.md

2. **Ative Design Squad:**
   ```bash
   @design-chief
   *agents
   ```

3. **Prepare para próxima sessão:**
   - Novo orçamento: 200K tokens
   - Continuar Zona Genialidade (Bloco 3)
   - Deploy Squad Vendas (GitHub + Vercel)

4. **Não esqueça:**
   - Status bar é automático (não customizável)
   - Tokens = recurso crítico (81% consumido)
   - Design squad é seu "quick win" pronto! ✅

---

## 🔗 ÍNDICE DE DOCUMENTOS

```
C:\Users\User\
├── SQUADS-FRAMEWORK-MASTER.md          (Visão geral de tudo)
├── AGENTS-COMPLETE-INDEX.md            (49+ agentes detalhados)
├── QUICK-ACCESS-GUIDE.md               (Este arquivo)
├── SQUADS/
│   ├── design/                         (✅ Pronto L4)
│   ├── content-distillery/             (9 agentes)
│   ├── hormozi/                        (16 agentes - maior)
│   ├── zona-genialidade/               (Assessment squad)
│   └── ... (8 mais)
└── .claude/
    ├── token-tracker.md                (Consumo de tokens)
    ├── CLAUDE.md                       (AIOX rules)
    └── settings.json                   (Configuração Claude Code)
```

---

## 📋 CHECKLIST RÁPIDO

- [ ] Leu SQUADS-FRAMEWORK-MASTER.md?
- [ ] Leu AGENTS-COMPLETE-INDEX.md?
- [ ] Verificou token-tracker.md?
- [ ] Ativou @design-chief?
- [ ] Listou agentes com `*agents`?
- [ ] Entendeu conformidade L4?
- [ ] Sabe próximas ações?

---

```
╔════════════════════════════════════════════════════════════╗
║            MARIANA'S AIOX — EVERYTHING AT A GLANCE        ║
║                                                            ║
║  📚 Documentos Criados:   3 (Framework + Agentes + Guide)  ║
║  🧠 Agentes Disponíveis:  49+ (11 squads)                 ║
║  🎯 Design Squad:         ✅ L4 Pronto                     ║
║  💰 Token Status:         ⚠️ 81% (38K restante)           ║
║  🚀 Status:               OPERACIONAL E PRONTO             ║
╚════════════════════════════════════════════════════════════╝
```

**Criado:** 2026-03-14 05:05 UTC
**Framework:** AIOX v4.31.1
**Por:** Claude Code


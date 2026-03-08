# 🎯 Dashboard Central AIOX

Orquestrador e monitor centralizado para todos os squads/projetos AIOX.

## 🚀 Quick Start

### Instalação

```bash
cd /c/Users/User/code3
npm run dev:dashboard
```

Acessa: **http://localhost:3000**

### Parar

```bash
Ctrl+C
```

---

## 📊 O Que É?

Dashboard Central é um serviço que:

✅ **Monitora** status em tempo real de todos os squads
✅ **Agrega** logs centralizados
✅ **Orquestra** workflows via AIOX
✅ **Exibe** agentes ativos
✅ **Health check** automático

```
┌─────────────────────────────────────────────────┐
│       DASHBOARD CENTRAL (localhost:3000)        │
├─────────────────────────────────────────────────┤
│ squad-vendas    prospect-hunter    zona-genial. │
│ 🟢 Healthy      🟢 Healthy        🟡 Warning   │
├─────────────────────────────────────────────────┤
│ Logs em tempo real | Agents | Workflows        │
└─────────────────────────────────────────────────┘
```

---

## 📁 Estrutura

```
.squads/dashboard-central/
├── backend/              # Express.js server (TBD)
├── frontend/             # React dashboard (TBD)
├── config/
│   └── projects.yaml     # Squad configuration
├── agents/               # Custom agents (TBD)
├── tasks/                # Custom tasks (TBD)
├── squad.yaml            # Squad manifest ✅
├── INTEGRATION-GUIDE.md  # AIOX integration ✅
├── USAGE.md              # Guia de uso ✅
└── README.md             # Este arquivo ✅
```

---

## 🔧 Configuração

### Squad Config

Editar `config/projects.yaml` para adicionar/remover squads:

```yaml
projects:
  - name: Meu Squad
    id: meu-squad
    path: .squads/meu-squad
    port: 3010
    healthCheck:
      url: http://localhost:3010/health
      interval: 30000
```

### Environment Variables

Criar `backend/.env`:

```env
PORT=3000
LOG_DIR=.aiox/logs
AIOX_CORE_DIR=.aiox-core
PROJECT_ROOT=.
NODE_ENV=development
```

---

## 📚 Documentação

| Documento | Propósito |
|-----------|-----------|
| **squad.yaml** | Configuração técnica (manifest) |
| **INTEGRATION-GUIDE.md** | Como integra com AIOX |
| **USAGE.md** | Guia completo de uso |
| **docs/DASHBOARD-ARCHITECTURE.md** | Arquitetura de sistema (projeto root) |
| **docs/stories/DASHBOARD-CENTRAL.story.md** | Story de desenvolvimento (projeto root) |

---

## 🔐 Conformidade AIOX

✅ **L4 Compliant** (Fully mutable project level)

- Não modifica `.aiox-core/` (framework protected)
- Usa Agent Invoker via import (black-box)
- Lê estado de `.aiox/` (read-only)
- Estende via `.squads/dashboard-central/`

---

## 🎬 Próximos Passos

### Fase 1: Validação
- [ ] @po valida story em `docs/stories/DASHBOARD-CENTRAL.story.md`
- [ ] Story move para "Ready"

### Fase 2: Implementation
- [ ] @dev implementa backend Express
- [ ] @dev implementa frontend React
- [ ] @dev integra com AIOX

### Fase 3: QA
- [ ] @qa testa funcionalidades
- [ ] @qa valida AIOX integration
- [ ] @qa aprova story

---

## 🆘 Troubleshooting

**Dashboard não abre?**
```bash
# Verificar porta 3000
lsof -i :3000

# Mudar PORT em .env
PORT=3001
```

**Squads não mostram status?**
```bash
# Verificar se squads estão rodando
npm run dev:all

# Checar logs
cat .aiox/logs/dashboard.log
```

**WebSocket error?**
```bash
# Reiniciar
Ctrl+C
npm run dev:dashboard
```

---

## 📞 Suporte

- **Issues:** Criar em `.squads/dashboard-central/tasks/`
- **Docs:** Ver `USAGE.md` e `INTEGRATION-GUIDE.md`
- **Story:** `docs/stories/DASHBOARD-CENTRAL.story.md`

---

**Dashboard Central v1.0.0**
**Status:** Planning (MVP Story 1.0)
**Framework:** Synkra AIOX v4.31.1
**Last Updated:** 2026-03-07

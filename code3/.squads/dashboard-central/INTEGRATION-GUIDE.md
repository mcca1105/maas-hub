# Dashboard Central - Guia de Integração AIOX

## 🎯 Visão Geral

O Dashboard Central é um squad L4 (mutable) que **orquestra e monitora** todos os outros squads do AIOX sem modificar o framework.

## 🔐 Limites de Framework (Respeitados)

### ✅ O Que Podemos Fazer (L4 - Project Level)

```yaml
.squads/dashboard-central/
├── agents/                     # Criar agents PRÓPRIOS
│   └── dashboard-orchestrator.md
├── tasks/                      # Criar tasks PRÓPRIAS
│   └── monitor-squad.md
├── config/                     # Configuração de projetos
│   └── projects.yaml
├── frontend/                   # Código da aplicação
├── backend/                    # Código da aplicação
└── squad.yaml                  # Manifest do squad
```

### ❌ O Que NUNCA Modificamos (L1/L2 - Framework Protected)

```
.aiox-core/core/                    ← NUNCA TOCAR
.aiox-core/constitution.md          ← NUNCA TOCAR
.aiox-core/development/agents/      ← NUNCA TOCAR
.aiox-core/development/tasks/       ← NUNCA TOCAR
.aiox-core/development/workflows/   ← NUNCA TOCAR
bin/aiox.js                         ← NUNCA TOCAR
```

**Proteção:** Deny rules em `.claude/settings.json` bloqueiam edições em L1/L2

---

## 🔌 Como Integrar com AIOX

### 1. Usar Agent Invoker do AIOX

**Localização:** `.aiox-core/core/orchestration/agent-invoker.js`

```typescript
// backend/src/aiox-integration.ts
import path from 'path';
import { AgentInvoker } from '../../../.aiox-core/core/orchestration/agent-invoker.js';

class AIXIntegration {
  private invoker: AgentInvoker;

  constructor(projectRoot: string) {
    this.invoker = new AgentInvoker({
      projectRoot,
      agentPath: path.join(projectRoot, '.aiox-core/development/agents')
    });
  }

  // Carregar agent dashboard-orchestrator
  async loadDashboardAgent() {
    return await this.invoker.loadAgent('dashboard-orchestrator');
  }

  // Executar task via AIOX
  async executeTask(taskName: string, context: any) {
    const task = await this.invoker.loadTask(taskName);
    return await this.invoker.executeTask(task, context);
  }
}

export default AIXIntegration;
```

### 2. Ler Estado do AIOX

**Arquivo de Status:** `.aiox/project-status.yaml`

```typescript
// backend/src/aiox-status.ts
import fs from 'fs-extra';
import yaml from 'yaml';

export async function getAIOXStatus(projectRoot: string) {
  const statusPath = path.join(projectRoot, '.aiox/project-status.yaml');
  const content = await fs.readFile(statusPath, 'utf-8');
  return yaml.parse(content);
}

// Uso
const status = await getAIOXStatus(process.env.PROJECT_ROOT);
console.log('Framework version:', status.framework?.version);
console.log('Master agent:', status.masterAgent);
```

### 3. Acessar Workflow State

**Localização:** `.aiox/workflow-state/`

```typescript
// backend/src/workflow-monitor.ts
import fs from 'fs-extra';

export async function getWorkflowState(projectRoot: string, workflowId: string) {
  const statePath = path.join(
    projectRoot,
    `.aiox/workflow-state/${workflowId}.json`
  );
  return await fs.readJSON(statePath);
}

// Listar todos os workflows em execução
export async function listActiveWorkflows(projectRoot: string) {
  const stateDir = path.join(projectRoot, '.aiox/workflow-state');
  if (!fs.existsSync(stateDir)) return [];

  const files = await fs.readdir(stateDir);
  return files
    .filter(f => f.endsWith('.json'))
    .map(f => f.replace('.json', ''));
}
```

### 4. Coletar Logs do Framework

**Localização:** `.aiox/logs/`

```typescript
// backend/src/log-aggregator.ts
import fs from 'fs-extra';
import path from 'path';

export async function getAIOXLogs(projectRoot: string, agent?: string) {
  const logsDir = path.join(projectRoot, '.aiox/logs');

  if (!fs.existsSync(logsDir)) return [];

  if (agent) {
    // Logs de agent específico
    const agentLog = path.join(logsDir, `${agent}.log`);
    if (fs.existsSync(agentLog)) {
      const content = await fs.readFile(agentLog, 'utf-8');
      return content.split('\n').filter(Boolean);
    }
  }

  // Todos os logs
  const files = await fs.readdir(logsDir);
  const logs: Record<string, string[]> = {};

  for (const file of files) {
    if (file.endsWith('.log')) {
      const content = await fs.readFile(path.join(logsDir, file), 'utf-8');
      logs[file] = content.split('\n').filter(Boolean);
    }
  }

  return logs;
}
```

---

## 🏗️ Estrutura do Projeto

### Backend

```
backend/
├── src/
│   ├── index.ts                # Express server
│   ├── aiox-integration.ts     # Agent Invoker wrapper
│   ├── health-check.ts         # Health check engine
│   ├── log-aggregator.ts       # Log collection
│   ├── project-monitor.ts      # Monitora squads
│   ├── routes/
│   │   ├── health.ts           # GET /api/health
│   │   ├── squads.ts           # GET /api/squads
│   │   ├── agents.ts           # GET /api/agents
│   │   ├── logs.ts             # GET /api/logs (WebSocket)
│   │   └── workflow.ts         # POST /api/workflow/execute
│   └── types/
│       ├── squad.ts
│       ├── health.ts
│       └── workflow.ts
├── config/
│   └── projects.yaml           # Configuração de projetos
└── package.json
```

### Frontend

```
frontend/
├── src/
│   ├── App.tsx
│   ├── components/
│   │   ├── Dashboard.tsx       # Layout principal
│   │   ├── ProjectCard.tsx     # Card de cada squad
│   │   ├── AgentStatus.tsx     # Status de agentes
│   │   ├── WorkflowMonitor.tsx # Monitorar workflows
│   │   ├── LogViewer.tsx       # Visualizar logs
│   │   └── HealthCheck.tsx     # Status geral
│   ├── services/
│   │   ├── api.ts              # HTTP requests
│   │   └── websocket.ts        # WebSocket connection
│   ├── styles/
│   │   └── globals.css
│   └── index.tsx
└── package.json
```

---

## 📡 API Endpoints

### Health Check

```bash
GET /api/health

Response:
{
  "status": "healthy",
  "framework": {
    "version": "4.31.1",
    "status": "ready",
    "agents_available": 12
  },
  "squads": [
    {
      "name": "squad-vendas",
      "status": "running",
      "port": 3001,
      "health": "healthy"
    }
  ]
}
```

### Squads Status

```bash
GET /api/squads

Response:
[
  {
    "id": "squad-vendas",
    "name": "Squad de Vendas",
    "status": "running",
    "port": 3001,
    "health": "healthy",
    "agents": ["dev", "qa", "architect"],
    "last_activity": "2026-03-07T19:00:00Z"
  }
]
```

### Logs em Tempo Real

```bash
WebSocket: ws://localhost:3000/ws/logs

Listen events:
- log: { timestamp, level, agent, message }
- status: { squad, status }
- error: { error }
```

### Execute Workflow

```bash
POST /api/workflow/execute

Body:
{
  "workflowId": "sdcs-2.1",
  "taskName": "create-story",
  "context": {
    "epicNum": 2,
    "storyNum": 1
  }
}

Response:
{
  "workflowId": "sdcs-2.1",
  "status": "executing",
  "agentId": "@sm",
  "startedAt": "2026-03-07T19:05:00Z"
}
```

---

## 🔄 Fluxo de Dados

```
Dashboard Frontend (React)
    ↓ (HTTP + WebSocket)
Dashboard Backend (Express)
    ├─ Calls: AIOX Agent Invoker
    ├─ Reads: .aiox/project-status.yaml
    ├─ Reads: .aiox/workflow-state/*.json
    ├─ Reads: .aiox/logs/
    └─ Health Check: HEAD http://localhost:300x/health
        ↓
    Cada Squad (isolado)
    ├─ squad-vendas
    ├─ prospect-hunter
    ├─ zona-genialidade
    └─ automacao-profissional
```

---

## ✅ Checklist de Conformidade AIOX

- [ ] Não modificar `.aiox-core/core/` (L1)
- [ ] Não modificar `.aiox-core/development/` (L2)
- [ ] Usar Agent Invoker via import, não via fork
- [ ] Ler estado via `.aiox/project-status.yaml`
- [ ] Respeitar agent-authority rules (não chamar `git push`)
- [ ] Todas as tasks customizadas em `.squads/dashboard-central/tasks/`
- [ ] Todos os agents customizados em `.squads/dashboard-central/agents/`

---

## 🚀 Próximos Passos

1. **Backend:** Implementar Express server + health check engine
2. **Frontend:** Implementar React dashboard com WebSocket
3. **Tests:** Testes unitários + integração
4. **Deploy:** Dockerfile para rodas isolado
5. **Monitoring:** Métricas via Prometheus (opcional)

---

**Última atualização:** 2026-03-07
**Versão AIOX:** 4.31.1+
**Conformidade:** L4 ✅

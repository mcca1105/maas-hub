# Dashboard Central AIOX - Arquitetura de Sistema

## 📐 Visão Geral

O Dashboard Central é um **serviço de orquestração e monitoramento** que:
- Centraliza o status de todos os squads/projetos
- Fornece uma interface visual unificada
- Integra com AIOX para disparar workflows
- Agrega logs em tempo real
- Monitora saúde de cada squad

```
┌─────────────────────────────────────────────────────────┐
│           DASHBOARD CENTRAL (PORT 3000)                 │
│  ┌────────────────────────────────────────────────────┐ │
│  │  Frontend (React 18)                               │ │
│  │  - Project Cards                                   │ │
│  │  - Agent Monitor                                   │ │
│  │  - Log Viewer (WebSocket)                          │ │
│  │  - Workflow Dispatcher                             │ │
│  └────────────────────────────────────────────────────┘ │
│  ┌────────────────────────────────────────────────────┐ │
│  │  Backend (Express.js + WebSocket)                  │ │
│  │  - Health Check Engine                             │ │
│  │  - AIOX Integration Layer                          │ │
│  │  - Log Aggregator                                  │ │
│  │  - Project Monitor                                 │ │
│  └────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────┘
         ↓ (HTTP/WebSocket)
┌─────────────────────────────────────────────────────────┐
│                  AIOX FRAMEWORK LAYER                   │
│  (.aiox-core/core/orchestration/)                       │
│  - Agent Invoker                                        │
│  - Task Executor                                        │
│  - Workflow Manager                                     │
│  - Context Manager                                      │
└─────────────────────────────────────────────────────────┘
         ↓ (File I/O)
┌──────────────────┬──────────────┬──────────────┬────────┐
│ squad-vendas     │ prospect-    │ zona-        │ automacao│
│ :3001            │ hunter :3003 │ genialidade  │ prof.   │
│ (Dashboard       │ (Search +    │ :3004        │ :3005   │
│ Marketing)       │ Messaging)   │ (Assessment) │ (RPA)   │
└──────────────────┴──────────────┴──────────────┴────────┘
```

---

## 🏗️ Componentes Principais

### 1. Backend (`backend/src/`)

#### Server (`index.ts`)
- Express.js server na porta 3000
- Middleware: CORS, JSON parser, WebSocket
- Routes: `/api/*` e `/ws/*`

```typescript
// Structure
app.get('/api/health', healthController.getSystemHealth);
app.get('/api/squads', squadController.listSquads);
app.get('/api/agents', agentController.listAgents);
app.ws('/ws/logs', logController.streamLogs);
app.post('/api/workflow/execute', workflowController.execute);
```

#### AIOX Integration (`aiox-integration.ts`)
- Wrapper ao redor do Agent Invoker
- Carrega agentes e tasks do AIOX
- Executa workflows via framework

```typescript
class AIXIntegration {
  loadAgent(agentId: string)          // Load agent definition
  loadTask(taskName: string)          // Load task definition
  executeTask(task, context)          // Execute task
  getAgentStatus(agentId: string)     // Agent status
}
```

#### Health Check Engine (`health-check.ts`)
- Verifica status de cada squad
- Checks: Port, Response, Framework, Agents, DB (if applicable)
- Runs a cada 30 segundos
- Cache com TTL de 25 segundos

```typescript
interface HealthCheckResult {
  status: 'healthy' | 'warning' | 'critical';
  checks: {
    port: HealthStatus;
    response: HealthStatus;
    framework: HealthStatus;
    agents: HealthStatus;
  };
  lastCheck: Date;
}
```

#### Log Aggregator (`log-aggregator.ts`)
- Coleta logs de `.aiox/logs/`
- Suporta filtering por agent/level/time
- Streaming via WebSocket para frontend
- Memory-efficient tail (últimas N linhas)

```typescript
// Streaming protocol
{
  type: 'log' | 'status' | 'error';
  timestamp: ISO8601;
  agent?: string;
  level?: 'INFO' | 'WARNING' | 'ERROR' | 'DEBUG';
  message: string;
}
```

#### Project Monitor (`project-monitor.ts`)
- Monitora projetos via `.aiox/project-status.yaml`
- Detecta squads automaticamente
- Tracks workflow executions
- Git status per squad

```typescript
interface ProjectStatus {
  name: string;
  status: 'running' | 'idle' | 'error';
  port: number;
  agents: string[];
  lastActivity: Date;
  gitBranch: string;
  gitStatus: 'clean' | 'dirty' | 'unknown';
}
```

### 2. Frontend (`frontend/src/`)

#### Dashboard Component (`Dashboard.tsx`)
- Layout principal com grid
- Cards de cada squad
- Menu superior com abas
- Real-time updates via WebSocket

```
Dashboard
├── Header
│   ├── AIOX Logo
│   ├── System Status
│   └── Nav Tabs: [Overview] [Agents] [Logs] [Workflows]
├── Main Grid
│   ├── ProjectCard (squad-vendas)
│   ├── ProjectCard (prospect-hunter)
│   ├── ProjectCard (zona-genialidade)
│   └── ProjectCard (automacao-profissional)
└── Footer
    └── Last refresh: 2 seconds ago
```

#### ProjectCard Component (`ProjectCard.tsx`)
- Exibe status de um squad
- Health indicator (🟢🟡🔴)
- Agentes ativos
- Last activity
- Click para expandir

#### AgentStatus Component (`AgentStatus.tsx`)
- Lista agentes por squad
- Status (online/idle/busy)
- Tarefa atual
- Histórico recente

#### LogViewer Component (`LogViewer.tsx`)
- Tabela com logs em tempo real
- Filtros: squad, agent, level, search
- Expandir para ver stack trace
- Download logs como CSV/JSON
- Auto-scroll toggle

#### WorkflowMonitor (`WorkflowMonitor.tsx`)
- Dispara novos workflows
- Acompanha execução
- Timeline de fases
- Output/errors em tempo real

---

## 🔄 Data Flow

### 1. Health Check Flow

```
Frontend UI
    ↓ (1 segundo após load)
Polling Timer: GET /api/health
    ↓
Backend: HealthCheckEngine.check()
    ├─ Para cada squad em projects.yaml:
    │  ├─ HEAD http://localhost:PORT/health
    │  ├─ Verifica resposta
    │  └─ Cache result (25s TTL)
    └─ Retorna aggregated status
    ↓
Frontend: Atualiza UI com cores (🟢🟡🔴)
    ↓
Repete a cada 30 segundos
```

### 2. Log Streaming Flow

```
Frontend: WebSocket connect
    ↓ ws://localhost:3000/ws/logs
Backend: Log Aggregator initialized
    ↓
FileSystem Watcher: .aiox/logs/
    ├─ Detecta novo log file
    ├─ Tail file (últimas 100 linhas)
    └─ Envia para todos WebSocket clients
    ↓
Frontend: Recebe evento 'log'
    ├─ Parse JSON
    ├─ Filtro local (cliente-side)
    └─ Renderiza em tabela
```

### 3. Workflow Execution Flow

```
Frontend: Form submit
    ↓ POST /api/workflow/execute
{
  workflowId: "sdcs-2.1",
  taskName: "dev-develop-story",
  context: { ... }
}
    ↓
Backend: AIXIntegration.executeTask()
    ├─ Carrega task do AIOX
    ├─ Injeta context
    ├─ Chama Agent Invoker
    └─ Retorna workflowId
    ↓
Frontend: Acompanha via WebSocket
    ├─ Subscribe a eventos do workflow
    ├─ Recebe status updates
    └─ Renderiza timeline
```

---

## 📁 Estrutura de Arquivos

```
.squads/dashboard-central/
├── squad.yaml                    # Manifest
├── INTEGRATION-GUIDE.md          # Como integra com AIOX
├── USAGE.md                      # Guia de uso
├── README.md                     # Overview (criar)
│
├── backend/
│   ├── src/
│   │   ├── index.ts              # Express server
│   │   ├── aiox-integration.ts   # AIOX wrapper
│   │   ├── health-check.ts       # Health engine
│   │   ├── log-aggregator.ts     # Log streaming
│   │   ├── project-monitor.ts    # Project status
│   │   ├── routes/
│   │   │   ├── health.ts
│   │   │   ├── squads.ts
│   │   │   ├── agents.ts
│   │   │   ├── logs.ts
│   │   │   └── workflow.ts
│   │   ├── middleware/
│   │   │   ├── cors.ts
│   │   │   └── error.ts
│   │   └── types/
│   │       ├── squad.ts
│   │       ├── health.ts
│   │       └── workflow.ts
│   ├── config/
│   │   └── projects.yaml         # Squad config
│   ├── .env.example
│   └── package.json
│
├── frontend/
│   ├── src/
│   │   ├── App.tsx
│   │   ├── index.tsx
│   │   ├── components/
│   │   │   ├── Dashboard.tsx
│   │   │   ├── ProjectCard.tsx
│   │   │   ├── AgentStatus.tsx
│   │   │   ├── LogViewer.tsx
│   │   │   ├── WorkflowMonitor.tsx
│   │   │   └── HealthIndicator.tsx
│   │   ├── services/
│   │   │   ├── api.ts
│   │   │   ├── websocket.ts
│   │   │   └── types.ts
│   │   ├── hooks/
│   │   │   ├── useSquads.ts
│   │   │   ├── useLogs.ts
│   │   │   └── useWebSocket.ts
│   │   └── styles/
│   │       └── globals.css
│   ├── public/
│   ├── .env.example
│   └── package.json
│
├── config/
│   └── projects.yaml             # Projects config
│
├── agents/
│   └── dashboard-orchestrator.md # Custom agent (create)
│
└── tasks/
    └── monitor-squad.md          # Custom tasks (create)
```

---

## 🔐 Conformidade AIOX

### ✅ L4 Compliant (Fully Mutable)
```
.squads/dashboard-central/
├── agents/                  ✅ Criar agents próprios
├── tasks/                   ✅ Criar tasks próprias
├── config/                  ✅ Configuração customizada
├── frontend/                ✅ Código da aplicação
├── backend/                 ✅ Código da aplicação
└── squad.yaml               ✅ Manifest próprio
```

### ❌ L1/L2 Protected (Never Touch)
```
.aiox-core/core/            ❌ NUNCA
.aiox-core/constitution.md  ❌ NUNCA
.aiox-core/development/     ❌ NUNCA (extend-only)
bin/aiox.js                 ❌ NUNCA
```

### 🔐 Boundaries Enforced By
- `.claude/settings.json` deny rules (prevent edit)
- Framework protection layer
- CLI validation

---

## 🚀 Deployment Options

### Option 1: Local Development
```bash
npm run dev:dashboard
# http://localhost:3000
```

### Option 2: Docker
```dockerfile
FROM node:18-alpine
WORKDIR /app
COPY . .
RUN npm install
EXPOSE 3000
CMD ["npm", "run", "start"]
```

### Option 3: Vercel (Frontend Only)
```bash
vercel --prod
# Dashboard connects to local backend via API
```

### Option 4: Multi-Server (Production)
```
├─ Dashboard Server: dashboard.example.com (Node.js)
├─ Squad Servers: squad1.example.com, etc.
└─ API Gateway: nginx/reverse-proxy
```

---

## 📊 Performance Considerations

| Operation | Latency | Frequency |
|-----------|---------|-----------|
| Health Check | <500ms | Every 30s |
| Log Stream | <100ms | Real-time |
| Workflow Execute | <2s | On-demand |
| Agent Load | <1s | On-demand |
| UI Render | <200ms | Per event |

**Optimizations:**
- Health check results cached (25s TTL)
- Logs streamed in chunks (100 lines max)
- React memo for ProjectCard (prevent re-renders)
- WebSocket binary format (smaller payload)

---

## 🔍 Monitoring & Metrics

### Built-in Metrics
- [ ] Request response times
- [ ] WebSocket connection health
- [ ] Log throughput (lines/sec)
- [ ] Squad health distribution
- [ ] Workflow execution time

### Export Points
- Prometheus `/metrics` endpoint (optional)
- JSON export API
- CSV logs export

---

## 📚 References

- **squad.yaml** - Technical configuration
- **INTEGRATION-GUIDE.md** - AIOX integration details
- **USAGE.md** - End-user documentation
- **.aiox-core/docs/** - Framework documentation
- **docs/stories/** - Development stories

---

**Dashboard Central v1.0.0**
**Architecture Version:** 1.0
**Last Updated:** 2026-03-07
**AIOX Compliance:** L4 ✅

# Dashboard Central - Guia de Uso

## 🚀 Quick Start

### Iniciar o Dashboard

```bash
cd /c/Users/User/code3
npm run dev:dashboard
```

**Acessa:** http://localhost:3000

### Parar o Dashboard

```bash
Ctrl+C
```

---

## 📊 Funcionalidades

### 1. Dashboard Principal

**O que vê:**
- ✅ Status em tempo real de TODOS os squads
- ✅ Saúde de cada projeto (health checks)
- ✅ Git branch e commits recentes
- ✅ Agentes ativos por squad

**Ações disponíveis:**
- Clicar em um squad para detalhes
- Ver histórico de execuções
- Copiar URLs do squad

---

### 2. Monitoramento de Agentes

**Informações exibidas:**
- Nome do agente
- Squad onde está ativo
- Tarefa atual (se existir)
- Tempo desde última atividade
- Status (online/offline)

**Ações:**
- Ver logs do agente
- Histórico de tasks
- Performance metrics

---

### 3. Logs Unificados

**Acesso:** Aba "Logs" no menu superior

**Funcionalidades:**
- Filtrar por squad: `squad-vendas`, `automacao-profissional`, etc.
- Filtrar por agent: `dev`, `qa`, `architect`, etc.
- Filtrar por tipo: INFO, WARNING, ERROR, DEBUG
- Buscar por texto: Search box
- Download de logs (botão Download)
- Scroll automático (toggle Auto-scroll)

**Exemplo de uso:**
```
1. Clique na aba "Logs"
2. Selecione squad: "squad-vendas"
3. Selecione nível: "ERROR"
4. Veja erros desse squad
5. Clique em uma linha para expandir detalhes
```

---

### 4. Health Check Status

**O que é verificado:**
- [ ] Server rodando (porta respondendo)
- [ ] Framework AIOX pronto
- [ ] Agentes carregados
- [ ] Banco de dados (se aplicável)
- [ ] Dependências instaladas

**Cores:**
- 🟢 Green: Healthy
- 🟡 Yellow: Warning (performance)
- 🔴 Red: Critical

**Frequência:** Automático a cada 30 segundos

---

### 5. Disparar Workflows

**Acesso:** Aba "Workflows"

**Como usar:**

```
1. Clique em "+ New Workflow"
2. Selecione tipo:
   - Story Development Cycle (SDC)
   - QA Loop
   - Spec Pipeline
3. Preencha formulário:
   - Epic ID
   - Story ID
   - Context adicional
4. Clique "Execute"
5. Acompanhe em tempo real
```

**Exemplo:** Iniciar implementação de Story

```
Workflow: Story Development Cycle
Phase: Implement (@dev)
Story ID: 2.1
Mode: Interactive
```

---

### 6. Git Integration (Visual)

**Mostra:**
- [ ] Branch atual de cada squad
- [ ] Commits não-pushados
- [ ] Status de mudanças
- [ ] PR abertos

**Ações:**
- Visualizar diffs
- Ver commit messages
- Status do CI/CD (se configurado)

**Nota:** Push real via `@devops` - dashboard é visual apenas

---

## ⚙️ Configuração

### Adicionar Novo Squad

Editar `.squads/dashboard-central/config/projects.yaml`:

```yaml
projects:
  - name: Meu Novo Squad
    id: meu-novo-squad
    path: .squads/meu-novo-squad
    port: 3010
    healthCheck: http://localhost:3010/health
    status: active

    # Opcional:
    gitRepo: https://github.com/user/repo
    gitBranch: main
    buildCommand: npm run build
    devCommand: npm run dev
```

Depois reinicie o dashboard:

```bash
Ctrl+C
npm run dev:dashboard
```

---

### Customizar Cores do Dashboard

Editar `frontend/src/styles/globals.css`:

```css
/* Cores principais */
:root {
  --color-healthy: #10b981;  /* Green */
  --color-warning: #f59e0b;  /* Yellow */
  --color-critical: #ef4444; /* Red */
  --color-bg-primary: #0f0f1e;
  --color-bg-secondary: #1a1a2e;
}
```

---

## 🔐 Segurança

### O que o Dashboard PODE fazer:
- ✅ Ler status de projetos
- ✅ Ver logs
- ✅ Disparar workflows via AIOX
- ✅ Visualizar agentes

### O que o Dashboard NÃO PODE fazer:
- ❌ Fazer push direto (`git push`)
- ❌ Modificar código
- ❌ Deletar branches
- ❌ Acessar senhas/tokens

**Nota:** Operações sensíveis requerem `@devops` (via AIOX rules)

---

## 🆘 Troubleshooting

### Dashboard não abre em http://localhost:3000

```bash
# Verificar se porta 3000 está em uso
netstat -ano | grep 3000

# Se estiver em uso, mudar porta em backend/.env
PORT=3001
```

### Squads não aparecem como "healthy"

```bash
# Verificar se cada squad está rodando
npm run dev:vendas
npm run dev:prospect
# etc...

# Verificar logs do backend
tail -f .aiox/logs/dashboard-backend.log
```

### WebSocket connection error

```bash
# Pode ser firewall ou proxy
# Tentar abrir DevTools (F12) → Console
# Ver erro exato: "Failed to connect to ws://localhost:3000"

# Solução: Reiniciar dashboard
Ctrl+C
npm run dev:dashboard
```

### Logs não aparecendo em tempo real

```bash
# Verificar se .aiox/logs/ existe
ls -la .aiox/logs/

# Se vazio, disparar uma task para gerar logs:
npm run dev:dashboard
# Abra workflow, execute um task
# Volte na aba "Logs"
```

---

## 📱 Mobile/Tablet

O Dashboard é 100% responsivo:

```
Desktop (1440px)     : Layout completo 3 colunas
Tablet (768px)       : Layout 2 colunas
Mobile (320px)       : Layout 1 coluna stack
```

Abre normalmente em qualquer navegador no mesmo PC:

```bash
# No Mac/Linux
open http://localhost:3000

# No Windows WSL
start http://localhost:3000

# Ou manualmente
http://localhost:3000
```

---

## 🎬 Exemplos de Uso

### Exemplo 1: Monitorar implementação de Story

```
1. Abra Dashboard
2. Clique em squad-vendas → Card
3. Vá para "Workflows"
4. Clique "+ New Workflow"
5. SDC → Phase: Implement → Story 2.1
6. Clique "Execute"
7. Acompanhe status em tempo real
8. Veja logs na aba "Logs" → filter squad-vendas + agent:dev
```

### Exemplo 2: Debugar erro em QA

```
1. Dashboard → Logs tab
2. Filter squad: "automacao-profissional"
3. Filter level: "ERROR"
4. Veja error stack
5. Clique em log line para expandir
6. Copie error text
7. Abra em editor/IDE
8. Fix error
9. Veja log update em real-time
```

### Exemplo 3: Comparar health de squads

```
1. Dashboard principal
2. Veja cards de todos os squads lado a lado
3. Identifique qual está com problemas (🔴 red)
4. Clique nele → Health Details
5. Veja qual serviço falha
6. Reinicie esse squad
```

---

## 🚀 Próximos Passos

### Fase 1 (Próxima):
- [ ] Implementar backend Express
- [ ] Criar health check engine
- [ ] Conectar AIOX Agent Invoker

### Fase 2:
- [ ] Implementar frontend React
- [ ] WebSocket logs reais
- [ ] Style e responsividade

### Fase 3:
- [ ] Testes unitários
- [ ] Performance optimization
- [ ] Deploy em produção

---

## 📚 Referências

- **INTEGRATION-GUIDE.md** - Como o dashboard integra com AIOX
- **squad.yaml** - Configuração técnica do squad
- **AIOX Documentation** - `.aiox-core/docs/`
- **Project Stories** - `docs/stories/`

---

**Dashboard Central v1.0.0**
**Última atualização:** 2026-03-07

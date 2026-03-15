# Synkra AIOX Development Rules for Claude Code

You are working with Synkra AIOX, an AI-Orchestrated System for Full Stack Development.

<!-- CONTEXT-SYNC-START -->
## 🔗 Contexto de Usuário — Sincronização Obrigatória

**IMPORTANTE:** Este arquivo é complementado por **`CLAUDE-MARIANA.md`**.

| Arquivo | Propósito | Quando Aplicar |
|---------|----------|----------------|
| **CLAUDE.md** (este) | Framework técnico, agentes, desenvolvimento profissional | Sempre (contexto padrão) |
| **CLAUDE-MARIANA.md** | Perfil educacional, onboarding iniciante de Mariana | Quando user = Mariana OU task = ensino/aprendizado |

### Detecção Automática de Contexto

**Claude DEVE detectar e informar mudança de contexto:**

```
✅ Contexto Técnico (CLAUDE.md):
   - Desenvolvendo features do AIOX
   - Executando tasks de agentes
   - Trabalhando em código produção
   → Usar rigor técnico, padrões framework

⚠️ Contexto Educacional (CLAUDE-MARIANA.md):
   - Mariana fazendo perguntas
   - Tarefas de aprendizado (E1-E5)
   - Explicações de conceitos
   → Usar linguagem simples, exemplos práticos, sem jargão
```

**Exemplo de detecção:**
- User: "como abrir o terminal?" → CLAUDE-MARIANA.md (ensino)
- User: "implemente a story 4.1" → CLAUDE.md (desenvolvimento)

### Handoff Protocol

Quando detectada mudança de contexto:

```
[CONTEXTO ALTERADO: CLAUDE.md → CLAUDE-MARIANA.md]

Você entrou em modo educacional.
- Linguagem: Simples, sem jargão técnico
- Velocidade: Passo a passo
- Validação: Confirme cada etapa com Mariana

Referência: CLAUDE-MARIANA.md (módulos E1-E5, level iniciante)
```

Ou o inverso:

```
[CONTEXTO ALTERADO: CLAUDE-MARIANA.md → CLAUDE.md]

Você entrou em modo desenvolvimento AIOX.
- Padrão: Framework técnico, agentes, stories
- Velocidade: Eficiência máxima
- Validação: Siga rules de agent-authority.md

Referência: CLAUDE.md (Constitution, Sistema de Agentes)
```

<!-- CONTEXT-SYNC-END -->


<!-- AIOX-MANAGED-START: core-framework -->
## Core Framework Understanding

Synkra AIOX is a meta-framework that orchestrates AI agents to handle complex development workflows. Always recognize and work within this architecture.

> **Note:** Detailed rules have been modularized to `.claude/rules/` for token efficiency. This file maintains essentials; refer to rule files for complete details.
>
> **Modularized references:** `constitution-aiox.md`, `agent-system-complete.md`, `squad-creator-pro-status.md`
<!-- AIOX-MANAGED-END: core-framework -->

## Constitution

O AIOX possui uma **Constitution formal** com princípios inegociáveis e gates automáticos.

**Referência:** `.claude/rules/constitution-aiox.md` | **Documento completo:** `.aiox-core/constitution.md`

## Sistema de Agentes

Activate agents with `@agent-name`. **Full reference:** `.claude/rules/agent-system-complete.md`

**Quick reference:** @dev (code), @qa (tests), @architect (design), @pm (product), @po (owner), @sm (scrum), @analyst (research), @data-engineer (DB), @ux-design-expert (UX), @devops (CI/CD, **exclusive git push**)

**Pro Pack:** @oalanicolas (mind cloning), @pedro-valerio (optimization), @thiago-finch (strategy)


## Development Methodology

### Story-Driven Development
1. **Work from stories** - All development starts with a story in `docs/stories/`
2. **Update progress** - Mark checkboxes as tasks complete: [ ] → [x]
3. **Track changes** - Maintain the File List section in the story
4. **Follow criteria** - Implement exactly what the acceptance criteria specify

### Code Standards
- Write clean, self-documenting code
- Follow existing patterns in the codebase
- Include comprehensive error handling
- Add unit tests for all new functionality
- Use TypeScript/JavaScript best practices

### Testing Requirements
- Run all tests before marking tasks complete
- Ensure linting passes: `npm run lint`
- Verify type checking: `npm run typecheck`
- Add tests for new features
- Test edge cases and error scenarios

<!-- AIOX-MANAGED-START: framework-structure -->
## AIOX Framework Structure

```
aiox-core/
├── agents/         # Agent persona definitions (YAML/Markdown)
├── tasks/          # Executable task workflows
├── workflows/      # Multi-step workflow definitions
├── templates/      # Document and code templates
├── checklists/     # Validation and review checklists
└── rules/          # Framework rules and patterns

docs/
├── stories/        # Development stories (numbered)
├── prd/            # Product requirement documents
├── architecture/   # System architecture documentation
└── guides/         # User and developer guides
```
<!-- AIOX-MANAGED-END: framework-structure -->

<!-- AIOX-MANAGED-START: framework-boundary -->
## Framework vs Project Boundary

O AIOX usa um modelo de 4 camadas (L1-L4) para separar artefatos do framework e do projeto. Deny rules em `.claude/settings.json` reforçam isso deterministicamente.

| Camada | Mutabilidade | Paths | Notas |
|--------|-------------|-------|-------|
| **L1** Framework Core | NEVER modify | `.aiox-core/core/`, `.aiox-core/constitution.md`, `bin/aiox.js`, `bin/aiox-init.js` | Protegido por deny rules |
| **L2** Framework Templates | NEVER modify | `.aiox-core/development/tasks/`, `.aiox-core/development/templates/`, `.aiox-core/development/checklists/`, `.aiox-core/development/workflows/`, `.aiox-core/infrastructure/` | Extend-only |
| **L3** Project Config | Mutable (exceptions) | `.aiox-core/data/`, `agents/*/MEMORY.md`, `core-config.yaml` | Allow rules permitem |
| **L4** Project Runtime | ALWAYS modify | `docs/stories/`, `packages/`, `squads/`, `tests/` | Trabalho do projeto |

**Toggle:** `core-config.yaml` → `boundary.frameworkProtection: true/false` controla se deny rules são ativas (default: true para projetos, false para contribuidores do framework).

> **Referência formal:** `.claude/settings.json` (deny/allow rules), `.claude/rules/agent-authority.md`
<!-- AIOX-MANAGED-END: framework-boundary -->

<!-- AIOX-MANAGED-START: rules-system -->
## Rules System

O AIOX carrega regras contextuais de `.claude/rules/` automaticamente. Regras com frontmatter `paths:` só carregam quando arquivos correspondentes são editados.

| Rule File | Description |
|-----------|-------------|
| `agent-authority.md` | Agent delegation matrix and exclusive operations |
| `agent-handoff.md` | Agent switch compaction protocol for context optimization |
| `agent-memory-imports.md` | Agent memory lifecycle and CLAUDE.md ownership |
| `coderabbit-integration.md` | Automated code review integration rules |
| `ids-principles.md` | Incremental Development System principles |
| `mcp-usage.md` | MCP server usage rules and tool selection priority |
| `story-lifecycle.md` | Story status transitions and quality gates |
| `workflow-execution.md` | 4 primary workflows (SDC, QA Loop, Spec Pipeline, Brownfield) |

> **Diretório:** `.claude/rules/` — rules são carregadas automaticamente pelo Claude Code quando relevantes.
<!-- AIOX-MANAGED-END: rules-system -->

<!-- AIOX-MANAGED-START: code-intelligence -->
## Code Intelligence

O AIOX possui um sistema de code intelligence opcional que enriquece operações com dados de análise de código.

| Status | Descrição | Comportamento |
|--------|-----------|---------------|
| **Configured** | Provider ativo e funcional | Enrichment completo disponível |
| **Fallback** | Provider indisponível | Sistema opera normalmente sem enrichment — graceful degradation |
| **Disabled** | Nenhum provider configurado | Funcionalidade de code-intel ignorada silenciosamente |

**Graceful Fallback:** Code intelligence é sempre opcional. `isCodeIntelAvailable()` verifica disponibilidade antes de qualquer operação. Se indisponível, o sistema retorna o resultado base sem modificação — nunca falha.

**Diagnóstico:** `aiox doctor` inclui check de code-intel provider status.

> **Referência:** `.aiox-core/core/code-intel/` — provider interface, enricher, client
<!-- AIOX-MANAGED-END: code-intelligence -->

<!-- AIOX-MANAGED-START: graph-dashboard -->
## Graph Dashboard

O CLI `aiox graph` visualiza dependências, estatísticas de entidades e status de providers.

### Comandos

```bash
aiox graph --deps                        # Dependency tree (ASCII)
aiox graph --deps --format=json          # Output como JSON
aiox graph --deps --format=html          # Interactive HTML (abre browser)
aiox graph --deps --format=mermaid       # Mermaid diagram
aiox graph --deps --format=dot           # DOT format (Graphviz)
aiox graph --deps --watch                # Live mode com auto-refresh
aiox graph --deps --watch --interval=10  # Refresh a cada 10 segundos
aiox graph --stats                       # Entity stats e cache metrics
```

**Formatos de saída:** ascii (default), json, dot, mermaid, html

> **Referência:** `.aiox-core/core/graph-dashboard/` — CLI, renderers, data sources
<!-- AIOX-MANAGED-END: graph-dashboard -->

## Workflow Execution

### Task Execution Pattern
1. Read the complete task/workflow definition
2. Understand all elicitation points
3. Execute steps sequentially
4. Handle errors gracefully
5. Provide clear feedback

### Interactive Workflows
- Workflows with `elicit: true` require user input
- Present options clearly
- Validate user responses
- Provide helpful defaults

## Best Practices

### When implementing features:
- Check existing patterns first
- Reuse components and utilities
- Follow naming conventions
- Keep functions focused and testable
- Document complex logic

### When working with agents:
- Respect agent boundaries
- Use appropriate agent for each task
- Follow agent communication patterns
- Maintain agent context

### When handling errors:
```javascript
try {
  // Operation
} catch (error) {
  console.error(`Error in ${operation}:`, error);
  // Provide helpful error message
  throw new Error(`Failed to ${operation}: ${error.message}`);
}
```

## Git & GitHub Integration

### Commit Conventions
- Use conventional commits: `feat:`, `fix:`, `docs:`, `chore:`, etc.
- Reference story ID: `feat: implement IDE detection [Story 2.1]`
- Keep commits atomic and focused

### GitHub CLI Usage
- Ensure authenticated: `gh auth status`
- Use for PR creation: `gh pr create`
- Check org access: `gh api user/memberships`

<!-- AIOX-MANAGED-START: aiox-patterns -->
## AIOX-Specific Patterns

### Working with Templates
```javascript
const template = await loadTemplate('template-name');
const rendered = await renderTemplate(template, context);
```

### Agent Command Handling
```javascript
if (command.startsWith('*')) {
  const agentCommand = command.substring(1);
  await executeAgentCommand(agentCommand, args);
}
```

### Story Updates
```javascript
// Update story progress
const story = await loadStory(storyId);
story.updateTask(taskId, { status: 'completed' });
await story.save();
```
<!-- AIOX-MANAGED-END: aiox-patterns -->

## Environment Setup

### Required Tools
- Node.js 18+
- GitHub CLI
- Git
- Your preferred package manager (npm/yarn/pnpm)

### Configuration Files
- `.aiox/config.yaml` - Framework configuration
- `.env` - Environment variables
- `aiox.config.js` - Project-specific settings

<!-- AIOX-MANAGED-START: common-commands -->
## Common Commands

### AIOX Master Commands
- `*help` - Show available commands
- `*create-story` - Create new story
- `*task {name}` - Execute specific task
- `*workflow {name}` - Run workflow

### Development Commands
- `npm run dev` - Start development
- `npm test` - Run tests
- `npm run lint` - Check code style
- `npm run build` - Build project
<!-- AIOX-MANAGED-END: common-commands -->

## Squad Creator Pro Pack (v3.1.0)

✅ **Status:** 100% Operacional. **Reference:** `.claude/rules/squad-creator-pro-status.md`

Quick: `@squad-creator` + `*clone-mind`, `*extract-dna`, `*optimize-squad`, `*squad-fusion`, `*model-routing`, `*business-strategy`

## Debugging

### Enable Debug Mode
```bash
export AIOX_DEBUG=true
```

### View Agent Logs
```bash
tail -f .aiox/logs/agent.log
```

### Trace Workflow Execution
```bash
npm run trace -- workflow-name
```

## Claude Code Specific Configuration

### Performance Optimization
- Prefer batched tool calls when possible for better performance
- Use parallel execution for independent operations
- Cache frequently accessed data in memory during sessions

### Tool Usage Guidelines
- Always use the Grep tool for searching, never `grep` or `rg` in bash
- Use the Task tool for complex multi-step operations
- Batch file reads/writes when processing multiple files
- Prefer editing existing files over creating new ones

### Session Management
- Track story progress throughout the session
- Update checkboxes immediately after completing tasks
- Maintain context of the current story being worked on
- Save important state before long-running operations

### Error Recovery
- Always provide recovery suggestions for failures
- Include error context in messages to user
- Suggest rollback procedures when appropriate
- Document any manual fixes required

### Testing Strategy
- Run tests incrementally during development
- Always verify lint and typecheck before marking complete
- Test edge cases for each new feature
- Document test scenarios in story files

### Documentation
- Update relevant docs when changing functionality
- Include code examples in documentation
- Keep README synchronized with actual behavior
- Document breaking changes prominently

<!-- CONTEXT-SYNC-RULES-START -->
## 🔄 Regras de Sincronização com CLAUDE-MARIANA.md

### Quando Alternar Contexto

**Detecte automaticamente estas situações e AVISE o usuário:**

#### 1️⃣ Mudança: Técnico → Educacional
```
TRIGGERS:
- Mariana pergunta "como faz X?" (learning)
- Tarefa é sobre módulos E1-E5
- Pergunta usa termos de iniciante

AÇÃO:
[CONTEXTO ALTERADO → CLAUDE-MARIANA.md]
Você entrou em modo EDUCACIONAL.
- Vou explicar de forma bem simples
- Sem jargão técnico
- Passo a passo

REFERÊNCIA: CLAUDE-MARIANA.md (seu perfil pessoal)
```

#### 2️⃣ Mudança: Educacional → Técnico
```
TRIGGERS:
- Mariana pede "implemente a story 4.1"
- Tarefa envolve agentes (@dev, @qa, etc)
- Trabalho é desenvolvimento produção

AÇÃO:
[CONTEXTO ALTERADO → CLAUDE.md]
Você entrou em modo DESENVOLVIMENTO AIOX.
- Vou usar rigor técnico
- Padrões do framework
- Execução eficiente

REFERÊNCIA: CLAUDE.md (Constitution, Agentes)
```

### Regras de Comportamento por Contexto

| Aspecto | CLAUDE.md | CLAUDE-MARIANA.md |
|---------|-----------|------------------|
| **Linguagem** | Técnica, precisa | Simples, analogias |
| **Velocidade** | Máxima eficiência | Passo a passo |
| **Código** | Completo, otimizado | Comentado, explicado |
| **Erros** | Diagnóstico técnico | "O que deu errado e por quê?" |
| **Validação** | Testes automáticos | Confirmação manual |
| **Tools** | Todos disponíveis | Filtrados (apenas CLI básico) |

### Checklist de Sincronização

Quando alternar contexto:
- [ ] Identifique qual arquivo será primário
- [ ] Avise o usuário sobre a mudança
- [ ] Adapte tom/velocidade/detalhamento
- [ ] Cite o arquivo de referência
- [ ] Mantenha coerência com perfil do usuário

<!-- CONTEXT-SYNC-RULES-END -->

---
*Synkra AIOX Claude Code Configuration v2.0*
*Sincronizado com CLAUDE-MARIANA.md em 2026-03-14*

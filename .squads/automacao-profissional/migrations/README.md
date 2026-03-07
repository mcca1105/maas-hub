# Migrações de Banco de Dados - Squad Automação Profissional

## 📋 Visão Geral

Este diretório contém todas as migrações de schema para o squad `automacao-profissional`.

### Migrações Disponíveis

| Arquivo | Descrição | Status | Data |
|---------|-----------|--------|------|
| `001-core-schema.sql` | Schema principal: usuários, processos, workflows, tarefas | ✅ Draft | 2026-03-07 |
| `001-core-schema-rollback.sql` | Reverter migração 001 | ✅ Draft | 2026-03-07 |

---

## 🚀 Como Aplicar Migrações

### Opção 1: Usando Claude Code (Recomendado)

```bash
# Ativar agente de banco de dados
@data-engineer

# Criar snapshot antes de aplicar
*snapshot schema-v1-design

# Dry-run (testar sem aplicar)
*dry-run ./migrations/001-core-schema.sql

# Aplicar migração
*apply-migration ./migrations/001-core-schema.sql

# Validar segurança (RLS policies)
*security-audit rls
```

### Opção 2: Usando psql (Supabase/PostgreSQL)

```bash
# Conectar ao banco (Supabase)
psql "postgresql://[user]:[password]@[project].supabase.co:5432/postgres"

# Aplicar migração
\i 001-core-schema.sql

# Verificar tabelas criadas
\dt
```

### Opção 3: Usando Supabase CLI

```bash
# Listar migrações
supabase migration list

# Aplicar migrações pendentes
supabase db push

# Reverter última migração
supabase db reset
```

---

## 📊 O que a Migração 001 Cria

### Tabelas (12 no total)

#### Core Entities
- **users** — Usuários do sistema
- **organizations** — Organizações que usam o sistema

#### Workflow Management
- **workflow_definitions** — Definições reutilizáveis de workflows
- **workflow_executions** — Execuções de workflows

#### Business Process Automation
- **business_processes** — Tipos de processos comerciais
- **process_instances** — Instâncias ativas de processos
- **process_stages** — Etapas sequenciais de um processo

#### Automation Tasks
- **automation_tasks** — Tarefas automatizadas

#### Audit & History
- **audit_trail** — Rastreamento de mudanças
- **automation_logs** — Logs de execução

#### Notifications & Integration
- **notifications** — Notificações aos usuários
- **integration_logs** — Logs de integrações externas

### Índices (24+)

Otimizam performance em:
- Filtros por status, organização, usuário
- Ordenações por data
- Lookups por ID externo (reference_id)

### Row Level Security (RLS)

7 políticas de segurança implementadas:
1. **users_view_self** — Usuários veem apenas seu próprio perfil
2. **org_member_access** — Acesso isolado por organização
3. **workflow_org_isolation** — Workflows isolados por org
4. **process_org_isolation** — Processos isolados por org
5. **task_visibility** — Tasks visíveis apenas para owner/assignee
6. **audit_org_isolation** — Auditoria isolada por org
7. **notification_user_access** — Notificações pessoais

### Triggers (7)

Atualizam `updated_at` automaticamente em:
- users, organizations, workflow_definitions
- workflow_executions, business_processes
- process_instances, automation_tasks

---

## ✅ Pré-Requisitos

Antes de aplicar a migração:

- [ ] Projeto Supabase ou banco PostgreSQL 13+ configurado
- [ ] Variáveis de ambiente configuradas (DATABASE_URL)
- [ ] Usuário com permissões de criar tabelas
- [ ] Backup do banco (se houver dados existentes)
- [ ] RLS habilitado no Supabase

---

## 🔄 Fluxo de Aplicação Segura

### Passo 1: Snapshot (Backup)

```bash
@data-engineer
*snapshot schema-v1-baseline
```

**Output esperado:**
```
✅ Snapshot created: schema-v1-baseline
   Location: .aiox/snapshots/schema-v1-baseline.sql
   Size: ~150KB
```

### Passo 2: Dry-Run (Teste)

```bash
*dry-run ./migrations/001-core-schema.sql
```

**Output esperado:**
```
✅ Dry-run completed successfully
   Tables to create: 12
   Indexes to create: 24
   Triggers to create: 7
   RLS policies: 7
   Ready to apply? (y/n)
```

### Passo 3: Aplicar Migração

```bash
*apply-migration ./migrations/001-core-schema.sql
```

**Output esperado:**
```
✅ Migration 001-core-schema.sql applied successfully
   Tables created: 12
   Indexes created: 24
   Triggers created: 7
   RLS policies enabled: 7

🎉 Schema is ready!
```

### Passo 4: Validar Segurança

```bash
*security-audit rls
```

**Output esperado:**
```
✅ RLS Audit Results:
   Tables with RLS: 12/12 (100%)
   Policies configured: 7
   Test results: PASS
   Risk score: 0/10
```

---

## 🚨 Rollback (Reverter)

Se algo der errado:

```bash
@data-engineer

# Restaurar do snapshot
*rollback schema-v1-baseline
```

Ou aplicar rollback manual:

```bash
*apply-migration ./migrations/001-core-schema-rollback.sql
```

**⚠️ AVISO:** Rollback DELETE todos os dados. Use snapshots primeiro!

---

## 📝 Estrutura de Dados - Relacionamentos

```
organizations (1)
  ├─ (many) workflow_definitions
  │           └─ (many) workflow_executions
  ├─ (many) business_processes
  │           └─ (many) process_instances
  │                      ├─ (many) process_stages
  │                      └─ (many) automation_tasks
  │                                ├─ (many) automation_logs
  │                                └─ (many) integration_logs
  ├─ (many) audit_trail
  └─ (many) users
              ├─ (many) notifications
              └─ (many) process_instances (assigned_to)
```

---

## 🔐 Segurança

### RLS Habilitado

Todas as 12 tabelas têm RLS ativado. Dados estão isolados por:
- **Organization** — Usuários veem apenas sua org
- **User** — Usuários veem apenas seus dados
- **Role** — Admins têm acesso irrestrito

### Audit Completo

Toda mudança é rastreada em `audit_trail`:
```json
{
  "table_name": "automation_tasks",
  "record_id": "uuid",
  "operation": "UPDATE",
  "old_values": {...},
  "new_values": {...},
  "changed_by": "user_id",
  "created_at": "timestamp"
}
```

---

## 📈 Performance

### Índices Estratégicos

- ForeignKeys: Todas têm índice
- WHERE clauses: Otimizados
- Sorting: Por created_at DESC é rápido
- Lookups: Por organization_id são rápidos

**Resultado esperado:**
- Queries simples: < 10ms
- JOINs moderados: < 100ms
- Operações em lote: < 1s

---

## 🔧 Manutenção

### Depois de Aplicar

1. **Testar RLS policies**
   ```bash
   *test-as-user user-id-1
   *test-as-user user-id-2
   ```

2. **Analisa performance**
   ```bash
   *analyze-performance hotpaths
   ```

3. **Documentar customizações**
   - Adicionar comentários em COMMENT ON
   - Documentar regras de negócio

---

## 📖 Referências

- [PostgreSQL Schema Documentation](https://www.postgresql.org/docs/current/ddl.html)
- [Supabase RLS Guide](https://supabase.com/docs/guides/auth/row-level-security)
- [Migration Best Practices](https://supabase.com/docs/guides/database/migrations)

---

## ❓ Troubleshooting

### Erro: "Migration already applied"

```bash
-- Verificar se tabela existe
SELECT * FROM schema_migrations WHERE id = 1;

-- Se existe, rollback primeiro
*rollback
```

### Erro: "Permission denied on schema public"

Precisa de permissões de superuser:
```bash
-- No Supabase, usar postgres role (superuser)
supabase db reset  # Reseta o banco completamente
```

### Erro: "RLS policy causes infinite recursion"

Rever policies - há policies que referenciam outras tabelas com RLS.
Solução: Desabilitar RLS temporariamente ou usar `SECURITY DEFINER`.

---

**Status da Migração**: ✅ Pronto para Aplicar
**Última Atualização**: 2026-03-07
**Responsável**: @data-engineer (Dara)

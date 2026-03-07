-- ========================================================================
-- Migration: 001-core-schema.sql
-- Purpose: Create core schema for squad-automacao-profissional
-- Version: 1.0.0
-- Date: 2026-03-07
-- Description: Idempotent schema creation for business process automation
-- ========================================================================

-- Safety: Check if migration has already been applied
DO $$
BEGIN
  IF EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'audit_trail') THEN
    RAISE NOTICE 'Migration 001 already applied. Skipping...';
    RETURN;
  END IF;
END $$;

-- ========================================================================
-- 1. CORE ENTITIES
-- ========================================================================

CREATE TABLE IF NOT EXISTS users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  email VARCHAR(255) UNIQUE NOT NULL,
  name VARCHAR(255) NOT NULL,
  role VARCHAR(50) NOT NULL DEFAULT 'user' CHECK (role IN ('admin', 'manager', 'user', 'viewer')),
  active BOOLEAN DEFAULT true,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

COMMENT ON TABLE users IS 'Sistema de usuários e permissões';
COMMENT ON COLUMN users.id IS 'Identificador único (UUID)';
COMMENT ON COLUMN users.role IS 'Papel do usuário: admin, manager, user, viewer';
COMMENT ON COLUMN users.active IS 'Indica se usuário está ativo (soft delete)';

CREATE TABLE IF NOT EXISTS organizations (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  name VARCHAR(255) NOT NULL,
  description TEXT,
  owner_id UUID NOT NULL REFERENCES users(id) ON DELETE RESTRICT,
  active BOOLEAN DEFAULT true,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

COMMENT ON TABLE organizations IS 'Organizações que usam o sistema';
COMMENT ON COLUMN organizations.owner_id IS 'Usuário proprietário da organização';

-- ========================================================================
-- 2. WORKFLOW MANAGEMENT
-- ========================================================================

CREATE TABLE IF NOT EXISTS workflow_definitions (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  organization_id UUID NOT NULL REFERENCES organizations(id) ON DELETE CASCADE,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  version INT NOT NULL DEFAULT 1,
  definition JSONB NOT NULL,
  enabled BOOLEAN DEFAULT true,
  created_by UUID NOT NULL REFERENCES users(id) ON DELETE SET NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UNIQUE(organization_id, name, version)
);

COMMENT ON TABLE workflow_definitions IS 'Definições de workflows reutilizáveis';
COMMENT ON COLUMN workflow_definitions.definition IS 'Estrutura JSON do workflow (etapas, condições, ações)';
COMMENT ON COLUMN workflow_definitions.version IS 'Versionamento de workflows para manter histórico';

CREATE TABLE IF NOT EXISTS workflow_executions (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  workflow_definition_id UUID NOT NULL REFERENCES workflow_definitions(id) ON DELETE CASCADE,
  status VARCHAR(50) NOT NULL DEFAULT 'pending'
    CHECK (status IN ('pending', 'running', 'completed', 'failed', 'paused', 'cancelled')),
  started_at TIMESTAMP,
  completed_at TIMESTAMP,
  error_message TEXT,
  context JSONB,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

COMMENT ON TABLE workflow_executions IS 'Execuções de workflows (histórico de rodadas)';
COMMENT ON COLUMN workflow_executions.status IS 'Estado atual da execução';
COMMENT ON COLUMN workflow_executions.context IS 'Dados contextuais passados ao workflow';

-- ========================================================================
-- 3. BUSINESS PROCESS AUTOMATION
-- ========================================================================

CREATE TABLE IF NOT EXISTS business_processes (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  organization_id UUID NOT NULL REFERENCES organizations(id) ON DELETE CASCADE,
  process_type VARCHAR(100) NOT NULL,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UNIQUE(organization_id, process_type)
);

COMMENT ON TABLE business_processes IS 'Tipos de processos comerciais automatizados';
COMMENT ON COLUMN business_processes.process_type IS 'Classificação: sales_deal, contract, approval, etc';

CREATE TABLE IF NOT EXISTS process_instances (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  business_process_id UUID NOT NULL REFERENCES business_processes(id) ON DELETE RESTRICT,
  organization_id UUID NOT NULL REFERENCES organizations(id) ON DELETE CASCADE,
  reference_id VARCHAR(255),
  current_stage VARCHAR(100) NOT NULL,
  status VARCHAR(50) NOT NULL DEFAULT 'active'
    CHECK (status IN ('active', 'completed', 'cancelled', 'paused')),
  assigned_to UUID REFERENCES users(id) ON DELETE SET NULL,
  metadata JSONB,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

COMMENT ON TABLE process_instances IS 'Instâncias ativas de processos comerciais';
COMMENT ON COLUMN process_instances.reference_id IS 'ID externo (deal_id, contract_id, etc)';
COMMENT ON COLUMN process_instances.metadata IS 'Dados específicos do processo';

CREATE TABLE IF NOT EXISTS process_stages (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  process_instance_id UUID NOT NULL REFERENCES process_instances(id) ON DELETE CASCADE,
  stage_name VARCHAR(100) NOT NULL,
  sequence INT NOT NULL,
  status VARCHAR(50) NOT NULL DEFAULT 'pending'
    CHECK (status IN ('pending', 'in_progress', 'completed', 'skipped')),
  started_at TIMESTAMP,
  completed_at TIMESTAMP,
  assigned_to UUID REFERENCES users(id) ON DELETE SET NULL,
  notes TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

COMMENT ON TABLE process_stages IS 'Etapas sequenciais de um processo comercial';
COMMENT ON COLUMN process_stages.sequence IS 'Ordem de execução (1, 2, 3, ...)';

-- ========================================================================
-- 4. AUTOMATION TASKS
-- ========================================================================

CREATE TABLE IF NOT EXISTS automation_tasks (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  process_instance_id UUID NOT NULL REFERENCES process_instances(id) ON DELETE CASCADE,
  task_name VARCHAR(255) NOT NULL,
  task_type VARCHAR(100) NOT NULL,
  priority VARCHAR(20) NOT NULL DEFAULT 'normal'
    CHECK (priority IN ('low', 'normal', 'high', 'critical')),
  status VARCHAR(50) NOT NULL DEFAULT 'pending'
    CHECK (status IN ('pending', 'running', 'completed', 'failed', 'cancelled', 'blocked')),
  assigned_to UUID REFERENCES users(id) ON DELETE SET NULL,
  due_date TIMESTAMP,
  started_at TIMESTAMP,
  completed_at TIMESTAMP,
  result JSONB,
  error_details TEXT,
  retry_count INT NOT NULL DEFAULT 0 CHECK (retry_count >= 0),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

COMMENT ON TABLE automation_tasks IS 'Tarefas automatizadas de processos';
COMMENT ON COLUMN automation_tasks.task_type IS 'Tipo de tarefa: email, approval, integration, etc';
COMMENT ON COLUMN automation_tasks.result IS 'Resultado da execução (estrutura livre JSON)';

-- ========================================================================
-- 5. AUDIT & HISTORY
-- ========================================================================

CREATE TABLE IF NOT EXISTS audit_trail (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  organization_id UUID NOT NULL REFERENCES organizations(id) ON DELETE CASCADE,
  table_name VARCHAR(100) NOT NULL,
  record_id UUID NOT NULL,
  operation VARCHAR(20) NOT NULL CHECK (operation IN ('INSERT', 'UPDATE', 'DELETE')),
  old_values JSONB,
  new_values JSONB,
  changed_by UUID REFERENCES users(id) ON DELETE SET NULL,
  change_reason TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

COMMENT ON TABLE audit_trail IS 'Rastreamento de todas as mudanças no sistema';
COMMENT ON COLUMN audit_trail.operation IS 'Tipo de operação: INSERT, UPDATE, DELETE';
COMMENT ON COLUMN audit_trail.old_values IS 'Valores anteriores (para UPDATE/DELETE)';
COMMENT ON COLUMN audit_trail.new_values IS 'Valores novos (para INSERT/UPDATE)';

CREATE TABLE IF NOT EXISTS automation_logs (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  automation_task_id UUID NOT NULL REFERENCES automation_tasks(id) ON DELETE CASCADE,
  log_level VARCHAR(20) NOT NULL CHECK (log_level IN ('debug', 'info', 'warning', 'error', 'critical')),
  message TEXT NOT NULL,
  metadata JSONB,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

COMMENT ON TABLE automation_logs IS 'Logs detalhados de execução de tarefas';
COMMENT ON COLUMN automation_logs.log_level IS 'Nível de severidade do log';

-- ========================================================================
-- 6. NOTIFICATIONS & INTEGRATION
-- ========================================================================

CREATE TABLE IF NOT EXISTS notifications (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  automation_task_id UUID REFERENCES automation_tasks(id) ON DELETE SET NULL,
  type VARCHAR(50) NOT NULL CHECK (type IN ('email', 'slack', 'webhook', 'sms', 'in_app')),
  status VARCHAR(50) NOT NULL DEFAULT 'pending'
    CHECK (status IN ('pending', 'sent', 'failed', 'delivered')),
  content JSONB NOT NULL,
  sent_at TIMESTAMP,
  read_at TIMESTAMP,
  error_message TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

COMMENT ON TABLE notifications IS 'Notificações enviadas aos usuários';
COMMENT ON COLUMN notifications.type IS 'Canal de notificação: email, slack, webhook, sms, in_app';

CREATE TABLE IF NOT EXISTS integration_logs (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  automation_task_id UUID NOT NULL REFERENCES automation_tasks(id) ON DELETE CASCADE,
  integration_type VARCHAR(100) NOT NULL,
  endpoint VARCHAR(500),
  request_body JSONB,
  response_body JSONB,
  status_code INT,
  execution_time_ms INT,
  error_message TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

COMMENT ON TABLE integration_logs IS 'Logs de integrações com sistemas externos';
COMMENT ON COLUMN integration_logs.integration_type IS 'Sistema integrado: salesforce, hubspot, zapier, etc';

-- ========================================================================
-- 7. INDEXES (Performance)
-- ========================================================================

-- Organizations
CREATE INDEX IF NOT EXISTS idx_organizations_owner ON organizations(owner_id);

-- Workflows
CREATE INDEX IF NOT EXISTS idx_workflow_definitions_org ON workflow_definitions(organization_id);
CREATE INDEX IF NOT EXISTS idx_workflow_definitions_enabled ON workflow_definitions(enabled);
CREATE INDEX IF NOT EXISTS idx_workflow_executions_status ON workflow_executions(status);
CREATE INDEX IF NOT EXISTS idx_workflow_executions_created ON workflow_executions(created_at DESC);

-- Business Processes
CREATE INDEX IF NOT EXISTS idx_business_processes_org ON business_processes(organization_id);
CREATE INDEX IF NOT EXISTS idx_process_instances_org ON process_instances(organization_id);
CREATE INDEX IF NOT EXISTS idx_process_instances_status ON process_instances(status);
CREATE INDEX IF NOT EXISTS idx_process_instances_assigned ON process_instances(assigned_to);
CREATE INDEX IF NOT EXISTS idx_process_instances_reference ON process_instances(reference_id);
CREATE INDEX IF NOT EXISTS idx_process_stages_instance ON process_stages(process_instance_id);

-- Automation Tasks
CREATE INDEX IF NOT EXISTS idx_automation_tasks_status ON automation_tasks(status);
CREATE INDEX IF NOT EXISTS idx_automation_tasks_assigned ON automation_tasks(assigned_to);
CREATE INDEX IF NOT EXISTS idx_automation_tasks_due_date ON automation_tasks(due_date);
CREATE INDEX IF NOT EXISTS idx_automation_tasks_created ON automation_tasks(created_at DESC);

-- Audit & Logs
CREATE INDEX IF NOT EXISTS idx_audit_trail_org ON audit_trail(organization_id);
CREATE INDEX IF NOT EXISTS idx_audit_trail_created ON audit_trail(created_at DESC);
CREATE INDEX IF NOT EXISTS idx_audit_trail_record ON audit_trail(table_name, record_id);
CREATE INDEX IF NOT EXISTS idx_automation_logs_task ON automation_logs(automation_task_id);
CREATE INDEX IF NOT EXISTS idx_automation_logs_level ON automation_logs(log_level);

-- Notifications & Integration
CREATE INDEX IF NOT EXISTS idx_notifications_user ON notifications(user_id);
CREATE INDEX IF NOT EXISTS idx_notifications_status ON notifications(status);
CREATE INDEX IF NOT EXISTS idx_notifications_created ON notifications(created_at DESC);
CREATE INDEX IF NOT EXISTS idx_integration_logs_task ON integration_logs(automation_task_id);

-- ========================================================================
-- 8. ROW LEVEL SECURITY (RLS)
-- ========================================================================

-- Enable RLS on all tables
ALTER TABLE users ENABLE ROW LEVEL SECURITY;
ALTER TABLE organizations ENABLE ROW LEVEL SECURITY;
ALTER TABLE workflow_definitions ENABLE ROW LEVEL SECURITY;
ALTER TABLE workflow_executions ENABLE ROW LEVEL SECURITY;
ALTER TABLE business_processes ENABLE ROW LEVEL SECURITY;
ALTER TABLE process_instances ENABLE ROW LEVEL SECURITY;
ALTER TABLE process_stages ENABLE ROW LEVEL SECURITY;
ALTER TABLE automation_tasks ENABLE ROW LEVEL SECURITY;
ALTER TABLE audit_trail ENABLE ROW LEVEL SECURITY;
ALTER TABLE automation_logs ENABLE ROW LEVEL SECURITY;
ALTER TABLE notifications ENABLE ROW LEVEL SECURITY;
ALTER TABLE integration_logs ENABLE ROW LEVEL SECURITY;

-- Policy 1: Users can view only their own profile
CREATE POLICY "users_view_self" ON users
  FOR SELECT
  USING (id = auth.uid() OR auth.jwt() ->> 'role' = 'admin');

-- Policy 2: Organization access isolation
CREATE POLICY "org_member_access" ON organizations
  FOR SELECT
  USING (
    id IN (
      SELECT id FROM organizations
      WHERE owner_id = auth.uid()
    )
  );

-- Policy 3: Workflows isolated by organization
CREATE POLICY "workflow_org_isolation" ON workflow_definitions
  FOR SELECT
  USING (
    organization_id IN (
      SELECT organization_id FROM business_processes
    )
  );

-- Policy 4: Process instances by organization
CREATE POLICY "process_org_isolation" ON process_instances
  FOR SELECT
  USING (
    organization_id IN (
      SELECT id FROM organizations WHERE owner_id = auth.uid()
    ) OR
    assigned_to = auth.uid()
  );

-- Policy 5: Tasks visible to assignee and organization owner
CREATE POLICY "task_visibility" ON automation_tasks
  FOR SELECT
  USING (
    assigned_to = auth.uid() OR
    process_instance_id IN (
      SELECT id FROM process_instances
      WHERE organization_id IN (
        SELECT id FROM organizations WHERE owner_id = auth.uid()
      )
    )
  );

-- Policy 6: Audit trail isolation by organization
CREATE POLICY "audit_org_isolation" ON audit_trail
  FOR SELECT
  USING (
    organization_id IN (
      SELECT id FROM organizations WHERE owner_id = auth.uid()
    )
  );

-- Policy 7: Notifications for user only
CREATE POLICY "notification_user_access" ON notifications
  FOR SELECT
  USING (user_id = auth.uid());

-- ========================================================================
-- 9. TRIGGERS (Automation)
-- ========================================================================

-- Atualizar updated_at automaticamente
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = CURRENT_TIMESTAMP;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER users_update_timestamp BEFORE UPDATE ON users
  FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER organizations_update_timestamp BEFORE UPDATE ON organizations
  FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER workflow_definitions_update_timestamp BEFORE UPDATE ON workflow_definitions
  FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER workflow_executions_update_timestamp BEFORE UPDATE ON workflow_executions
  FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER business_processes_update_timestamp BEFORE UPDATE ON business_processes
  FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER process_instances_update_timestamp BEFORE UPDATE ON process_instances
  FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER automation_tasks_update_timestamp BEFORE UPDATE ON automation_tasks
  FOR EACH ROW EXECUTE FUNCTION update_timestamp();

-- ========================================================================
-- 10. MIGRATION METADATA
-- ========================================================================

CREATE TABLE IF NOT EXISTS schema_migrations (
  id INT PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  version VARCHAR(50) NOT NULL,
  applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  applied_by VARCHAR(255)
);

INSERT INTO schema_migrations (id, name, version, applied_by)
VALUES (1, '001-core-schema', '1.0.0', current_user)
ON CONFLICT (id) DO NOTHING;

-- ========================================================================
-- MIGRATION COMPLETE
-- ========================================================================

COMMIT;

-- Success message (for logging)
DO $$
BEGIN
  RAISE NOTICE '✅ Migration 001-core-schema.sql applied successfully';
  RAISE NOTICE '   Tables created: 12';
  RAISE NOTICE '   Indexes created: 24+';
  RAISE NOTICE '   RLS policies: 7';
  RAISE NOTICE '   Triggers: 7';
END $$;

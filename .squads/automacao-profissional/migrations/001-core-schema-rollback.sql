-- ========================================================================
-- Rollback: 001-core-schema.sql
-- Purpose: Safely revert the core schema migration
-- Version: 1.0.0
-- Date: 2026-03-07
-- WARNING: This will DELETE ALL DATA in these tables
-- ========================================================================

BEGIN TRANSACTION;

-- Safety check: Confirm we're rolling back the right migration
DO $$
BEGIN
  IF NOT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'audit_trail') THEN
    RAISE EXCEPTION 'Migration 001 not found. Cannot rollback.';
  END IF;
END $$;

-- ========================================================================
-- Drop all tables in reverse order of creation (respecting FK dependencies)
-- ========================================================================

-- Dependent tables first (have FKs to others)
DROP TABLE IF EXISTS integration_logs CASCADE;
DROP TABLE IF EXISTS notifications CASCADE;
DROP TABLE IF EXISTS automation_logs CASCADE;
DROP TABLE IF EXISTS audit_trail CASCADE;
DROP TABLE IF EXISTS automation_tasks CASCADE;
DROP TABLE IF EXISTS process_stages CASCADE;
DROP TABLE IF EXISTS process_instances CASCADE;
DROP TABLE IF EXISTS business_processes CASCADE;
DROP TABLE IF EXISTS workflow_executions CASCADE;
DROP TABLE IF EXISTS workflow_definitions CASCADE;
DROP TABLE IF EXISTS organizations CASCADE;
DROP TABLE IF EXISTS users CASCADE;

-- Metadata table
DROP TABLE IF EXISTS schema_migrations CASCADE;

-- ========================================================================
-- Drop all functions and triggers
-- ========================================================================

DROP TRIGGER IF EXISTS users_update_timestamp ON users;
DROP TRIGGER IF EXISTS organizations_update_timestamp ON organizations;
DROP TRIGGER IF EXISTS workflow_definitions_update_timestamp ON workflow_definitions;
DROP TRIGGER IF EXISTS workflow_executions_update_timestamp ON workflow_executions;
DROP TRIGGER IF EXISTS business_processes_update_timestamp ON business_processes;
DROP TRIGGER IF EXISTS process_instances_update_timestamp ON process_instances;
DROP TRIGGER IF EXISTS automation_tasks_update_timestamp ON automation_tasks;

DROP FUNCTION IF EXISTS update_timestamp();

-- ========================================================================
-- Confirmation
-- ========================================================================

COMMIT TRANSACTION;

DO $$
BEGIN
  RAISE NOTICE '✅ Rollback of migration 001-core-schema.sql completed';
  RAISE NOTICE '   ⚠️  WARNING: All data has been deleted!';
  RAISE NOTICE '   All tables, indexes, and functions removed';
END $$;

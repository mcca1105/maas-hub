# Phase 3 — MCP Configuration Task for @oalanicolas

**Status:** 🔴 DELEGATED (awaiting agent execution)
**Priority:** High
**Time estimate:** 20 minutes
**Delegated to:** @oalanicolas (Mind Architect) or @devops (Gage)

---

## Objective

Enable 3 critical MCPs for Mariana:
1. **Gmail MCP** — Read/send emails automatically
2. **Google Calendar MCP** — Check deadlines & schedule automatically
3. **Notion MCP** — Access personal Notion database automatically

## Current Status

All 3 MCPs currently show ⚠️ error in Claude Code. Impact: Mariana must manually copy/paste data instead of Claude accessing it directly.

## MCPs to Configure

### 1. Gmail MCP

**Purpose:** Mariana says "responda meus últimos emails" → Claude reads Gmail and responds

**Configuration steps:**
```bash
# 1. Create/update MCP server config
docker mcp server add gmail \
  --image gmail-mcp:latest \
  --env GMAIL_API_KEY="{user-gmail-credentials}" \
  --env GMAIL_API_SECRET="{from-google-oauth}"

# 2. Test connection
docker mcp tools ls | grep gmail

# 3. Update ~/.claude/settings.json to include gmail MCP
# Then verify in Claude Code settings UI
```

**Required:** Google OAuth credentials (Mariana's Google account)

### 2. Google Calendar MCP

**Purpose:** Mariana says "qual é meu próximo compromisso?" → Claude checks Calendar automatically

**Configuration steps:**
```bash
docker mcp server add google-calendar \
  --image google-calendar-mcp:latest \
  --env CALENDAR_API_KEY="{from-google-oauth}" \
  --env CALENDAR_API_SECRET="{from-google-oauth}"
```

**Required:** Same OAuth as Gmail (they're linked)

### 3. Notion MCP

**Purpose:** Mariana says "adicione um item ao meu Notion" → Claude updates Notion automatically

**Configuration steps:**
```bash
docker mcp server add notion \
  --image notion-mcp:latest \
  --env NOTION_API_TOKEN="{notion-integration-token}" \
  --env NOTION_DATABASE_IDS="{mariana-database-ids}"
```

**Required:**
- Notion API integration token (create at notion.com/my-integrations)
- Database IDs where Claude should have access

## Verification Checklist

- [ ] Gmail MCP appears in Claude Code settings without ⚠️
- [ ] Google Calendar MCP appears in Claude Code settings without ⚠️
- [ ] Notion MCP appears in Claude Code settings without ⚠️
- [ ] Test Gmail: `*test-mcp gmail` → reads Mariana's last 5 emails
- [ ] Test Calendar: `*test-mcp calendar` → shows next 3 events
- [ ] Test Notion: `*test-mcp notion` → lists Mariana's databases

## Credentials Needed from Mariana

**Before starting, request:**

1. **Google OAuth:**
   - Google Account email
   - Permission to create OAuth credentials (https://console.cloud.google.com)
   - Gmail & Calendar scopes enabled

2. **Notion API Token:**
   - Create at: https://www.notion.com/my-integrations
   - Copy integration token
   - Share relevant databases with integration

## Timeline

- **Step 1:** Request credentials from Mariana (2 min)
- **Step 2:** Configure Gmail (5 min)
- **Step 3:** Configure Google Calendar (3 min)
- **Step 4:** Configure Notion (7 min)
- **Step 5:** Test all 3 MCPs (3 min)
- **Total:** ~20 minutes

## Success Criteria

✅ All 3 MCPs operational without errors
✅ Claude can read Mariana's emails (Gmail test)
✅ Claude can check Mariana's calendar (Calendar test)
✅ Claude can access Mariana's Notion databases (Notion test)
✅ Mariana's token usage reduced due to less manual copy/paste

## Post-Configuration

After MCPs are live:
- Update `MEMORY.md`: "MCPs configured: Gmail, Google Calendar, Notion"
- Test with Mariana: "Ask Claude to check your emails and calendar"
- Document any issues in `.claude/projects/C--Users-User/memory/mcp-status.md`

---

**Ready for @oalanicolas to execute when approved.**

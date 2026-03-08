# Story 1: Dashboard Central - MVP

**Epic:** Infrastructure & Monitoring
**Story ID:** 1.0
**Assigned To:** @dev (start) → @qa (review)
**Status:** Draft
**Points:** 13
**Priority:** High
**Created:** 2026-03-07

---

## 📋 Description

Create a centralized dashboard that orchestrates and monitors all AIOX squads/projects in a single web interface. The dashboard will display real-time health status, agent activity, logs, and allow dispatching of workflows.

### Problem Statement
Currently, multiple projects/squads run independently:
- squad-vendas (landing page)
- prospect-hunter (full-stack app)
- zona-genialidade (assessment tool)
- automacao-profissional (backend)

Each has its own `dev` script. This creates fragmentation, making it hard to:
- Monitor all projects simultaneously
- See cross-squad logs
- Dispatch workflows from a central point
- Understand system health at a glance

### Solution
Build a **Dashboard Central** that:
- Aggregates status of all squads
- Provides unified log viewer
- Monitors agent activity
- Integrates with AIOX for workflow orchestration
- Respects AIOX boundaries (L1-L4 framework protection)

---

## ✅ Acceptance Criteria

### Must Have (Core MVP)
- [ ] Dashboard server running on port 3000
- [ ] React frontend displays all squads as cards
- [ ] Real-time health checks for each squad
- [ ] WebSocket connection for logs streaming
- [ ] Display active agents per squad
- [ ] Integration with AIOX Agent Invoker
- [ ] Basic styling (dark mode cibernético)
- [ ] Mobile responsive layout
- [ ] All tests passing
- [ ] Documentation complete

### Should Have (Secondary)
- [ ] Workflow dispatcher UI
- [ ] Log filtering (squad, agent, level, text search)
- [ ] Download logs as CSV/JSON
- [ ] Git branch display per squad
- [ ] Performance metrics display

### Nice to Have (Stretch Goals)
- [ ] Docker containerization
- [ ] Kubernetes manifests
- [ ] CI/CD integration display
- [ ] Database connection pooling
- [ ] Authentication/Authorization

---

## 🎯 Scope

### IN (Included)
- Backend: Express.js server with health checks
- Frontend: React dashboard with WebSocket
- AIOX integration via Agent Invoker
- Real-time log aggregation from `.aiox/logs/`
- Squad configuration via YAML
- API: `/api/health`, `/api/squads`, `/api/logs`
- WebSocket: `ws://localhost:3000/ws/logs`

### OUT (Not Included)
- Database persistence (logs are real-time only)
- User authentication (local development only)
- Email notifications
- Slack integration
- Mobile app
- Load balancing

---

## 🔗 Dependencies

### Framework & System
- AIOX framework >= 4.31.1
- Node.js 18+
- npm or yarn
- Bash shell (for scripts)

### Prerequisite Stories
- None (greenfield)

### External Services
- All squads must have health check endpoints
- All squads must log to `.aiox/logs/`

### Resources Needed
- Port 3000 (Dashboard)
- Disk space: ~500 MB for dependencies

---

## 📊 Definition of Done

- [x] All acceptance criteria met
- [ ] Code passes linting: `npm run lint`
- [ ] Type checking passes: `npm run typecheck`
- [ ] Unit tests pass: `npm run test`
- [ ] Integration tests pass
- [ ] No console errors/warnings
- [ ] Documentation complete (INTEGRATION-GUIDE, USAGE)
- [ ] README.md written
- [ ] squad.yaml configured
- [ ] Git commit with story ID reference
- [ ] Story moved to "Done" status
- [ ] Artifacts listed in File List section

---

## 🔄 Implementation Tasks

### Phase 1: Backend Setup (4 pts)

- [ ] Task: Create Express.js server structure
  - Create `backend/src/index.ts`
  - Setup middleware (CORS, JSON, error handling)
  - Create `.env.example` with PORT, LOG_DIR
  - Start server on `npm run dev`

- [ ] Task: Implement Health Check Engine
  - Create `backend/src/health-check.ts`
  - Check squad port availability
  - Verify AIOX framework status
  - Cache results (25s TTL)
  - Return aggregated health status

- [ ] Task: Create AIOX Integration Layer
  - Create `backend/src/aiox-integration.ts`
  - Load Agent Invoker from `.aiox-core/`
  - Wrapper methods: `loadAgent()`, `loadTask()`, `executeTask()`
  - Handle errors gracefully
  - Log to `.aiox/logs/`

### Phase 2: Frontend Setup (4 pts)

- [ ] Task: Create React App Structure
  - Setup React 18+ with TypeScript
  - Install Tailwind CSS
  - Create App.tsx with main layout
  - Setup Socket.io client for WebSocket
  - Create `src/styles/globals.css`

- [ ] Task: Build UI Components
  - ProjectCard.tsx: Display squad status
  - AgentStatus.tsx: List active agents
  - HealthIndicator.tsx: Status colors
  - LogViewer.tsx: Real-time log table
  - Dashboard.tsx: Main layout

- [ ] Task: Implement WebSocket Client
  - Connect to `ws://localhost:3000/ws/logs`
  - Handle connection/disconnect events
  - Parse log JSON events
  - Display in LogViewer in real-time
  - Handle reconnection logic

### Phase 3: Integration (3 pts)

- [ ] Task: Connect Backend & Frontend
  - Create API routes: `/api/health`, `/api/squads`
  - Create WebSocket route: `/ws/logs`
  - Test HTTP + WebSocket communication
  - Verify real-time updates

- [ ] Task: Configuration & Deployment
  - Create `config/projects.yaml` with squad definitions
  - Create startup script
  - Update main `package.json` with `dev:dashboard` script
  - Test full flow: start, health check, logs stream

- [ ] Task: Documentation & Testing
  - Write INTEGRATION-GUIDE.md
  - Write USAGE.md
  - Create unit tests for key functions
  - Run full test suite
  - Verify lint and typecheck

---

## 📁 File List

### Created Files
- [ ] `.squads/dashboard-central/squad.yaml`
- [ ] `.squads/dashboard-central/INTEGRATION-GUIDE.md`
- [ ] `.squads/dashboard-central/USAGE.md`
- [ ] `.squads/dashboard-central/README.md` (new)
- [ ] `.squads/dashboard-central/backend/package.json` (new)
- [ ] `.squads/dashboard-central/backend/src/index.ts` (new)
- [ ] `.squads/dashboard-central/backend/src/health-check.ts` (new)
- [ ] `.squads/dashboard-central/backend/src/aiox-integration.ts` (new)
- [ ] `.squads/dashboard-central/backend/src/routes/health.ts` (new)
- [ ] `.squads/dashboard-central/backend/src/routes/squads.ts` (new)
- [ ] `.squads/dashboard-central/backend/src/routes/logs.ts` (new)
- [ ] `.squads/dashboard-central/frontend/package.json` (new)
- [ ] `.squads/dashboard-central/frontend/src/App.tsx` (new)
- [ ] `.squads/dashboard-central/frontend/src/components/Dashboard.tsx` (new)
- [ ] `.squads/dashboard-central/frontend/src/components/ProjectCard.tsx` (new)
- [ ] `.squads/dashboard-central/frontend/src/components/AgentStatus.tsx` (new)
- [ ] `.squads/dashboard-central/frontend/src/components/LogViewer.tsx` (new)
- [ ] `.squads/dashboard-central/frontend/src/services/api.ts` (new)
- [ ] `.squads/dashboard-central/frontend/src/services/websocket.ts` (new)
- [ ] `.squads/dashboard-central/frontend/src/styles/globals.css` (new)
- [ ] `.squads/dashboard-central/config/projects.yaml` (new)
- [ ] `docs/DASHBOARD-ARCHITECTURE.md` (new)
- [ ] `docs/stories/DASHBOARD-CENTRAL.story.md` (new)
- [ ] `package.json` (updated with dev:dashboard script)
- [ ] `.squads/INDEX.md` (updated with dashboard-central entry)

### Modified Files
- [ ] `package.json`: Add `dev:dashboard` script
- [ ] `.squads/INDEX.md`: Add dashboard-central to squad list

---

## 🏗️ Technical Decisions

### Backend Framework
**Decision:** Express.js
**Rationale:**
- Lightweight and flexible
- Perfect for orchestration/monitoring
- Good WebSocket support via Socket.io
- Easy to integrate with AIOX

### Frontend Framework
**Decision:** React 18 + TypeScript + Tailwind
**Rationale:**
- React ecosystem maturity
- TypeScript for type safety
- Tailwind for rapid styling
- Socket.io React hooks available

### Real-time Communication
**Decision:** WebSocket via Socket.io
**Rationale:**
- Native for real-time log streaming
- Built-in reconnection logic
- Lower latency than polling
- Fire-and-forget log events

### Logging Strategy
**Decision:** Read from `.aiox/logs/`, stream to frontend
**Rationale:**
- No database needed (simpler)
- Respects AIOX framework
- Real-time without persistence
- Easy to tail files on Unix

---

## ⚠️ Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|-----------|
| Port 3000 already in use | Can't start | Check before start, allow PORT env var |
| Squads not running | Health check fails | Add offline detection, retry logic |
| WebSocket connection drops | Lost logs | Implement reconnection with buffer |
| AIOX Agent Invoker errors | Workflow fails | Wrap in try-catch, log errors, notify UI |
| Performance with many logs | UI lag | Implement pagination, chunk streaming |

---

## 🧪 Testing Strategy

### Unit Tests
- Health check logic
- Log parsing
- Configuration loading
- Error handling

### Integration Tests
- Backend ↔ Frontend communication
- WebSocket streaming
- AIOX integration
- Squad detection

### Manual Testing
- Start all squads
- Open dashboard
- Verify health checks
- Stream logs in real-time
- Dispatch workflow
- Test on mobile

---

## 📝 Notes

### Architecture
The dashboard respects AIOX L1-L4 boundaries:
- Uses Agent Invoker as black-box (don't modify)
- Reads state files (don't modify)
- Extends via `.squads/dashboard-central/` (fully mutable)
- Follows squad manifest pattern

### Why Not Modify AIOX?
- L1/L2 are protected by deny rules
- Framework updates would break changes
- Dashboard is use-case specific (not framework core)
- Squad model is designed for this extensibility

### Future Enhancements
- Add persistent database for historical data
- Implement user authentication
- Add alerting (Slack, email)
- Build mobile app
- Deploy to Vercel/Heroku
- Add metrics/monitoring (Prometheus)

---

## 🔄 Change Log

| Date | Status | Author | Change |
|------|--------|--------|--------|
| 2026-03-07 | Draft | Mariana | Story created with full scope |

---

## 👥 Team

- **Product Owner:** @po (Pax)
- **Scrum Master:** @sm (River)
- **Dev Lead:** @dev (Dex)
- **QA Lead:** @qa (Quinn)
- **Architect:** @architect (Aria)

---

## 🎬 How to Start

### Next Immediate Actions

1. **Validate Story** (`@po`)
   ```
   @po *validate-story-draft DASHBOARD-CENTRAL
   ```

2. **Move to Ready** (if ≥7/10)
   ```
   Update status: Draft → Ready
   ```

3. **Start Implementation** (`@dev`)
   ```
   @dev *develop DASHBOARD-CENTRAL
   ```

### Development Setup

```bash
# Install dependencies
cd /c/Users/User/code3/.squads/dashboard-central
cd backend && npm install
cd ../frontend && npm install

# Run dev server
cd /c/Users/User/code3
npm run dev:dashboard

# Run tests
npm test

# Check lint & typecheck
npm run lint
npm run typecheck
```

---

**Story Status:** Draft → (Ready after validation) → InProgress → InReview → Done
**Target Completion:** 1-2 weeks (13 points)
**Last Updated:** 2026-03-07

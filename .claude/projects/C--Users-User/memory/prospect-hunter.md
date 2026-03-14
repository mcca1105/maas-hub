# Prospect Hunter - Project Memory

## Project Info
- **Path**: C:\Users\User\prospect-hunter
- **Tech Stack**: Next.js 14, TypeScript, SQLite, NextAuth.js, Apify, Gemini
- **Status**: Early stage (29.8% complete - 34/114 pts)
- **Last Session**: 2026-03-07

## Session 2026-03-07 Results
- **Stories Completed**: 5 (2.4, 3.1, 3.2, 3.3, 3.4)
- **Points Earned**: +14 pts (20 → 34)
- **Epic 3 Status**: COMPLETE (17/17 pts)
- **Commits**: 11 new

## Key Architecture Decisions
1. **Database**: SQLite (better-sqlite3) with 8 tables
2. **Auth**: NextAuth.js with email/password
3. **Search**: Apify API (Instagram + LinkedIn)
4. **Messages**: Gemini API (not started yet)
5. **Frontend**: Next.js App Router with TailwindCSS

## Critical Files
- `db/schema.sql` — All table definitions
- `src/lib/db-helpers.ts` — 30+ CRUD functions
- `src/lib/apify.ts` — Apify integration client
- `src/lib/auth-middleware.ts` — Auth helpers
- `src/lib/validators.ts` — Zod schemas

## What's Done (Epic 3)
- ✅ User Plans table (2 pts)
- ✅ 5 API endpoints for prospects (3 pts)
- ✅ Apify search triggers (Instagram + LinkedIn) (4 pts)
- ✅ Status polling endpoint (3 pts)
- ✅ Results import/parsing (2 pts)

## What's Next (80 pts remaining)
1. **Window 1**: Messaging (11 pts) — Stories 4.1-4.4
2. **Window 2**: Frontend (18 pts) — Stories 5.1-5.6
3. **Window 3**: QA & Launch (25 pts) — Stories 6.1-9.2
4. **Polish**: Extra stories (26 pts) — If time permits

## Parallel Execution Plan
- Run 3-4 windows simultaneously
- Each window ~100-150 mins
- Total: 3 sessions to complete
- Estimated tokens: ~295K (need 4 janelas, not 3)

## Environment Setup Needed
```
.env file (from .env.example):
- APIFY_API_TOKEN (required for search)
- GEMINI_API_KEY (required for messaging)
- NEXTAUTH_SECRET
- DATABASE_PATH
```

## No Blockers
- All backend APIs working
- Database schema complete
- Can start frontend immediately
- All tests passing

## Token Budget
- Session used: ~165K / 200K (82.5%)
- Remaining: ~35K
- **Need**: New janela for Window 3

## Commands
```bash
cd /c/Users/User/prospect-hunter
npm run dev           # Start dev
npm run lint          # Check code
npm run build         # Build
git log --oneline    # See commits
```

## Session Metrics
- Avg: 2.8 pts/hour
- Code: ~900 new lines
- Quality: 0 errors, 4 warnings pre-existing
- Efficiency: High

## For Next Session
1. Pull latest: `git pull origin master`
2. Setup .env with Apify + Gemini keys
3. Open 3 parallel windows
4. Follow story docs in `/docs/STORY-*.md`
5. No dependencies between windows

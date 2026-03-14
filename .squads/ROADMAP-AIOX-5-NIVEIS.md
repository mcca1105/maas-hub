# 🤖 ROADMAP TÉCNICO AIOX — 5 Níveis de Receita

**Orquestração de IA para Automação Multi-Nível**
**Data:** 8 de março de 2026
**Status:** BLUEPRINT PARA IMPLEMENTAÇÃO
**Arquitetura:** Story-Driven + Agent Orchestration + Workflow Automation

---

## I. VISÃO GERAL AIOX

### Estrutura de Agentes

```yaml
Agent Roles (Agent Authority Matrix):
  └─ Core Operations:
     ├─ @pm (Morgan)           → Epic orchestration (5 níveis)
     ├─ @sm (River)            → Story creation (por nível)
     ├─ @dev (Dex)             → Automation code (APIs, bots)
     ├─ @architect (Aria)      → System design (fluxos integrados)
     └─ @analyst (Alex)        → Research (INPI, mercado, prospects)

  └─ Domain-Specific:
     ├─ @data-engineer (Dara)  → Data layer (CRM, leads, docs)
     ├─ @thiago-finch          → Business decisions (Nível X?)
     └─ @pedro-valerio         → Process optimization (funnels)

  └─ Pro Pack (Squad Creator):
     ├─ @oalanicolas           → Mind cloning (expert extraction)
     └─ (others for later)
```

### Workflow Tipos

```yaml
4 Primary Workflows:
  ├─ Story Development Cycle (SDC)
  │  └─ Create → Validate → Implement → QA Gate
  │
  ├─ QA Loop (iterativo)
  │  └─ Review → Fix → Approve
  │
  ├─ Spec Pipeline (pre-implementation)
  │  └─ Gather → Assess → Research → Write → Critique → Plan
  │
  └─ Brownfield Discovery (legacy assessment)
     └─ 10-phase technical debt assessment
```

---

## II. ROADMAP POR NÍVEL

### NÍVEL 1: Protection Academy (Isca)

#### Objetivos AIOX
```
Automação: 95%
├─ Landing page geração automática
├─ Email sequence (sequência de vendas)
├─ Lead scoring + qualification
├─ CRM ingestion
└─ Upsell trigger (Nível 2)

Humano: 5%
└─ Copywriting base (1h/semana suporte)
```

#### Stories a Criar

```yaml
Epic-1: Protection Academy Foundation
├─ Story 1.1: Landing page gerador
│  └─ Agent: @dev (Dex)
│  └─ Acceptance Criteria:
│     ├─ [x] React component com Tailwind
│     ├─ [x] SEO meta tags
│     ├─ [x] Form com Zod validation
│     ├─ [x] Email capture → CRM webhook
│     └─ [x] Mobile responsive
│  └─ File List: src/app/academy/page.tsx, etc.
│
├─ Story 1.2: Email sequence automation
│  └─ Agent: @dev (Dex) + @analyst (Alex)
│  └─ Acceptance Criteria:
│     ├─ [x] Resend.io integration (email service)
│     ├─ [x] 7-email sequence template
│     ├─ [x] Variable personalization ({{name}}, {{interests}})
│     ├─ [x] Delivery scheduling
│     └─ [x] Open rate tracking
│  └─ File List: lib/email/sequences.ts, api/emails/send.ts
│
├─ Story 1.3: Lead scoring engine
│  └─ Agent: @dev (Dex) + @analyst (Alex)
│  └─ Acceptance Criteria:
│     ├─ [x] Lead source tracking
│     ├─ [x] Engagement scoring (email opens, clicks)
│     ├─ [x] Behavioral triggers (ready to upsell?)
│     ├─ [x] CRM sync (update lead status)
│     └─ [x] API endpoint: GET /api/leads/score
│  └─ File List: lib/leads/scoring.ts, api/leads/score.ts
│
└─ Story 1.4: CRM integration (webhook)
   └─ Agent: @data-engineer (Dara)
   └─ Acceptance Criteria:
      ├─ [x] SQLite tables: leads, email_logs, conversions
      ├─ [x] POST /api/webhooks/lead-acquired
      ├─ [x] Email sequence trigger on lead insert
      ├─ [x] Conversion tracking
      └─ [x] Reports: leads/week, conversion rate, LTV
   └─ File List: db/migrations/004-academy.sql, api/webhooks/leads.ts
```

#### Processo AIOX de Execução

```
Phase 1: Create (Agent: @sm)
├─ Pre-fill: Epic context
├─ Elicit: Copy angle, target audience
└─ Output: 4 stories com ACs claras

Phase 2: Validate (Agent: @po)
├─ Checklist: 10-point validation
└─ Decision: GO or REWORK

Phase 3: Implement (Agent: @dev)
├─ Mode: Interactive + CodeRabbit reviews
└─ Output: Code + tests + lint clean

Phase 4: QA Gate (Agent: @qa)
├─ Tests: Unit + integration + e2e
└─ Decision: APPROVE or CONCERNS
```

#### Métricas AIOX de Sucesso

```
KPIs:
├─ Landing page CTR: >5% (baseline)
├─ Email open rate: >25%
├─ Conversion to Academy: 15-20%
├─ Lead cost: <R$ 50 (paid ads) ou R$ 0 (organic)
└─ Cycle time: Stories 1-4 em 2-3 semanas
```

---

### NÍVEL 2: Serviço de Marca (Revenue Driver)

#### Objetivos AIOX

```
Automação: 70%
├─ Lead qualification (é cliente marca?)
├─ INPI research (pesquisa automática)
├─ Proposta geração
├─ Documentação
├─ Notificações + tracking

Humano: 30%
├─ Especialista INPI (depósito, validação)
├─ Comunicação cliente
└─ Caso complexo (risco de rejeição)
```

#### Stories a Criar

```yaml
Epic-2: Serviço de Marca Integrado
├─ Story 2.1: Lead qualification form
│  └─ Agent: @dev (Dex)
│  └─ Scope: Detecta se lead = candidato marca
│     ├─ Questões: Já tem marca? Tipo? Segmento?
│     ├─ Scoring: Score >70 = manda pro Nível 2
│     └─ CRM tag: "marca-candidate"
│
├─ Story 2.2: INPI research automation
│  └─ Agent: @analyst (Alex) + @dev (Dex)
│  └─ Scope: Busca automática no INPI
│     ├─ API: INPI integration (se existir) ou web scraping Apify
│     ├─ Output: JSON com resultados (conflitos, disponibilidade)
│     └─ Cache: 30 dias (INPI é lento, não precisa refresh)
│
├─ Story 2.3: Proposta generator
│  └─ Agent: @dev (Dex)
│  └─ Scope: PDF proposta automática
│     ├─ Template: Marca X → INPI research → timeline → preço
│     ├─ Variable: {{client_name}}, {{mark_name}}, {{nclass}}
│     └─ Output: PDF download + email
│
├─ Story 2.4: Especialista INPI integration
│  └─ Agent: @data-engineer (Dara)
│  └─ Scope: Workflow com especialista
│     ├─ Notificação: "Novo deal marca: R$ 2.5K"
│     ├─ Atribuição: Especialista recebe task
│     ├─ Checklist: Depósito INPI → acompanhamento → resultado
│     └─ Status: pending → processing → filed → registered
│
└─ Story 2.5: Tracking + reporting
   └─ Agent: @analyst (Alex)
   └─ Scope: Dashboard de deals
      ├─ Leads que qualificaram
      ├─ Propostas enviadas (quando converteu?)
      ├─ Marcas registradas (pipeline)
      └─ Revenue: R$ X por marca
```

#### Diagrama Fluxo

```
Lead (Nível 1)
  ↓
[Qualification Form] → "Você quer registrar marca?"
  ↓ (SIM)
[INPI Research] → Automático (Apify ou API)
  ↓
[Score Risk] → Alto risco de conflito? → Avisa especialista
  ↓
[Proposta Generator] → PDF automático
  ↓
[Email Envio] → "Aqui está sua proposta"
  ↓
[Status Tracking] → Cliente visualiza em dashboard
  ↓ (Cliente aceita)
[Especialista Assigned] → "Novo deal: depositar marca X"
  ↓
[INPI Filing] → Especialista faz depósito
  ↓
[Acompanhamento] → Email updates automáticas
  ↓ (INPI approve/reject)
[Final Status] → "Marca registrada!" ✅
  ↓
[CRM Close] → Revenue: R$ 2.5K + lead history
```

#### Métricas AIOX

```
KPIs:
├─ Lead-to-lead qualification: 30-40% (quantos da 1 viram candidatos 2?)
├─ Propostas enviadas: 20-30/mês (escala AIOX)
├─ Conversion rate: 50-70% (propostas → fechado)
├─ Marca filing rate: 100% (automático)
├─ Timeline média: 6-8 semanas (INPI)
└─ Revenue/mês: R$ 50-100K (20-40 deals)
```

---

### NÍVEL 3: Holding Tributária (High Ticket)

#### Objetivos AIOX

```
Automação: 30%
├─ Análise de regime atual (IR, contribuições)
├─ Simulação fiscal (econômico)
├─ Documentação base
└─ Propostas parametrizadas

Humano: 70%
├─ Contador (aprovação estrutura)
├─ Advogado (revisão legal)
├─ Comunicação complexa
└─ Estruturação executiva
```

#### Stories a Criar

```yaml
Epic-3: Holding Tributária Enterprise
├─ Story 3.1: Regime analysis tool
│  └─ Agent: @dev (Dex) + @analyst (Alex)
│  └─ Scope: Analisador de regime tributário
│     ├─ Input: Faturamento, segmento, estrutura atual
│     ├─ Output: Simulação (IR, ICMS, PIS, COFINS)
│     ├─ Recommendation: "Seu regime ideal é X"
│     └─ KPI: Economia potencial
│
├─ Story 3.2: Fiscal simulation engine
│  └─ Agent: @data-engineer (Dara)
│  └─ Scope: Engine de cálculos fiscais
│     ├─ Modelos: Simples, Lucro Real, Lucro Presumido, Holding
│     ├─ Database: Alíquotas atualizadas (SEFAZ, IRPJ, etc)
│     └─ Output: JSON com simulação 12-meses
│
├─ Story 3.3: Proposta gerador (Holding)
│  └─ Agent: @dev (Dex)
│  └─ Scope: PDF proposta automática
│     ├─ Template: Análise atual → recomendação → economia → timeline
│     ├─ Variables: {{company}}, {{revenue}}, {{eco_estimate}}
│     └─ Output: PDF + email
│
├─ Story 3.4: Contador + advogado workflow
│  └─ Agent: @pm (Morgan)
│  └─ Scope: Epic para estruturação
│     ├─ Task 1: Contador aprovação (checklist)
│     ├─ Task 2: Advogado revisão legal (checklist)
│     ├─ Task 3: Cliente assinatura (contrato)
│     └─ Task 4: Implementação (PGFN, cartório, CVM se aplicável)
│
└─ Story 3.5: Compliance tracker
   └─ Agent: @data-engineer (Dara)
   └─ Scope: Dashboard de conformidade
      ├─ Clientes estruturados
      ├─ Status (análise → proposta → implementação)
      ├─ Documentação armazenada (audit trail)
      └─ Alertas de risco (Receita Federal investiga?)
```

#### Métricas AIOX

```
KPIs:
├─ Lead-to-holding candidate: 5-10% (é empreendedor com economia potencial?)
├─ Propostas enviadas: 5-10/mês
├─ Conversion rate: 40-60% (propostas → fechado)
├─ Economia média/cliente: R$ 100K-500K/ano
├─ Ticket/cliente: R$ 15K-30K (estruturação)
├─ Compliance: 100% documentado
└─ Revenue/mês: R$ 30-100K (2-5 deals)
```

---

### NÍVEL 4: Advisory / Gestão Ativos (Exponencial)

#### Objetivos AIOX

```
Automação: 50%
├─ Pesquisa ativos (renda fixa, ações, cripto)
├─ Análise de carteira
├─ Recomendações parametrizadas
├─ Acompanhamento automático
└─ Alertas de mercado

Humano: 50%
├─ Consultor senior (decisão final)
├─ Comunicação executiva
├─ Auditoria anual
└─ Ajustes estratégicos
```

#### Stories a Criar

```yaml
Epic-4: Advisory Patrimonial Escalado
├─ Story 4.1: Asset research engine
│  └─ Agent: @analyst (Alex)
│  └─ Scope: Pesquisa automática de ativos
│     ├─ Fontes: Renda fixa (tesouro, LCI), ações, ETFs, cripto
│     ├─ Data: Integração com APIs (B3, Tesouro Nacional, CoinGecko)
│     └─ Output: JSON com opções recomendadas
│
├─ Story 4.2: Portfolio analysis tool
│  └─ Agent: @dev (Dex) + @data-engineer (Dara)
│  └─ Scope: Análise de carteira
│     ├─ Input: Ativos do cliente (histórico)
│     ├─ Analysis: Risco, rentabilidade, diversificação
│     └─ Output: Rebalancing recommendation
│
├─ Story 4.3: Recommendation engine
│  └─ Agent: @dev (Dex)
│  └─ Scope: Engine de recomendações (AI)
│     ├─ Perfil: Risco, horizonte, objetivos (entrevista)
│     ├─ Algorithm: Parametrizado (não ML complex)
│     └─ Output: "Recomendamos 40% renda fixa, 30% ações, 30% cripto"
│
├─ Story 4.4: Client portal
│  └─ Agent: @dev (Dex)
│  └─ Scope: Dashboard cliente (próximo → Story 5.2)
│     ├─ Views: Carteira, performance, recomendações, alertas
│     ├─ Updates: Real-time (preços de fechamento)
│     └─ Notificações: "Ação caiu 10%, rebalancing recomendado"
│
└─ Story 4.5: Compliance + reporting
   └─ Agent: @data-engineer (Dara)
   └─ Scope: Audit trail + relatórios
      ├─ Documentação: Cada recomendação registrada
      ├─ Relatórios: Trimestral, anual (enviado cliente)
      └─ Compliance: 100% rastreável
```

#### Métricas AIOX

```
KPIs:
├─ Lead-to-advisory candidate: 10-15% (tem poupança/patrimônio?)
├─ Ticket médio: R$ 5-15K/mês (gestão contínua)
├─ Clientes alvo: 20-60 em 12 meses
├─ Fee: 0.5-1.5% a.a. de AUM (exemplo: R$ 1M = R$ 5-15K/mês)
├─ Automação: 60-70% (pesquisa, análise, alertas)
└─ Revenue/mês: R$ 100-300K (escalável)
```

---

### NÍVEL 5: Operações Imobiliárias (Cash Flow)

#### Objetivos AIOX

```
Automação: 20%
├─ Análise de leilão (viabilidade)
├─ Análise de custo reforma
├─ Precificação automática
├─ Documentação SPE
└─ Acompanhamento projeto

Humano: 80%
├─ Arrematação (negociação)
├─ Reforma (project management)
├─ Venda/aluguel (comercial)
└─ Resolução de problemas
```

#### Stories a Criar

```yaml
Epic-5: Operações Imobiliárias Integradas
├─ Story 5.1: Leilão analyzer
│  └─ Agent: @analyst (Alex)
│  └─ Scope: Análise automática de leilões
│     ├─ Input: URL leilão (BACENJUD/SAERJEC/cartório)
│     ├─ Scraping: Apify robot (valor, localização, documentação)
│     ├─ Analysis: Mercado local, tendências
│     └─ Output: "Viabilidade: 70% (bom deal)"
│
├─ Story 5.2: Reforma cost estimator
│  └─ Agent: @dev (Dex) + @analyst (Alex)
│  └─ Scope: Estimador de custo reforma
│     ├─ Input: Fotos, metragem, tipo reforma
│     ├─ ML?: Tabela de custos (pintura, alvenaria, elétrica)
│     └─ Output: "Reforma estimada: R$ 100-150K (80% confidence)"
│
├─ Story 5.3: Property valuation
│  └─ Agent: @analyst (Alex)
│  └─ Scope: Valuation automático (revenda/aluguel)
│     ├─ Comparables: Integração com Zap Imóveis, Vivareal
│     ├─ Market: Análise de bairro, demanda
│     └─ Output: "Estimativa de revenda: R$ 500K (após reforma)"
│
├─ Story 5.4: SPE manager
│  └─ Agent: @data-engineer (Dara)
│  └─ Scope: Gestão de SPE (Sociedade de Propósito Específico)
│     ├─ Documentation: Contrato sociedade, termo de parceria
│     ├─ Parcerias: Sócios (cotas), split de receita
│     └─ Output: SPE pronto pra operação
│
└─ Story 5.5: Project tracker
   └─ Agent: @pm (Morgan)
   └─ Scope: Acompanhamento de operação
      ├─ Phases: Leilão → Arrematação → Reforma → Venda
      ├─ Status: Em tempo real (fotos, invoices)
      └─ Dashboard: Cliente visualiza progresso
```

#### Métricas AIOX

```
KPIs:
├─ Leilões analisados: 10-20/mês (prospection)
├─ Operações executadas: 2-4/ano
├─ Ticket/operação: R$ 500K-5M
├─ Retorno/operação: 15-25% (em 6-12 meses)
├─ Revenue: R$ 75K-1M+ por operação
└─ Total/ano: R$ 300K-5M (se 1-3 ops/ano)
```

---

## III. INFRAESTRUTURA AIOX

### Data Layer (Agent: @data-engineer)

```yaml
Database Schema:
  Tables:
    ├─ leads (origin, channel, qualification_score)
    ├─ prospects (potential customers, nível_alvo)
    ├─ messages (DM, email, SMS history)
    ├─ proposals (proposta enviada, status)
    ├─ contracts (contrato assinado, timestamps)
    ├─ transactions (pagamento, receita)
    ├─ compliance (audit trail, documentação)
    └─ analytics (KPIs, funnels, conversão)

  APIs:
    ├─ /api/leads/qualify (qual nível?)
    ├─ /api/proposals/generate (PDF automático)
    ├─ /api/contracts/sign (e-signature)
    ├─ /api/analytics/kpis (dashboard)
    └─ /api/webhooks/* (external integrations)
```

### Integration Layer

```yaml
External Services:
  ├─ Email: Resend.io (campaigns, transactional)
  ├─ CRM: SQLite local (ou Supabase if scale)
  ├─ Web scraping: Apify (INPI, leilões, properties)
  ├─ Legal docs: DocuSign (e-signature)
  ├─ Payment: Stripe (recebimento)
  ├─ Market data: APIs (Tesouro Nacional, B3, Zap Imóveis)
  └─ Notifications: Telegram, WhatsApp (cliente updates)
```

### Agent Workflows

```yaml
Workflow Automation:
  ├─ Nível 1: Lead → Score → Email sequence → Track
  ├─ Nível 2: Lead → Qualify → INPI research → Proposta → Track
  ├─ Nível 3: Lead → Regime analysis → Proposta → Contador → Advogado → Implement
  ├─ Nível 4: Lead → Research → Portfolio analysis → Recommendation → Track
  └─ Nível 5: Leilão → Analysis → SPE → Operação → Venda
```

---

## IV. TIMELINE DE IMPLEMENTAÇÃO

```
FASE 1: Foundation (Semanas 1-2)
├─ Epic-1 stories (Nível 1)
├─ Database schema
├─ API foundation
└─ @dev + @data-engineer

FASE 2: Revenue Driver (Semanas 3-6)
├─ Epic-2 stories (Nível 2)
├─ INPI integration
├─ Especialista workflow
└─ @analyst + @dev

FASE 3: Enterprise (Semanas 7-12)
├─ Epic-3 stories (Nível 3)
├─ Contador + advogado workflow
├─ Compliance tracking
└─ @pm + @data-engineer

FASE 4: Exponential (Semanas 13-16)
├─ Epic-4 stories (Nível 4)
├─ Portal client
├─ Asset research
└─ @analyst + @dev

FASE 5: Operations (Semanas 17+)
├─ Epic-5 stories (Nível 5)
├─ Leilão analyzer
├─ SPE manager
└─ @pm + @analyst
```

---

## V. COMANDOS AIOX PARA COMEÇAR

```bash
# Criar épica por nível
@pm *create-epic "Nível 1: Protection Academy"
@pm *create-epic "Nível 2: Serviço de Marca"
# ... etc

# Criar stories de desenvolvimento
@sm *create-story "1.1: Landing page gerador"
@sm *create-story "1.2: Email sequence automation"
# ... etc

# Validar stories
@po *validate-story-draft "docs/stories/1.1.md"

# Implementar código
@dev *develop-story "docs/stories/1.1.md"

# QA testing
@qa *qa-gate "docs/stories/1.1.md"

# Otimização de processos
@pedro-valerio *optimize-squad "5-niveis-receita"

# Business decisões
@thiago-finch *business-strategy "Decidir Euro Junior GO/NO-GO"
```

---

**Status:** BLUEPRINT PRONTO PARA IMPLEMENTAÇÃO
**Próximo:** Ativar @pm para criar primeiras épicas
**Duração estimada:** 4-6 meses (Fase 1-5)
**ROI esperado:** R$ 200K-2M+ (ano 1)

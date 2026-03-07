# Squad: Zona Genialidade — Guia de Instalação

**Status:** ✅ Instalado | **Data:** 2026-03-07 | **AIOX Conformidade:** 100%

## Visão Geral

Squad que **identifica sua zona de genialidade em 30 minutos** e recomenda qual squad criar/operar baseado no seu perfil comportamental único.

- **Processo:** Assessment (30min) → Analysis (automático) → Blueprint (entrega)
- **Agentes:** 7 especialistas de comportamento e monetização
- **Frameworks:** 7 (Zone of Genius, CliftonStrengths, Wealth Dynamics, etc)
- **Público:** Alunos do Cohort Fundamentals, empreendedores

## Como Usar

### 1. Ativar o Chief (Zona Genialidade Chief)
```bash
@zona-genialidade-chief
```

### 2. Ativar Pipeline Completo (Recomendado)
```bash
/ZonaGenialidade:tasks:start
```

O sistema vai:
1. Pedir ~43 perguntas
2. Processar com 7 analistas
3. Entregar Blueprint completo em ~20-30 minutos

### 3. Ativar Tarefas Específicas

```bash
@zona-genialidade-chief *assess              # Apenas assessment
@zona-genialidade-chief *blueprint           # Apenas blueprint final
@zona-genialidade-chief *recommend-squad     # Recomendação de squad
@zona-genialidade-chief *help                # Menu de ajuda
```

## 7 Especialistas

| Agente | Persona | Framework | Expertise |
|--------|---------|-----------|-----------|
| **zona-genialidade-chief** | Orquestra | — | Coordena fluxo |
| **gay-hendricks** | Tier 0 | Zone of Genius | Diagnostica zona |
| **don-clifton** | Tier 1 | CliftonStrengths 34 | Perfil de talentos |
| **dan-sullivan** | Tier 1 | Unique Ability | Habilidade única |
| **roger-hamilton** | Tier 1 | Wealth Dynamics | Perfil de riqueza |
| **alex-hormozi** | Tier 1 | Value Equation | Monetização |
| **kathy-kolbe** | Tier 2 | Kolbe Action Modes | Estilo de execução |
| **sally-hogshead** | Tier 2 | Fascination Advantage | Posicionamento |

## O que Você Vai Receber

### 📊 Perfil Comportamental Completo
```
✅ Zone of Genius (Gay Hendricks)
   └── Sua zona atual + caminho para genius zone

✅ CliftonStrengths 34
   └── Top 5 talentos + como aproveitar

✅ Unique Ability (Dan Sullivan)
   └── Sua habilidade única + diferencial no mercado

✅ Wealth Dynamics (Roger Hamilton)
   └── Profile de riqueza (8 tipos) + squad recomendado

✅ Value Equation (Alex Hormozi)
   └── Como monetizar sua zona

✅ Kolbe Action Modes
   └── Seu estilo de execução (conativo)

✅ Fascination Advantage
   └── Seu arquétipo + posicionamento pessoal
```

### 🎯 Squad Recomendado
Baseado no seu perfil, qual squad criar:
- **Content Distillery?** (se você gosta de produção)
- **Hormozi?** (se você quer vender mais)
- **Marketing ARM?** (se você quer gerar leads)
- **Automação Profissional?** (se você quer otimizar)
- **Outro?**

### 💰 Plano de Monetização
- Como transformar zona de genialidade em receita
- Modelo de negócio recomendado
- Primeiros passos concretos

## 4 Casos de Uso

| Caso | Fluxo |
|------|-------|
| **UC1: Diagnóstico** | Assessment → CliftonStrengths + Big Five |
| **UC2: Mapeamento** | Assessment → Zone + Wealth Dynamics |
| **UC3: Squad Match** | Assessment → Recomendação de squad ideal |
| **UC4: Monetização** | Assessment → Value Equation + plano concreto |

## Timeline

```
[Dia 1]
30 min  → Responder ~43 perguntas (assessment)
20 min  → 7 analistas processam dados (automático)
10 min  → Chief entrega Blueprint

[Total: ~60 minutos]
```

## Quality Gates

| Gate | Fase | Descrição |
|------|------|-----------|
| QG-001 | Input → Tier 0 | Intake validado |
| QG-002 | Assessment → Analysis | Assessment completo |
| QG-003 | Analysis → Matching | Perfil sintetizado |
| QG-004 | Output → Entrega | Blueprint revisado |

## Estrutura de Pastas

```
.squads/zona-genialidade/
├── squad.yaml              (AIOX manifest)
├── INSTALL.md              (este arquivo)
├── README.md               (overview)
├── agents/                 (7 agentes)
├── tasks/                  (workflows)
├── checklists/             (validações)
├── data/                   (assessment templates)
├── docs/                   (documentação)
└── outputs/                (blueprints gerados)
```

## Quick Start

```bash
# Opção 1: Pipeline completo (RECOMENDADO)
/ZonaGenialidade:tasks:start

# Opção 2: Via Chief
@zona-genialidade-chief *start-assessment

# Opção 3: Tasks individuais
@zona-genialidade-chief *run-assessment
@zona-genialidade-chief *analyze-genius-profile
@zona-genialidade-chief *recommend-squad
@zona-genialidade-chief *generate-blueprint
```

## O Que Levar

Tenha em mãos:
- Últimas 2-3 coisas que você fez e adorou ❤️
- Últimas 2-3 coisas que você fez e odiou 😤
- O que as pessoas mais pedem sua ajuda
- Quanto você quer ganhar no próximo ano
- Se tem time ou trabalha solo

## Próximas Ações

1. Comece: `/ZonaGenialidade:tasks:start`
2. Responda as ~43 perguntas
3. Espere processamento automático
4. Receba Blueprint com perfil + squad + plano
5. Implemente o plano!

---

**Instalado:** 2026-03-07 | **AIOX Conformance:** 100% ✅

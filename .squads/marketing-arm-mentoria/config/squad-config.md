# ⚙️ Configuração do Squad Marketing ARM

## Squad Manifest

```yaml
squad_id: marketing-arm-mentoria
name: Marketing ARM - Mentoria & Consultoria
version: 1.0.0
status: active
```

## Estrutura de Diretórios

```
squads/marketing-arm-mentoria/
├── squad.yaml                    # Manifest principal
├── README.md                     # Overview
├── config/
│   ├── squad-config.md          # Este arquivo
│   ├── roles-definitions.md     # Job descriptions (7 roles)
│   ├── weekly-workflow.md       # Fluxo semanal
│   ├── content-guidelines.md    # Padrões de conteúdo
│   └── kpi-dashboard.md         # Métricas
├── agents/
│   ├── cmo.yaml                 # CMO agent
│   ├── ideacao-instagram.yaml   # Ideação IG
│   ├── ideacao-linkedin.yaml    # Ideação LinkedIn
│   ├── producao.yaml            # Produção
│   ├── designer.yaml            # Designer
│   ├── distribuicao.yaml        # Distribuição
│   └── metricas.yaml            # Métricas
├── tasks/
│   ├── weekly-ideation.md       # Task de ideação semanal
│   ├── content-production.md    # Task de produção
│   ├── content-distribution.md  # Task de distribuição
│   └── weekly-analytics.md      # Task de análise
├── templates/
│   ├── post-instagram.md        # Template IG
│   ├── post-linkedin.md         # Template LinkedIn
│   ├── video-brief.md           # Template de briefing
│   └── analytics-report.md      # Template de relatório
└── data/
    ├── content-calendar.csv     # Calendário de conteúdo
    └── audience-profiles.md     # Perfis de público
```

## Configurações Principais

### Plataformas
- **Instagram:** Reels (60s max), Stories (15s), Posts estáticos
- **LinkedIn:** Artigos (800-1200 palavras), Carousels (7-10 slides), Posts (100-300 caracteres)
- **YouTube:** Vídeos longos (5-15 min), Shorts (30-60s)

### Horários Ótimos de Publicação
- **Instagram:** 7am, 1pm, 6pm (horário do Brasil)
- **LinkedIn:** 8am, 12pm (horário do Brasil)
- **YouTube:** Sexta-feira 7pm (maior engajamento)

### Público-Alvo
1. **Autônomos:** 25-55 anos, buscam aumentar renda
2. **Médicos:** 30-60 anos, buscam gestão empresarial
3. **Advogados:** 25-55 anos, buscam crescimento profissional

### Tone of Voice
- Profissional mas acessível
- Educativo e prático
- Inspirador mas realista
- Confiável e expert

## Fluxo de Aprovação

```
Ideador → CMO (aprovação) → Produtor/Designer → Distribuidor → Métricas
```

## Links Importantes

- [Job Descriptions](./roles-definitions.md)
- [Weekly Workflow](./weekly-workflow.md)
- [Content Guidelines](./content-guidelines.md)
- [KPI Dashboard](./kpi-dashboard.md)

---

**Data de criação:** 2026-02-08
**Última atualização:** 2026-02-08
**Versão:** 1.0.0

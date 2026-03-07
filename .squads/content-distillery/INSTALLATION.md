# Content Distillery Squad — Instalação

**Data de Instalação:** 2026-03-07
**Versão:** 1.0.0
**Localização:** `.squads/content-distillery/`
**Status:** ✅ OPERACIONAL

## Componentes Instalados

### ✅ Agentes (9)
- `distillery-chief` — Orchestrador principal
- `tacit-extractor` — Extração de conhecimento tácito (Cedric Chin)
- `model-identifier` — Identificação de frameworks (Shane Parrish)
- `knowledge-architect` — Arquitetura de conhecimento (Tiago Forte)
- `content-atomizer` — Atomização de conteúdo (Gary Vaynerchuk)
- `idea-multiplier` — Multiplicação de ideias (Cole & Bush)
- `ecosystem-designer` — Design de ecossistema (Dan Koe)
- `production-ops` — Operações de produção (Justin Welsh)
- `youtube-strategist` — Estratégia YouTube (Paddy Galloway)

### ✅ Workflows (3)
- `full-distillery-pipeline` — Pipeline completo (6 fases)
- `framework-extraction` — Extração apenas (3 fases)
- `content-derivation` — Derivação de conteúdo (3 fases)

### ✅ Tasks (12)
- `ingest-youtube` — Download e transcrição de vídeos
- `extract-tacit-knowledge` — Extração de conhecimento tácito
- `identify-frameworks` — Identificação de frameworks
- `progressive-summarize` — Sumarização progressiva (5 camadas)
- `build-knowledge-base` — Construção de base de conhecimento
- `multiply-ideas` — Multiplicação de ideias (4A Framework)
- `atomize-content` — Atomização em peças por plataforma
- `design-ecosystem` — Design de ecossistema
- `produce-batch` — Produção em batch
- `optimize-youtube` — Otimização para YouTube
- `distill-single-live` — Orquestração de pipeline completo
- `cross-reference-frameworks` — Comparação de frameworks

### ✅ Quality Gates (5)
- QG-001: Validação de Transcrição (routing)
- QG-002: Extração Completa (blocking)
- QG-003: Destilação Validada (blocking)
- QG-004: Conteúdo Revisado (blocking)
- QG-005: YouTube Ready (advisory)

### ✅ Templates (3)
- `framework-template.md` — Documentação de frameworks
- `distillation-report.md` — Relatório de destilação
- `content-piece-template.md` — Template de peça de conteúdo

### ✅ Checklists (2)
- `distillation-quality.md` — QG-001 até QG-005
- `squad-checklist.md` — Validação completa do squad

## Como Usar

### Comando Principal
```bash
@content-distillery:distillery-chief
```

### Quick Start - Pipeline Completo
```bash
@content-distillery:distillery-chief *distill https://youtube.com/watch?v=VIDEO_ID
```

### Extração de Frameworks
```bash
@content-distillery:distillery-chief *extract https://youtube.com/watch?v=VIDEO_ID
```

### Derivar Conteúdo de Frameworks Existentes
```bash
@content-distillery:distillery-chief *derive outputs/distillery/SLUG/frameworks.yaml
```

### Comparar Frameworks
```bash
@content-distillery:distillery-chief *compare outputs/distillery/SLUG_A/ outputs/distillery/SLUG_B/
```

### Verificar Status
```bash
@content-distillery:distillery-chief *status
```

## Resultado Esperado

Processando um vídeo do YouTube (1-4 horas):
- **Frameworks extraídos:** 5-8
- **Heurísticas:** 10-15
- **Ideias de conteúdo:** 80+
- **Peças finais:** 60+
- **Calendário:** 4 semanas

## Dependências Externas

⚠️ Nota: As seguintes dependências devem ser instaladas separadamente:
- `etl-data-collector` — Download e transcrição do YouTube
- `transcription-pro` — Pipeline de transcrição de áudio
- `youtube-transcript` — API de legendas do YouTube
- `whisper` — OpenAI Whisper para transcrição
- `ffmpeg` — Processamento de áudio

## Próximos Passos

1. ✅ Squad instalado e pronto para uso
2. ⏳ Configure as dependências externas quando necessário
3. ⏳ Comece a processar vídeos do YouTube
4. ⏳ Use o knowledge base gerado para derivar conteúdo

---

**Instalado em:** 2026-03-07
**Versão:** v1.0.0

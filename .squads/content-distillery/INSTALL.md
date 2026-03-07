# Squad: Content Distillery — Guia de Instalação

**Status:** ✅ Instalado | **Data:** 2026-03-07 | **AIOX Conformidade:** 100%

## Visão Geral

Squad que transforma **livestreams do YouTube (1-4 horas) em 60+ peças de conteúdo** estruturado via framework extraction, knowledge distillation e produção multi-plataforma.

- **Entrada:** 1 livestream
- **Saída:** 60+ content pieces
- **Agentes:** 9 especialistas
- **Pipeline:** 6 fases (Ingest → Optimize)

## Como Usar

### 1. Ativar o Chief (Distillery Chief)
```bash
@content-distillery:distillery-chief
```

### 2. Ativar Especialistas

| Agente | Persona | Expertise |
|--------|---------|-----------|
| **distillery-chief** | Orchestrator | Coordena pipeline |
| **tacit-extractor** | Cedric Chin | Extração de conhecimento tácito |
| **model-identifier** | Shane Parrish | Identificação de modelos mentais |
| **knowledge-architect** | Tiago Forte | Arquitetura PARA |
| **content-atomizer** | Gary Vaynerchuk | Decomposição de conteúdo |
| **idea-multiplier** | Nicolas Cole & Dickie | Multiplicação de angles |
| **ecosystem-designer** | Dan Koe | Design de ecossistema |
| **production-ops** | Justin Welsh | Operações em batch |
| **youtube-strategist** | Paddy Galloway | Otimização YouTube |

### 3. Workflows

#### Pipeline Completo (Recomendado)
```bash
@content-distillery:distillery-chief *distill https://youtube.com/watch?v=VIDEO_ID
```

#### Extração de Frameworks Apenas
```bash
@content-distillery:distillery-chief *extract https://youtube.com/watch?v=VIDEO_ID
```

#### Derivar Conteúdo de Frameworks Existentes
```bash
@content-distillery:distillery-chief *derive outputs/distillery/SLUG/frameworks.yaml
```

#### Comparar Frameworks
```bash
@content-distillery:distillery-chief *compare outputs/distillery/SLUG_A/ outputs/distillery/SLUG_B/
```

## 6 Fases do Pipeline

### 1️⃣ **Ingest** (Cedric + Chief)
- Download do vídeo
- Transcrição automática
- Parsing de timestamps

### 2️⃣ **Extract** (Cedric + Shane)
- Extração de knowledge tácito
- Identificação de frameworks
- Identificação de heuristics
- Identificação de modelos mentais

### 3️⃣ **Distill** (Tiago Forte)
- Progressive summarization (5 camadas)
- PARA classification
- Knowledge base estruturado

### 4️⃣ **Multiply** (Nicolas Cole, Dickie Bush, Dan Koe)
- 4A Framework angles
- Variações de formato
- Idea scoring
- Ecosystem mapping

### 5️⃣ **Produce** (Gary V + Justin Welsh)
- Platform-specific content
- Ecosystem calendar
- Batch production
- Multi-format adaptation

### 6️⃣ **Optimize** (Paddy Galloway)
- YouTube-specific optimization
- Titles, thumbnails, tags
- Algoritmo-aware tweaks

## Output Esperado (60+ peças)

```
Frameworks & Models (5-8)
├── Frameworks sintetizados
├── Heuristics compiladas
├── Mental models extraídos
└── Padrões de decisão

Content Pieces (40-50)
├── Blog posts
├── Email sequences
├── Social media posts
├── Video scripts
├── Podcast transcripts
├── Infographics briefs
└── Variações multi-formato

Knowledge Assets (5-10)
├── Structured KB
├── Idea directory
├── Source attribution
└── Connection mapping
```

## Quick Start

```bash
# Full pipeline em 1 comando
@content-distillery:distillery-chief *distill https://youtube.com/watch?v=ABC123

# Monitorar progresso
@content-distillery:distillery-chief *status ABC123

# Revisar frameworks extraídos
@content-distillery:distillery-chief *review-frameworks ABC123

# Exportar para Notion/Obsidian
@content-distillery:distillery-chief *export ABC123 [notion|obsidian]
```

## Estrutura de Pastas

```
.squads/content-distillery/
├── squad.yaml              (AIOX manifest)
├── INSTALL.md              (este arquivo)
├── README.md               (overview)
├── agents/                 (9 agentes)
├── tasks/                  (tarefas)
├── workflows/              (orchestration)
├── templates/              (output templates)
├── data/                   (config, presets)
└── outputs/                (conteúdo processado)
    └── distillery/
        └── {SLUG}/
            ├── frameworks.yaml
            ├── content-pieces.md
            ├── knowledge-base.yaml
            └── ecosystem-calendar.md
```

## Casos de Uso

1. **Transformar Aula em 50+ Posts** — Extrair frameworks + conteúdo
2. **Livro em Threads no X** — Distill por capítulos + criar threads
3. **Podcast em Newsletter** — Extrair insights + escrever sequences
4. **Palestra em Conteúdo Viral** — Multiplicar angles para TikTok/Reels

## Próximas Ações

1. Tenha URL do YouTube livestream pronto
2. Ative distillery-chief
3. Execute `*distill [URL]`
4. Espere processamento (~20-30 min para livestream de 2h)
5. Revise outputs
6. Customize conforme necessário

---

**Instalado:** 2026-03-07 | **AIOX Conformance:** 100% ✅

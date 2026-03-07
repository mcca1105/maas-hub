# Squad: Desafio AIOX — Guia de Instalação

**Status:** ✅ Instalado | **Data:** 2026-03-07 | **AIOX Conformidade:** 100%

## Visão Geral

Squad de **agentes IA para criadores de conteúdo**, criado para participantes do Desafio AIOX.

- **Agentes:** 5 (Chief + 4 especialistas)
- **Tasks:** 3 workflows guiados
- **Checklists:** 4 validações de qualidade
- **Foco:** Video editing, análise concorrencial, repurposing, roteiros

## Como Usar

### 1. Ativar o Chief (Recomendado)
```bash
/aiox-chief
```

O **AIOX Chief** é o líder que sabe qual agente chamar para cada tarefa.

### 2. Ativar Agentes Diretamente

| Comando | Agente | Função |
|---------|--------|--------|
| `/aiox-chief` | Chief | Coordena, roteia |
| `/video-editor` | Editor | Corta vídeos, cria shorts/reels |
| `/espiao` | Espião | Analisa canais e concorrentes |
| `/repurposing` | Repurposing | Multiplica 1 vídeo em 10+ peças |
| `/scriptwriter` | Roteirista | Cria roteiros com hook + CTA |

### 3. Workflows

```bash
# Análise de canal
@aiox-chief: "Analisa o canal do @fulano"
→ Chief aciona Espião

# Cortes de vídeo
@aiox-chief: "Preciso de 10 cortes da minha live"
→ Chief aciona Video Editor

# Repurposing
@aiox-chief: "Transforma esse vídeo em posts pro Instagram"
→ Chief aciona Repurposing
```

## Recursos Extras

| Recurso | Tipo | Uso |
|---------|------|-----|
| **Capa Lendária** | Aplicação Web | Gera thumbnails profissionais |

## Estrutura de Pastas

```
.squads/desafio-aiox/
├── squad.yaml              (AIOX manifest)
├── INSTALL.md              (este arquivo)
├── README.md               (overview)
├── agents/                 (5 agentes)
├── tasks/                  (workflows)
├── checklists/             (validações)
└── docs/                   (documentação)
```

## Quick Commands

```bash
# Análise concorrencial
/espiao [URL ou canal]

# Editar vídeo
/video-editor [arquivo.mp4]

# Gerar roteiro
/scriptwriter [tema]

# Multiplicar conteúdo
/repurposing [vídeo]
```

## Casos de Uso

1. **Criar Shorts** — Video Editor corta e otimiza para TikTok/Instagram Reels
2. **Analisar Concorrência** — Espião mapeia estratégia de canal similar
3. **Gerar Roteiros** — Scriptwriter cria hooks + CTAs comprovados
4. **Multiplicar Conteúdo** — Repurposing transforma 1 vídeo em 10+ peças
5. **Orquestração** — Chief roteia automaticamente

## Próximas Ações

1. Ative o Chief: `/aiox-chief`
2. Descreva seu projeto
3. O Chief recomendará qual agente usar
4. Execute a tarefa
5. Valide com checklists

---

**Instalado:** 2026-03-07 | **AIOX Conformance:** 100% ✅

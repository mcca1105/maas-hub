# 📖 Usage Guide — Content Distillery

Exemplos práticos de uso para cada caso de uso.

---

## 1️⃣ Livestream → 60+ Peças de Conteúdo

**Comando:**
```bash
@content-distillery:distillery-chief *distill https://youtube.com/watch?v=ABC123
```

**Saída esperada em `.squads/content-distillery/outputs/distillery/{SLUG}/`:**
```
frameworks.yaml              (5-8 frameworks + heuristics)
content-pieces.md            (60+ peças estruturadas)
knowledge-base.yaml          (KB estruturada)
ecosystem-calendar.md        (4 semanas publicação)
distillation-report.md       (Relatório completo)
```

---

## 2️⃣ Extrair Só Frameworks & Mental Models

**Comando:**
```bash
@content-distillery:distillery-chief *extract https://youtube.com/watch?v=ABC123
```

**Saída:**
```
frameworks.yaml              (Frameworks + heuristics)
mental-models.yaml           (Modelos mentais)
knowledge-base.yaml          (Base de conhecimento)
```

**Caso de uso:** Quando você quer frameworks sem produção de conteúdo.

---

## 3️⃣ Derivar Conteúdo de Frameworks Existentes

**Comando:**
```bash
@content-distillery:distillery-chief *derive outputs/distillery/hormozi-2h-livestream/frameworks.yaml
```

**Saída:**
```
content-pieces.md            (60+ peças novas)
ecosystem-calendar.md        (Calendário otimizado)
variation-report.md          (Relatório de variações)
```

**Caso de uso:** Reutilizar frameworks antigos para gerar novo conteúdo.

---

## 4️⃣ Comparar Frameworks de Duas Fontes

**Comando:**
```bash
@content-distillery:distillery-chief *compare \
  outputs/distillery/hormozi/ \
  outputs/distillery/gary-vaynerchuk/
```

**Saída:**
```
comparison-matrix.yaml       (Frameworks lado-a-lado)
reinforcements.md            (Ideias confirmadas)
contradictions.md            (Pontos em conflito)
complements.md               (Ideias complementares)
meta-frameworks.md           (Síntese de ambos)
```

**Caso de uso:** Validar ideias, encontrar consenso entre experts.

---

## 5️⃣ Monitorar Progresso de Pipeline

**Comando:**
```bash
@content-distillery:distillery-chief *status ABC123
```

**Resposta:**
```
✅ Phase 1: INGEST — Complete (3 min)
✅ Phase 2: EXTRACT — Complete (6 min)
✅ Phase 3: DISTILL — Complete (5 min)
⏳ Phase 4: MULTIPLY — In Progress (2/5 min)
⭕ Phase 5: PRODUCE — Queued
⭕ Phase 6: OPTIMIZE — Queued

ETA: 18 minutos para completar
```

---

## 6️⃣ Revisar Frameworks Antes de Conteúdo

**Comando:**
```bash
@content-distillery:distillery-chief *review-frameworks ABC123
```

**Resposta:**
```
Frameworks Identificados (7):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. The Core 4 (Hormozi)
   └─ Revenue, Margin, Scale, Impact

2. $100M Offer Architecture
   └─ Problem, Promise, Price

3. Qualification Framework
   └─ Budget, Authority, Need, Timeline

4. Follow-up Sequences
   └─ 1st, 3rd, 5th, 7th day

5. Scaling Levers
   └─ Traffic, Conversion, AOV

6. Retention Pyramid
   └─ Product, Community, Education

7. Pricing Strategy
   └─ Value-based vs Cost-plus
```

---

## 7️⃣ Visualizar Content Pieces Gerados

**Comando:**
```bash
@content-distillery:distillery-chief *list-content ABC123
```

**Resposta:**
```
Content Pieces (60):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📝 Blog Posts (5)
  ✓ "How to Structure a $100M Offer"
  ✓ "The Core 4 Framework Explained"
  ✓ "Qualification: Pre-Sale Mastery"
  ✓ "Why Pricing is Psychology"
  ✓ "The Scaling Pyramid"

📧 Email Sequences (8)
  ✓ "5-Day Offer Breakdown Series"
  ✓ "Core 4 Deep Dive"
  ✓ ... (6 mais)

🐦 Twitter Threads (12)
  ✓ Thread 1: "Core 4 Overview"
  ✓ Thread 2: "Revenue Mechanics"
  ✓ ... (10 mais)

📱 Instagram Carousels (10)
  ✓ "5 Steps to Better Offers"
  ✓ "Pricing Psychology 101"
  ✓ ... (8 mais)

🎬 TikTok/Reels Scripts (8)
  ✓ "30-sec: Core 4 Explainer"
  ✓ "60-sec: Pricing Breakdown"
  ✓ ... (6 mais)

📹 YouTube Shorts (7)
  ✓ "What is the Core 4?"
  ✓ "Why Your Offer Fails"
  ✓ ... (5 mais)

🎙️ Podcast Highlights (3)
  ✓ "Best 5 Quotes from Livestream"
  ✓ "30-min Edited Segment"
  ✓ "Full Transcript + Timestamps"

✨ Outros (7)
  ✓ Infographics briefs
  ✓ LinkedIn posts
  ✓ Newsletter outlines
  ✓ Webinar scripts
  ✓ Case study angles
  ✓ FAQ content
  ✓ Resource guides
```

---

## 8️⃣ Exportar para Notion / Obsidian

**Comando:**
```bash
@content-distillery:distillery-chief *export ABC123 notion
```

**Resultado:** Tudo importado no Notion (databases + relations)

**Ou para Obsidian:**
```bash
@content-distillery:distillery-chief *export ABC123 obsidian
```

**Resultado:** Pasta estruturada em Obsidian com backlinks.

---

## 9️⃣ Batch: Processar Múltiplos Livestreams

**Comando:**
```bash
@content-distillery:distillery-chief *batch-distill \
  https://youtube.com/watch?v=URL1 \
  https://youtube.com/watch?v=URL2 \
  https://youtube.com/watch?v=URL3
```

**Saída:** 3 folders separados em outputs/, processados em paralelo.

---

## 🔟 Avançado: Customizar Fase de Derivação

**Comando:**
```bash
@content-distillery:distillery-chief *derive \
  outputs/distillery/hormozi/frameworks.yaml \
  --angles 4a \
  --platforms twitter,linkedin,tiktok \
  --quantity 80
```

**Saída:** 80 peças APENAS para Twitter/LinkedIn/TikTok, focado em 4A angles.

---

## Casos de Uso Recomendados

### Caso A: Aula → Posts Semanais
```bash
1. *distill https://youtube.com/watch?v=aula-completa
2. Espere 25 min
3. *export outputs/distillery/aula/content-pieces.md notion
4. Publique 1 por dia por 60 dias
```

### Caso B: Livro → Threads do X
```bash
1. Para cada capítulo, *extract [URL]
2. *derive outputs/distillery/cap-1/frameworks.yaml --platforms twitter
3. Crie 1 thread por capítulo (25-30 frameworks = 30 threads)
```

### Caso C: Podcast → Newsletter
```bash
1. *extract [URL_PODCAST]
2. *list-content ABC123 | filter email
3. *export ABC123 markdown
4. Customize + envie na newsletter
```

### Caso D: Validação de Ideias
```bash
1. *extract https://youtube.com/watch?v=expert-1
2. *extract https://youtube.com/watch?v=expert-2
3. *compare outputs/distillery/expert-1/ outputs/distillery/expert-2/
4. Veja o que AMBOS confirmam (high-confidence ideas)
```

---

## ⚡ Tips & Tricks

**Dica 1:** Use `*status` antes de `*review-frameworks` para esperar completion.

**Dica 2:** Salve `frameworks.yaml` separado — reutilize depois com `*derive`.

**Dica 3:** Compare 3+ fontes para encontrar "consensus frameworks".

**Dica 4:** Customize templates em `.squads/content-distillery/templates/` para seu estilo.

**Dica 5:** Use `--quantity 120` para gerar MUITO mais ideias (ideal para batch).

---

## 📊 Benchmarks Esperados

| Métrica | Baseline | Otimizado |
|---------|----------|-----------|
| Frameworks extraídos | 5-8 | 10-12 |
| Content pieces | 40-50 | 60-80 |
| Processing time (2h video) | 25 min | 20 min |
| Idea quality score | 3.5/5 | 4.2/5 |
| Reusable frameworks | 60% | 85% |

---

**Mais dúvidas?** Veja `TROUBLESHOOTING.md`.

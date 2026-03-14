# 🔧 Troubleshooting Guide — Content Distillery

FAQ e soluções para problemas comuns.

---

## ❌ Squad não é reconhecido

### Sintoma
```
Error: @content-distillery:distillery-chief not found
```

### Soluções

**1. Verificar localização:**
```bash
ls -la /c/Users/User/.squads/content-distillery/squad.yaml
```
Se não existir, squad não está instalado corretamente.

**2. Recarregar Claude Code:**
```
Menu → Settings → Reload
```

**3. Verificar squad.yaml:**
```bash
cat /c/Users/User/.squads/content-distillery/squad.yaml | head -10
```
Deve ter `apiVersion: aiox/v1` e `kind: Squad`.

---

## ❌ Agentes não aparecem

### Sintoma
```
No agents found in content-distillery
```

### Solução
Verificar pasta `agents/`:
```bash
ls /c/Users/User/.squads/content-distillery/agents/ | wc -l
```
Deve ter 9 arquivos `.md`.

Se faltar, copiar de Downloads:
```bash
cp -r /c/Users/User/Downloads/content-distillery/agents/* \
  /c/Users/User/.squads/content-distillery/agents/
```

---

## ❌ Workflows não funcionam

### Sintoma
```
Workflow 'full-distillery-pipeline' not found
```

### Solução
```bash
ls /c/Users/User/.squads/content-distillery/workflows/
```

Deve ter 3 arquivos:
- full-distillery-pipeline.yaml ✓
- framework-extraction.yaml ✓
- content-derivation.yaml ✓

Se faltar, copiar:
```bash
cp -r /c/Users/User/Downloads/content-distillery/workflows/* \
  /c/Users/User/.squads/content-distillery/workflows/
```

---

## ❌ URL do YouTube não funciona

### Sintoma
```
Error: Invalid YouTube URL
```

### Soluções

**1. Verificar formato:**
```bash
✅ https://youtube.com/watch?v=dQw4w9WgXcQ
✅ https://youtu.be/dQw4w9WgXcQ
❌ youtube.com/watch?v=dQw4w9WgXcQ (falta https://)
❌ https://youtube.com/shorts/ABC (Shorts, não livestream)
```

**2. Verificar se é livestream:**
O vídeo precisa estar completo (já finalizado o livestream).

**3. Verificar acesso público:**
O vídeo deve ser público (não privado/unlisted).

---

## ⏳ Pipeline muito lento

### Sintoma
```
Processing taking longer than expected (> 40 min)
```

### Causas & Soluções

| Causa | Solução |
|-------|---------|
| Vídeo > 4 horas | Use `*extract` em vez de `*distill` |
| Livestream de baixa qualidade | Transcrição toma mais tempo |
| Sistema ocupado | Aguarde ou reexecute depois |
| Muitas tasks em fila | Cancele outros `*distill` em execução |

### Cancelar operação:
```bash
@content-distillery:distillery-chief *cancel ABC123
```

---

## 📁 Outputs não aparecem

### Sintoma
```
Directory not found: outputs/distillery/
```

### Solução
Criar pasta manualmente:
```bash
mkdir -p /c/Users/User/.squads/content-distillery/outputs/distillery
```

Ou verificar se fase 1 (INGEST) completou:
```bash
@content-distillery:distillery-chief *status ABC123
```

---

## 💾 Frameworks são vazios

### Sintoma
```
frameworks.yaml exists but empty or minimal content
```

### Causas

| Causa | Solução |
|-------|---------|
| Vídeo tem pouco conteúdo | Use vídeo mais denso (aulas, palestras) |
| Transcrição ruim | YouTube não conseguiu transcrever |
| Especialista não encontrou frameworks | Tente outro vídeo |

### Debug:
```bash
@content-distillery:distillery-chief *review-frameworks ABC123
```

Se vazio, vídeo pode não ter frameworks identificáveis.

---

## 🎯 Content pieces têm baixa qualidade

### Sintoma
```
Content pieces seem generic or low quality
```

### Soluções

**1. Verificar frameworks extraídos:**
```bash
@content-distillery:distillery-chief *review-frameworks ABC123
```

Se frameworks forem fracos, conteúdo será fraco.

**2. Usar outro vídeo:**
Escolher vídeo com frameworks mais claros (Hormozi, Gary Vee, Tiago Forte, etc).

**3. Customizar durante derivação:**
```bash
@content-distillery:distillery-chief *derive \
  outputs/distillery/SLUG/frameworks.yaml \
  --angles 4a \
  --tone [professional|casual|viral]
```

---

## 🔁 Comparação não funciona

### Sintoma
```
Error comparing frameworks
```

### Soluções

**1. Verificar caminhos:**
```bash
ls /c/Users/User/.squads/content-distillery/outputs/distillery/slug1/frameworks.yaml
ls /c/Users/User/.squads/content-distillery/outputs/distillery/slug2/frameworks.yaml
```

Ambos devem existir.

**2. Sintaxe correta:**
```bash
@content-distillery:distillery-chief *compare \
  outputs/distillery/slug1/ \
  outputs/distillery/slug2/
```

(Caminhos relativos a `.squads/content-distillery/`)

---

## 📤 Export não funciona

### Sintoma
```
Error exporting to Notion / Obsidian
```

### Soluções

**Para Notion:**
- [ ] Verificar se Notion API key está configurada
- [ ] Verificar se database Notion existe
- [ ] Verificar permissões da key

**Para Obsidian:**
- [ ] Verificar se vault Obsidian está aberto
- [ ] Verificar caminho correto do vault
- [ ] Verificar permissões de escrita

**Fallback:** Use export markdown:
```bash
@content-distillery:distillery-chief *export ABC123 markdown
```

---

## 🔐 Erros de permissão

### Sintoma
```
Permission denied: outputs/distillery/
```

### Solução

**No Windows:**
```bash
icacls "C:\Users\User\.squads\content-distillery\outputs" /grant:r "%username%:F"
```

**No Mac/Linux:**
```bash
chmod -R 755 ~/.squads/content-distillery/outputs/
```

---

## 💻 Erro de memória

### Sintoma
```
Out of memory error during processing
```

### Soluções

**1. Usar apenas extraction:**
```bash
@content-distillery:distillery-chief *extract [URL]
```
(Muito menos memória que `*distill`)

**2. Processar em batch com delay:**
```bash
@content-distillery:distillery-chief *distill URL1
# Aguarde completar (25-30 min)
@content-distillery:distillery-chief *distill URL2
```

**3. Reiniciar Claude Code:**
```
Menu → Restart
```

---

## 🆘 Chief não responde

### Sintoma
```
@content-distillery:distillery-chief — No response
```

### Soluções

**1. Verificar se Chief está ativo:**
```bash
@content-distillery:distillery-chief *status
```

**2. Se nenhuma resposta, reativar:**
```bash
*exit
@content-distillery:distillery-chief
```

**3. Verificar logs:**
```bash
tail -f .claude/logs/agent.log | grep content-distillery
```

---

## 📊 Quality gates falhando

### Sintoma
```
Quality gate QG-003 failed: Distillation validation error
```

### Causas & Soluções

| Gate | Significa | Solução |
|------|-----------|---------|
| QG-001 | Transcrição inválida | Re-tentar com vídeo diferente |
| QG-002 | Extraction incompleto | Aguarde completion |
| QG-003 | Distillation falhou | Vídeo pode não ter frameworks |
| QG-004 | Conteúdo não passou QA | Customizar templates |
| QG-005 | YouTube prep incompleto | Ignorável (advisory only) |

**Bypass quality gate (use com cuidado):**
```bash
@content-distillery:distillery-chief *distill \
  https://youtube.com/watch?v=ABC123 \
  --skip-quality-gate QG-005
```

---

## 🤔 Perguntas Frequentes

### P: Quanto tempo leva?
**R:** 20-30 min para livestream de 2 horas. Videos mais curtos = mais rápido.

### P: Preciso estar online o tempo todo?
**R:** Sim, até completion. Claude Code não funciona offline.

### P: Posso processar vários ao mesmo tempo?
**R:** Não recomendado (overhead). Processe sequencialmente.

### P: Os outputs são salvos?
**R:** Sim, em `.squads/content-distillery/outputs/distillery/{SLUG}/`.

### P: Posso editar outputs?
**R:** Sim, são markdown normais. Edite e reutilize com `*derive`.

### P: Como integrar com meu sistema?
**R:** Use exports (notion, obsidian, markdown, rss).

---

## 🆘 Problema Não Listado?

**Reporte em:** `.squads/content-distillery/` → issue tracking

**Ou ative debug:**
```bash
@content-distillery:distillery-chief *debug-enable
@content-distillery:distillery-chief *distill [URL]
# Veja output detalhado com stack trace
```

---

**Resolvido?** Excelente! 🎉

**Não resolveu?** Leia `ACTIVATION.md` ou `INSTALL.md`.

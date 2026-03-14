# 🚀 Quick Start — Content Distillery

**⏱️ Tempo:** 2 minutos para ativar | 20-30 minutos para processar livestream

---

## 30 Segundos: Ativar o Chief

```bash
@content-distillery:distillery-chief
```

**Esperado:** Chief ativado e pronto para receber comandos.

---

## 2 Minutos: Seu Primeiro Pipeline

Tenha a URL do YouTube pronta:

```bash
@content-distillery:distillery-chief *distill https://youtube.com/watch?v=ABC123DEF456
```

**O que acontece:**
1. ✅ Baixa vídeo + transcrição
2. ✅ Extrai frameworks + heuristics
3. ✅ Cria sumário progressivo (5 camadas)
4. ✅ Gera 80+ ideias de conteúdo
5. ✅ Produz 60+ peças prontas
6. ✅ Otimiza para YouTube

---

## 3 Usos Comuns

### Uso 1: Livestream → Conteúdo (Completo)
```bash
@content-distillery:distillery-chief *distill [URL]
```
**Saída:** Frameworks + 60+ peças de conteúdo + calendário de publicação

### Uso 2: Extrair Só Frameworks
```bash
@content-distillery:distillery-chief *extract [URL]
```
**Saída:** 5-8 frameworks + 10-15 heuristics (SEM produção de conteúdo)

### Uso 3: Conteúdo de Frameworks Existentes
```bash
@content-distillery:distillery-chief *derive outputs/distillery/SLUG/frameworks.yaml
```
**Saída:** 60+ peças de conteúdo derivadas de frameworks já extraídos

---

## 📊 Exemplo Real (Hormozi Livestream)

**Entrada:**
- URL: `https://youtube.com/watch?v=hormozi-sales-breakdown`
- Duração: 2 horas

**Saída Esperada:**
```
📦 Frameworks Extraídos (6)
├── The Core 4 (Revenue, Margin, Scale, Impact)
├── $100M Offer Architecture
├── Qualification Framework
├── Follow-up Sequences
├── Scaling Levers
└── Retention Pyramid

📝 Content Pieces (60+)
├── Blog Posts (5)
├── Email Sequences (8)
├── Twitter Threads (12)
├── LinkedIn Posts (10)
├── TikTok Scripts (8)
├── Instagram Carousels (10)
├── YouTube Shorts (7)
└── Podcast Highlights (3)

📅 Calendar
├── Week 1: Foundations (Offer architecture)
├── Week 2: Deepdive (Core 4 mechanics)
├── Week 3: Application (Case studies)
└── Week 4: Scaling (Advanced tactics)
```

---

## ⚙️ Processamento

| Phase | Tempo | O que acontece |
|-------|-------|---|
| Ingest | 2-3 min | Download + transcrição |
| Extract | 5-7 min | Frameworks + knowledge |
| Distill | 5 min | Summarization + PARA |
| Multiply | 5 min | 4A angles + ideas |
| Produce | 8-10 min | Content pieces |
| Optimize | 2-3 min | YouTube tweaks |
| **TOTAL** | **20-30 min** | **60+ peças prontas** |

---

## 🎯 Monitorar Progresso

```bash
# Status em tempo real
@content-distillery:distillery-chief *status ABC123

# Revisar frameworks extraídos
@content-distillery:distillery-chief *review-frameworks ABC123

# Visualizar content pieces
@content-distillery:distillery-chief *list-content ABC123

# Comparar com outro livestream
@content-distillery:distillery-chief *compare outputs/distillery/hormozi/ outputs/distillery/gary-vee/
```

---

## 💾 Exportar & Usar

```bash
# Salvar tudo em Markdown
@content-distillery:distillery-chief *export ABC123 markdown

# Integrar com Notion
@content-distillery:distillery-chief *export ABC123 notion

# Enviar para Obsidian
@content-distillery:distillery-chief *export ABC123 obsidian

# Gerar feed RSS
@content-distillery:distillery-chief *export ABC123 rss
```

---

## 🔗 Próximos Passos

1. **Escolha um livestream** (aula, palestra, podcast)
2. **Copie a URL** do YouTube
3. **Execute** `@content-distillery:distillery-chief *distill [URL]`
4. **Aguarde** 20-30 minutos
5. **Revise** frameworks e conteúdo
6. **Customize** conforme necessário
7. **Publique** no seu calendário

---

## 📚 Mais Detalhes

- **Documentação Completa:** `INSTALL.md`
- **Agentes & Personas:** `README.md`
- **Arquitetura Técnica:** `squad.yaml`

---

**Ready?** 🎬 Vá para `INSTALL.md` para detalhes completos.

# Backups de Squads e Documentos

**Locação:** `backups-squads/`
**Propósito:** Armazenar squads em formato .zip e documentação histórica
**Padrão:** L4 Project Runtime (AIOX) — backup de componentes não ativos

---

## 📦 Squads Zipados (12 arquivos)

| Arquivo | Tamanho | Data | Descrição | Status |
|---------|---------|------|-----------|--------|
| `squad-aios-global-v3.zip` | 3.6 MB | 2026-03-06 | Squad global AIOS v3 (latest) | Archivado |
| `squad-aios-global-v2.zip` | 2.8 MB | 2026-03-06 | Squad global AIOS v2 | Archivado |
| `DESAFIO-AIOX-main.zip` | 31 MB | 2026-03-01 | Desafio AIOX completo | Archivado |
| `hormozi.zip` | 1.9 MB | 2026-03-06 | Material Hormozi | Archivado |
| `squad-creator-pro.zip` | 961 KB | 2026-03-06 | Squad Creator Pro | Archivado |
| `squad-creator-premium.zip` | 1.0 MB | 2026-02-28 | Squad Creator Premium | Archivado |
| `squad-creator.zip` | 1.0 MB | 2026-03-06 | Squad Creator Base | Archivado |
| `design.zip` | 678 KB | 2026-02-28 | Design Squad | Archivado |
| `direct-response-marketing.zip` | 574 KB | 2026-02-24 | Direct Response Marketing | Archivado |
| `jose_amorim.zip` | 340 KB | 2026-02-28 | Material José Amorim | Archivado |
| `content-distillery.zip` | 287 KB | 2026-02-28 | Content Distillery | Archivado |
| `squad-desafio-aiox-main.zip` | 39 KB | 2026-03-02 | Desafio AIOX (mini) | Archivado |

**Total:** 48.8 MB em 12 arquivos

---

## 📄 Documentação (PDFs)

**Pasta:** `DOCUMENTOS PDF/`

| Arquivo | Descrição |
|---------|-----------|
| `FireShot Capture 1155 - Matre Marcas - Registro e Proteção de Marcas - Propriedade Intelectual - [].pdf` | Marca registrada - propriedade intelectual |
| `print dos squads download - curso AIOS COHORT - AIOS Cohort Fundamentals - Jose Amorim.pdf` | Material do curso AIOS Cohort |

---

## 🎯 Como Usar

### Ativar um Squad do Backup

```bash
# 1. Extrair o .zip para .squads/
unzip backups-squads/squad-creator-pro.zip -d .squads/

# 2. Validar squad.yaml
cat .squads/squad-creator-pro/squad.yaml

# 3. Ativar squad
@squad-creator-pro
```

### Criar Versão de Backup de Squad Ativo

```bash
# Quando finalizar trabalho em um squad
cd .squads/meu-squad
zip -r ../backups-squads/meu-squad-v1.0.0.zip .
```

---

## 📋 Política de Retenção

- ✅ **Manter:** Squads em desenvolvimento (em `.squads/`)
- ✅ **Manter:** Versões stables no backup (tagged)
- ⚠️ **Revisar:** Squads com > 6 meses sem uso
- ⚠️ **Limpar:** Duplicatas de versão (v2 quando v3 estável)

### Recomendação
- Remover: `squad-aios-global-v2.zip` (v3 é mais nova)
- Remover: `squad-creator-premium.zip` + `squad-creator.zip` (manter apenas `squad-creator-pro.zip`)

---

## 🔗 Estrutura Relacionada

```
~/
├── .squads/                    ← Squads ATIVOS (L4 Project Runtime)
│   ├── automacao-profissional/ ✅
│   ├── marketing-arm-mentoria/ ✅
│   └── squad-vendas/           ✅
│
├── backups-squads/             ← Squads ARQUIVADOS + PDFs
│   ├── *.zip
│   ├── DOCUMENTOS PDF/
│   └── README.md (este arquivo)
│
└── docs/                       ← Documentação do projeto
```

---

## 📖 Notas

- Todos os .zip files estão **organizados** em uma pasta única
- PDFs históricos estão **centralizados** em `DOCUMENTOS PDF/`
- A pasta `.squads/` está **limpa** e segue padrão AIOX
- Squads zipados podem ser **ativados sob demanda**

---

*Último update: 6 de março de 2026*
*Gerenciado por: AIOX Compliance System*

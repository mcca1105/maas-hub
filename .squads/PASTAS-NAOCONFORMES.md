# Pastas Não Conformes em `.squads/`

**Data:** 6 de março de 2026
**Status:** ⚠️ PENDENTE LIMPEZA
**Ação Recomendada:** Remover ou arquivar

---

## 📋 Resumo

Existem **10 pastas extraídas** de arquivos .zip que **não são squads formais AIOX**. Estas pastas foram extraídas manualmente mas seus correspondentes .zip já foram movidos para `backups-squads/`.

| Pasta | .zip Original | Tamanho | Status |
|-------|--------------|---------|--------|
| `content-distillery/` | `content-distillery.zip` | ? | ⚠️ Extraída, .zip em backup |
| `DESAFIO-AIOX-main/` | `DESAFIO-AIOX-main.zip` | 31 MB | ⚠️ Extraída, .zip em backup |
| `design/` | `design.zip` | ? | ⚠️ Extraída, .zip em backup |
| `direct-response-marketing/` | `direct-response-marketing.zip` | ? | ⚠️ Extraída, .zip em backup |
| `jose_amorim/` | `jose_amorim.zip` | ? | ⚠️ Extraída, .zip em backup |
| `squad-creator/` | `squad-creator.zip` | 1.0 MB | ⚠️ Extraída, .zip em backup |
| `squad-creator-premium/` | `squad-creator-premium.zip` | 1.0 MB | ⚠️ Extraída, .zip em backup |
| `squad-creator-pro/` | `squad-creator-pro.zip` | 961 KB | ⚠️ Extraída, .zip em backup |
| `squad-desafio-aiox-main/` | `squad-desafio-aiox-main.zip` | 39 KB | ⚠️ Extraída, .zip em backup |
| `Automacao_Profissional/` | — | — | ⚠️ Nome em PascalCase (deveria ser kebab-case) |

---

## ❌ Por que NÃO são conformes?

1. **Falta `squad.yaml`** — Não possuem manifesto formal AIOX
2. **Naming inconsistente** — Alguns em UPPER_CASE, alguns em snake_case
3. **Sem estrutura L4** — Não possuem `agents/`, `tasks/`, `workflows/`
4. **Redundância** — .zip já está em `backups-squads/`
5. **Poluição visual** — Pioram a legibilidade do catálogo

---

## 🎯 Opções Recomendadas

### Opção A: REMOVER (Recomendado ✅)
**Ação:** Deletar todas as pastas não conformes
**Risco:** Baixo — .zip backups estão em `backups-squads/`
**Ganho:** Pasta `.squads/` fica 100% conforme AIOX

```bash
# Deletar pastas não conformes
rm -rf .squads/content-distillery/
rm -rf ".squads/DESAFIO-AIOX-main/"
rm -rf .squads/design/
rm -rf .squads/direct-response-marketing/
rm -rf .squads/jose_amorim/
rm -rf .squads/squad-creator/
rm -rf .squads/squad-creator-premium/
rm -rf .squads/squad-creator-pro/
rm -rf ".squads/squad-desafio-aiox-main/"

# Resultado: Apenas squads conformes ficam em .squads/
# - automacao-profissional/
# - marketing-arm-mentoria/
```

**Vantagens:**
- ✅ `.squads/` fica 100% conforme AIOX
- ✅ Melhor performance (menos pastas)
- ✅ Clareza visual — só squads ativos

**Desvantagens:**
- ⚠️ Precisa extrair .zip novamente se precisar usar

---

### Opção B: ARQUIVAR (Alternativa)
**Ação:** Mover pastas para `backups-squads/` como diretórios
**Risco:** Médio — mais organização manual
**Ganho:** Mantém referência local

```bash
# Mover para backup como diretórios (não .zip)
mv .squads/content-distillery/ backups-squads/squads-extracted/
mv .squads/DESAFIO-AIOX-main/ backups-squads/squads-extracted/
# ... (resto dos diretórios)
```

**Vantagens:**
- ✅ Mantém referência sem extrair .zip novamente
- ✅ Organiza tudo em um lugar (`backups-squads/`)

**Desvantagens:**
- ⚠️ Duplica conteúdo (.zip + diretório)
- ⚠️ Usa mais espaço em disco

---

### Opção C: FORMALIZAR (Se aplicável)
**Ação:** Converter pastas extraídas em squads AIOX formais
**Risco:** Alto — requer análise manual de cada uma
**Ganho:** Squads novos disponíveis

```bash
# Exemplo: Converter squad-creator-pro em squad formal
cd .squads/squad-creator-pro/
# 1. Criar squad.yaml baseado em template
# 2. Mapear agents/, tasks/, workflows/
# 3. Validar contra schema
@squad-creator *validate squad-creator-pro
```

**Vantagens:**
- ✅ Mais squads disponíveis
- ✅ Reutilizáveis em múltiplos projetos

**Desvantagens:**
- ⚠️ Requer análise de cada pasta
- ⚠️ Tempo investido (1-2 horas por squad)
- ⚠️ Alguns podem não ser viáveis (ex: apenas PDFs)

---

## 🔴 Caso Especial: `Automacao_Profissional/`

**Problema:** Nome em PascalCase em vez de kebab-case
**Situação:** Já é um squad FORMAL com `squad.yaml`
**Solução:** **RENOMEAR** para `automacao-profissional`

```bash
# Renomear para padrão AIOX
mv .squads/Automacao_Profissional/ .squads/automacao-profissional/

# Resultado: Nome conforme AIOX (kebab-case)
```

**Crítico:** Fazer esse rename **ANTES** de usar o squad em scripts ou imports!

---

## 📊 Impacto por Opção

| Opção | `.squads/` Conformidade | Espaço Disco | Tempo | Recomendação |
|-------|----------------------|------------|-------|--------------|
| **A: Remover** | 100% ✅ | -100% | 1 min | ✅ MELHOR |
| **B: Arquivar** | 100% ✅ | -50% | 10 min | ⚠️ OK |
| **C: Formalizar** | 100% ✅ | +200% | 2-4h | ❌ Overkill |

---

## 🎯 Recomendação Final

**Execute em ordem:**

1. **PRIMEIRO:** Renomear `Automacao_Profissional/` → `automacao-profissional/`
2. **DEPOIS:** Remover (Opção A) todas as outras pastas não conformes
3. **RESULTADO:** `.squads/` fica 100% conforme AIOX

```bash
# Script completo (2 minutos)
mv .squads/Automacao_Profissional/ .squads/automacao-profissional/
rm -rf .squads/content-distillery/
rm -rf ".squads/DESAFIO-AIOX-main/"
rm -rf .squads/design/
rm -rf .squads/direct-response-marketing/
rm -rf .squads/jose_amorim/
rm -rf .squads/squad-creator/
rm -rf .squads/squad-creator-premium/
rm -rf .squads/squad-creator-pro/
rm -rf ".squads/squad-desafio-aiox-main/"

# Verificar
ls -la .squads/
# Resultado esperado: INDEX.md, ANALISE-*.md, automacao-profissional/, marketing-arm-mentoria/
```

---

## ✅ Próximos Passos

Após **Opção A (Remover):**

- [ ] Executar script de rename + delete
- [ ] Validar `ls -la .squads/` (deveria ter apenas 2 dirs + 2 .md)
- [ ] Update INDEX.md (remover ⚠️ de pastas não conformes)
- [ ] Git commit: `chore: Clean .squads/ directory — remove non-conform extracted folders`
- [ ] `.squads/` estará 100% conforme AIOX ✅

---

*Documento gerado: 2026-03-06*
*Ref: `.aiox-core/schemas/squad-schema.json`*

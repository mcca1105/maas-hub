# DRM Squad — Validation Scripts

Scripts de validação automática para o squad Direct Response Marketing.

## Scripts Disponíveis

### 1. `validate-copy-quality.py`
Valida qualidade de copy contra os padrões Gary Halbert/DRM.

**O que verifica:**
- Especificidade (ratio de claims específicos vs vagos)
- Abertura proibida (nunca começar com nome da empresa ou "Olá, me chamo...")
- Elementos estruturais presentes (headline, problema, mecanismo, prova, CTA, garantia, urgência)
- Voz passiva excessiva
- Balanceamento você vs nós/eu

**Uso:**
```bash
python validate-copy-quality.py --file path/to/copy.md
python validate-copy-quality.py --dir path/to/multiple/copies/
python validate-copy-quality.py --text "Cole seu copy aqui"
```

**Exit codes:**
- `0` = Score >= 70 (PASS)
- `1` = Score < 70 (NEEDS WORK)

---

### 2. `score-awareness-stage.py`
Determina o estágio de consciência Eugene Schwartz do copy e/ou da audiência.

**O que verifica:**
- Estágio de consciência para o qual o copy está calibrado (Stage 1-5)
- Estágio de consciência real da audiência (baseado em dados VOC/pesquisa)
- Match ou mismatch entre copy e audiência

**Estágios Eugene Schwartz:**
- Stage 1 (Unaware): não sabe que tem o problema
- Stage 2 (Problem Aware): sabe o problema, não a solução
- Stage 3 (Solution Aware): sabe que soluções existem, não seu produto
- Stage 4 (Product Aware): sabe seu produto, não comprou ainda
- Stage 5 (Most Aware): pronto para comprar, precisa da oferta certa

**Uso:**
```bash
python score-awareness-stage.py --copy path/to/copy.md
python score-awareness-stage.py --research path/to/voc-research.md
python score-awareness-stage.py --copy copy.md --research voc.md  # full match analysis
python score-awareness-stage.py --text "Cole texto aqui"
```

---

### 3. `drm-cohesion-validator.py`
Valida consistência (message match, oferta, vocabulário, urgência) entre todos os assets do funil.

**O que verifica:**
1. **Message Match**: Headline/tema é consistente entre ad → landing page → VSL → email
2. **Consistência de Preço**: Mesmo preço mencionado em todos os assets
3. **Consistência de Vocabulário**: Mesmos termos-chave usados em todo o funil
4. **Consistência de Urgência**: Mesmo deadline/mecanismo de escassez em todos os assets

**Uso:**
```bash
# Valida uma pasta inteira de assets do funil
python drm-cohesion-validator.py --dir path/to/funnel/assets/

# Valida arquivos específicos
python drm-cohesion-validator.py --ad ad.md --landing landing.md --email email.md --vsl vsl.md
```

**Exit codes:**
- `0` = PASS (todas as verificações passaram)
- `1` = FAIL ou REVIEW (problemas encontrados)

---

## Fluxo de Uso Recomendado

```
1. Escrever copy → validate-copy-quality.py (verifica qualidade individual)
2. Pesquisar audiência → score-awareness-stage.py --research (diagnostica estágio)
3. Revisar copy → score-awareness-stage.py --copy --research (verifica match)
4. Montar funil completo → drm-cohesion-validator.py --dir (verifica coesão)
```

## Requisitos

- Python 3.8+
- Nenhuma dependência externa — apenas biblioteca padrão Python

## Scores e Thresholds

| Script | Pass Threshold | Output |
|--------|---------------|--------|
| validate-copy-quality.py | Score >= 70/100 | Score detalhado |
| score-awareness-stage.py | Match encontrado | Estágio + recomendação |
| drm-cohesion-validator.py | Todos checks PASS | Relatório de coesão |

## Integração com Workflows

Estes scripts são referenciados nos seguintes workflows:
- `wf-complete-funnel-build.yaml` → Phase 8 (Quality Review)
- `wf-paid-traffic-campaign.yaml` → Phase 4 (Landing Page Alignment)
- `wf-avatar-research.yaml` → Phase 4 (Awareness Stage Mapping)

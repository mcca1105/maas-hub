---
name: Instalação ia-main (Alan Nicolas)
description: Preferência de instalação: commands/prompts apenas, sem squads/agents
type: feedback
---

## Preferência de Instalação

**Decisão:** NÃO usar estrutura de agents/squads para ia-main
- ❌ Sem `.squads/`
- ❌ Sem agents customizados
- ✅ Só commands + prompts
- ✅ Git clone do repositório

**Repositório:**
```bash
git clone https://github.com/oalanicolas/mentelendaria.com.git
```

**Por quê:** Manter simples, evitar overhead de squads, integração direta

**Como aplicar:**
- Clonar e integrar commands em `.claude/commands/ia-alan/`
- Integrar prompts em `.claude/prompts/ia-alan/` ou similar
- Documentar uso
- Deixar pronto para execução immediate

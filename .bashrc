#!/bin/bash
# ============================================
# .bashrc - Configuração do Bash para Windows
# ============================================
# Este arquivo é carregado automaticamente
# toda vez que você abre um terminal Bash
# ============================================

# ============================================
# 1. CONFIGURAÇÕES BÁSICAS
# ============================================

# Histórico de comandos maior
HISTSIZE=10000
HISTFILESIZE=20000

# Evitar duplicatas no histórico
HISTCONTROL=ignoredups:ignorespace

# Append para histórico (não sobrescrever)
shopt -s histappend

# ============================================
# 2. ALIASES ÚTEIS (Atalhos)
# ============================================

# Listar arquivos de forma mais legível
alias ls='ls -lh --color=auto'
alias la='ls -lha'
alias ll='ls -lh'

# Navegação mais fácil
alias ..='cd ..'
alias ...='cd ../..'
alias ~='cd ~'

# Limpar terminal
alias cls='clear'

# Editar .bashrc
alias editrc='nano ~/.bashrc'

# Ver conteúdo de arquivo
alias cat='cat -n'

# Criar pastas e entrar nela
mkcd() {
    mkdir -p "$1" && cd "$1"
}

# Procurar arquivo
alias grep='grep --color=auto'

# ============================================
# 3. PROMPT CUSTOMIZADO COM CORES
# ============================================

# Cores ANSI
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
WHITE='\033[1;37m'
NC='\033[0m' # No Color

# Prompt: username@computador:pasta$
PS1="\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ "

# ============================================
# 5. FUNCTIONS ÚTEIS
# ============================================

# Criar um diretório e entrar nele
function mkcd() {
    mkdir -p "$@" && cd "$_"
}

# Procurar por um arquivo
function findfile() {
    find . -name "$1"
}

# Procurar texto dentro de arquivos
function findtext() {
    grep -r "$1" .
}

# Ver informações do sistema
function sysinfo() {
    echo "=== INFORMAÇÕES DO SISTEMA ==="
    echo "Usuário: $(whoami)"
    echo "Computador: $(hostname)"
    echo "Pasta atual: $(pwd)"
    echo "Data/Hora: $(date)"
    echo "Shell: $SHELL"
}

# ============================================
# 6. VARIÁVEIS DE AMBIENTE
# ============================================

# Definir editor padrão
export EDITOR=nano

# Idioma
export LANG=pt_BR.UTF-8

# ============================================
# 7. AUTO-COMPLETE
# ============================================

# Ativar bash-completion (se disponível)
if [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
fi

# ============================================
# 8. GIT (Se instalado)
# ============================================

# Mostrar branch do git no prompt
git_branch() {
    git branch 2>/dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/ (\1)/'
}

# Versão do prompt com git (opcional)
# PS1="\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[01;31m\]$(git_branch)\[\033[00m\]\$ "

# ============================================
# 9. AIOX CLI ALIASES (Synkra AIOX)
# ============================================

# AIOX Master CLI wrapper
alias aiox='node .aiox-core/bin/aiox-core.js'
alias aiox_doctor='npm run aiox:doctor'
alias aiox_graph='npm run aiox:graph'

# ============================================
# FIM DO ARQUIVO .bashrc
# ============================================

# Para recarregar este arquivo, execute:
# source ~/.bashrc

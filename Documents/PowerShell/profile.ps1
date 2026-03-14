# ============================================
# PowerShell Profile - Configuração Automática
# ============================================
# Este arquivo é carregado automaticamente
# toda vez que você abre o PowerShell
# ============================================

# ============================================
# 2. ALIASES ÚTEIS (Atalhos)
# ============================================

# Atalhos para navegação
Set-Alias ll ls
Set-Alias la Get-ChildItem
Set-Alias clear Clear-Host
Set-Alias cls Clear-Host

# Git (se instalado)
Set-Alias git "C:\Program Files\Git\bin\git.exe"

# Editor preferido
Set-Alias nano "C:\Program Files\Git\usr\bin\nano.exe"

# ============================================
# 3. FUNCTIONS ÚTEIS
# ============================================

# Criar pasta e entrar nela
function mkcd($path) {
    New-Item -ItemType Directory -Path $path -Force | Out-Null
    Set-Location $path
}

# Limpar histórico
function Clear-History {
    [System.IO.File]::WriteAllText((Get-PSReadlineOption).HistorySavePath, "")
}

# Ver informações do sistema
function Show-SystemInfo {
    Write-Host "=== INFORMAÇÕES DO SISTEMA ===" -ForegroundColor Cyan
    Write-Host "Usuário: $(whoami)" -ForegroundColor Green
    Write-Host "Computador: $($env:COMPUTERNAME)" -ForegroundColor Green
    Write-Host "Pasta atual: $(Get-Location)" -ForegroundColor Green
    Write-Host "Data/Hora: $(Get-Date)" -ForegroundColor Green
    Write-Host "PowerShell versão: $($PSVersionTable.PSVersion)" -ForegroundColor Green
}

# Atalho mais curto
Set-Alias sysinfo Show-SystemInfo

# Procurar arquivo recursivamente
function Find-File($name) {
    Get-ChildItem -Path . -Filter $name -Recurse
}

# Procurar texto em arquivos
function Find-Text($pattern) {
    Get-ChildItem -Recurse | Select-String -Pattern $pattern
}

# ============================================
# 4. CONFIGURAÇÕES DE PROMPT
# ============================================

# Função para mostrar o prompt customizado
function prompt {
    # Cores
    $user = [System.Security.Principal.WindowsIdentity]::GetCurrent().Name
    $location = Get-Location
    $time = Get-Date -Format "HH:mm:ss"

    # Admin check (mostra [ADMIN] se for administrador)
    $admin = ""
    if ([bool](
        [System.Security.Principal.WindowsPrincipal]
        [System.Security.Principal.WindowsIdentity]::GetCurrent()
    ).IsInRole([System.Security.Principal.WindowsBuiltInRole]::Administrator)) {
        $admin = "[ADMIN] "
    }

    # Mostrar prompt
    Write-Host "$admin" -ForegroundColor Red -NoNewline
    Write-Host "$user" -ForegroundColor Green -NoNewline
    Write-Host " @ " -ForegroundColor White -NoNewline
    Write-Host "$location" -ForegroundColor Cyan -NoNewline
    Write-Host " [$time] > " -ForegroundColor Yellow

    return ""
}

# ============================================
# 5. HISTÓRICO E AUTOCOMPLETAR
# ============================================

# Aumentar tamanho do histórico
$MaximumHistoryCount = 4000

# Salvar histórico entre sessões
Set-PSReadlineOption -HistorySaveStyle SaveIncrementally
Set-PSReadlineOption -HistorySearchCursorMovesToEnd:$true

# Setas para cima/baixo buscam histórico
Set-PSReadlineKeyHandler -Key UpArrow -Function HistorySearchBackward
Set-PSReadlineKeyHandler -Key DownArrow -Function HistorySearchForward

# ============================================
# 6. VARIÁVEIS DE AMBIENTE
# ============================================

# Editor padrão
$env:EDITOR = "nano"

# ============================================
# 7. MENSAGEM DE BOAS-VINDAS
# ============================================

Write-Host ""
Write-Host "╔════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║  Bem-vindo ao PowerShell, Mariana! 👋  ║" -ForegroundColor Cyan
Write-Host "╚════════════════════════════════════════╝" -ForegroundColor Cyan
Write-Host ""
Write-Host "Comandos úteis:" -ForegroundColor Yellow
Write-Host "  • sysinfo     - Ver informações do sistema" -ForegroundColor Green
Write-Host "  • mkcd <name> - Criar pasta e entrar nela" -ForegroundColor Green
Write-Host "  • find-file <name> - Procurar arquivo" -ForegroundColor Green
Write-Host "  • editrc - Editar este arquivo" -ForegroundColor Green
Write-Host ""

# ============================================
# FIM DO ARQUIVO PROFILE.PS1
# ============================================

# Para recarregar este arquivo, execute:
# . $PROFILE

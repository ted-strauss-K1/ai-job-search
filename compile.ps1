# compile.ps1
# Compile LaTeX CVs and cover letters using Docker (texlive/texlive image)
# Usage: .\compile.ps1 [target]
#   targets: all (default), cv, covers, directit, telus, cmhc, lawzero, cmhc-steward
#
# First run: pulls texlive/texlive (~4GB). Subsequent runs are fast.

param(
    [string]$Target = "all"
)

$ProjectRoot = $PSScriptRoot
$Image = "texlive/texlive:latest"

# Map Windows path to Docker-friendly path
$MountPath = $ProjectRoot -replace "\\", "/"
$MountPath = $MountPath -replace "^([A-Za-z]):", '/$1'

$CVs = @(
    "main_directit.tex",
    "main_telus.tex",
    "main_cmhc.tex",
    "main_lawzero.tex",
    "main_cmhc_steward.tex"
)

$Covers = @(
    "cover_directit_ai_governance.tex",
    "cover_telus_km_ai.tex",
    "cover_cmhc_data_protection.tex",
    "cover_lawzero_ai_governance.tex",
    "cover_cmhc_data_steward.tex"
)

function Compile-CVs {
    $cmds = ($CVs | ForEach-Object { "lualatex -interaction=nonstopmode $_" }) -join " && "
    $script = "cd /workspace/cv && $cmds"
    Write-Host "Compiling CVs..." -ForegroundColor Cyan
    docker run --rm -v "${MountPath}:/workspace" $Image bash -c $script
}

function Compile-Covers {
    $cmds = ($Covers | ForEach-Object { "xelatex -interaction=nonstopmode $_" }) -join " && "
    $script = "cd /workspace/cover_letters && $cmds"
    Write-Host "Compiling cover letters..." -ForegroundColor Cyan
    docker run --rm -v "${MountPath}:/workspace" $Image bash -c $script
}

function Compile-One {
    param([string]$File, [string]$Dir, [string]$Compiler)
    $script = "cd /workspace/$Dir && $Compiler -interaction=nonstopmode $File"
    Write-Host "Compiling $File..." -ForegroundColor Cyan
    docker run --rm -v "${MountPath}:/workspace" $Image bash -c $script
}

switch ($Target.ToLower()) {
    "all" {
        Compile-CVs
        Compile-Covers
    }
    "cv" {
        Compile-CVs
    }
    "covers" {
        Compile-Covers
    }
    "directit" {
        Compile-One "main_directit.tex" "cv" "lualatex"
        Compile-One "cover_directit_ai_governance.tex" "cover_letters" "xelatex"
    }
    "telus" {
        Compile-One "main_telus.tex" "cv" "lualatex"
        Compile-One "cover_telus_km_ai.tex" "cover_letters" "xelatex"
    }
    "cmhc" {
        Compile-One "main_cmhc.tex" "cv" "lualatex"
        Compile-One "cover_cmhc_data_protection.tex" "cover_letters" "xelatex"
    }
    "lawzero" {
        Compile-One "main_lawzero.tex" "cv" "lualatex"
        Compile-One "cover_lawzero_ai_governance.tex" "cover_letters" "xelatex"
    }
    "cmhc-steward" {
        Compile-One "main_cmhc_steward.tex" "cv" "lualatex"
        Compile-One "cover_cmhc_data_steward.tex" "cover_letters" "xelatex"
    }
    default {
        Write-Host "Unknown target: $Target. Use: all, cv, covers, directit, telus, cmhc, lawzero, cmhc-steward" -ForegroundColor Red
        exit 1
    }
}

Write-Host ""
Write-Host "Done. PDFs:" -ForegroundColor Green
Get-ChildItem "$ProjectRoot\cv\*.pdf", "$ProjectRoot\cover_letters\*.pdf" -ErrorAction SilentlyContinue |
    Select-Object Name, @{N='KB';E={[math]::Round($_.Length/1KB)}} |
    Format-Table -AutoSize

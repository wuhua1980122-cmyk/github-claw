# claw-agent 技能包安装脚本
# 用法: powershell -ExecutionPolicy Bypass -File install.ps1

$targetDir = "$env:USERPROFILE\.claw-agent"
$repoUrl = "https://github.com/wuhua1980122-cmyk/github-claw.git"

Write-Host "=== 🦞 Claw Agent 技能包安装 ===" -ForegroundColor Cyan
Write-Host "目标目录: $targetDir"

# 检查是否已安装
if (Test-Path $targetDir) {
    $choice = Read-Host "已检测到安装目录，是否覆盖? (y/n)"
    if ($choice -ne 'y') {
        Write-Host "安装已取消" -ForegroundColor Yellow
        exit
    }
    Remove-Item $targetDir -Recurse -Force
}

# 克隆仓库
Write-Host "正在从 $repoUrl 克隆..." -ForegroundColor Green
git clone $repoUrl $targetDir

if ($LASTEXITCODE -ne 0) {
    Write-Host "克隆失败，请检查网络连接" -ForegroundColor Red
    exit 1
}

# 创建符号链接或复制到 workspace
$workspace = Get-Location
Write-Host "安装完成！" -ForegroundColor Green
Write-Host "技能位置: $targetDir\agents\skills\" -ForegroundColor Yellow
Write-Host ""
Write-Host "使用方法:" -ForegroundColor Cyan
Write-Host "1. 在仓库页打开 Copilot Chat" -ForegroundColor White
Write-Host "2. 说 '安装 website-optimizer 技能' 或 'SEO 审计' 来激活对应技能" -ForegroundColor White
Write-Host "3. 查看 skills.json 获取完整技能清单" -ForegroundColor White
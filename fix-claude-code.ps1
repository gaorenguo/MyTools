# Claude Code Exit Code 3 Fix Script
# Run this script as Administrator

Write-Host "==================================" -ForegroundColor Cyan
Write-Host "Claude Code Exit Code 3 Fix" -ForegroundColor Cyan
Write-Host "==================================" -ForegroundColor Cyan
Write-Host ""

# Step 1: Add Windows Defender Exclusions
Write-Host "[Step 1/4] Adding Windows Defender exclusions..." -ForegroundColor Yellow
try {
    Add-MpPreference -ExclusionPath "$env:USERPROFILE\.vscode"
    Add-MpPreference -ExclusionPath "$env:APPDATA\Code"
    Add-MpPreference -ExclusionPath "$env:LOCALAPPDATA\Programs\Microsoft VS Code"
    Write-Host "✓ Defender exclusions added successfully" -ForegroundColor Green
} catch {
    Write-Host "⚠ Failed to add exclusions (you may need to run as Administrator)" -ForegroundColor Red
    Write-Host "  Error: $($_.Exception.Message)" -ForegroundColor Red
}

Write-Host ""

# Step 2: Close VSCode
Write-Host "[Step 2/4] Checking for running VSCode processes..." -ForegroundColor Yellow
$vscodeProcesses = Get-Process -Name "Code" -ErrorAction SilentlyContinue
if ($vscodeProcesses) {
    Write-Host "⚠ VSCode is currently running. Please close VSCode manually and press Enter to continue..." -ForegroundColor Yellow
    Read-Host
} else {
    Write-Host "✓ No running VSCode processes found" -ForegroundColor Green
}

Write-Host ""

# Step 3: Remove corrupted extension
Write-Host "[Step 3/4] Removing corrupted Claude Code extension..." -ForegroundColor Yellow
$extensionPath = "$env:USERPROFILE\.vscode\extensions\anthropic.claude-code-2.0.13-win32-x64"
if (Test-Path $extensionPath) {
    try {
        Remove-Item -Path $extensionPath -Recurse -Force
        Write-Host "✓ Extension removed successfully" -ForegroundColor Green
    } catch {
        Write-Host "⚠ Failed to remove extension" -ForegroundColor Red
        Write-Host "  Error: $($_.Exception.Message)" -ForegroundColor Red
    }
} else {
    Write-Host "ℹ Extension directory not found (may already be removed)" -ForegroundColor Cyan
}

# Clean extension cache
Write-Host "  Cleaning extension cache..." -ForegroundColor Yellow
$cacheLocations = @(
    "$env:APPDATA\Code\User\globalStorage\anthropic.claude-code",
    "$env:APPDATA\Code\CachedExtensions"
)

foreach ($cache in $cacheLocations) {
    if (Test-Path $cache) {
        try {
            Remove-Item -Path $cache -Recurse -Force -ErrorAction SilentlyContinue
            Write-Host "  ✓ Cleaned: $cache" -ForegroundColor Green
        } catch {
            Write-Host "  ⚠ Could not clean: $cache" -ForegroundColor Yellow
        }
    }
}

Write-Host ""

# Step 4: Instructions for reinstallation
Write-Host "[Step 4/4] Ready for reinstallation" -ForegroundColor Yellow
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Cyan
Write-Host "  1. Open VSCode" -ForegroundColor White
Write-Host "  2. Go to Extensions (Ctrl+Shift+X)" -ForegroundColor White
Write-Host "  3. Search for 'Claude Code'" -ForegroundColor White
Write-Host "  4. Click Install" -ForegroundColor White
Write-Host "  5. Restart VSCode" -ForegroundColor White
Write-Host "  6. Click the Claude Code icon to test" -ForegroundColor White
Write-Host ""
Write-Host "==================================" -ForegroundColor Cyan
Write-Host "Fix script completed!" -ForegroundColor Green
Write-Host "==================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Press Enter to exit..."
Read-Host
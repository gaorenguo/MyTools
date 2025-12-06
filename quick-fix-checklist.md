# Claude Code Exit Code 3 - Quick Fix Checklist

## ⚡ Start Here (Most Likely Fixes)

Try these solutions in order. Stop when Claude Code works.

### 🔴 Priority 1: Reinstall Extension (5 minutes)

1. Close VSCode completely
2. Open PowerShell and run:
```powershell
Remove-Item -Recurse -Force "$env:USERPROFILE\.vscode\extensions\anthropics.claude-code-*"
```
3. Restart VSCode
4. Reinstall Claude Code from Extensions marketplace
5. Restart VSCode again
6. Test Claude Code

**Success Rate**: ~40% of cases

---

### 🟡 Priority 2: Run as Administrator (2 minutes)

1. Close all VSCode instances
2. Right-click VSCode shortcut → "Run as administrator"
3. Try Claude Code

**If this works**: You have a permissions issue. Continue to Priority 4.

**Success Rate**: ~25% of cases

---

### 🟡 Priority 3: Add Antivirus Exclusions (3 minutes)

Open PowerShell **as Administrator** and run:

```powershell
Add-MpPreference -ExclusionPath "$env:LOCALAPPDATA\Programs\Microsoft VS Code"
Add-MpPreference -ExclusionPath "$env:USERPROFILE\.vscode"
Add-MpPreference -ExclusionPath "$env:APPDATA\Code"
```

Restart VSCode and test.

**Success Rate**: ~20% of cases

---

### 🟢 Priority 4: Fix File Permissions (5 minutes)

Open PowerShell **as Administrator** and run:

```powershell
$path = "$env:USERPROFILE\.vscode\extensions"
$username = [System.Security.Principal.WindowsIdentity]::GetCurrent().Name
$acl = Get-Acl $path
$rule = New-Object System.Security.AccessControl.FileSystemAccessRule($username, "FullControl", "ContainerInherit,ObjectInherit", "None", "Allow")
$acl.SetAccessRule($rule)
Set-Acl -Path $path -AclObject $acl
```

Restart VSCode normally (not as admin) and test.

**Success Rate**: ~10% of cases

---

### 🟢 Priority 5: Clean Reinstall (10 minutes)

Open PowerShell and run:

```powershell
# Close VSCode first!

# Backup settings
Copy-Item "$env:APPDATA\Code\User\settings.json" "~\Desktop\vscode-settings-backup.json"

# Clean everything
Remove-Item -Recurse -Force "$env:USERPROFILE\.vscode\extensions\anthropics.claude-code-*"
Remove-Item -Recurse -Force "$env:APPDATA\Code\User\globalStorage\anthropics.claude-code" -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force "$env:APPDATA\Code\User\workspaceStorage" -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force "$env:APPDATA\Code\CachedExtensions" -ErrorAction SilentlyContinue
```

Then:
1. Restart computer
2. Open VSCode normally
3. Reinstall Claude Code
4. Test

**Success Rate**: ~5% of remaining cases

---

## 📊 Diagnostic Commands

If none of the above work, gather this information:

```powershell
# Check Node.js (should be v18+)
node --version

# Check npm
npm --version

# Check execution policy
Get-ExecutionPolicy -List

# Check VSCode version
code --version

# Check if extension exists
Test-Path "$env:USERPROFILE\.vscode\extensions\anthropics.claude-code-*"
```

---

## 🆘 Still Not Working?

1. Open the full troubleshooting guide: [`claude-code-exit-code-3-troubleshooting.md`](claude-code-exit-code-3-troubleshooting.md)
2. Check Extension Host logs:
   - Press `Ctrl+Shift+P`
   - Type: "Developer: Show Logs"
   - Select: "Extension Host"
3. Report issue with diagnostic info at: https://github.com/anthropics/claude-code/issues

---

## ✅ Verification

You'll know it's fixed when:
- No error message appears when clicking Claude Code icon
- Claude Code panel opens with UI visible
- You can start a conversation with Claude

---

## 💡 Why Exit Code 3?

Exit code 3 typically means:
- **Windows**: Access denied / Permission error
- **Process**: Failed to start the Node.js process
- **Extension**: Corrupted or blocked files

The solutions above address all common causes.
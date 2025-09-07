# 🛡️ Branch Protection Configuration

## Empfohlene Einstellungen für main-Branch

### Basis-Schutz
- ✅ **Require a pull request before merging**
  - Required approving reviews: `1`
  - Dismiss stale PR approvals when new commits are pushed: `✅`
  - Require review from code owners: `❌` (für Solo-Entwicklung)

### Status Checks
- ✅ **Require status checks to pass before merging**
  - Require branches to be up to date before merging: `✅`
  - Required status checks:
    - `test (3.9)`
    - `test (3.10)`
    - `test (3.11)`
    - `test (3.12)`

### Erweiterte Einstellungen
- ✅ **Require conversation resolution before merging**
- ❌ **Require signed commits** (optional)
- ❌ **Include administrators** (für Solo-Entwicklung)
- ❌ **Allow force pushes**
- ❌ **Allow deletions**

## Nach der Aktivierung

### Neuer Workflow:
```bash
# 1. Feature-Branch erstellen
git checkout -b feature/neue-funktion

# 2. Änderungen machen und committen
git add .
git commit -m "feat: neue funktion"

# 3. Branch pushen
git push origin feature/neue-funktion

# 4. Pull Request über GitHub UI erstellen

# 5. CI/CD Tests abwarten (automatisch)

# 6. PR mergen über GitHub UI

# 7. Feature-Branch wird automatisch gelöscht
```

### Vorteile:
- 🛡️ **Schutz vor kaputten Commits** auf main
- 🧪 **Automatische Tests** vor jedem Merge
- 📝 **Dokumentierte Änderungen** durch PR-Beschreibungen
- 🔄 **Einfaches Rollback** bei Problemen
- 👥 **Teamwork-ready** für zukünftige Mitarbeiter

## Testen der Branch Protection

Nach der Aktivierung:
1. Versuche direkt auf main zu pushen → sollte blockiert werden
2. Erstelle einen Test-PR → sollte funktionieren
3. Merge den PR → sollte nach erfolgreichen Tests funktionieren

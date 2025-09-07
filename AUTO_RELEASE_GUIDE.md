# Automatische Releases bei Git Push

Dieses Dokument erklärt, wie Sie automatisch Releases erstellen können, einfach durch das Pushen von Commits mit bestimmten Nachrichten.

## 🚀 Verfügbare Workflows

### 1. Semantic Release (empfohlen)
Verwendet Conventional Commits für vollautomatische Releases.

### 2. Simple Auto Release
Reagiert auf spezielle Commit-Messages und Tags.

## 📝 Commit-Message Patterns

### Semantic Release (Conventional Commits)

```bash
# Patch Release (1.2.3 → 1.2.4) - Bug-Fixes
git commit -m "fix: behebe Problem mit Datei-Speicherung"
git commit -m "fix(ui): korrigiere Button-Layout"

# Minor Release (1.2.3 → 1.3.0) - Neue Features
git commit -m "feat: füge neue Export-Funktion hinzu"
git commit -m "feat(editor): implementiere Syntax-Highlighting"

# Major Release (1.2.3 → 2.0.0) - Breaking Changes
git commit -m "feat!: ändere API-Struktur komplett"
git commit -m "feat: neue UI

BREAKING CHANGE: Die alte UI ist nicht mehr verfügbar"
```

### Simple Auto Release

```bash
# Patch Release
git commit -m "fix: behebe kritischen Bug [release]"
git commit -m "Beliebiger Text [release]"

# Minor Release
git commit -m "Neue Funktion hinzugefügt [minor]"

# Major Release  
git commit -m "Große Änderungen [major]"
```

## 🔄 Workflow-Ablauf

### Bei jedem Push auf `main`:

1. **Commit-Analyse** → System prüft Commit-Messages
2. **Version berechnen** → Neue Versionsnummer wird ermittelt
3. **Dateien aktualisieren** → VERSION, pyproject.toml, __version__.py
4. **Tag erstellen** → Git-Tag wird automatisch erstellt
5. **Release erstellen** → GitHub Release mit Artefakten
6. **Build-Prozess** → Python-Pakete und Flatpak werden gebaut
7. **PyPI-Upload** → Automatische Veröffentlichung auf https://pypi.org/project/bash-script-maker/

## 📋 Beispiele für die Praxis

### Bug-Fix Release
```bash
git add .
git commit -m "fix: behebe Absturz beim Speichern großer Dateien"
git push origin main
# → Automatischer Patch-Release (z.B. 1.2.3 → 1.2.4)
```

### Feature Release
```bash
git add .
git commit -m "feat: füge Dark Mode hinzu"
git push origin main
# → Automatischer Minor-Release (z.B. 1.2.3 → 1.3.0)
```

### Breaking Change
```bash
git add .
git commit -m "feat!: neue Plugin-API

BREAKING CHANGE: Alte Plugins sind nicht mehr kompatibel"
git push origin main
# → Automatischer Major-Release (z.B. 1.2.3 → 2.0.0)
```

### Manueller Release-Trigger
```bash
git add .
git commit -m "Verschiedene Verbesserungen [release]"
git push origin main
# → Automatischer Patch-Release
```

## 🎯 Commit-Types und ihre Bedeutung

| Type | Release | Beschreibung | Beispiel |
|------|---------|--------------|----------|
| `fix:` | Patch | Bug-Fixes | `fix: behebe Speicher-Leak` |
| `feat:` | Minor | Neue Features | `feat: füge Export-Funktion hinzu` |
| `feat!:` | Major | Breaking Changes | `feat!: neue API-Struktur` |
| `docs:` | Kein | Dokumentation | `docs: aktualisiere README` |
| `style:` | Kein | Code-Formatierung | `style: formatiere mit black` |
| `refactor:` | Kein | Code-Refactoring | `refactor: vereinfache Parser` |
| `test:` | Kein | Tests | `test: füge Unit-Tests hinzu` |
| `chore:` | Kein | Wartung | `chore: aktualisiere Dependencies` |

## 🛠️ Konfiguration

### Workflow aktivieren/deaktivieren

```bash
# Semantic Release deaktivieren
mv .github/workflows/semantic-release.yml .github/workflows/semantic-release.yml.disabled

# Simple Auto Release deaktivieren  
mv .github/workflows/auto-release-on-push.yml .github/workflows/auto-release-on-push.yml.disabled
```

### PyPI-Integration einrichten

1. **PyPI API Token erstellen:**
   - https://pypi.org/manage/account/token/

2. **GitHub Secret hinzufügen:**
   - Repository Settings → Secrets → `PYPI_API_TOKEN`

## 🚫 Releases überspringen

```bash
# Commit ohne Release
git commit -m "fix: kleine Korrektur [skip ci]"

# Oder für Semantic Release
git commit -m "docs: aktualisiere README"  # docs löst keinen Release aus
```

## 📊 Monitoring und Debugging

### GitHub Actions überwachen
```
https://github.com/securebitsorg/bash-script-maker/actions
```

### Workflow-Logs prüfen
1. Gehen Sie zu Actions
2. Wählen Sie den fehlgeschlagenen Workflow
3. Klicken Sie auf den Job für Details

### Häufige Probleme

#### Problem: Release wird nicht erstellt
**Lösung:**
- Überprüfen Sie die Commit-Message
- Stellen Sie sicher, dass der Push auf `main` erfolgt
- Prüfen Sie die Workflow-Logs

#### Problem: PyPI-Upload fehlgeschlagen
**Lösung:**
- Überprüfen Sie das `PYPI_API_TOKEN` Secret
- Version könnte bereits auf PyPI existieren

#### Problem: Flatpak-Build fehlschlägt
**Lösung:**
- Überprüfen Sie `bash_script_maker_flatpak.py`
- Prüfen Sie die Flatpak-Manifest-Syntax

## 🔧 Erweiterte Konfiguration

### Custom Release-Rules
Bearbeiten Sie `.releaserc.json` für Semantic Release:

```json
{
  "branches": ["main"],
  "plugins": [
    [
      "@semantic-release/commit-analyzer",
      {
        "releaseRules": [
          {"type": "docs", "scope": "README", "release": "patch"},
          {"type": "refactor", "release": "patch"},
          {"scope": "no-release", "release": false}
        ]
      }
    ]
  ]
}
```

### Workflow-Anpassungen
Bearbeiten Sie `.github/workflows/semantic-release.yml` oder `.github/workflows/auto-release-on-push.yml` nach Ihren Bedürfnissen.

## 📝 Best Practices

1. **Konsistente Commit-Messages** verwenden
2. **Ein Feature pro Commit** für saubere Release-Notes
3. **Tests vor dem Push** ausführen
4. **Breaking Changes klar kennzeichnen**
5. **Release-Notes im CHANGELOG** pflegen

## 🎉 Zusammenfassung

Mit diesen Workflows können Sie:
- ✅ **Automatische Releases** bei jedem Push
- ✅ **Semantic Versioning** basierend auf Commits
- ✅ **Professionelle Release-Notes**
- ✅ **Multi-Format Builds** (Python, Flatpak)
- ✅ **PyPI-Integration**
- ✅ **Null manueller Aufwand**

**Einfach committen und pushen - der Rest passiert automatisch! 🚀**

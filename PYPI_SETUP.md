# PyPI Automatische Veröffentlichung

Dieses Dokument beschreibt, wie Sie die automatische Veröffentlichung auf PyPI einrichten.

## 🔑 PyPI API Token einrichten

### 1. PyPI Account erstellen
- Gehen Sie zu: https://pypi.org/account/register/
- Erstellen Sie einen Account falls noch nicht vorhanden
- **Wichtig**: Aktivieren Sie 2FA (Two-Factor Authentication)

### 2. API Token erstellen
1. **Login bei PyPI**: https://pypi.org/account/login/
2. **Token-Seite**: https://pypi.org/manage/account/token/
3. **Neues Token**:
   - Klicken Sie "Add API token"
   - **Token name**: `bash-script-maker-github-actions`
   - **Scope**: `Entire account` (empfohlen für den Start)
   - Klicken Sie "Add token"
4. **Token kopieren**: 
   - ⚠️ **WICHTIG**: Kopieren Sie das Token SOFORT
   - Format: `pypi-AgEIcHlwaS5vcmcC...` (beginnt mit `pypi-`)
   - Sie können es später nicht mehr einsehen!

### 3. GitHub Secret hinzufügen
1. **Repository Settings**: https://github.com/securebitsorg/bash-script-maker/settings/secrets/actions
2. **Neues Secret**:
   - Klicken Sie "New repository secret"
   - **Name**: `PYPI_API_TOKEN`
   - **Secret**: Ihr komplettes PyPI Token
   - Klicken Sie "Add secret"

## 🚀 Automatische Veröffentlichung

### Wann wird veröffentlicht?

**Automatisch bei jedem Release** (alle Workflows):
- ✅ **Semantic Release**: Bei `feat:` und `fix:` Commits
- ✅ **Auto Release on Push**: Bei `[release]`, `[minor]`, `[major]` Tags
- ✅ **Manual Release**: Bei Tag-Erstellung

### Was wird veröffentlicht?

- **Source Distribution** (`.tar.gz`)
- **Wheel** (`.whl`) - für schnelle Installation
- **Automatische Metadaten** aus `setup.py` und `pyproject.toml`

## 📋 Workflow-Details

### Semantic Release Workflow
```yaml
publish-pypi:
  name: Publish to PyPI
  needs: [release, build-and-upload]
  runs-on: ubuntu-latest
  if: needs.release.outputs.new_release_published == 'true' && !contains(needs.release.outputs.new_release_version, '-')
  
  steps:
    - name: Build packages
      run: python setup.py sdist bdist_wheel
      
    - name: Publish to PyPI
      uses: pypa/gh-action-pypi-publish@release/v1
      with:
        password: ${{ secrets.PYPI_API_TOKEN }}
        skip-existing: true
```

### Bedingungen für PyPI-Upload

- ✅ **Release wurde erstellt** (`new_release_published == 'true'`)
- ✅ **Keine Pre-Release Version** (keine `-alpha`, `-beta`, `-rc`)
- ✅ **PyPI Token ist verfügbar** (`PYPI_API_TOKEN` Secret)
- ✅ **Build erfolgreich** (alle vorherigen Jobs erfolgreich)

## 🧪 Testen der Konfiguration

### Test 1: Lokaler Build
```bash
# Pakete lokal bauen
python setup.py sdist bdist_wheel

# Prüfen der Artefakte
ls -la dist/
```

### Test 2: TestPyPI (Optional)
Für Tests können Sie zuerst TestPyPI verwenden:

1. **TestPyPI Token**: https://test.pypi.org/manage/account/token/
2. **GitHub Secret**: `TEST_PYPI_API_TOKEN`
3. **Temporärer Test-Upload**:
```bash
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```

### Test 3: Release erstellen
```bash
# Minor Release (neue Features)
git commit -m "feat: neue Funktion für PyPI-Test"
git push origin main
# → Automatischer Release + PyPI Upload

# Patch Release (Bug-Fixes)
git commit -m "fix: kleiner Bugfix für PyPI-Test"
git push origin main
# → Automatischer Release + PyPI Upload
```

## 📊 Monitoring

### PyPI Projekt-Seite
Nach dem ersten Upload verfügbar unter:
- **Projekt**: https://pypi.org/project/bash-script-maker/
- **Statistiken**: https://pypistats.org/packages/bash-script-maker

### GitHub Actions
- **Workflows**: https://github.com/securebitsorg/bash-script-maker/actions
- **Logs**: Klicken Sie auf einen Workflow → "publish-pypi" Job

### Installation testen
```bash
# Nach dem Upload
pip install bash-script-maker

# Spezifische Version
pip install bash-script-maker==1.3.1

# Upgrade
pip install --upgrade bash-script-maker
```

## 🔧 Erweiterte Konfiguration

### Projekt-spezifisches Token (Empfohlen nach erstem Upload)

Nach dem ersten erfolgreichen Upload:

1. **PyPI Projekt-Seite**: https://pypi.org/project/bash-script-maker/
2. **Settings** → **Manage** → **Publishing**
3. **Neues Token**:
   - **Scope**: `Project: bash-script-maker`
   - **Name**: `bash-script-maker-github-actions-project`
4. **GitHub Secret aktualisieren**: Ersetzen Sie `PYPI_API_TOKEN`

### Trusted Publishing (Moderne Alternative)

PyPI unterstützt auch "Trusted Publishing" ohne Token:

```yaml
# .github/workflows/semantic-release.yml
- name: Publish to PyPI
  uses: pypa/gh-action-pypi-publish@release/v1
  with:
    # Kein password nötig mit Trusted Publishing
```

Setup: https://docs.pypi.org/trusted-publishers/

## 🚨 Sicherheit

### Best Practices

- ✅ **2FA aktivieren** auf PyPI
- ✅ **Projekt-spezifische Tokens** verwenden
- ✅ **Regelmäßig Tokens rotieren**
- ✅ **Logs überwachen** für unerwartete Uploads
- ✅ **Skip-existing** verwenden um Fehler zu vermeiden

### Token-Sicherheit

- 🔒 **Niemals Token committen** in Git
- 🔒 **Nur GitHub Secrets** verwenden
- 🔒 **Bei Kompromittierung sofort widerrufen**
- 🔒 **Minimale Berechtigungen** (projekt-spezifisch)

## 📝 Troubleshooting

### Häufige Probleme

#### Problem: "Invalid or non-existent authentication information"
**Lösung**: 
- Prüfen Sie das `PYPI_API_TOKEN` Secret
- Token muss mit `pypi-` beginnen
- Token könnte abgelaufen sein

#### Problem: "File already exists"
**Lösung**:
- `skip-existing: true` ist bereits konfiguriert
- Version könnte bereits auf PyPI existieren
- Prüfen Sie: https://pypi.org/project/bash-script-maker/

#### Problem: "Invalid distribution metadata"
**Lösung**:
- Prüfen Sie `setup.py` und `pyproject.toml`
- Lokalen Build testen: `python setup.py check`

### Debug-Informationen

```bash
# Lokale Validierung
python setup.py check --strict
twine check dist/*

# Upload-Simulation
twine upload --dry-run dist/*
```

## 🎉 Zusammenfassung

Nach der Einrichtung:

1. **Automatische Uploads** bei jedem Release
2. **Professionelle Paketverteilung** über PyPI
3. **Einfache Installation** für Benutzer: `pip install bash-script-maker`
4. **Versionsverwaltung** synchron mit Git-Tags
5. **Null manueller Aufwand** - vollautomatisch!

**Einfach committen, pushen - PyPI-Upload passiert automatisch! 🚀**

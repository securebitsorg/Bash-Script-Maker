# Release-Prozess für Bash-Script-Maker

Dieses Dokument beschreibt den automatisierten Release-Prozess für Bash-Script-Maker.

## Automatischer Release-Prozess

### Übersicht

Der Release-Prozess wird durch GitHub Actions automatisiert und wird ausgelöst, wenn ein neuer Git-Tag erstellt wird.

### Workflow-Schritte

1. **Tag erstellen** → Automatischer Release wird gestartet
2. **GitHub Release** → Release-Seite wird erstellt
3. **Build-Artefakte** → Python-Pakete und Flatpak werden gebaut
4. **Upload** → Alle Dateien werden zum Release hinzugefügt
5. **PyPI** → Automatische Veröffentlichung auf PyPI (optional)
6. **CHANGELOG** → Automatische Aktualisierung

## Release erstellen

### Methode 1: Automatisch bei Git Push (Neu! 🚀)

**Einfach committen und pushen - Release passiert automatisch:**

```bash
# Bug-Fix → Patch Release (1.2.3 → 1.2.4)
git commit -m "fix: behebe kritischen Fehler"
git push origin main

# Feature → Minor Release (1.2.3 → 1.3.0)  
git commit -m "feat: füge neue Export-Funktion hinzu"
git push origin main

# Breaking Change → Major Release (1.2.3 → 2.0.0)
git commit -m "feat!: neue API-Struktur"
git push origin main
```

**Verfügbare Workflows:**
- **Semantic Release**: Basiert auf Conventional Commits
- **Simple Auto Release**: Reagiert auf `[release]`, `[minor]`, `[major]` Tags

Siehe: [AUTO_RELEASE_GUIDE.md](./AUTO_RELEASE_GUIDE.md)

### Methode 2: Helper-Script

```bash
# Interaktiv - wählen Sie die Art des Releases
./create_release.sh

# Oder direkt mit Version
./create_release.sh 1.2.3
```

Das Script:
- Aktualisiert alle Versionsdateien
- Erstellt einen Commit
- Erstellt und pusht den Tag
- Startet automatisch den Release-Prozess

### Methode 3: Manuell

```bash
# 1. Version in allen Dateien aktualisieren
echo "1.2.3" > VERSION
# Aktualisiere auch __version__.py und pyproject.toml

# 2. Änderungen committen
git add .
git commit -m "chore: bump version to 1.2.3"

# 3. Tag erstellen und pushen
git tag -a v1.2.3 -m "Release version 1.2.3"
git push origin main
git push origin v1.2.3
```

## Release-Artefakte

Jeder Release enthält automatisch:

### 1. Python-Pakete
- `bash-script-maker-X.Y.Z-py3-none-any.whl` (Wheel)
- `bash-script-maker-X.Y.Z.tar.gz` (Source Distribution)

### 2. Flatpak-Paket
- `BashScriptMaker-X.Y.Z.flatpak` (Flatpak Bundle)

### 3. Source-Code
- `bash-script-maker-X.Y.Z-source.tar.gz` (Vollständiger Quellcode)

## Release-Notes

Release-Notes werden automatisch aus dem CHANGELOG.md extrahiert:

### CHANGELOG-Format

```markdown
## [Unreleased]

### Added
- Neue Features

### Changed
- Änderungen

### Fixed
- Bug-Fixes

## [1.2.3] - 2024-01-01

### Added
- Feature A
- Feature B

### Fixed
- Bug X
```

### Automatische Extraktion

Der Workflow extrahiert automatisch die Inhalte zwischen `## [X.Y.Z]` und dem nächsten `## [` für die Release-Notes.

## PyPI-Veröffentlichung

### Setup (einmalig)

1. **PyPI API Token erstellen:**
   - Gehen Sie zu https://pypi.org/manage/account/token/
   - Erstellen Sie einen Token für das Projekt

2. **GitHub Secret hinzufügen:**
   - Repository Settings → Secrets and variables → Actions
   - Neues Secret: `PYPI_API_TOKEN` mit dem Token-Wert

### Automatische Veröffentlichung

- Erfolgt automatisch bei stabilen Releases (ohne `-` im Tag)
- Pre-Releases (z.B. `v1.2.3-beta`) werden **nicht** auf PyPI veröffentlicht

## Versionstypen

### Semantic Versioning

- **MAJOR** (1.0.0): Breaking Changes
- **MINOR** (1.1.0): Neue Features (rückwärtskompatibel)
- **PATCH** (1.1.1): Bug-Fixes

### Pre-Releases

- **Alpha**: `v1.2.3-alpha.1`
- **Beta**: `v1.2.3-beta.1`
- **Release Candidate**: `v1.2.3-rc.1`

## Troubleshooting

### Release fehlgeschlagen

1. **Überprüfen Sie die GitHub Actions:**
   ```
   https://github.com/securebitsorg/bash-script-maker/actions
   ```

2. **Häufige Probleme:**
   - PyPI-Token fehlt oder ungültig
   - Versionsnummer bereits auf PyPI vorhanden
   - Build-Fehler in der Anwendung

### Tag löschen und neu erstellen

```bash
# Lokalen Tag löschen
git tag -d v1.2.3

# Remote Tag löschen
git push --delete origin v1.2.3

# Neuen Tag erstellen
git tag -a v1.2.3 -m "Release version 1.2.3"
git push origin v1.2.3
```

## Workflow-Dateien

- `.github/workflows/auto-release.yml` - Hauptworkflow
- `.github/workflows/flatpak-build.yml` - Flatpak-spezifischer Build
- `create_release.sh` - Helper-Script für Releases

## Monitoring

### GitHub Actions Status

Überwachen Sie den Release-Fortschritt:
- https://github.com/securebitsorg/bash-script-maker/actions

### Release-Seite

Alle Releases finden Sie hier:
- https://github.com/securebitsorg/bash-script-maker/releases

### PyPI-Status

Überprüfen Sie die PyPI-Veröffentlichung:
- https://pypi.org/project/bash-script-maker/

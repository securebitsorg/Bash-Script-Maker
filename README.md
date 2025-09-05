# Bash-Script-Maker

Ein benutzerfreundliches GUI-Programm zur Erstellung von Bash-Scripts mit visueller Unterstützung.

[![CI/CD Pipeline](https://github.com/securebitsorg/Bash-Script-Maker/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/securebitsorg/Bash-Script-Maker/actions/workflows/ci-cd.yml)
[![GitHub Release](https://img.shields.io/github/v/release/securebitsorg/Bash-Script-Maker?include_prereleases&sort=semver)](https://github.com/securebitsorg/Bash-Script-Maker/releases)
[![PyPI Version](https://img.shields.io/pypi/v/bash-script-maker)](https://pypi.org/project/bash-script-maker/)
[![Python Versions](https://img.shields.io/pypi/pyversions/bash-script-maker)](https://pypi.org/project/bash-script-maker/)
[![License](https://img.shields.io/github/license/securebitsorg/Bash-Script-Maker)](https://opensource.org/licenses/MIT)
[![GitHub last commit](https://img.shields.io/github/last-commit/securebitsorg/Bash-Script-Maker)](https://github.com/securebitsorg/Bash-Script-Maker/commits/main)
[![Downloads](https://img.shields.io/github/downloads/securebitsorg/Bash-Script-Maker/total)](https://github.com/securebitsorg/Bash-Script-Maker/releases)
[![Issues](https://img.shields.io/github/issues/securebitsorg/Bash-Script-Maker)](https://github.com/securebitsorg/Bash-Script-Maker/issues)

## Features

### Hauptfunktionen
- **Visuelle Script-Erstellung**: Einfache Erstellung von Bash-Scripts durch Drag-and-Drop von Befehlsbausteinen
- **Intelligente Tab-Unterstützung**: Automatische Einrückung mit 4 Leerzeichen (Bash-Standard)
- **Autovervollständigung**: Kontextabhängige Vorschläge für Befehle, Variablen und Pfade
- **Syntax-Highlighting**: Automatische Hervorhebung von Bash-Syntaxelementen
- **Zenity-Integration**: Einfache Integration von Zenity-Dialogen für interaktive Scripts
- **Live-Editor**: Echtzeit-Syntaxhervorhebung während der Eingabe
- **Automatische Formatierung**: Smarte Einrückung basierend auf Bash-Strukturen
- **Script-Ausführung**: Direktes Testen der erstellten Scripts

### Verfügbare Befehlsbausteine

#### Grundlagen
- Shebang-Zeile
- Echo-Befehle
- Eingabe lesen
- Bedingte Anweisungen (if/then/else)
- Schleifen (for/while)
- Case-Anweisungen
- Funktionsdefinitionen

#### Zenity-Dialoge
- Info-Dialoge
- Fehler-Dialoge
- Warnungs-Dialoge
- Frage-Dialoge
- Eingabedialoge
- Dateiauswahl
- Fortschrittsbalken
- Listen-Dialoge

#### Systembefehle
- Dateioperationen (ls, cd, mkdir, rm, cp, mv)
- Berechtigungen (chmod)
- Prozessverwaltung (ps, kill)
- Textverarbeitung (grep, sed, awk)

#### Variablen und Operatoren
- Variablenzuweisung
- String-Operationen
- Array-Operationen
- Vergleichsoperatoren

## Installation

### Voraussetzungen
- Python 3.8 oder höher
- Tkinter (GUI-Bibliothek)
- Zenity (für Dialog-Funktionen)
- Linux-Distribution mit apt, dnf, pacman oder ähnlichem Paketmanager

### Automatische Installation mit Desktop-Integration

**Empfohlene Methode (automatische Erkennung):**
```bash
git clone https://github.com/securebitsorg/bash-script-maker.git
cd bash-script-maker
./install.sh
```

Das Script erkennt automatisch Ihren Paketmanager, installiert alle notwendigen Abhängigkeiten und richtet die Desktop-Integration ein.

**Spezifisch für Distributionen:**

Für Ubuntu/Debian-basierte Systeme:
```bash
./install_apt.sh
```

Für Fedora/RHEL/CentOS-basierte Systeme:
```bash
./install_dnf.sh
```

### Nur Desktop-Integration installieren

Falls Sie die App bereits installiert haben und nur die Desktop-Integration hinzufügen möchten:

```bash
./install_desktop_integration.sh
```

### Manuelle Installation

Wenn die automatischen Scripts nicht funktionieren, installieren Sie die Pakete manuell:

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install python3 python3-tk python3-pip zenity xterm
```

**Fedora/RHEL/CentOS:**
```bash
sudo dnf install python3 python3-tkinter python3-pip zenity xterm
```

**Arch Linux:**
```bash
sudo pacman -S python python-tk python-pip zenity xterm
```

**Andere Distributionen:**
Siehe `packages.txt` für detaillierte Paketlisten.

### Python-Abhängigkeiten
```bash
pip install -r requirements.txt
```

### Überprüfung der Installation

Nach der Installation können Sie testen, ob alles korrekt funktioniert:
```bash
./test_installation.sh
./tools/test_dependencies.py
```

Diese Scripts überprüfen alle Abhängigkeiten und geben detaillierte Informationen über eventuelle Probleme.

### Verfügbare Scripts

Das Projekt enthält folgende Installations- und Hilfsscripts:

- `install.sh` - **Universelles Installationsscript** (empfohlen)
- `install_apt.sh` - Spezifisch für Ubuntu/Debian
- `install_dnf.sh` - Spezifisch für Fedora/RHEL/CentOS
- `test_installation.sh` - Überprüft die Installation
- `tools/test_dependencies.py` - Detaillierte Dependency-Tests
- `tests/test_basic.py` - Pytest-Tests für grundlegende Funktionalität
- `start.sh` - Startet das Programm mit Abhängigkeitsprüfung

Alle Scripts sind ausführbar und können direkt aufgerufen werden.

## Verwendung

### Programm starten

**Über das Anwendungsmenü:**
Nach der Installation finden Sie "Bash-Script-Maker" im Anwendungsmenü Ihrer Desktop-Umgebung.

**Über das Terminal:**
```bash
bash-script-maker
```

**Direkt aus dem Quellcode:**
```bash
python3 bash_script_maker.py
```

### Desktop-Integration

Die App wird automatisch mit einem benutzerdefinierten Icon und Desktop-Integration installiert:
- **Icon**: Ein modernes SVG-Icon mit Terminal-Design
- **Desktop-Datei**: Vollständige Integration in das Anwendungsmenü
- **Kategorien**: Development und Utility
- **Unterstützte Distributionen**: Alle Linux-Distributionen mit Desktop-Umgebung

### Script erstellen
1. Wählen Sie die gewünschten Befehlsbausteine aus der linken Palette
2. Klicken Sie auf einen Baustein, um ihn in den Editor einzufügen
3. Bearbeiten Sie die Parameter nach Bedarf
4. Speichern Sie das Script
5. Testen Sie es mit der Ausführen-Funktion

### Tastenkombinationen
- `Ctrl+N`: Neues Script
- `Ctrl+O`: Script öffnen
- `Ctrl+S`: Script speichern
- `Ctrl+Shift+S`: Script speichern unter
- `Ctrl+Q`: Programm beenden
- `F5`: Script ausführen
- `Ctrl+Z`: Rückgängig
- `Ctrl+Y`: Wiederholen

### Editor-Tastenkombinationen
- `Tab`: Einrücken (aktuelle Zeile oder Auswahl)
- `Shift+Tab`: Ausrücken (aktuelle Zeile oder Auswahl)
- `Ctrl+A`: Alles auswählen
- `Ctrl+D`: Zeile duplizieren
- `Ctrl+/`: Kommentar umschalten
- `Ctrl+Space`: Autovervollständigung anzeigen
- `Ctrl+Tab`: Alternative für Autovervollständigung
- `Enter`: Automatische Einrückung in neuen Zeilen
- `Backspace`: Intelligente Ausrückung bei Tab-Stops
- `Escape`: Vorschlagsliste schließen

### Automatische Formatierung
Der Editor erkennt automatisch Bash-Strukturen und passt die Einrückung an:
- Nach `if`, `then`, `else`, `for`, `while`, `case`, `function` wird eingerückt
- Nach `fi`, `done`, `esac` wird ausgerückt
- Einrückung mit 4 Leerzeichen (Bash-Standard)

### Autovervollständigung
Die intelligente Autovervollständigung bietet kontextabhängige Vorschläge:

#### Unterstützte Vorschlagstypen
- **Bash-Befehle**: ls, cp, mv, grep, sed, awk, find, etc.
- **Bash-Schlüsselwörter**: if, then, else, fi, for, while, function, etc.
- **Variablen**: $HOME, $PATH, $PWD, $USER, benutzerdefinierte Variablen
- **Datei- und Pfadvervollständigung**: Automatische Vervollständigung von Pfaden
- **Befehlsoptionen**: Häufig verwendete Optionen für bekannte Befehle

#### Navigation in Vorschlägen
- `↑/↓`: Zwischen Vorschlägen navigieren
- `Enter/Tab`: Vorschlag übernehmen
- `Escape`: Vorschlagsliste schließen
- `Mausrad`: Durch Liste scrollen

#### Kontextabhängige Vorschläge
- **Am Zeilenanfang**: Alle verfügbaren Befehle und Schlüsselwörter
- **Bei $**: Variablen-Vorschläge
- **Bei Pfaden**: Datei- und Verzeichnisvervollständigung
- **Nach bekannten Befehlen**: Relevante Optionen

## Beispiel-Script

Das Programm erstellt automatisch ein grundlegendes Script-Template:



## Technische Details

- **GUI-Framework**: Tkinter
- **Syntax-Highlighting**: Regex-basierte Mustererkennung
- **Dateiformat**: Reine Bash-Scripts (.sh)
- **Encoding**: UTF-8
- **Plattform**: Linux (aufgrund Zenity-Abhängigkeit)

## CI/CD Pipeline

Dieses Projekt verwendet GitHub Actions für kontinuierliche Integration und automatische Releases.

- **CI/CD Pipeline** (`.github/workflows/ci-cd.yml`):
  - Tests auf Python 3.8-3.12
  - Code-Qualität-Checks (Flake8, Black, MyPy)
  - **Automatische Releases mit semantic-release**
  - Package-Publishing zu PyPI und GitHub Packages
  - Docker-Image-Erstellung
  - Dokumentationsgenerierung
  - Sicherheitsscans (Bandit, Safety)

### Automatische Releases

Das Projekt verwendet [Conventional Commits](https://www.conventionalcommits.org/) für automatische Versionierung:

- `feat:` → Minor Release (1.1.0 → 1.2.0)
- `fix:` → Patch Release (1.1.0 → 1.1.1)
- `BREAKING CHANGE:` → Major Release (1.1.0 → 2.0.0)

**Beispiel-Commits:**
```bash
git commit -m "feat: add new syntax highlighting theme"
git commit -m "fix: resolve tab indentation bug"
git commit -m "docs: update installation instructions"
```

- **Security Scan** (`.github/workflows/security-scan.yml`):
  - Security-Scans mit Bandit und Safety
  - Funktioniert in Forks und Haupt-Repository
  - Keine speziellen Berechtigungen erforderlich

- **Manueller Release** (`.github/workflows/manual-release.yml`):
  - Manuelle Versionserstellung
  - Flexible Release-Notes

### Lokale Entwicklung

#### Pre-commit Hooks einrichten:
```bash
pip install pre-commit
pre-commit install
pre-commit run --all-files
```

#### Tests ausführen:
```bash
tox
# oder spezifische Umgebungen
tox -e py39,lint,type
```

#### Package bauen:
```bash
python -m build
```

#### Tests ausführen:
```bash
# Alle Tests mit Coverage
pytest

# Spezifische Tests
pytest tests/test_basic.py

# Mit Coverage-Bericht
pytest --cov=bash_script_maker --cov=syntax_highlighter --cov-report=html
```

## Mitwirken

Beiträge sind willkommen! Siehe [CONTRIBUTING.md](CONTRIBUTING.md) für detaillierte Anweisungen.

### Schnellstart für Contributors:
1. Fork das Repository
2. `git clone https://github.com/securebitsorg/bash-script-maker.git`
3. `cd bash-script-maker && ./install.sh`
4. `pip install -e ".[dev]"`
5. `pre-commit install`
6. Entwickeln und testen
7. `./init_github.sh` (für automatischen Push)
8. Pull Request erstellen

### Übersetzungen beisteuern

Wir freuen uns über Hilfe bei der Übersetzung des Bash-Script-Makers in neue Sprachen!

**So fügen Sie eine neue Sprache hinzu:**

1.  **Sprach-Code finden:** Finden Sie den zweibuchstabigen ISO 639-1 Code für Ihre Sprache (z.B. `fr` für Französisch).

2.  **Verzeichnis erstellen:** Erstellen Sie ein neues Verzeichnis unter `locales/`. Für Französisch wäre das `locales/fr/LC_MESSAGES/`.

3.  **Übersetzungsdatei erstellen:**
    *   Kopieren Sie die deutsche Vorlagendatei: `cp locales/de/LC_MESSAGES/base.po locales/fr/LC_MESSAGES/base.po`
    *   Öffnen Sie die neue `.po`-Datei mit einem Texteditor oder einem speziellen Tool wie [Poedit](https://poedit.net/).

4.  **Texte übersetzen:**
    *   Gehen Sie die Datei durch und übersetzen Sie alle Texte, die in `msgid "..."` stehen.
    *   Tragen Sie Ihre Übersetzung in das `msgstr "..."`-Feld direkt darunter ein.
    *   **Wichtig:** Lassen Sie Platzhalter wie `{}` unverändert.

    **Beispiel:**
    ```po
    msgid "Datei"
    msgstr "File"

    msgid "Script gespeichert: {}"
    msgstr "Script saved: {}"
    ```

5.  **Übersetzung kompilieren:**
    *   Damit das Programm Ihre Übersetzung nutzen kann, muss sie kompiliert werden. Führen Sie dazu einfach das mitgelieferte Skript aus:
    ```bash
    python compile_translations.py
    ```
    *   Dieses Skript benötigt eventuell die `polib`-Bibliothek. Falls nicht vorhanden, installieren Sie sie mit: `pip install polib`.

6.  **Sprache im Menü hinzufügen:**
    *   Öffnen Sie die Datei `bash_script_maker.py`.
    *   Suchen Sie nach `language_menu`.
    *   Fügen Sie einen neuen Eintrag für Ihre Sprache hinzu, ähnlich wie die bereits vorhandenen für Deutsch und Englisch.

7.  **Pull Request erstellen:** Erstellen Sie einen Pull Request mit Ihren Änderungen, damit wir die neue Sprache in das Projekt aufnehmen können.

Vielen Dank für Ihre Hilfe!

### Repository zu GitHub pushen:
```bash
# Automatisch (empfohlen)
./init_github.sh

# Oder manuell
git add .
git commit -m "Your commit message"
git push
```

## Lizenz

Dieses Projekt steht unter der MIT-Lizenz. Siehe LICENSE-Datei für Details.

## Autor

Erstellt von Marcel Dellmann mit ❤️ für Bash-Script-Enthusiasten\n> Automatisches Release: Testeintrag.

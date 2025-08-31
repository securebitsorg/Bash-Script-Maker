# Bash-Script-Maker

Ein benutzerfreundliches GUI-Programm zur Erstellung von Bash-Scripts mit visueller Unterstützung.

[![CI/CD Pipeline](https://github.com/yourusername/bash-script-maker/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/yourusername/bash-script-maker/actions/workflows/ci-cd.yml)
[![CodeQL Analysis](https://github.com/yourusername/bash-script-maker/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/yourusername/bash-script-maker/actions/workflows/codeql-analysis.yml)
[![PyPI Version](https://img.shields.io/pypi/v/bash-script-maker)](https://pypi.org/project/bash-script-maker/)
[![Python Versions](https://img.shields.io/pypi/pyversions/bash-script-maker)](https://pypi.org/project/bash-script-maker/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

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

### Automatische Installation

**Empfohlene Methode (automatische Erkennung):**
```bash
git clone https://github.com/yourusername/bash-script-maker.git
cd bash-script-maker
./install.sh
```

**Spezifisch für Distributionen:**

Für Ubuntu/Debian-basierte Systeme:
```bash
./install_apt.sh
```

Für Fedora/RHEL/CentOS-basierte Systeme:
```bash
./install_dnf.sh
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
```

Dieses Script überprüft alle Abhängigkeiten und gibt detaillierte Informationen über eventuelle Probleme.

### Verfügbare Scripts

Das Projekt enthält folgende Installations- und Hilfsscripts:

- `install.sh` - **Universelles Installationsscript** (empfohlen)
- `install_apt.sh` - Spezifisch für Ubuntu/Debian
- `install_dnf.sh` - Spezifisch für Fedora/RHEL/CentOS
- `test_installation.sh` - Überprüft die Installation
- `start.sh` - Startet das Programm mit Abhängigkeitsprüfung

Alle Scripts sind ausführbar und können direkt aufgerufen werden.

## Verwendung

### Programm starten
```bash
python bash_script_maker.py
```

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

Dieses Projekt verwendet GitHub Actions für kontinuierliche Integration und Bereitstellung.

> 📖 **Detaillierte Setup-Anleitung**: Siehe [GITHUB_SETUP.md](GITHUB_SETUP.md) für eine Schritt-für-Schritt Anleitung zum Einrichten der GitHub Secrets.

### Automatische Workflows

- **CI/CD Pipeline** (`.github/workflows/ci-cd.yml`):
  - Tests auf Python 3.6-3.11
  - Code-Qualität-Checks (Flake8, Black, MyPy)
  - Automatische Releases
  - Package-Publishing zu PyPI und GitHub Packages
  - Docker-Image-Erstellung
  - Dokumentationsgenerierung

- **CodeQL Security** (`.github/workflows/codeql-analysis.yml`):
  - Wöchentliche Security-Scans
  - Automatische Schwachstellenerkennung

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

## Mitwirken

Beiträge sind willkommen! Siehe [CONTRIBUTING.md](CONTRIBUTING.md) für detaillierte Anweisungen.

### Schnellstart für Contributors:
1. Fork das Repository
2. `git clone https://github.com/YOUR_USERNAME/bash-script-maker.git`
3. `cd bash-script-maker && ./install.sh`
4. `pip install -e ".[dev]"`
5. `pre-commit install`
6. Entwickeln und testen
7. `./init_github.sh` (für automatischen Push)
8. Pull Request erstellen

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

Erstellt von Marcel Dellmann mit ❤️ für Bash-Script-Enthusiasten
# Contributing to Bash-Script-Maker

Danke, dass du zu Bash-Script-Maker beitragen möchtest! Wir freuen uns über alle Beiträge, die unser Projekt verbessern.

## Entwicklungsumgebung einrichten

### Voraussetzungen
- Python 3.6+
- Git
- Linux-System (für Tkinter und Zenity)

### Einrichtung
1. Fork das Repository
2. Klonen Sie Ihren Fork:
   ```bash
   git clone https://github.com/securebitsorg/bash-script-maker.git
   cd bash-script-maker
   ```

3. Installieren Sie Abhängigkeiten:
   ```bash
   pip install -e ".[dev]"
   ```

4. Installieren Sie Pre-commit Hooks:
   ```bash
   pip install pre-commit
   pre-commit install
   ```

## Entwicklungsworkflow

### 1. Branch erstellen
```bash
git checkout -b feature/your-feature-name
# oder
git checkout -b fix/issue-number
```

### 2. Code schreiben
- Folge dem bestehenden Code-Stil
- Schreibe aussagekräftige Commit-Nachrichten
- Teste deine Änderungen

### 3. Pre-commit Checks
```bash
pre-commit run --all-files
```

### 4. Tests ausführen
```bash
tox
# oder spezifische Tests
tox -e py39,lint,type
```

### 5. Pull Request erstellen
- Pushen deinen Branch
- Erstelle einen Pull Request auf GitHub
- Beschreibe deine Änderungen detailliert

## Code-Standards

### Python
- Verwende **Black** für die Code-Formatierung
- Folge PEP 8
- Verwende Type Hints wo möglich
- Schreibe Docstrings für alle öffentlichen Funktionen

### Git Commits
- Verwende prägnante, beschreibende Commit-Nachrichten
- Beginne mit einem Verb (Add, Fix, Update, Remove)
- Referenziere Issues mit `#issue-number`

Beispiele:
```
feat: add autocomplete for bash commands
fix: resolve tab indentation bug in editor
docs: update installation instructions
```

### Branch-Namen
- Features: `feature/feature-name`
- Bugfixes: `fix/issue-number`
- Hotfixes: `hotfix/issue-number`
- Dokumentation: `docs/topic`

## Testen

### Unit Tests
```bash
pytest
```

### Integration Tests
```bash
python -c "import bash_script_maker; import syntax_highlighter"
```

### Linting und Type Checking
```bash
flake8 bash_script_maker.py syntax_highlighter.py
mypy bash_script_maker.py syntax_highlighter.py
black --check bash_script_maker.py syntax_highlighter.py
```

## Dokumentation

### Code-Dokumentation
- Verwende Docstrings im Google-Style
- Dokumentiere alle Parameter, Rückgabewerte und Ausnahmen
- Halte Kommentare auf Englisch

### Projekt-Dokumentation
- Aktualisiere die README.md bei neuen Features
- Füge Änderungen zu CHANGELOG.md hinzu
- Aktualisiere diese CONTRIBUTING.md bei Bedarf

## Releases

Releases werden automatisch über GitHub Actions erstellt:

### Patch Release (z.B. 1.0.1)
```bash
git tag v1.0.1
git push origin v1.0.1
```

### Minor Release (z.B. 1.1.0)
```bash
git tag v1.1.0
git push origin v1.1.0
```

### Major Release (z.B. 2.0.0)
```bash
git tag v2.0.0
git push origin v2.0.0
```

## Sicherheit

- Melde Sicherheitslücken nicht öffentlich!!!
- Kontaktiere die Maintainers direkt
- Verwende keine unsicheren Abhängigkeiten
- Führe einen Security-Scans durch: `bandit -r .`

## Lizenz

Durch das Beitragen zu diesem Projekt stimmst du zu, dass deine Beiträge unter der MIT-Lizenz stehen.

## Fragen?

Bei Fragen:
- Öffnen einen [GitHub Issue](https://github.com/securebitsorg/bash-script-maker/issues)
- Schreibe in [GitHub Discussions](https://github.com/securebitsorg/bash-script-maker/discussions)
- Kontaktiere die Maintainers

Vielen Dank für deinen Beitrag! 🚀

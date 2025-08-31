# Contributing to Bash-Script-Maker

Danke, dass Sie zu Bash-Script-Maker beitragen möchten! Wir freuen uns über alle Beiträge, die unser Projekt verbessern.

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
- Folgen Sie dem bestehenden Code-Stil
- Schreiben Sie aussagekräftige Commit-Nachrichten
- Testen Sie Ihre Änderungen

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
- Pushen Sie Ihren Branch
- Erstellen Sie einen Pull Request auf GitHub
- Beschreiben Sie Ihre Änderungen detailliert

## Code-Standards

### Python
- Verwenden Sie Black für Code-Formatierung
- Folgen Sie PEP 8
- Verwenden Sie Type Hints wo möglich
- Schreiben Sie Docstrings für alle öffentlichen Funktionen

### Git Commits
- Verwenden Sie prägnante, beschreibende Commit-Nachrichten
- Beginnen Sie mit einem Verb (Add, Fix, Update, Remove)
- Referenzieren Sie Issues mit `#issue-number`

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
- Verwenden Sie Docstrings im Google-Style
- Dokumentieren Sie alle Parameter, Rückgabewerte und Ausnahmen
- Halten Sie Kommentare auf Englisch

### Projekt-Dokumentation
- Aktualisieren Sie README.md bei neuen Features
- Fügen Sie Änderungen zu CHANGELOG.md hinzu
- Aktualisieren Sie diese CONTRIBUTING.md bei Bedarf

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

- Melden Sie Sicherheitslücken nicht öffentlich
- Kontaktieren Sie die Maintainers direkt
- Verwenden Sie keine unsicheren Abhängigkeiten
- Führen Sie Security-Scans durch: `bandit -r .`

## Lizenz

Durch das Beitragen zu diesem Projekt stimmen Sie zu, dass Ihre Beiträge unter der MIT-Lizenz stehen.

## Fragen?

Bei Fragen:
- Öffnen Sie ein [GitHub Issue](https://github.com/securebitsorg/bash-script-maker/issues)
- Schreiben Sie in [GitHub Discussions](https://github.com/securebitsorg/bash-script-maker/discussions)
- Kontaktieren Sie die Maintainers

Vielen Dank für Ihren Beitrag! 🚀

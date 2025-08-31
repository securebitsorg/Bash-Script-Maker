# GitHub Setup für Bash-Script-Maker

Dieses Dokument erklärt, wie Sie GitHub Secrets für die CI/CD-Pipeline einrichten.

## 📋 Erforderliche Secrets

### 1. PyPI API Token (für Package Publishing)

**Secret Name:** `PYPI_API_TOKEN`

**Verwendung:** Zum automatischen Upload von Packages zu PyPI

#### Wie Sie Ihren PyPI API Token erhalten:
1. Gehen Sie zu [PyPI.org](https://pypi.org/)
2. Melden Sie sich an (oder erstellen Sie einen Account)
3. Gehen Sie zu **Account Settings** → **API Tokens**
4. Klicken Sie auf **Add API Token**
5. Geben Sie einen Namen ein (z.B. "Bash-Script-Maker GitHub Actions")
6. Wählen Sie **Scope**: "Entire account (all projects)"
7. Klicken Sie auf **Add token**
8. **Kopieren Sie den Token sofort** (er wird nur einmal angezeigt!)

### 2. GitHub Token (automatisch verfügbar)

**Secret Name:** `GITHUB_TOKEN`

**Verwendung:** Für GitHub API Zugriffe innerhalb von Actions

✅ **Dieses Secret wird automatisch von GitHub bereitgestellt** - keine manuelle Einrichtung nötig!

## 🚀 Schritt-für-Schritt Anleitung

### Schritt 1: Repository Settings öffnen
1. Gehen Sie zu Ihrem GitHub Repository: `https://github.com/YOUR_USERNAME/bash-script-maker`
2. Klicken Sie auf **Settings** (Zahnrad-Symbol)
3. Scrollen Sie im linken Menü nach unten zu **Secrets and variables**
4. Klicken Sie auf **Actions**

### Schritt 2: PyPI Token hinzufügen
1. Klicken Sie auf **New repository secret**
2. **Name:** `PYPI_API_TOKEN`
3. **Value:** Fügen Sie Ihren PyPI API Token ein
4. Klicken Sie auf **Add secret**

### Schritt 3: Überprüfen der Secrets
1. Sie sollten jetzt diese Secrets in der Liste sehen:
   - `PYPI_API_TOKEN` ✅
   - `GITHUB_TOKEN` ✅ (automatisch)

## 🔐 Best Practices für Secrets

### Sicherheit
- ✅ **Teilen Sie Secrets niemals** in Code, Commits oder Issues
- ✅ **Rotieren Sie Token regelmäßig**
- ✅ Verwenden Sie **dedizierte Token** mit minimalen Berechtigungen
- ✅ **Löschen Sie alte Token**, die nicht mehr benötigt werden

### Token-Management
- 📝 **Dokumentieren Sie** Ihre Token und deren Zweck
- 🔄 **Erneuern Sie Token** bei Sicherheitsvorfällen
- 🏷️ Verwenden Sie **beschreibende Namen** für Token

## 🧪 Testen der Secrets

### Manuelles Testen der PyPI-Verbindung
```bash
# Installieren Sie Twine
pip install twine

# Testen Sie die Verbindung (ohne Upload)
python -m build
python -m twine check dist/*

# Testen Sie den Upload (nur wenn Sie bereit sind)
python -m twine upload --repository testpypi dist/*
```

### GitHub Actions Testen
1. **Push zu main branch** → CI/CD Pipeline wird automatisch gestartet
2. **Überprüfen Sie den Actions Tab** in GitHub
3. **Sehen Sie sich die Logs an** für Fehler oder Erfolgsmeldungen

## 🔧 Troubleshooting

### Problem: "PYPI_API_TOKEN not found"
**Lösung:**
1. Überprüfen Sie die Schreibweise: `PYPI_API_TOKEN` (alles Großbuchstaben)
2. Stellen Sie sicher, dass das Secret im richtigen Repository gesetzt ist
3. Überprüfen Sie, dass der Token nicht abgelaufen ist

### Problem: "Upload failed"
**Mögliche Ursachen:**
1. ❌ Ungültiger PyPI Token
2. ❌ Package-Name bereits vergeben (ändern Sie den Namen in `setup.py`)
3. ❌ Netzwerkprobleme (versuchen Sie es später erneut)

### Problem: Token vergessen?
**Lösung:**
1. Gehen Sie zu PyPI → Account Settings → API Tokens
2. Löschen Sie den alten Token
3. Erstellen Sie einen neuen Token
4. Aktualisieren Sie das GitHub Secret

## 📊 Überwachen der Pipeline

### GitHub Actions Status
- **Actions Tab**: Zeigt alle Workflow-Läufe
- **Badge hinzufügen**: `![CI](https://github.com/YOUR_USERNAME/bash-script-maker/workflows/CI/CD%20Pipeline/badge.svg)`

### Logs analysieren
1. Klicken Sie auf einen Workflow-Lauf
2. Öffnen Sie einzelne Jobs
3. Suchen Sie nach Fehlermeldungen
4. Verwenden Sie die Suchfunktion für spezifische Fehler

## 🎯 Nächste Schritte nach Setup

### 1. Ersten Test-Release erstellen
```bash
# Lokaler Test
python -m build
python -m twine check dist/*

# GitHub Release erstellen
# Gehen Sie zu GitHub → Releases → "Create a new release"
# Tag: v1.0.0
# Title: First Release
# Description: Initial release of Bash-Script-Maker
```

### 2. Automatische Releases aktivieren
```bash
# Für zukünftige Releases einfach Tags pushen
git tag v1.0.1
git push origin v1.0.1
```

### 3. Repository-Settings anpassen
- **Branches**: Schützen Sie den main branch
- **Issues**: Aktivieren Sie Issue Templates
- **Discussions**: Für Community-Support
- **Wiki**: Für erweiterte Dokumentation

## 📞 Support

Bei Problemen mit den Secrets:

1. **GitHub Documentation**: [Creating and storing encrypted secrets](https://docs.github.com/en/actions/security-guides/encrypted-secrets)
2. **PyPI Documentation**: [Using API tokens](https://pypi.org/help/#apitoken)
3. **GitHub Community**: [GitHub Actions Forum](https://github.community/c/github-actions/41)

## ✅ Checklist

- [ ] GitHub Repository erstellt/geklont
- [ ] PyPI Account und API Token erstellt
- [ ] `PYPI_API_TOKEN` Secret in GitHub gesetzt
- [ ] `GITHUB_TOKEN` automatisch verfügbar
- [ ] Erster Test-Push durchgeführt
- [ ] CI/CD Pipeline erfolgreich gelaufen
- [ ] Erstes Release erstellt
- [ ] Badges zum README hinzugefügt

---

## 🔑 Schnellübersicht: Secrets setzen

### 1. Repository Settings öffnen
```
GitHub.com → Ihr Repository → Settings → Secrets and variables → Actions
```

### 2. PyPI Token hinzufügen
```
New repository secret
Name: PYPI_API_TOKEN
Value: [Ihr PyPI API Token]
```

### 3. Überprüfen
```
✅ PYPI_API_TOKEN sollte in der Liste erscheinen
✅ GITHUB_TOKEN ist automatisch verfügbar
```

## 🎯 Erste Schritte nach dem Setup

### Repository zu GitHub pushen

**Option 1: Automatisch (empfohlen)**
```bash
./init_github.sh
```

**Option 2: Manuell**
```bash
git init  # falls noch nicht geschehen
git add .
git commit -m "🎉 Initial commit: Bash-Script-Maker mit GitHub Actions CI/CD

✨ Features:
• GUI-Programm zur Bash-Script-Erstellung
• Syntax-Highlighting für Bash-Scripts
• Autovervollständigung
• Intelligente Tab-Funktionalität
• Zenity-Dialog-Integration

🔧 Technik:
• Vollständige GitHub Actions CI/CD Pipeline
• Automatische Releases und Package-Publishing
• CodeQL Security Scanning
• Mehrere Linux-Distributionen unterstützt
• Umfassende Test-Suite"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/bash-script-maker.git
git push -u origin main
```

### Ersten Release erstellen
1. Gehen Sie zu GitHub → **Releases** → **Create a new release**
2. **Tag version**: `v1.0.0`
3. **Release title**: `First Release`
4. **Description**: `Initial release of Bash-Script-Maker`
5. **Publish release**

### Badges aktualisieren
Nach dem ersten Release aktualisieren Sie die Badge-URLs im README.md:
```markdown
# Ersetzen Sie 'yourusername' mit Ihrem GitHub-Benutzernamen
[![CI/CD Pipeline](https://github.com/IHR_BENUTZERNAME/bash-script-maker/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/IHR_BENUTZERNAME/bash-script-maker/actions/workflows/ci-cd.yml)
```

## 🚨 Wichtige Hinweise

### Token-Sicherheit
- 🔒 **Speichern Sie Token niemals** in Code oder öffentlichen Commits
- 🔄 **Rotieren Sie Token** alle 6-12 Monate
- 🗑️ **Löschen Sie nicht mehr benötigte Token**
- 📝 **Dokumentieren Sie** Ihre Token für Team-Mitglieder

### Troubleshooting
- **"Secret not found"**: Überprüfen Sie die Schreibweise (alles Großbuchstaben)
- **"Invalid token"**: Token könnte abgelaufen sein - neuen Token erstellen
- **"Permission denied"**: Token hat nicht die richtigen Berechtigungen

### GitHub Actions Limits
- **Free Tier**: 2.000 Minuten/Monat für öffentliche Repositories
- **Pro Tier**: 3.000 Minuten/Monat
- **Storage**: 500 MB pro Repository
- **Concurrency**: 20 gleichzeitige Jobs

---

**Hinweis:** Secrets sind für alle Repository-Typen kostenlos verfügbar. Bei privaten Repositorys haben Sie jedoch mehr Minuten für GitHub Actions zur Verfügung.

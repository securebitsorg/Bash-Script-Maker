# 📦 GitHub Releases Guide

## Übersicht

Dieses Dokument erklärt, wie GitHub Releases für das Bash-Script-Maker Projekt verwaltet werden.

## 🎯 Was sind GitHub Releases?

GitHub Releases sind veröffentlichte Versionen deiner Software, die:
- **Versionsnummern** haben (z.B. v1.8.0)
- **Release Notes** enthalten
- **Assets** (Dateien) bereitstellen können
- **Download-Links** für Benutzer bieten

## 📋 Aktuelle Release-Strategie

### Automatische Releases
- ✅ **Trigger**: Jeder Push auf `main` mit Commit-Message-Patterns
- ✅ **Versioning**: Automatisches Semantic Versioning
- ✅ **Assets**: Python Packages (.whl, .tar.gz)
- ✅ **PyPI**: Automatischer Upload zu PyPI
- ✅ **GitHub Packages**: Docker Images in GHCR

### Release-Patterns
```bash
feat: neue Funktion     → Minor Version (1.8.0 → 1.9.0)
fix: Bugfix            → Patch Version (1.8.0 → 1.8.1)  
BREAKING CHANGE:       → Major Version (1.8.0 → 2.0.0)
```

## 🚀 Workflow mit Pull Requests

### 1. Feature-Branch erstellen
```bash
git checkout -b feature/neue-funktion
# Änderungen machen
git commit -m "feat: neue coole Funktion"
git push origin feature/neue-funktion
```

### 2. Pull Request erstellen
```bash
gh pr create --title "Feature: Neue Funktion" --body "Beschreibung..."
```

### 3. Review & Merge
- CI/CD Tests laufen automatisch
- Code Review (optional für Solo-Entwicklung)
- Merge über GitHub UI
- **Automatisches Release** wird ausgelöst

## 📊 Release-Historie

Aktuell haben wir **30+ Tags** erstellt:
- v0.1.0 bis v1.9.0
- Vollständige Historie auf GitHub verfügbar
- Jede Version mit eigenen Release Notes

## 🛠️ Nächste Schritte

1. **Branch Protection** aktivieren
2. **Pull Request Template** erstellen  
3. **Issue Templates** hinzufügen
4. **Automatische Changelog** Generation

---

*Erstellt als Teil des Pull-Request-Workflows*

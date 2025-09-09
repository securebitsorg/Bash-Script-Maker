# 📋 CHANGELOG Automatisierung

Diese Dokumentation erklärt, wie die automatische CHANGELOG-Generierung in Bash-Script-Maker funktioniert.

## 🔄 Automatische CHANGELOG-Updates

### Bei jedem Release wird automatisch:

1. **📝 CHANGELOG.md aktualisiert** mit neuer Version und Änderungen
2. **🏷️ Kategorisierung** basierend auf Commit-Message-Präfixen
3. **📅 Datum hinzugefügt** im Format `YYYY-MM-DD`
4. **🔗 Version verlinkt** für bessere Navigation

## 📊 Commit-Message-Kategorien

Die CHANGELOG-Kategorisierung erfolgt automatisch basierend auf Commit-Message-Präfixen:

| Präfix | CHANGELOG-Kategorie | Beschreibung |
|--------|-------------------|--------------|
| `feat:` / `feature:` | **Added** | Neue Features |
| `fix:` / `bugfix:` | **Fixed** | Fehlerbehebungen |
| `docs:` / `doc:` | **Documentation** | Dokumentation |
| `style:` / `refactor:` | **Changed** | Code-Änderungen |
| `test:` / `tests:` | **Testing** | Test-Verbesserungen |
| `chore:` / `build:` / `ci:` | **Technical** | Technische Änderungen |
| `perf:` / `performance:` | **Performance** | Performance-Optimierungen |
| `security:` / `sec:` | **Security** | Sicherheits-Updates |
| `Merge pull request` | **Added** | Pull Request merged |

## 🎯 Beispiele

### ✅ Gute Commit-Messages für CHANGELOG

```bash
# Wird zu "Added" Kategorie
feat: add dark mode toggle to settings
feature(ui): implement new dashboard layout

# Wird zu "Fixed" Kategorie  
fix: resolve memory leak in script parser
bugfix(editor): fix syntax highlighting for large files

# Wird zu "Documentation" Kategorie
docs: update installation guide for Ubuntu 22.04
doc(api): add examples for custom syntax highlighters

# Wird zu "Changed" Kategorie
style: apply black formatting to all Python files
refactor: restructure main application class

# Wird zu "Security" Kategorie
security: update dependencies to fix CVE-2023-1234
```

### 📋 Resultierende CHANGELOG-Einträge

```markdown
## [1.11.0] - 2025-01-15

### Added
- Add dark mode toggle to settings

## [1.10.1] - 2025-01-14

### Fixed
- Resolve memory leak in script parser

## [1.10.0] - 2025-01-13

### Documentation
- Update installation guide for Ubuntu 22.04
```

## 🛠️ Manuelle CHANGELOG-Generierung

Für lokale Tests oder manuelle Einträge:

```bash
# CHANGELOG-Eintrag für neue Version generieren
python3 generate_changelog_entry.py "1.2.3" "feat: add new awesome feature"

# Mit spezifischem Release-Typ
python3 generate_changelog_entry.py "1.3.0" "feat: major UI improvements" "minor"

# Bugfix
python3 generate_changelog_entry.py "1.2.4" "fix: resolve parser issue" "patch"
```

## 🔧 Workflow-Integration

### Automatische Updates im GitHub Actions Workflow

Der `auto-release-on-push.yml` Workflow:

1. **📝 Analysiert** die Commit-Message
2. **🏷️ Kategorisiert** die Änderung
3. **📋 Generiert** CHANGELOG-Eintrag
4. **💾 Committet** die Änderungen
5. **🚀 Erstellt** GitHub Release

### Workflow-Schritte

```yaml
- name: Generate release notes and update CHANGELOG
  run: |
    # Commit-Message analysieren
    COMMIT_MSG="${{ github.event.head_commit.message }}"
    
    # CHANGELOG-Kategorie bestimmen
    if [[ "$COMMIT_MSG" =~ ^(feat|feature) ]]; then
      CATEGORY="Added"
    elif [[ "$COMMIT_MSG" =~ ^(fix|bugfix) ]]; then
      CATEGORY="Fixed"
    # ... weitere Kategorien
    fi
    
    # CHANGELOG.md aktualisieren
    cat > CHANGELOG.md << EOF
    ## [$NEW_VERSION] - $CURRENT_DATE
    
    ### $CATEGORY
    - $CLEAN_MESSAGE
    EOF
```

## 📁 CHANGELOG-Struktur

### Standard-Format (Keep a Changelog)

```markdown
# Changelog

## [Unreleased]

### Added
- Neue Features für nächste Version

## [1.2.0] - 2025-01-15

### Added
- Neue Feature-Implementierung
- Weitere neue Funktionalität

### Fixed
- Behobener Bug in Parser
- Korrigierte UI-Darstellung

### Changed
- Verbesserte Performance
- Aktualisierte Abhängigkeiten

## [1.1.0] - 2025-01-10

### Added
- Erste Version der neuen API
```

## 🎯 Best Practices

### ✅ Empfohlene Commit-Messages

```bash
# Klar und beschreibend
feat: add user authentication system
fix: resolve crash when opening large files
docs: update README with new installation steps

# Mit Scope für bessere Organisation
feat(editor): add syntax highlighting for Python
fix(parser): handle edge case with empty scripts
style(ui): improve button spacing and colors
```

### ❌ Zu vermeidende Commit-Messages

```bash
# Zu unspezifisch
fix: bug
feat: stuff
docs: update

# Ohne Präfix (wird als "Changed" kategorisiert)
Add new feature
Fix the thing
Update documentation
```

## 🔍 Troubleshooting

### Problem: CHANGELOG wird nicht aktualisiert

**Lösung:**
```bash
# Workflow-Logs überprüfen
# Sicherstellen, dass Commit-Message erkannt wird
# CHANGELOG.md Permissions überprüfen
```

### Problem: Falsche Kategorisierung

**Lösung:**
```bash
# Commit-Message-Präfix überprüfen
# generate_changelog_entry.py lokal testen
python3 generate_changelog_entry.py "1.2.3" "deine-commit-message"
```

### Problem: Duplikate in CHANGELOG

**Lösung:**
```bash
# CHANGELOG.md manuell bereinigen
# Workflow-Logik für Duplikat-Erkennung prüfen
```

## 🚀 Erweiterte Features

### Geplante Verbesserungen

- [ ] **🔗 Automatische Links** zu Issues und PRs
- [ ] **📊 Contributor-Credits** in CHANGELOG
- [ ] **🏷️ Scope-basierte Gruppierung** (ui, api, docs)
- [ ] **📈 Release-Statistiken** (Zeilen Code, Tests, etc.)
- [ ] **🌐 Mehrsprachige CHANGELOG** (DE/EN)

### Konfiguration

Die CHANGELOG-Automatisierung kann über Umgebungsvariablen angepasst werden:

```yaml
env:
  CHANGELOG_FORMAT: "keepachangelog"  # oder "conventional"
  CHANGELOG_LANGUAGE: "de"           # oder "en"
  CHANGELOG_INCLUDE_LINKS: "true"    # Links zu Commits/PRs
```

## 📚 Weitere Ressourcen

- [Keep a Changelog](https://keepachangelog.com/de/1.0.0/)
- [Semantic Versioning](https://semver.org/lang/de/)
- [Conventional Commits](https://www.conventionalcommits.org/de/v1.0.0/)
- [GitHub Releases Best Practices](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases)

---

**🎉 Mit dieser Automatisierung wird jeder Release professionell dokumentiert!**

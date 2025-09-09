#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CHANGELOG Generator für Bash-Script-Maker
Generiert automatisch CHANGELOG-Einträge basierend auf Commit-Messages
"""

import sys
import re
from datetime import datetime
from pathlib import Path


def categorize_commit(commit_msg):
    """Kategorisiert Commit-Message und extrahiert relevante Informationen"""
    
    categories = {
        r'^(feat|feature)(\(.+\))?: ': ('Added', 'Neue Features'),
        r'^(fix|bugfix)(\(.+\))?: ': ('Fixed', 'Fehlerbehebungen'),
        r'^(docs|doc)(\(.+\))?: ': ('Documentation', 'Dokumentation'),
        r'^(style|refactor)(\(.+\))?: ': ('Changed', 'Änderungen'),
        r'^(test|tests)(\(.+\))?: ': ('Testing', 'Tests'),
        r'^(chore|build|ci)(\(.+\))?: ': ('Technical', 'Technische Änderungen'),
        r'^(perf|performance)(\(.+\))?: ': ('Performance', 'Performance-Verbesserungen'),
        r'^(security|sec)(\(.+\))?: ': ('Security', 'Sicherheit'),
        r'^Merge[[:space:]]pull[[:space:]]request': ('Added', 'Pull Request merged')
    }
    
    for pattern, (category, description) in categories.items():
        if re.match(pattern, commit_msg):
            # Extrahiere die eigentliche Nachricht (nach dem Präfix)
            clean_msg = re.sub(r'^[^:]*: ', '', commit_msg)
            return category, clean_msg
    
    # Fallback für unerkannte Patterns
    return 'Changed', commit_msg


def generate_changelog_entry(version, commit_msg, release_type='patch'):
    """Generiert einen CHANGELOG-Eintrag für eine neue Version"""
    
    current_date = datetime.now().strftime('%Y-%m-%d')
    category, clean_msg = categorize_commit(commit_msg)
    
    entry = f"""## [{version}] - {current_date}

### {category}
- {clean_msg}

"""
    
    return entry


def update_changelog(new_entry, changelog_path='CHANGELOG.md'):
    """Fügt neuen Eintrag am Anfang der CHANGELOG hinzu"""
    
    changelog_file = Path(changelog_path)
    
    if not changelog_file.exists():
        print(f"❌ CHANGELOG-Datei nicht gefunden: {changelog_path}")
        return False
    
    # Aktuelle CHANGELOG lesen
    with open(changelog_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Finde die Position nach dem Header (nach "## [Unreleased]" Sektion)
    lines = content.split('\n')
    insert_pos = 0
    
    # Suche nach der ersten Version oder dem Ende des Headers
    for i, line in enumerate(lines):
        if re.match(r'^## \[\d+\.\d+\.\d+\]', line) or line.strip() == '# Changelog':
            insert_pos = i
            break
    
    # Wenn wir eine automatisch generierte Sektion am Anfang haben, überspringen
    if insert_pos < len(lines) and '# [1.4.0]' in lines[0]:
        # Finde das Ende der ersten Sektion
        for i in range(1, len(lines)):
            if lines[i].startswith('# ') or lines[i].startswith('## ['):
                insert_pos = i
                break
    
    # Neuen Eintrag einfügen
    new_lines = lines[:insert_pos] + new_entry.strip().split('\n') + [''] + lines[insert_pos:]
    
    # CHANGELOG schreiben
    with open(changelog_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(new_lines))
    
    print(f"✅ CHANGELOG erfolgreich aktualisiert: {changelog_path}")
    return True


def main():
    """Hauptfunktion für CLI-Nutzung"""
    
    if len(sys.argv) < 3:
        print("""
🔖 CHANGELOG Entry Generator

Verwendung:
    python generate_changelog_entry.py <version> <commit_message> [release_type]

Beispiele:
    python generate_changelog_entry.py "1.2.3" "feat: add new feature"
    python generate_changelog_entry.py "1.2.4" "fix: resolve bug in parser" "patch"
    python generate_changelog_entry.py "1.3.0" "feat: major UI improvements" "minor"

Release-Typen:
    - patch: Bugfixes (1.2.3 → 1.2.4)
    - minor: Neue Features (1.2.3 → 1.3.0)  
    - major: Breaking Changes (1.2.3 → 2.0.0)
""")
        sys.exit(1)
    
    version = sys.argv[1]
    commit_msg = sys.argv[2]
    release_type = sys.argv[3] if len(sys.argv) > 3 else 'patch'
    
    print(f"📝 Generiere CHANGELOG-Eintrag für Version {version}...")
    print(f"📋 Commit-Message: {commit_msg}")
    print(f"🔖 Release-Typ: {release_type}")
    
    # CHANGELOG-Eintrag generieren
    entry = generate_changelog_entry(version, commit_msg, release_type)
    
    print(f"\n📄 Generierter Eintrag:\n{entry}")
    
    # CHANGELOG aktualisieren
    if update_changelog(entry):
        print("🎉 CHANGELOG erfolgreich aktualisiert!")
        
        # Vorschau der ersten 15 Zeilen
        with open('CHANGELOG.md', 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        print("\n📋 CHANGELOG-Vorschau (erste 15 Zeilen):")
        print("-" * 50)
        for i, line in enumerate(lines[:15], 1):
            print(f"{i:2d}| {line.rstrip()}")
        print("-" * 50)
    else:
        print("❌ Fehler beim Aktualisieren der CHANGELOG")
        sys.exit(1)


if __name__ == '__main__':
    main()

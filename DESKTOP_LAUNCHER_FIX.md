# 🔧 Desktop Launcher Fix

## Problem
Die Anwendung lässt sich nicht über das Startmenü starten:
```
Fehlermeldung: Programm „/home/marci/.local/bin/bash-script-maker" ist nicht auffindbar
```

## Lösung - Schritt für Schritt

### 1. ✅ App korrekt installieren
```bash
cd /home/marci/Code/Bash-Script-Maker
pip install -e .
```

### 2. ✅ Prüfen ob ausführbare Datei existiert
```bash
ls -la ~/.local/bin/bash-script-maker
# Sollte anzeigen: -rwxr-xr-x. 1 marci marci 219 ... bash-script-maker
```

### 3. ✅ Desktop-Integration installieren
```bash
./install_desktop_integration.sh
```

### 4. ✅ Desktop-Datenbank aktualisieren
```bash
update-desktop-database ~/.local/share/applications
gtk-update-icon-cache ~/.local/share/icons/hicolor/ --ignore-theme-index
```

### 5. 🔄 Desktop-Umgebung neu starten
```bash
# GNOME/KDE/XFCE neu starten oder
# Abmelden und wieder anmelden
```

## Diagnose-Befehle

### Prüfe Installation:
```bash
which bash-script-maker
~/.local/bin/bash-script-maker --version
```

### Prüfe Desktop-Datei:
```bash
cat ~/.local/share/applications/bash-script-maker.desktop
desktop-file-validate ~/.local/share/applications/bash-script-maker.desktop
```

### Prüfe Icons:
```bash
ls ~/.local/share/icons/hicolor/*/apps/bash-script-maker.*
```

### Prüfe PATH:
```bash
echo $PATH | grep -o '/home/marci/.local/bin'
```

## Alternative Lösungen

### Wenn das Problem weiterhin besteht:

#### Option 1: Absolute Pfade in Desktop-Datei
```bash
# Desktop-Datei bearbeiten
sed -i 's|Icon=bash-script-maker|Icon=/home/marci/.local/share/icons/hicolor/scalable/apps/bash-script-maker.svg|' ~/.local/share/applications/bash-script-maker.desktop
```

#### Option 2: System-weite Installation
```bash
sudo pip install -e .
# Dann Desktop-Integration mit sudo ausführen
```

#### Option 3: Desktop-Datei manuell erstellen
```bash
cat > ~/.local/share/applications/bash-script-maker.desktop << 'EOF'
[Desktop Entry]
Name=Bash-Script-Maker
Comment=Ein GUI-Programm zur Erstellung von Bash-Scripts
Exec=/home/marci/.local/bin/bash-script-maker
Icon=/home/marci/.local/share/icons/hicolor/48x48/apps/bash-script-maker.png
Terminal=false
Type=Application
Categories=Development;Utility;TextEditor;
Keywords=bash;script;editor;generator;development;
StartupWMClass=bash-script-maker
MimeType=text/x-shellscript;application/x-shellscript;
EOF

chmod +x ~/.local/share/applications/bash-script-maker.desktop
update-desktop-database ~/.local/share/applications
```

## Status nach Fix

- ✅ App installiert: v1.9.0
- ✅ Ausführbare Datei: `/home/marci/.local/bin/bash-script-maker`
- ✅ Desktop-Datei: `~/.local/share/applications/bash-script-maker.desktop`
- ✅ Icons installiert: Verschiedene Größen
- ✅ Desktop-Datenbank aktualisiert

## Test
```bash
# Terminal-Start (sollte funktionieren):
bash-script-maker

# Desktop-Start: Über Anwendungsmenü testen
```

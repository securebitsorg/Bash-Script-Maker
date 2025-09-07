# Flatpak Package Guide

## 🚀 Flatpak-Pakete für Bash-Script-Maker

Dieses Dokument erklärt, wie Sie die Flatpak-Pakete von Bash-Script-Maker verwenden können.

## 📦 Verfügbare Pakete

### GitHub Packages (Container Registry)
- **Repository**: `ghcr.io/securebitsorg/bash-script-maker-flatpak`
- **Tags**: `latest`, `1.4.2`, etc.
- **Format**: OCI Container mit Flatpak-Bundle

### GitHub Releases
- **Location**: https://github.com/securebitsorg/bash-script-maker/releases
- **Format**: `.flatpak` Bundle-Dateien
- **Naming**: `BashScriptMaker-{VERSION}.flatpak`

## 🛠️ Installation

### Methode 1: Direkter Download und Installation

```bash
# 1. Aktuellste Version herunterladen
wget https://github.com/securebitsorg/bash-script-maker/releases/latest/download/BashScriptMaker-1.4.2.flatpak

# 2. Installieren
flatpak install --user BashScriptMaker-1.4.2.flatpak

# 3. Ausführen
flatpak run org.securebits.bashscriptmaker
```

### Methode 2: Via Container Registry

```bash
# 1. Container herunterladen
docker pull ghcr.io/securebitsorg/bash-script-maker-flatpak:latest

# 2. Flatpak-Bundle extrahieren
docker create --name temp-container ghcr.io/securebitsorg/bash-script-maker-flatpak:latest
docker cp temp-container:/BashScriptMaker.flatpak ./BashScriptMaker.flatpak
docker rm temp-container

# 3. Installieren
flatpak install --user BashScriptMaker.flatpak

# 4. Ausführen
flatpak run org.securebits.bashscriptmaker
```

### Methode 3: Lokaler Build

```bash
# 1. Repository klonen
git clone https://github.com/securebitsorg/bash-script-maker.git
cd bash-script-maker

# 2. Flatpak bauen
./build_flatpak.sh

# 3. Installieren (Bundle wird automatisch erstellt)
flatpak install --user BashScriptMaker-*.flatpak
```

## 🔍 Paket-Informationen

### App-ID
```
org.securebits.bashscriptmaker
```

### Laufzeit-Anforderungen
- **Runtime**: `org.freedesktop.Platform//23.08`
- **SDK**: `org.freedesktop.Sdk//23.08`

### Berechtigungen
- `--share=ipc` - Inter-Process Communication
- `--socket=wayland` - Wayland Display Server
- `--socket=x11` - X11 Display Server
- `--socket=pulseaudio` - Audio-Zugriff
- `--device=dri` - Hardware-Beschleunigung
- `--filesystem=home` - Zugriff auf Home-Verzeichnis
- `--filesystem=host` - Zugriff auf Host-Dateisystem
- `--talk-name=org.freedesktop.Notifications` - Desktop-Benachrichtigungen

## 🐛 Fehlerbehebung

### Problem: "No such file or directory"
```bash
# Prüfen Sie, ob Flatpak installiert ist
flatpak --version

# Installieren Sie Flatpak falls nötig (Ubuntu/Debian)
sudo apt install flatpak

# Installieren Sie Flatpak falls nötig (Fedora)
sudo dnf install flatpak
```

### Problem: "Runtime not found"
```bash
# Flathub-Repository hinzufügen
flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo

# Runtime installieren
flatpak install flathub org.freedesktop.Platform//23.08
flatpak install flathub org.freedesktop.Sdk//23.08
```

### Problem: "Permission denied"
```bash
# Installieren Sie als User (nicht System-weit)
flatpak install --user your-package.flatpak

# Oder geben Sie explizite Berechtigungen
flatpak run --filesystem=home org.securebits.bashscriptmaker
```

### Problem: "App startet nicht"
```bash
# Debug-Modus aktivieren
flatpak run --verbose org.securebits.bashscriptmaker

# Oder mit Shell-Zugriff
flatpak run --command=bash org.securebits.bashscriptmaker
```

## 📊 Paket-Größe und Performance

### Bundle-Größe
- **Flatpak-Bundle**: ~2-5 MB (komprimiert)
- **Installiert**: ~10-15 MB
- **Runtime-Dependencies**: ~200-300 MB (einmalig)

### Performance
- **Startzeit**: Ähnlich wie native Installation
- **Speicherverbrauch**: Minimal zusätzlicher Overhead
- **Sandbox-Sicherheit**: Vollständige Isolation

## 🔄 Updates

### Automatische Updates
```bash
# Alle Flatpak-Apps aktualisieren
flatpak update

# Nur Bash-Script-Maker aktualisieren
flatpak update org.securebits.bashscriptmaker
```

### Manuelle Updates
```bash
# Neue Version herunterladen
wget https://github.com/securebitsorg/bash-script-maker/releases/latest/download/BashScriptMaker-{NEW_VERSION}.flatpak

# Installieren (überschreibt alte Version)
flatpak install --user BashScriptMaker-{NEW_VERSION}.flatpak
```

## 🗑️ Deinstallation

```bash
# App deinstallieren
flatpak uninstall org.securebits.bashscriptmaker

# Alle Daten löschen (optional)
rm -rf ~/.var/app/org.securebits.bashscriptmaker

# Runtime deinstallieren (falls nicht von anderen Apps verwendet)
flatpak uninstall --unused
```

## 🔐 Sicherheit

### Sandbox-Vorteile
- ✅ **Isolierte Ausführung** - App kann nur auf erlaubte Ressourcen zugreifen
- ✅ **Kontrollierte Berechtigungen** - Explizite Dateisystem- und Netzwerk-Zugriffe
- ✅ **Automatische Updates** - Sicherheits-Patches werden automatisch verteilt
- ✅ **Konsistente Umgebung** - Gleiche Runtime auf allen Systemen

### Berechtigungs-Überprüfung
```bash
# Aktuelle Berechtigungen anzeigen
flatpak info --show-permissions org.securebits.bashscriptmaker

# Berechtigungen überschreiben (falls nötig)
flatpak override --user --filesystem=home org.securebits.bashscriptmaker
```

## 📈 Monitoring

### Installierte Pakete
```bash
# Alle installierten Flatpak-Apps auflisten
flatpak list

# Details zu Bash-Script-Maker
flatpak info org.securebits.bashscriptmaker
```

### Logs und Debugging
```bash
# Runtime-Logs anzeigen
journalctl --user -f -u flatpak-session.service

# App-spezifische Logs
flatpak run --log-session-bus org.securebits.bashscriptmaker
```

## 🌐 Distribution

### Für Entwickler
```bash
# Eigenes Flatpak-Repository erstellen
flatpak build-repo my-repo build-dir

# Bundle für Distribution erstellen
flatpak build-bundle my-repo BashScriptMaker.flatpak org.securebits.bashscriptmaker
```

### Für Benutzer
- **Direkter Download**: Einfachste Methode für Endbenutzer
- **Container Registry**: Für automatisierte Deployments
- **Lokaler Build**: Für Entwickler und Power-User

## 📞 Support

Bei Problemen mit dem Flatpak-Paket:

1. **GitHub Issues**: https://github.com/securebitsorg/bash-script-maker/issues
2. **Logs sammeln**: `flatpak run --verbose org.securebits.bashscriptmaker`
3. **System-Info**: `flatpak --version` und `uname -a`

**Das Flatpak-Paket bietet eine sichere, konsistente und einfach zu installierende Variante von Bash-Script-Maker! 📦✨**

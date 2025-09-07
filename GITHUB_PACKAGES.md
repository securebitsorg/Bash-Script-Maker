# GitHub Packages für Bash-Script-Maker

Dieses Repository veröffentlicht automatisch Pakete über GitHub Packages bei jedem Release.

## 📦 Verfügbare Pakete

### GitHub Container Registry (GHCR)

Docker-Images werden automatisch bei jedem Release erstellt und in der GitHub Container Registry veröffentlicht.

#### Installation und Verwendung

```bash
# Neueste Version ziehen
docker pull ghcr.io/securebitsorg/bash-script-maker:latest

# Spezifische Version ziehen
docker pull ghcr.io/securebitsorg/bash-script-maker:1.4.7

# Container ausführen (mit X11-Weiterleitung für GUI)
docker run -it --rm \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
  -v $(pwd):/workspace \
  ghcr.io/securebitsorg/bash-script-maker:latest
```

#### Verfügbare Tags

- `latest` - Neueste stabile Version
- `v1.4.7`, `v1.4.8`, etc. - Spezifische Versionen
- `1.4`, `1.5`, etc. - Major.Minor Versionen

## 🔧 Erweiterte Docker-Verwendung

### Mit GUI-Unterstützung (Linux)

```bash
# X11-Socket für GUI-Anwendungen freigeben
xhost +local:docker

# Container mit GUI-Unterstützung starten
docker run -it --rm \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
  -v $(pwd):/workspace \
  --name bash-script-maker \
  ghcr.io/securebitsorg/bash-script-maker:latest

# Nach der Verwendung X11-Zugriff wieder einschränken
xhost -local:docker
```

### Mit persistentem Speicher

```bash
# Arbeitsverzeichnis persistent machen
docker run -it --rm \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
  -v $(pwd)/scripts:/app/scripts \
  -v $(pwd)/output:/app/output \
  ghcr.io/securebitsorg/bash-script-maker:latest
```

### Docker Compose

Erstelle eine `docker-compose.yml`:

```yaml
version: '3.8'

services:
  bash-script-maker:
    image: ghcr.io/securebitsorg/bash-script-maker:latest
    environment:
      - DISPLAY=${DISPLAY}
    volumes:
      - /tmp/.X11-unix:/tmp/.X11-unix:rw
      - ./scripts:/app/scripts
      - ./output:/app/output
    stdin_open: true
    tty: true
    network_mode: host
```

Ausführen:
```bash
docker-compose up
```

## 🚀 Automatische Updates

Die Pakete werden automatisch bei jedem Release aktualisiert:

1. **Bei einem Push** mit entsprechender Commit-Message (`feat:`, `fix:`, etc.)
2. **Automatische Versionierung** basierend auf Conventional Commits
3. **Multi-Platform Builds** für verschiedene Architekturen
4. **Optimierte Layer-Caching** für schnelle Builds

## 📋 Image-Informationen

### Base Image
- **Python 3.11 Slim**: Optimiert für Größe und Sicherheit
- **Debian-basiert**: Stabile und sichere Basis

### Enthaltene Abhängigkeiten
- Python 3.11
- tkinter (GUI-Framework)
- ttkbootstrap (moderne UI-Komponenten)
- pygments (Syntax-Highlighting)
- Pillow (Icon-Unterstützung)
- zenity (Dialog-Unterstützung)

### Sicherheitsfeatures
- **Non-root User**: Läuft als `appuser`, nicht als root
- **Minimale Abhängigkeiten**: Nur notwendige Pakete installiert
- **Health Checks**: Automatische Gesundheitsprüfung
- **Metadaten**: Vollständige OCI-Labels

## 🔍 Verfügbare Versionen

Alle verfügbaren Versionen findest du unter:
- [GitHub Packages](https://github.com/securebitsorg/Bash-Script-Maker/pkgs/container/bash-script-maker)

## 🐛 Problembehebung

### GUI funktioniert nicht
```bash
# X11-Berechtigung prüfen
xhost +local:docker

# DISPLAY-Variable prüfen
echo $DISPLAY
```

### Container startet nicht
```bash
# Logs anzeigen
docker logs bash-script-maker

# Interactive Shell für Debugging
docker run -it --rm --entrypoint /bin/bash \
  ghcr.io/securebitsorg/bash-script-maker:latest
```

### Speicher-Probleme
```bash
# Container mit mehr Speicher starten
docker run -it --rm \
  --memory=1g \
  --memory-swap=2g \
  ghcr.io/securebitsorg/bash-script-maker:latest
```

## 📞 Support

Bei Problemen oder Fragen:
- [Issues](https://github.com/securebitsorg/Bash-Script-Maker/issues) öffnen
- [Discussions](https://github.com/securebitsorg/Bash-Script-Maker/discussions) teilnehmen
- [Wiki](https://github.com/securebitsorg/Bash-Script-Maker/wiki) konsultieren

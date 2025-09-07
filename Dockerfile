FROM python:3.11-slim

# Metadaten
LABEL org.opencontainers.image.title="Bash Script Maker"
LABEL org.opencontainers.image.description="Ein GUI-Programm zur Erstellung von Bash-Scripts"
LABEL org.opencontainers.image.vendor="SecureBits"
LABEL org.opencontainers.image.licenses="MIT"
LABEL org.opencontainers.image.source="https://github.com/securebitsorg/Bash-Script-Maker"

# Arbeitsverzeichnis setzen
WORKDIR /app

# System-Abhängigkeiten installieren
RUN apt-get update && apt-get install -y \
    zenity \
    python3-tk \
    xvfb \
    x11-apps \
    && rm -rf /var/lib/apt/lists/*

# Python-Abhängigkeiten kopieren und installieren
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Anwendung kopieren
COPY . .

# Berechtigungen setzen
RUN chmod +x bash_script_maker.py

# Benutzer erstellen (nicht als root laufen)
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

# Umgebungsvariablen für GUI
ENV DISPLAY=:99
ENV PYTHONUNBUFFERED=1

# Healthcheck
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD python3 -c "import bash_script_maker; print('OK')" || exit 1

# Expose Port für potentielle Web-Schnittstelle (falls später hinzugefügt)
EXPOSE 8080

# Standard-Befehl
CMD ["python3", "bash_script_maker.py"]
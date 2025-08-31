#!/bin/bash
# Installationsscript für Fedora/RHEL-basierte Systeme (dnf)
# Bash-Script-Maker - Abhängigkeiten Installation

echo "=== Bash-Script-Maker Installation (dnf) ==="
echo "Dieses Script installiert alle notwendigen Abhängigkeiten für Fedora/RHEL-basierte Systeme."
echo ""

# Farbcodes für bessere Lesbarkeit
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Funktion für farbige Ausgabe
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Überprüfe, ob das Script als root läuft
if [[ $EUID -eq 0 ]]; then
   print_warning "Das Script läuft als root. Das ist normal für die Installation."
else
   print_warning "Das Script läuft nicht als root. Möglicherweise werden Sie nach dem Passwort gefragt."
fi

# Paketliste für dnf
REQUIRED_PACKAGES=(
    "python3"           # Python 3 Interpreter
    "python3-tkinter"   # Tkinter für GUI
    "python3-pip"       # Python Package Installer
    "zenity"            # Dialog-Programme für Scripts
    "xterm"             # Terminal-Emulator (falls nicht vorhanden)
)

OPTIONAL_PACKAGES=(
    "git"               # Für Versionskontrolle
    "vim"               # Erweiterter Texteditor
    "nano"              # Einfacher Texteditor
    "gedit"             # GUI-Texteditor
)

print_status "Überprüfe vorhandene Pakete..."

# Überprüfe, welche Pakete bereits installiert sind
MISSING_PACKAGES=()
OPTIONAL_MISSING=()

for package in "${REQUIRED_PACKAGES[@]}"; do
    if ! rpm -q "$package" &> /dev/null; then
        MISSING_PACKAGES+=("$package")
    fi
done

for package in "${OPTIONAL_PACKAGES[@]}"; do
    if ! rpm -q "$package" &> /dev/null; then
        OPTIONAL_MISSING+=("$package")
    fi
done

# Zeige Zusammenfassung
echo ""
print_status "=== INSTALLATIONSZUSAMMENFASSUNG ==="
echo "Erforderliche Pakete zu installieren: ${#MISSING_PACKAGES[@]}"
if [ ${#MISSING_PACKAGES[@]} -gt 0 ]; then
    for package in "${MISSING_PACKAGES[@]}"; do
        echo "  - $package"
    done
fi

echo "Optionale Pakete zu installieren: ${#OPTIONAL_MISSING[@]}"
if [ ${#OPTIONAL_MISSING[@]} -gt 0 ]; then
    for package in "${OPTIONAL_MISSING[@]}"; do
        echo "  - $package"
    done
fi

# Frage nach Bestätigung
echo ""
if [ ${#MISSING_PACKAGES[@]} -eq 0 ] && [ ${#OPTIONAL_MISSING[@]} -eq 0 ]; then
    print_success "Alle Pakete sind bereits installiert!"
    exit 0
fi

read -p "Möchten Sie fortfahren? (j/N): " -n 1 -r
echo ""
if [[ ! $REPLY =~ ^[Jj]$ ]]; then
    print_warning "Installation abgebrochen."
    exit 1
fi

# Installiere erforderliche Pakete
if [ ${#MISSING_PACKAGES[@]} -gt 0 ]; then
    print_status "Installiere erforderliche Pakete..."
    if ! sudo dnf install -y "${MISSING_PACKAGES[@]}"; then
        print_error "Fehler bei der Installation der erforderlichen Pakete."
        exit 1
    fi
    print_success "Erforderliche Pakete erfolgreich installiert."
fi

# Frage nach optionalen Paketen
if [ ${#OPTIONAL_MISSING[@]} -gt 0 ]; then
    echo ""
    read -p "Möchten Sie auch optionale Pakete installieren? (j/N): " -n 1 -r
    echo ""
    if [[ $REPLY =~ ^[Jj]$ ]]; then
        print_status "Installiere optionale Pakete..."
        if ! sudo dnf install -y "${OPTIONAL_MISSING[@]}"; then
            print_error "Fehler bei der Installation der optionalen Pakete."
            exit 1
        fi
        print_success "Optionale Pakete erfolgreich installiert."
    fi
fi

# Überprüfe Python-Version
print_status "Überprüfe Python-Version..."
python3 --version

# Überprüfe Tkinter
print_status "Überprüfe Tkinter..."
if python3 -c "import tkinter; print('Tkinter verfügbar')"; then
    print_success "Tkinter ist verfügbar."
else
    print_error "Tkinter ist nicht verfügbar. Möglicherweise müssen Sie python3-tkinter manuell installieren."
fi

# Überprüfe Zenity
print_status "Überprüfe Zenity..."
if command -v zenity &> /dev/null; then
    print_success "Zenity ist verfügbar."
else
    print_error "Zenity ist nicht verfügbar."
fi

echo ""
print_success "=== INSTALLATION ABGESCHLOSSEN ==="
print_status "Sie können Bash-Script-Maker jetzt starten mit:"
print_status "  cd /pfad/zu/bash-script-maker"
print_status "  ./start.sh"
echo ""
print_status "Oder direkt mit:"
print_status "  python3 bash_script_maker.py"

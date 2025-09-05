#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Setup script for Bash-Script-Maker
"""

from setuptools import setup, find_packages
import os
import re
import shutil
import sys
from pathlib import Path


# Read version from VERSION file
def read_version():
    version_file = os.path.join(os.path.dirname(__file__), "VERSION")
    if os.path.exists(version_file):
        with open(version_file, "r", encoding="utf-8") as f:
            return f.read().strip()
    return "0.1.0"


# Read README for long description
def read_readme():
    readme_file = os.path.join(os.path.dirname(__file__), "README.md")
    if os.path.exists(readme_file):
        with open(readme_file, "r", encoding="utf-8") as f:
            return f.read()
    return ""


# Read requirements
def read_requirements():
    req_file = os.path.join(os.path.dirname(__file__), "requirements.txt")
    if os.path.exists(req_file):
        with open(req_file, "r", encoding="utf-8") as f:
            return [
                line.strip() for line in f if line.strip() and not line.startswith("#")
            ]
    return []


def install_desktop_files():
    """Installiert Desktop-Dateien und Icons für die Desktop-Integration"""
    if sys.platform.startswith('linux'):
        try:
            # Desktop-Datei installieren
            desktop_file = "bash-script-maker.desktop"
            icon_file = "assets/bash-script-maker.svg"
            
            # Zielverzeichnisse
            applications_dir = Path.home() / ".local" / "share" / "applications"
            icons_dir = Path.home() / ".local" / "share" / "icons" / "hicolor" / "scalable" / "apps"
            
            # Verzeichnisse erstellen
            applications_dir.mkdir(parents=True, exist_ok=True)
            icons_dir.mkdir(parents=True, exist_ok=True)
            
            # Desktop-Datei kopieren
            if os.path.exists(desktop_file):
                shutil.copy2(desktop_file, applications_dir / desktop_file)
                print(f"Desktop-Datei installiert: {applications_dir / desktop_file}")
            
            # Icon kopieren
            if os.path.exists(icon_file):
                shutil.copy2(icon_file, icons_dir / "bash-script-maker.svg")
                print(f"Icon installiert: {icons_dir / 'bash-script-maker.svg'}")
            
            # Desktop-Datenbank aktualisieren
            try:
                import subprocess
                subprocess.run(["update-desktop-database", str(applications_dir)], check=False)
                subprocess.run(["gtk-update-icon-cache", "-f", "-t", str(icons_dir.parent)], check=False)
            except (subprocess.CalledProcessError, FileNotFoundError):
                pass  # Nicht kritisch, Desktop wird trotzdem funktionieren
                
        except Exception as e:
            print(f"Warnung: Desktop-Integration konnte nicht installiert werden: {e}")


VERSION = read_version()
LONG_DESCRIPTION = read_readme()
REQUIREMENTS = read_requirements()

setup(
    name="bash-script-maker",
    version=VERSION,
    author="Marc",
    author_email="",  # Add your email here
    description="Ein GUI-Programm zur Erstellung von Bash-Scripts mit visueller Unterstützung",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/securebitsorg/bash-script-maker",  # Update with your GitHub URL
    license="MIT",
    packages=[],
    py_modules=["bash_script_maker", "syntax_highlighter"],
    include_package_data=True,
    install_requires=REQUIREMENTS,
    extras_require={
        "dev": [
            "pytest>=6.0.0",
            "pytest-cov>=2.10.0",
            "flake8>=3.8.0",
            "black>=21.0.0",
            "mypy>=0.800",
            "tox>=3.20.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "bash-script-maker=bash_script_maker:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Utilities",
        "Topic :: Text Editors :: Integrated Development Environments (IDE)",
        "Topic :: Software Development :: Code Generators",
    ],
    keywords="bash script gui editor generator linux",
    python_requires=">=3.8",
    project_urls={
        "Bug Reports": "https://github.com/securebitsorg/bash-script-maker/issues",
        "Source": "https://github.com/securebitsorg/bash-script-maker",
        "Documentation": "https://github.com/securebitsorg/bash-script-maker#readme",
    },
)

# Desktop-Integration nach der Installation
if len(sys.argv) > 1 and sys.argv[1] == 'install':
    install_desktop_files()

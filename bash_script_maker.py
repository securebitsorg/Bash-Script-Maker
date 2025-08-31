#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bash-Script-Maker - Ein GUI-Programm zur Erstellung von Bash-Scripts
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, filedialog
import subprocess
import os
import sys
from datetime import datetime
from syntax_highlighter import EnhancedScriptEditor


class BashScriptMaker:
    def __init__(self, root):
        self.root = root
        self.root.title("Bash-Script-Maker")
        self.root.geometry("1200x800")

        # Script-Variablen
        self.current_script = ""
        self.script_name = "mein_script.sh"

        # GUI erstellen
        self.create_menu()
        self.create_main_interface()
        self.create_command_palette()
        self.create_script_editor()

        # Willkommensnachricht
        self.update_script_content(
            "#!/bin/bash\n# Erstellt mit Bash-Script-Maker\n# "
            + datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            + "\n\n"
        )

    def create_menu(self):
        """Erstellt das Menü der Anwendung"""
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        # Datei-Menü
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Datei", menu=file_menu)
        file_menu.add_command(
            label="Neu", command=self.new_script, accelerator="Ctrl+N"
        )
        file_menu.add_command(
            label="Öffnen", command=self.open_script, accelerator="Ctrl+O"
        )
        file_menu.add_command(
            label="Speichern", command=self.save_script, accelerator="Ctrl+S"
        )
        file_menu.add_command(
            label="Speichern unter",
            command=self.save_script_as,
            accelerator="Ctrl+Shift+S",
        )
        file_menu.add_separator()
        file_menu.add_command(
            label="Beenden", command=self.root.quit, accelerator="Ctrl+Q"
        )

        # Bearbeiten-Menü
        edit_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Bearbeiten", menu=edit_menu)
        edit_menu.add_command(
            label="Rückgängig",
            command=lambda: self.text_editor.edit_undo(),
            accelerator="Ctrl+Z",
        )
        edit_menu.add_command(
            label="Wiederholen",
            command=lambda: self.text_editor.edit_redo(),
            accelerator="Ctrl+Y",
        )
        edit_menu.add_separator()
        edit_menu.add_command(
            label="Ausschneiden",
            command=lambda: self.text_editor.event_generate("<<Cut>>"),
            accelerator="Ctrl+X",
        )
        edit_menu.add_command(
            label="Kopieren",
            command=lambda: self.text_editor.event_generate("<<Copy>>"),
            accelerator="Ctrl+C",
        )
        edit_menu.add_command(
            label="Einfügen",
            command=lambda: self.text_editor.event_generate("<<Paste>>"),
            accelerator="Ctrl+V",
        )

        # Skript-Menü
        script_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Skript", menu=script_menu)
        script_menu.add_command(
            label="Ausführen", command=self.execute_script, accelerator="F5"
        )
        script_menu.add_command(
            label="Als ausführbar markieren", command=self.make_executable
        )
        script_menu.add_separator()
        script_menu.add_command(
            label="Skript-Info anzeigen", command=self.show_script_info
        )

        # Hilfe-Menü
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Hilfe", menu=help_menu)
        help_menu.add_command(label="Über", command=self.show_about)

        # Tastenkombinationen
        self.root.bind("<Control-n>", lambda e: self.new_script())
        self.root.bind("<Control-o>", lambda e: self.open_script())
        self.root.bind("<Control-s>", lambda e: self.save_script())
        self.root.bind("<Control-Shift-S>", lambda e: self.save_script_as())
        self.root.bind("<Control-q>", lambda e: self.root.quit())
        self.root.bind("<F5>", lambda e: self.execute_script())

    def create_main_interface(self):
        """Erstellt die Hauptbenutzeroberfläche"""
        # Hauptframe
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Toolbar
        toolbar = ttk.Frame(main_frame)
        toolbar.pack(fill=tk.X, pady=(0, 5))

        # Script-Name Eingabe
        ttk.Label(toolbar, text="Script-Name:").pack(side=tk.LEFT, padx=(0, 5))
        self.name_entry = ttk.Entry(toolbar, width=30)
        self.name_entry.pack(side=tk.LEFT, padx=(0, 10))
        self.name_entry.insert(0, self.script_name)
        self.name_entry.bind("<KeyRelease>", self.update_script_name)

        # Toolbar Buttons
        ttk.Button(toolbar, text="Neu", command=self.new_script).pack(
            side=tk.LEFT, padx=(0, 5)
        )
        ttk.Button(toolbar, text="Öffnen", command=self.open_script).pack(
            side=tk.LEFT, padx=(0, 5)
        )
        ttk.Button(toolbar, text="Speichern", command=self.save_script).pack(
            side=tk.LEFT, padx=(0, 5)
        )
        ttk.Button(toolbar, text="Ausführen", command=self.execute_script).pack(
            side=tk.LEFT, padx=(0, 5)
        )

        # Statusleiste
        self.status_var = tk.StringVar()
        self.status_var.set("Bereit")
        status_bar = ttk.Label(
            main_frame, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W
        )
        status_bar.pack(fill=tk.X, side=tk.BOTTOM)

    def create_command_palette(self):
        """Erstellt die Befehlspalette mit verfügbaren Komponenten"""
        # Linker Frame für Befehlspalette
        left_frame = ttk.LabelFrame(self.root, text="Befehle & Komponenten", padding=5)
        left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(5, 0), pady=5)

        # Notebook für verschiedene Kategorien
        self.notebook = ttk.Notebook(left_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Grundbefehle Tab
        basic_tab = ttk.Frame(self.notebook)
        self.notebook.add(basic_tab, text="Grundlagen")

        basic_commands = [
            ("#!/bin/bash", "Shebang"),
            ('echo "Hallo Welt"', "Echo-Befehl"),
            ('read -p "Eingabe: " variable', "Eingabe lesen"),
            ("if [ ]; then\nfi", "If-Bedingung"),
            ("for i in {1..10}; do\necho $i\ndone", "For-Schleife"),
            ("while [ ]; do\ndone", "While-Schleife"),
            ("case $var in\n  pattern) ;;\n  *) ;;\nesac", "Case-Anweisung"),
            ("function name() {\n}", "Funktion"),
        ]

        self.create_command_buttons(basic_tab, basic_commands)

        # Zenity Tab
        zenity_tab = ttk.Frame(self.notebook)
        self.notebook.add(zenity_tab, text="Zenity")

        zenity_commands = [
            ('zenity --info --text="Info"', "Info-Dialog"),
            ('zenity --error --text="Fehler"', "Fehler-Dialog"),
            ('zenity --warning --text="Warnung"', "Warnungs-Dialog"),
            ('zenity --question --text="Frage"', "Frage-Dialog"),
            ('result=$(zenity --entry --text="Eingabe")', "Eingabedialog"),
            ("file=$(zenity --file-selection)", "Dateiauswahl"),
            ('zenity --progress --text="Fortschritt"', "Fortschrittsbalken"),
            ('zenity --list --title="Liste" --column="Option"', "Listen-Dialog"),
        ]

        self.create_command_buttons(zenity_tab, zenity_commands)

        # System Tab
        system_tab = ttk.Frame(self.notebook)
        self.notebook.add(system_tab, text="System")

        system_commands = [
            ("ls -la", "Dateien auflisten"),
            ("pwd", "Aktuelles Verzeichnis"),
            ("cd /pfad", "Verzeichnis wechseln"),
            ("mkdir neuer_ordner", "Ordner erstellen"),
            ("rm -rf datei", "Datei/Ordner löschen"),
            ("cp quelle ziel", "Kopieren"),
            ("mv quelle ziel", "Verschieben"),
            ("chmod +x script.sh", "Ausführbar machen"),
            ("ps aux", "Prozesse anzeigen"),
            ("kill PID", "Prozess beenden"),
        ]

        self.create_command_buttons(system_tab, system_commands)

        # Variablen Tab
        variables_tab = ttk.Frame(self.notebook)
        self.notebook.add(variables_tab, text="Variablen")

        variable_commands = [
            ('variable="wert"', "Variable zuweisen"),
            ("echo $variable", "Variable ausgeben"),
            ("${variable:-default}", "Variable mit Default"),
            ("${#variable}", "String-Länge"),
            ("${variable:0:5}", "String extrahieren"),
            ("array=(wert1 wert2)", "Array erstellen"),
            ("echo ${array[0]}", "Array-Element"),
            ("echo ${#array[@]}", "Array-Länge"),
        ]

        self.create_command_buttons(variables_tab, variable_commands)

    def create_command_buttons(self, parent, commands):
        """Erstellt Buttons für Befehle"""
        canvas = tk.Canvas(parent)
        scrollbar = ttk.Scrollbar(parent, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        for cmd, desc in commands:
            btn = ttk.Button(
                scrollable_frame,
                text=desc,
                command=lambda c=cmd: self.insert_command(c),
            )
            btn.pack(fill=tk.X, pady=1, padx=5)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def create_script_editor(self):
        """Erstellt den Script-Editor"""
        # Rechter Frame für Editor
        right_frame = ttk.LabelFrame(self.root, text="Script-Editor", padding=5)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(5, 5), pady=5)

        # Erweiterter Text-Editor mit Syntax-Highlighting
        self.text_editor = EnhancedScriptEditor(right_frame, wrap=tk.WORD)
        self.text_editor.pack(fill=tk.BOTH, expand=True)

    def insert_command(self, command):
        """Fügt einen Befehl in den Editor ein"""
        self.text_editor.insert_command_at_cursor(command)
        self.status_var.set(f"Befehl eingefügt: {command[:30]}...")

    def update_script_content(self, content):
        """Aktualisiert den Script-Inhalt"""
        self.text_editor.delete(1.0, tk.END)
        self.text_editor.insert(1.0, content)

    def update_script_name(self, event=None):
        """Aktualisiert den Script-Namen"""
        self.script_name = self.name_entry.get()

    def new_script(self):
        """Erstellt ein neues Script"""
        if messagebox.askyesno(
            "Neues Script",
            "Möchten Sie ein neues Script erstellen? Nicht gespeicherte Änderungen gehen verloren.",
        ):
            self.script_name = "mein_script.sh"
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(0, self.script_name)
            self.update_script_content(
                "#!/bin/bash\n# Erstellt mit Bash-Script-Maker\n# "
                + datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                + "\n\n"
            )
            self.status_var.set("Neues Script erstellt")

    def open_script(self):
        """Öffnet ein vorhandenes Script"""
        file_path = filedialog.askopenfilename(
            title="Script öffnen",
            filetypes=[("Bash Scripts", "*.sh"), ("Alle Dateien", "*.*")],
        )
        if file_path:
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    content = file.read()
                self.update_script_content(content)
                self.script_name = os.path.basename(file_path)
                self.name_entry.delete(0, tk.END)
                self.name_entry.insert(0, self.script_name)
                self.status_var.set(f"Script geladen: {file_path}")
            except Exception as e:
                messagebox.showerror(
                    "Fehler", f"Fehler beim Laden des Scripts: {str(e)}"
                )

    def save_script(self):
        """Speichert das aktuelle Script"""
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, self.script_name)

        try:
            content = self.text_editor.get(1.0, tk.END).strip()
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(content)
            self.status_var.set(f"Script gespeichert: {file_path}")
        except Exception as e:
            messagebox.showerror("Fehler", f"Fehler beim Speichern: {str(e)}")

    def save_script_as(self):
        """Speichert das Script unter einem neuen Namen"""
        file_path = filedialog.asksaveasfilename(
            title="Script speichern unter",
            defaultextension=".sh",
            filetypes=[("Bash Scripts", "*.sh"), ("Alle Dateien", "*.*")],
        )
        if file_path:
            try:
                content = self.text_editor.get(1.0, tk.END).strip()
                with open(file_path, "w", encoding="utf-8") as file:
                    file.write(content)
                self.script_name = os.path.basename(file_path)
                self.name_entry.delete(0, tk.END)
                self.name_entry.insert(0, self.script_name)
                self.status_var.set(f"Script gespeichert: {file_path}")
            except Exception as e:
                messagebox.showerror("Fehler", f"Fehler beim Speichern: {str(e)}")

    def execute_script(self):
        """Führt das aktuelle Script aus"""
        script_dir = os.path.dirname(os.path.abspath(__file__))
        script_path = os.path.join(script_dir, self.script_name)

        # Script zuerst speichern
        self.save_script()

        try:
            # Script ausführbar machen
            os.chmod(script_path, 0o755)

            # Script ausführen
            result = subprocess.run(
                [script_path], capture_output=True, text=True, cwd=script_dir
            )

            # Ergebnis anzeigen
            output_window = tk.Toplevel(self.root)
            output_window.title("Script-Ausgabe")
            output_window.geometry("600x400")

            text_output = scrolledtext.ScrolledText(output_window, wrap=tk.WORD)
            text_output.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

            if result.stdout:
                text_output.insert(tk.END, "STDOUT:\n" + result.stdout + "\n\n")
            if result.stderr:
                text_output.insert(tk.END, "STDERR:\n" + result.stderr + "\n\n")
            if result.returncode == 0:
                text_output.insert(
                    tk.END,
                    f"Script erfolgreich beendet (Exit-Code: {result.returncode})",
                )
            else:
                text_output.insert(
                    tk.END,
                    f"Script mit Fehler beendet (Exit-Code: {result.returncode})",
                )

            text_output.config(state=tk.DISABLED)

        except Exception as e:
            messagebox.showerror(
                "Fehler", f"Fehler beim Ausführen des Scripts: {str(e)}"
            )

    def make_executable(self):
        """Macht das Script ausführbar"""
        script_dir = os.path.dirname(os.path.abspath(__file__))
        script_path = os.path.join(script_dir, self.script_name)

        try:
            os.chmod(script_path, 0o755)
            self.status_var.set("Script ist nun ausführbar")
        except Exception as e:
            messagebox.showerror(
                "Fehler", f"Fehler beim Ändern der Berechtigungen: {str(e)}"
            )

    def show_script_info(self):
        """Zeigt Informationen über das aktuelle Script"""
        content = self.text_editor.get(1.0, tk.END)
        lines = len(content.split("\n"))
        chars = len(content)

        info = f"Script-Name: {self.script_name}\n"
        info += f"Zeilen: {lines}\n"
        info += f"Zeichen: {chars}\n"
        info += f"Größe: {len(content.encode('utf-8'))} Bytes"

        messagebox.showinfo("Script-Info", info)

    def show_about(self):
        """Zeigt About-Dialog"""
        about_text = """Bash-Script-Maker

Ein GUI-Programm zur einfachen Erstellung von Bash-Scripts.

Funktionen:
• Visuelle Script-Erstellung
• Zenity-Dialog-Integration
• Syntax-Hervorhebung
• Script-Ausführung
• Verschiedene Befehls-Bausteine

Version: 1.0
Erstellt mit Python und Tkinter"""

        messagebox.showinfo("Über Bash-Script-Maker", about_text)


def main():
    root = tk.Tk()
    app = BashScriptMaker(root)
    root.mainloop()


if __name__ == "__main__":
    main()

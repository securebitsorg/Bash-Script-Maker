#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test script to verify all dependencies are working correctly
"""

import sys
import subprocess
import importlib

def run_command(cmd, description):
    """Run a command and return success status"""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ {description}: OK")
            return True
        else:
            print(f"❌ {description}: FAILED")
            print(f"   Error: {result.stderr.strip()}")
            return False
    except Exception as e:
        print(f"❌ {description}: ERROR - {str(e)}")
        return False

def test_import(module_name, description):
    """Test if a module can be imported"""
    try:
        importlib.import_module(module_name)
        print(f"✅ {description}: OK")
        return True
    except ImportError as e:
        print(f"❌ {description}: FAILED - {str(e)}")
        return False
    except Exception as e:
        print(f"⚠️  {description}: WARNING - {str(e)}")
        return True

def main():
    print("=== Bash-Script-Maker Dependency Test ===\n")

    success_count = 0
    total_tests = 0

    # Test Python version
    total_tests += 1
    python_version = sys.version_info
    if python_version >= (3, 8):
        print(f"✅ Python Version {python_version.major}.{python_version.minor}.{python_version.micro}: OK")
        success_count += 1
    else:
        print(f"❌ Python Version {python_version.major}.{python_version.minor}.{python_version.micro}: FAILED (requires 3.8+)")

    # Test core imports
    core_modules = [
        ("tkinter", "Tkinter GUI Library"),
        ("os", "Operating System Interface"),
        ("sys", "System-specific parameters"),
        ("subprocess", "Subprocess management"),
        ("re", "Regular expressions"),
    ]

    for module, description in core_modules:
        total_tests += 1
        if test_import(module, description):
            success_count += 1

    # Test bash_script_maker imports
    bash_modules = [
        ("bash_script_maker", "Main application module"),
        ("syntax_highlighter", "Syntax highlighting module"),
    ]

    for module, description in bash_modules:
        total_tests += 1
        if test_import(module, description):
            success_count += 1

    # Test development tools (optional)
    dev_tools = [
        ("pytest", "pytest testing framework"),
        ("flake8", "flake8 code linter"),
        ("black", "black code formatter"),
        ("mypy", "mypy type checker"),
        ("bandit", "bandit security linter"),
        ("safety", "safety dependency checker"),
        ("twine", "twine package uploader"),
        ("build", "build package builder"),
        ("tox", "tox testing environments"),
    ]

    print(f"\n--- Development Tools (Optional) ---")
    dev_success = 0
    for tool, description in dev_tools:
        if test_import(tool, description):
            dev_success += 1

    print(f"\nDevelopment tools: {dev_success}/{len(dev_tools)} available")

    # Test external commands
    print(f"\n--- External Commands ---")
    commands = [
        ("python3 --version", "Python 3 executable"),
        ("pip --version", "pip package manager"),
    ]

    for cmd, description in commands:
        total_tests += 1
        if run_command(cmd, description):
            success_count += 1

    # Summary
    print(f"\n=== Test Summary ===")
    print(f"Passed: {success_count}/{total_tests} tests")
    print(".1f")

    if success_count == total_tests:
        print("🎉 All tests passed! Bash-Script-Maker is ready to use.")
        return 0
    elif success_count >= total_tests * 0.8:  # 80% success rate
        print("⚠️  Most tests passed. Some optional components might be missing.")
        return 0
    else:
        print("❌ Critical components are missing. Please check the installation.")
        return 1

if __name__ == "__main__":
    sys.exit(main())

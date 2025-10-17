#!/usr/bin/env python
"""
Simple manage.py wrapper to provide a `runserver` command for this project.

Usage:
    python manage.py runserver

It forwards to `Grocery_webapp/backend/server.py` which starts a Flask server on port 5000.
"""
import os
import sys
import subprocess

ROOT_DIR = os.path.dirname(__file__)
BACKEND_SCRIPT = os.path.join(ROOT_DIR, 'Grocery_webapp', 'backend', 'server.py')

def print_help():
    print('Usage: python manage.py runserver')

def runserver():
    if not os.path.exists(BACKEND_SCRIPT):
        print(f"Backend script not found: {BACKEND_SCRIPT}")
        sys.exit(1)
    # Use the same Python executable to run the backend script
    python_exec = sys.executable
    # Execute the backend script in a subprocess so it behaves like the direct run
    subprocess.check_call([python_exec, BACKEND_SCRIPT])

def main():
    if len(sys.argv) < 2:
        print_help()
        sys.exit(1)

    cmd = sys.argv[1]
    if cmd == 'runserver':
        runserver()
    else:
        print(f"Unknown command: {cmd}")
        print_help()

if __name__ == '__main__':
    main()

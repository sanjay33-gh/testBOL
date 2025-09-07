#!/usr/bin/env python3
"""
Simple testBOL application
A basic Python application that can be run to demonstrate functionality.
"""

import sys
from datetime import datetime

def main():
    """Main application function"""
    print("=" * 50)
    print("🚀 Welcome to testBOL Application! 🚀")
    print("=" * 50)
    print(f"📅 Current time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"🐍 Python version: {sys.version}")
    print("=" * 50)
    print("✅ Application is running successfully!")
    print("💡 This is a simple test application for the testBOL repository.")
    print("=" * 50)

if __name__ == "__main__":
    main()
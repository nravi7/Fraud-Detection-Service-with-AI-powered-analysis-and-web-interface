#!/usr/bin/env python3
"""
Simple startup script for the Fraud Detection Service
"""
import os
import sys
import subprocess

def main():
    print("🛡️  Starting Fraud Detection Service by Ravi N...")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not os.path.exists("app/main.py"):
        print("❌ Error: Please run this script from the project root directory")
        sys.exit(1)
    
    # Set OpenAI API key if provided
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key:
        print(f"✅ OpenAI API key found: {api_key[:20]}...")
    else:
        print("⚠️  No OpenAI API key found - using demo mode")
        print("   Set OPENAI_API_KEY environment variable for full functionality")
    
    print("\n🚀 Starting server on http://localhost:8000")
    print("📖 API docs available at http://localhost:8000/docs")
    print("🌐 Web interface at http://localhost:8000")
    print("\nPress Ctrl+C to stop the server")
    print("=" * 50)
    
    try:
        # Start the server
        subprocess.run([
            sys.executable, "-m", "uvicorn", 
            "app.main:app", 
            "--reload", 
            "--port", "8000",
            "--host", "127.0.0.1"
        ])
    except KeyboardInterrupt:
        print("\n\n👋 Server stopped. Goodbye!")
    except Exception as e:
        print(f"\n❌ Error starting server: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

"""
Convenience Launcher for SmartStock AI.
Allows starting both the FastAPI backend and Streamlit frontend.
"""

import subprocess
import sys
import time
import os

def launch():
    print("=" * 60)
    print("🚀 Launching SmartStock AI Platform")
    print("=" * 60)
    print("1. Starting FastAPI Backend on http://127.0.0.1:8000...")
    backend = subprocess.Popen([
        sys.executable, "-m", "uvicorn", "backend.main:app",
        "--host", "127.0.0.1", "--port", "8000"
    ])

    time.sleep(2)

    print("2. Launching Streamlit Frontend on http://localhost:8501...")
    try:
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", "frontend/app.py"
        ])
    except KeyboardInterrupt:
        pass
    finally:
        print("\nShutting down backend...")
        backend.terminate()
        try:
            backend.wait(timeout=3)
        except Exception:
            backend.kill()
        print("Shutdown complete. All services stopped.")

if __name__ == "__main__":
    launch()


import subprocess
import sys

def main():
    # Run the voice_capture.py script
    subprocess.run([sys.executable, 'voice/voice_capture.py'])


if __name__ == "__main__":
    main()
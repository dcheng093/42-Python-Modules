import os
import site
import sys


def main():
    in_venv = sys.prefix != sys.base_prefix
    python_executable = sys.executable

    if in_venv:
        venv_path = sys.prefix
        venv_name = os.path.basename(venv_path)

        # Package location inside the virtual environment
        current_packages = site.getsitepackages()[0]

        print("\nMATRIX STATUS: Welcome to the construct\n")
        print(f"Current Python: {python_executable}")
        print(f"Virtual Environment: {venv_name}")
        print(f"Environment Path: {venv_path}\n")

        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.\n")

        print("Virtual environment packages:")
        print(current_packages)

    else:
        # Current and global are the same when not using a venv

        print("\nMATRIX STATUS: You're still plugged in\n")
        print(f"Current Python: {python_executable}")
        print("Virtual Environment: None detected\n")

        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")
        print("\nTo enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate  # On Unix")
        print(r"matrix_env\Scripts\activate     # On Windows")
        print("\nThen run this program again.")


if __name__ == "__main__":
    main()

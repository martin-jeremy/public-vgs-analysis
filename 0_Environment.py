import os
import subprocess
import venv

if __name__ == "__main__":
    # Define the directory for venv
    venv_dir = '.venv'

    # Create venv
    venv.create(venv_dir, with_pip=True)

    # Echo
    print(f"Virtual environment created at {os.path.abspath(venv_dir)}")

    # Install needed packages
    packages = ['requests', 'numpy', 'scipy', 'pandas', 'scikit-learn', 'matplotlib', 'seaborn', 'pyarrow']
    pip_ex = os.path.join(venv_dir, 'bin', 'pip') if os.name != 'nt' else os.path.join(venv_dir, 'Scripts', 'pip.exe')
    [subprocess.check_call([pip_ex, 'install', '-U', package]) for package in packages]

    print(f"Packages installed in {os.path.abspath(venv_dir)}")
    [subprocess.check_call([pip_ex, 'show', package]) for package in packages]

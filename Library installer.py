import subprocess

def install_libraries(file_name: str):
    """
    Installs all the libraries listed in a requirements.txt file.
    """
    with open(file_name) as f:
        libraries = f.read().splitlines()
    for library in libraries:
        subprocess.run(["pip", "install", library])

install_libraries("requirements.txt")
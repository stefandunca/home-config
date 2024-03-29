import sh
import sys
import tempfile

from setup.helpers.helpers import out, echo

def is_docker_installed():
    try:
        sh.docker("--version", **out)
        return True
    except sh.ErrorReturnCode:
        return False

def install_docker():
    try:
        echo("Downloading Docker installation script...")

        with tempfile.TemporaryDirectory() as temp_dir:
            script_path = f"{temp_dir}/get-docker.sh"
            sh.curl("-fsSL", "https://get.docker.com", "-o", script_path, **out)
            
            echo("Running Docker installation script...")
            sh.sudo("sh", script_path, **out)
            
            echo("Docker installed successfully.")
    except sh.ErrorReturnCode as e:
        echo(f"An error occurred during Docker installation: {e}", err=True)
        sys.exit(1)
    except Exception as e:
        echo(f"Unexpected error: {e}", err=True)
        sys.exit(1)

def install_docker_compose():
    try:
        echo("Installing Docker Compose...")
        sh.sudo("pip3", "install", "docker-compose", **out)
        echo("Docker Compose installed successfully.")
    except sh.ErrorReturnCode as e:
        echo(f"An error occurred during Docker Compose installation: {e}", err=True)
        sys.exit(1)

def install():
    if not is_docker_installed():
        install_docker()
    else:
        echo("Docker is already installed.")

    install_docker_compose()

if __name__ == "__main__":
    install()
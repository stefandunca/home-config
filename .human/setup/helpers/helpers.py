import os
import re
import sh
import click
import requests
import tempfile
from enum import Enum
import platform
from typing import Literal, Union

from urllib.parse import urlparse

out = {'_out': click.get_text_stream('stdout'),
    '_err': click.get_text_stream('stderr')
    }

def echo(message: str, *args, err=False, **kwargs):
    args_str = f"; {args}" if args else ""
    kwargs_str = f"; {kwargs}" if kwargs else ""
    color_code = '\033[91m' if err else '\033[92m'  # Red for error, green otherwise
    click.echo(f'{color_code}HUMAN: {message}{args_str}{kwargs_str}\033[0m')

def download(url: str, file: str):
    with requests.get(url, stream=True) as r:
        with open(file, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)


def download_script_and_run(url: str, filename: str = None):
    with tempfile.TemporaryDirectory() as tmpdir:
        if filename is None:
            parsed_url = urlparse(url)
            if parsed_url.path:
                filename = os.path.basename(parsed_url.path)
            else:
                filename = "downloaded_script.sh"

        tmpfile = os.path.join(tmpdir, "downloaded_{filename}")
        echo(f"download and install {url}")
        download(url, tmpfile)
        sh.sh(tmpfile, **out)


def append_if_missing(file_path, regex, new_content):
    """
    File is not created if missing
    return True if file was modified
    """
    if not os.path.exists(file_path):
        return False

    with open(file_path, 'a+') as f:
        f.seek(0)
        content = f.read()
        if not re.match(regex, content, re.DOTALL):
            f.write(new_content)

            return True
    return False


def replace_line_matching(file_path, regex, new_content):
    """
    File is not created if missing
    return True if file was modified
    """
    if not os.path.exists(file_path):
        return False

    ret = False
    with open(file_path, 'r+') as f:
        content = f.readlines()
        if new_content not in content:
            f.seek(0)
            for line in content:
                if re.match(regex, line):
                    f.write(new_content)
                    ret = True
                else:
                    f.write(line)
            f.truncate()

    return ret



class OSType(Enum):
    UBUNTU = "Ubuntu"
    MACOS = "macOS"
    UNKNOWN = "Unknown"


def which_os() -> OSType:
    system = platform.system()
    
    if system == "Linux":
        distro = platform.freedesktop_os_release().get("ID", "")
        if distro == "ubuntu":
            return OSType.UBUNTU
    elif system == "Darwin":
        return OSType.MACOS
    
    return OSType.UNKNOWN

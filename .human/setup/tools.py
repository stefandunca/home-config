#!python
# first: `source ~/.human/.venv/bin/activate`
import os
import sys
from dataclasses import dataclass

from typing import List

from helpers.helpers import *
from packages import *

script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(script_dir)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from tools.install_docker import install as install_docker

base: List[Package] = [
    Package("zsh"),
    Package("git"),
    Package("curl"),
    Package("wget"),
    Package("htop"),
    Package("mc"),
    Package("tree"),
    Package("xclip"),
    Package("nano"),
    Package("uv"),
]

workstation_base: List[Package] = [
    Package("dict"),
    Package("p7zip"),
    Package("vim"),
    Package("util-linux", apt="util-linux"),
    Package("rmlint"),
    StrictPackage("gparted", apt="gparted"),
    Package("borg", apt="borgbackup", brew="borgbackup"),

    # Standard Packages
    StrictPackage("yay", pacman="yay", allow=["manjaro"]),

    # Software Packages
    Package("vlc", brew=None, brew_cask="vlc"),
    Package("gimp", brew=None, brew_cask="gimp"),
    Package("inkscape", brew=None, brew_cask="inkscape"),

    # Misc
    Package("cheat")
]

dev_base: List[Package] = [
    Package("bench"),
    StrictPackage("net-tools", apt="net-tools"),
    Package("docker-credential-helper", brew="docker-credential-helper"),
    Package("docker", brew="docker"),
    Package("colima", brew="colima"),

    # Standard Packages
    Package("git-extras"),
    StrictPackage("base-devel", apt="build-essential"),
]

dev: List[Package] = [
    Package("kubectl"),
]

upgrade()

install(base)

os_type: OSType = which_os()

if not is_raspberry_pi():
    install([*workstation_base, *dev_base, *dev])

if os_type is not OSType.MACOS:
    install_docker()
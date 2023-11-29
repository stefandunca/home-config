#!/usr/bin/env python3
import os
import sys
from dataclasses import dataclass

from typing import List

from helpers import *
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

    PipPackage("shell-gpt"),
    PipPackage("watchdog"),
]

workstation_base: List[Package] = [
    Package("dict"),
    Package("p7zip"),
    Package("vim"),
    Package("util-linux"),
    Package("rmlint"),
    Package("bench"),
    Package("gparted"),
    Package("net-tools"),
    Package("borg", apt="borgbackup", brew="borgbackup"),

    # Standard Packages
    Package("git-extras"),
    Package("yay", pacman="yay", allow=["manjaro"]),
    Package("base-devel", apt="build-essential"),

    # Software Packages
    Package("vscode", aur="visual-studio-code-bin", deb="https://code.visualstudio.com/sha/download?build=stable&os=linux-deb-x64", brew_cask="visual-studio-code", deny=["wsl"]),

    # Java Packages
    Package("java", apt="default-jre", pacman="jre-openjdk", choco="javaruntime", brew_cask="temurin"),

    # Misc
    Package("cheat", brew="cheat")
]

install(base)

# Call the function to install Docker
install_docker()
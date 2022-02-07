from enum import IntEnum, auto
from dataclasses import dataclass

import subprocess

import yaml


class OS(IntEnum):
    ARCH = auto()
    UBUNTU = auto()

class Environment(IntEnum):
    HOST = auto()
    CONSOLE = auto()
    SERVER = auto()

@dataclass
class PackageDefinition:
    name: str
    desc: str
    os: OS
    env: Environment

class PackageInstaller:
    def install(package: PackageDefinition):
        args = ["pacman", "-Suy"]
        args.append(package.name)
        with subprocess.Popen(args) as p:
            print(p.stdout.read())

class PackageGenerator:
    def __init__(elem, name:str = ""):
        if isinstance(elem, str):
            PackageDefinition
        else:
            print(elem['src'], ": ", pkg_item)

def parse_file(file_path: str = "packages.yaml"):
    with open(file_path, 'r') as stream:
        parse_packages_definitions(stream)

def parse_packages_definitions(stream):
    try:
        pack_objs = yaml.safe_load(stream)

        for pkg_set_name, pkg_set_items in pack_objs.items():
            if isinstance(pkg_set_items, list):
                for pkg_item in pkg_set_items:
                    pack = PackageGenerator(pkg_set_items)
            else:
                if isinstance(pkg_set_items, str):
                    print("pacman: ", pkg_set_items)
                else:
                    print(type(pkg_set_items))
                    print(pkg_set_items)
    except yaml.YAMLError as exc:
        print(exc)
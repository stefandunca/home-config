import sh
import shutil

from typing import List, Tuple

from helpers.helpers import echo, out

class Package:
    def __init__(self, name: str, allow=None, **targets):
        self.name = name
        self.targets = targets

    def get_package(self, target: str) -> Tuple[str, bool]:
        """returns (<package name>, <if registered for target>)"""
        return self.targets.get(target, self.name), ((not self.targets) or (target in self.targets))

class PipPackage(Package):
    def __init__(self, name, **targets):
        super().__init__(name, pip=name, **targets)

def install(list: List[Package]):
    if shutil.which("apt") is not None:
        echo("Update apt packages")
        sh.sudo.apt("update", **out)
        sh.sudo.apt("upgrade", "-y", **out)

        packages = get_names_for(list, "apt")
        echo("Install apt", packages=packages)
        sh.sudo.apt("install", "-y", *packages, **out)

def get_names_for(list: List[Package], target: str):
    res = []
    for p in list:
        name, found = p.get_package(target)
        if found:
            res.append(name)
    return res
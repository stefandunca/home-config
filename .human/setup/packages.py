import sh

from typing import List, Tuple

from helpers.helpers import echo, out, OSType, which_os

class Package:
    def __init__(self, name: str, specific: bool = False, **targets):
        """if specific is False, the name is used as package for all targets"""
        self.name = name
        self.targets = targets
        self.name_as_package = not specific

    def get_package(self, target: str, strict = False) -> Tuple[str, bool]:
        """returns (<package name>, <if specifically registered for target>)"""
        package, found = self.targets.get(target, self.name), ((self.name_as_package and not strict) or target in self.targets)
        return package if package is not None else self.name, found and package is not None

class StrictPackage(Package):
    def __init__(self, name, **targets):
        super().__init__(name, specific=True, **targets)

def upgrade():
    os_type: OSType = which_os()
    if os_type is OSType.UBUNTU:
        echo("Update apt packages")
        sh.sudo.apt("update", **out)
        sh.sudo.apt("upgrade", "-y", **out)
    elif os_type == OSType.MACOS:
        echo("Update brew packages")
        sh.brew("update", **out)
        sh.brew("upgrade", **out)
    else:
        echo("Unsupported OS", os_type=os_type)
        return


def install(list: List[Package]):
    os_type: OSType = which_os()
    if os_type is OSType.UBUNTU:
        packages = get_names_for(list, "apt")
        echo("Install apt", packages=packages)
        sh.sudo.apt("install", "-y", *packages, **out)
    elif os_type == OSType.MACOS:
        packages = get_names_for(list, "brew")
        installed = sh.brew("leaves").splitlines()
        new = [p for p in packages if p not in installed]
        if new:
            echo("Install brew", packages=new)
            sh.brew("install", *new, **out)

        installed = sh.brew("list", "--cask").split()
        packages = get_names_for(list, "brew_cask", strict=True)
        new = [p for p in packages if p not in installed]
        if new:
            echo("Install brew cask", packages=new)
            sh.brew("install", "--cask", *new, **out)
    else:
        echo("Unsupported OS", os_type=os_type)
        return


def get_names_for(list: List[Package], target: str, strict = False) -> List[str]:
    """If strict is True, only return packages that are specifically registered for the target"""
    res = []
    for p in list:
        name, found = p.get_package(target, strict)
        if found:
            res.append(name)
    return res
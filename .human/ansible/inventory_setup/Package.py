from PySide6 import QtCore
from PySide6 import QtQuick
from PySide6 import QtQml

from CustomApt import CustomApt
from CustomBrewTap import CustomBrewTap

from __feature__ import snake_case, true_property

QML_IMPORT_NAME = "dev.dunca.home"
QML_IMPORT_MAJOR_VERSION = 1

@QtQml.QmlElement
class Package(QtQuick.QQuickItem):
    def __init__(self):
        QtQuick.QQuickItem.__init__(self)
        self.exclude_val = False    # True ensures it is removed and installed otherwise
        # Only include package if these labels are in the allow list
        self.allowlist_val = list()
        # Don't include package if these labels are in the allow list
        self.denylist_val = list()
        # Only allow if attached labes are in this list
        self.targets = {"pacman": None, "aur": None, "apt": None,
                        "snap": None, "choco": None, "pip": None,
                        "deb": None, "custom_apt": None, "brew": None, "brew_cask": None, "brew_tap": None}

    # `name` property
    @QtCore.Signal
    def name_changed(self):
        pass

    @QtCore.Property(str, notify=name_changed)
    def name(self):
        return self.object_name

    @name.setter
    def name(self, val):
        if val == self.object_name:
            return
        self.object_name = val

    # `pacman` property
    @QtCore.Signal
    def pacman_changed(self):
        pass

    @QtCore.Property(str, notify=pacman_changed)
    def pacman(self):
        return self.targets["pacman"]

    @pacman.setter
    def pacman(self, val):
        if val == self.targets["pacman"]:
            return
        self.targets["pacman"] = val
        self.pacman_changed.emit()

    # `aur` property
    @QtCore.Signal
    def aur_changed(self):
        pass

    @QtCore.Property(str, notify=aur_changed)
    def aur(self):
        return self.targets["aur"]

    @aur.setter
    def aur(self, val):
        if val == self.targets["aur"]:
            return
        self.targets["aur"] = val
        self.aur_changed.emit()

    # `apt` property
    @QtCore.Signal
    def apt_changed(self):
        pass

    @QtCore.Property(str, notify=apt_changed)
    def apt(self):
        return self.targets["apt"]

    @apt.setter
    def apt(self, val):
        if val == self.targets["apt"]:
            return
        self.targets["apt"] = val
        self.apt_changed.emit()

    # `snap` property
    @QtCore.Signal
    def snap_changed(self):
        pass

    @QtCore.Property(str, notify=snap_changed)
    def snap(self):
        return self.targets["snap"]

    @snap.setter
    def snap(self, val):
        if val == self.targets["snap"]:
            return
        self.targets["snap"] = val
        self.snap_changed.emit()

    # `choco` property
    @QtCore.Signal
    def choco_changed(self):
        pass

    @QtCore.Property(str, notify=choco_changed)
    def choco(self):
        return self.targets["choco"]

    @choco.setter
    def choco(self, val):
        if val == self.targets["choco"]:
            return
        self.targets["choco"] = val
        self.choco_changed.emit()

    # `pip` property
    @QtCore.Signal
    def pip_changed(self):
        pass

    @QtCore.Property(str, notify=pip_changed)
    def pip(self):
        return self.targets["pip"]

    @pip.setter
    def pip(self, val):
        if val == self.targets["pip"]:
            return
        self.targets["pip"] = val
        self.pip_changed.emit()

    # `deb` property
    @QtCore.Signal
    def deb_changed(self):
        pass

    @QtCore.Property(str, notify=deb_changed)
    def deb(self):
        return self.targets["deb"]

    @deb.setter
    def deb(self, val):
        if val == self.targets["deb"]:
            return
        self.targets["deb"] = val
        self.deb_changed.emit()

    # `custom_apt` property
    @QtCore.Signal
    def custom_apt_changed(self):
        pass

    @QtCore.Property(CustomApt, notify=custom_apt_changed)
    def custom_apt(self):
        return self.targets["custom_apt"]

    @custom_apt.setter
    def custom_apt(self, val):
        if val == self.targets["custom_apt"]:
            return
        self.targets["custom_apt"] = val
        self.custom_apt_changed.emit()

    # `brew` property
    @QtCore.Signal
    def brew_changed(self):
        pass

    @QtCore.Property(str, notify=brew_changed)
    def brew(self):
        return self.targets["brew"]

    @brew.setter
    def brew(self, val):
        if val == self.targets["brew"]:
            return
        self.targets["brew"] = val
        self.brew_changed.emit()

    # `brew_cask` property
    @QtCore.Signal
    def brew_cask_changed(self):
        pass

    @QtCore.Property(str, notify=brew_cask_changed)
    def brew_cask(self):
        return self.targets["brew_cask"]

    @brew_cask.setter
    def brew_cask(self, val):
        if val == self.targets["brew_cask"]:
            return
        self.targets["brew_cask"] = val
        self.brew_cask_changed.emit()

    # `brew_tap` property
    @QtCore.Signal
    def brew_tap_changed(self):
        pass

    @QtCore.Property(CustomBrewTap, notify=brew_tap_changed)
    def brew_tap(self):
        return self.targets["brew_tap"]

    @brew_tap.setter
    def brew_tap(self, val):
        if val == self.targets["brew_tap"]:
            return
        self.targets["brew_tap"] = val
        self.brew_tap_changed.emit()

    # `exclude` property
    # If False install package. If True ensure it is removed
    @QtCore.Signal
    def exclude_changed(self):
        pass

    @QtCore.Property(bool, notify=exclude_changed)
    def exclude(self):
        return self.exclude_val

    @exclude.setter
    def exclude(self, val):
        if val == self.exclude_val:
            return
        self.exclude_val = val
        self.exclude_changed.emit()

    # `allowlist` property
    # List of labels. Install if allowlisted labels are defined otherwise not
    @QtCore.Signal
    def allowlist_changed(self):
        pass

    @QtCore.Property('QVariantList', notify=allowlist_changed)
    def allowlist(self):
        return self.allowlist_val

    @allowlist.setter
    def allowlist(self, val):
        if val == self.allowlist_val:
            return
        self.allowlist_val = val
        self.allowlist_changed.emit()

    # List of supported package managers
    def supported_targets(self):
        return [k for k, v in self.targets.items() if v != None]

    # `denylist` property
    # List of labels. Don't install if deny labels are defined
    @QtCore.Signal
    def denylist_changed(self):
        pass

    @QtCore.Property('QVariantList', notify=denylist_changed)
    def denylist(self):
        return self.denylist_val

    @denylist.setter
    def denylist(self, val):
        if val == self.denylist_val:
            return
        self.denylist_val = val
        self.denylist_changed.emit()

    # List of supported package managers
    def supported_targets(self):
        return [k for k, v in self.targets.items() if v != None]
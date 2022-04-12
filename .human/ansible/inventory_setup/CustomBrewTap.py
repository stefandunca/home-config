from PySide6 import QtCore
from PySide6 import QtQuick
from PySide6 import QtQml

from properties import PropertyMeta, Property

from __feature__ import snake_case, true_property

QML_IMPORT_NAME = "dev.dunca.home"
QML_IMPORT_MAJOR_VERSION = 1

@QtQml.QmlElement
class CustomBrewTap(QtCore.QObject, metaclass=PropertyMeta):
    brew = Property(str)
    cask = Property(str)
    tap = Property(str)

    def __init__(self):
        QtCore.QObject.__init__(self)

    def getPropertyNames(self):
        # brew and cask are optional
        return [prop for prop in ["brew", "cask"] if hasattr(self, prop) and getattr(self, prop)] + ["tap"]
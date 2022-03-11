from PySide6.QtCore import QObject
from PySide6 import QtQuick
from PySide6 import QtQml

from properties import PropertyMeta, Property

from __feature__ import snake_case, true_property

QML_IMPORT_NAME = "dev.dunca.home"
QML_IMPORT_MAJOR_VERSION = 1

@QtQml.QmlElement
class CustomApt(QtQuick.QQuickItem, metaclass=PropertyMeta):
    name = Property(str)
    key = Property(str)

    def __init__(self):
        QtQuick.QQuickItem.__init__(self)
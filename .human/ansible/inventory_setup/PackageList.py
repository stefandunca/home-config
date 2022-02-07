# This Python file uses the following encoding: utf-8
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine, QmlElement, QmlSingleton
from PySide6.QtCore import QObject, Property, Signal, Slot
from PySide6.QtQuick import QQuickItem

from __feature__ import snake_case, true_property

QML_IMPORT_NAME = "dev.dunca.home"
QML_IMPORT_MAJOR_VERSION = 1

@QmlElement
class PackageList(QQuickItem):
    def __init__(self):
        QQuickItem.__init__(self)

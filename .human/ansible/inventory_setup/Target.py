from PackageList import PackageList

from PySide6 import QtCore
from PySide6 import QtQuick
from PySide6 import QtQml

from __feature__ import snake_case, true_property

QML_IMPORT_NAME = "dev.dunca.home"
QML_IMPORT_MAJOR_VERSION = 1

@QtQml.QmlElement
class Target(QtCore.QObject):
    def __init__(self):
        QtCore.QObject.__init__(self)
        self.package_list_val = list()
        self.host_val = None
        self.allow_labels_val = list()

    # Host property
    @QtCore.Signal
    def host_changed(self):
        pass

    @QtCore.Property(str, notify=host_changed)
    def host(self):
        return self.host_val

    @host.setter
    def host(self, val):
        if val == self.host_val:
            return
        self.host_val = val
        self.host_changed.emit()

    # package_list property
    @QtCore.Signal
    def package_list_changed(self):
        pass

    @QtCore.Property('QVariantList', notify=package_list_changed)
    def package_list(self):
        return self.package_list_val

    @package_list.setter
    def package_list(self, val):
        if val == self.package_list_val:
            return
        self.package_list_val = val
        self.package_list_changed.emit()

    # `allow_labels` property
    # List of labels. Install if allowed labels are defined otherwise not
    @QtCore.Signal
    def allow_labels_changed(self):
        pass

    @QtCore.Property('QVariantList', notify=allow_labels_changed)
    def allow_labels(self):
        return self.allow_labels_val

    @allow_labels.setter
    def allow_labels(self, val):
        if val == self.allow_labels_val:
            return
        self.allow_labels_val = val
        self.allow_labels_changed.emit()
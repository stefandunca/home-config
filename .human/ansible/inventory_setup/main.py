# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys
import argparse

from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine, QmlElement, QmlSingleton
from PySide6.QtCore import QObject, Property, Signal, Slot
from PySide6.QtQuick import QQuickItem
from __feature__ import snake_case, true_property

from Package import Package
from PackageList import PackageList
from Target import Target

import yaml

QML_IMPORT_NAME = "dev.dunca.home"
QML_IMPORT_MAJOR_VERSION = 1

@QmlElement
class AnsibleVarsExporter(QQuickItem):
    def __init__(self):
        QQuickItem.__init__(self)

    def process_configuration(self, out_dir):
        targets = list()
        for item in self.children():
            if type(item) is Target:
                targets.append(item)

        for target in targets:
            present = dict()
            not_present = dict()
            for item in target.package_list:
                if type(item) is PackageList:
                    for p in item.children():
                        for pm in p.supported_targets():
                            if p.exclude:
                                if pm not in not_present:
                                    not_present[pm] = list()
                                not_present[pm].append(p[pm])
                            else:
                                if pm not in present:
                                    present[pm] = list()
                                present[pm].append(getattr(p, pm))
            content = dict()
            if len(present) > 0:
                content["present"] = present
            if len(not_present) > 0:
                content["not_present"] = not_present

            if len(content):
                fname = target.host + ".yaml"
                fpath = os.path.join(out_dir, fname)
                f = open(fpath, "w")
                f.write(yaml.dump(content))
                f.close()


#
# Script entry
if __name__ == "__main__":
    # Parse command line
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", "-f", type=str, required=True)
    parser.add_argument("--output_dir", "-o", type=str, required=True)
    args = parser.parse_args()

    # Construct qml engine with it's dependencies
    app = QGuiApplication(sys.argv + ["QT_QPA_PLATFORM", "minimal"])
    engine = QQmlApplicationEngine()

    # Load and process QML configuration file
    engine.load(os.path.abspath(args.config))
    if not engine.root_objects():
        sys.exit(-1)

    # Expect that root dir is an AnsibleVarsExporter
    package_exporter = engine.root_objects()[0]
    if type(package_exporter) == AnsibleVarsExporter:
        package_exporter.process_configuration(args.output_dir)
    else:
        print("Wrong root QML item for the configuration file:", args.config, "; type", type(package_exporter), "; expected AnsibleVarsExporter")
        sys.exit(-2)

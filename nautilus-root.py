#!/usr/bin/env python3

import os, subprocess
from gi.repository import Nautilus, GObject

class NautilusRoot(Nautilus.MenuProvider, GObject.GObject):
    def __init__(self):
        pass

    def get_background_items(self, window, file):
        items = []
        self.window = window
        items += [self._create_background_item(file)]
        return items

    def _create_background_item(self, file):
        item = Nautilus.MenuItem(name="NautilusRoot::OpenAsRoot",
                                 label="Open as root",
                                 tip="Secure run")
        item.connect("activate", self._Terminal_run, file)
        return item

    def _Terminal_run(self, menu, file):
        subprocess.Popen(["/usr/bin/nautilus-root", file.get_location().get_path()])


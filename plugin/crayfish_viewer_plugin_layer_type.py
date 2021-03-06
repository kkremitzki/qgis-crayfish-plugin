# -*- coding: utf-8 -*-

# Crayfish - A collection of tools for TUFLOW and other hydraulic modelling packages
# Copyright (C) 2014 Lutra Consulting

# info at lutraconsulting dot co dot uk
# Lutra Consulting
# 23 Chestnut Close
# Burgess Hill
# West Sussex
# RH15 8HN

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *

from crayfish_viewer_plugin_layer import CrayfishViewerPluginLayer
from crayfish_viewer_plugin_layer_props_dialog import CrayfishViewerPluginPropsDialog

class CrayfishViewerPluginLayerType(QgsPluginLayerType):

    def __init__(self):
        QgsPluginLayerType.__init__(self, CrayfishViewerPluginLayer.LAYER_TYPE)

    def createLayer(self, uri=None):
        if uri:
            return CrayfishViewerPluginLayer(uri)
        else:
            return CrayfishViewerPluginLayer()

    def showLayerProperties(self, layer):
        dlg = CrayfishViewerPluginPropsDialog(layer)
        dlg.exec_()
        return True

# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Regionalization
                                 A QGIS plugin
 Pruebas de regionalizacion
                              -------------------
        begin                : 2014-03-03
        copyright            : (C) 2014 by CentroGeo
        email                : pablo.lopez@centrogeo.edu.mx
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
# Initialize Qt resources from file resources.py
import resources_rc
# Import the code for the dialog
from regionalizationdialog import RegionalizationDialog
import os.path
log = lambda m: QgsMessageLog.logMessage(m,'My Plugin') 


class Regionalization:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value("locale/userLocale")[0:2]
        localePath = os.path.join(self.plugin_dir, 'i18n', 'regionalization_{}.qm'.format(locale))

        if os.path.exists(localePath):
            self.translator = QTranslator()
            self.translator.load(localePath)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Create the dialog (after translation) and keep reference
        self.dlg = RegionalizationDialog()

    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(
            QIcon(":/plugins/regionalization/icon.png"),
            u"Pruebas de regionalizacion", self.iface.mainWindow())
        # connect the action to the run method
        self.action.triggered.connect(self.run)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu(u"&Regionalization", self.action)

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu(u"&Regionalization", self.action)
        self.iface.removeToolBarIcon(self.action)

    # run method that performs all the real work
    def run(self):
        # show the dialog
 
        capa = self.iface.activeLayer()
        campos = capa.pendingFields()
        lista = self.dlg.listWidget  
        for c in campos:
            item =   QListWidgetItem(c.name())
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
            item.setCheckState(Qt.Unchecked)
            lista.addItem(item)


        self.dlg.show()        
        result = self.dlg.exec_()
        # See if OK was pressed
        if result == 1:
            
            selected=[]
            for index in xrange( lista.count()):
                itm = lista.item(index)
                if itm.checkState()==2:
                    selected.append(itm.text())
                      
            iter = capa.getFeatures()
            indices = [capa.fieldNameIndex(n) for n in selected]
            renglones= []
            for f in iter:
                renglones.append([f.attributes()[j] for j in indices])
            

#             
#             values = []
#             for i,j in enumerate(indices):
#                 values.append([])
#                 
#             for f in iter:
#                 for i,j in enumerate(indices):
#                     values[i].append(f.attributes()[j])
#  
#             distancias = []
#             dif=[[]for l in values]
#             for k,l in enumerate(values):
#                 for i in l:
#                     for j in range(0,len(l)):
#                         dif[k].append(i-l[j])
                        
            # do something useful (delete the line containing pass and
            QMessageBox.information( self.iface.mainWindow(),"Info",str(renglones))
            

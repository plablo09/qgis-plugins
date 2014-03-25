# -*- coding: utf-8 -*-
"""
/***************************************************************************
 MaxP
                                 A QGIS plugin
 Wrapper para el algoritmo Max-P de pysal
                              -------------------
        begin                : 2014-03-04
        copyright            : (C) 2014 by pablo lópez
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
import pysal
import numpy as np
# Initialize Qt resources from file resources.py
import resources_rc
# Import the code for the dialog
from maxpdialog import MaxPDialog
import os.path


class MaxP:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value("locale/userLocale")[0:2]
        localePath = os.path.join(self.plugin_dir, 'i18n', 'maxp_{}.qm'.format(locale))

        if os.path.exists(localePath):
            self.translator = QTranslator()
            self.translator.load(localePath)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Create the dialog (after translation) and keep reference
        self.dlg = MaxPDialog()

    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(
            QIcon(":/plugins/maxp/icon.png"),
            u"Regionalizacion MAX-P", self.iface.mainWindow())
        # connect the action to the run method
        self.action.triggered.connect(self.run)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu(u"&Regionalizacion MAX-P", self.action)

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu(u"&Regionalizacion MAX-P", self.action)
        self.iface.removeToolBarIcon(self.action)

    # run method that performs all the real work
    def run(self):
        capa = self.iface.activeLayer()
        if not capa:
            QMessageBox.information( self.iface.mainWindow(),"Error","No hay capa activa, por favor agrega una capa")
            return
       
        myfilepath= os.path.dirname( unicode( capa.dataProvider().dataSourceUri() ) )
        archivoDBF = os.path.join(myfilepath,capa.name()+'.dbf')
        archivoSHP = os.path.join(myfilepath,capa.name()+'.shp')
        dbf=pysal.open(archivoDBF)
        campos=dbf.header
        
        
        #campos = capa.pendingFields()
        
        listaCampos = self.dlg.listWidget 
        if listaCampos.count() == 0:            
            for c in campos:
                item =   QListWidgetItem(c)
                item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
                item.setCheckState(Qt.Unchecked)
                listaCampos.addItem(item)
    
        self.dlg.show()        
        result = self.dlg.exec_()
        # See if OK was pressed
        if result == 1:
            floor = self.dlg.textFloor.toPlainText()
            try:
                 floor = int(floor)
            except:
                 QMessageBox.information( self.iface.mainWindow(),"Error","La varible floor debe ser un entero")
                 return
                 
            seed = self.dlg.textSeed.toPlainText()
            try:
                 seed = int(seed)
            except:
                 QMessageBox.information( self.iface.mainWindow(),"Error","La varible seed debe ser un entero")
                 return
            fDilg = QFileDialog(self.iface.mainWindow(),'Open File', '*.dbf')
            #fDilg.setDirectory(myfilepath)
            filename = fDilg.getSaveFileName(directory=myfilepath.encode('utf8'))
            
            if self.dlg.queenButton.isChecked():
                w = pysal.queen_from_shapefile(archivoSHP)
            else:
                 w = pysal.rook_from_shapefile(archivoSHP)
            
            selected=[]
            for index in xrange( listaCampos.count()):
                itm = listaCampos.item(index)
                if itm.checkState()==2:
                    selected.append(itm.text())

            pci=np.array([dbf.by_col[str(y)] for y in selected])
            pci=pci.transpose()
            w=pysal.queen_from_shapefile(archivoSHP)
            size = w.n
            r=pysal.Maxp(w,pci,floor=floor,floor_variable=np.ones((size,1)),initial=seed)
            outputFName = filename
            dbfW=pysal.open(os.path.join(myfilepath,outputFName),'w','dbf')
            dbfW.header=['id','region']
            dbfW.field_spec=[('N',9,0),('N',9,0)]
            for i,region in enumerate(r.regions):
                for id in region:
                    dbfW.write((id,i))
                    
            dbfW.close()
            listaCampos = None
            selected = None
            
            
            

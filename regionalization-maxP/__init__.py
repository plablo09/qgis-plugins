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
 This script initializes the plugin, making it known to QGIS.
"""

def classFactory(iface):
    # load Regionalization class from file Regionalization
    from regionalization import Regionalization
    return Regionalization(iface)

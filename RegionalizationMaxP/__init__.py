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
 This script initializes the plugin, making it known to QGIS.
"""

def classFactory(iface):
    # load MaxP class from file MaxP
    from maxp import MaxP
    return MaxP(iface)

# -*- coding: utf-8 -*-
"""
/***************************************************************************
 PipelinePlanner
                                 A QGIS plugin
 Allow the user to create a line and evaluate impacts.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2021-07-21
        copyright            : (C) 2021 by M.Rat96
        email                : maciekrat96@gmail.com
        git sha              : $Format:%H$
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


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load PipelinePlanner class from file PipelinePlanner.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .pipeline_planner import PipelinePlanner
    return PipelinePlanner(iface)

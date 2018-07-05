# -*- coding: utf-8 -*-
"""
/***************************************************************************
 foo
                                 A QGIS plugin
 baz
                             -------------------
        begin                : 2018-07-05
        copyright            : (C) 2018 by Fide&Paulk
        email                : foo@localhost
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
    """Load foo class from file foo.

    :param iface: A QGIS interface instance.
    :type iface: QgisInterface
    """
    #
    from .Bautz import foo
    return foo(iface)

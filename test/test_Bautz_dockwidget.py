# coding=utf-8
"""DockWidget test.

.. note:: This program is free software; you can redistribute it and/or modify
     it under the terms of the GNU General Public License as published by
     the Free Software Foundation; either version 2 of the License, or
     (at your option) any later version.

"""

__author__ = 'foo@localhost'
__date__ = '2018-07-05'
__copyright__ = 'Copyright 2018, Fide&Paulk'

import unittest

from PyQt4.QtGui import QDockWidget

from Bautz_dockwidget import fooDockWidget

from utilities import get_qgis_app

QGIS_APP = get_qgis_app()


class fooDockWidgetTest(unittest.TestCase):
    """Test dockwidget works."""

    def setUp(self):
        """Runs before each test."""
        self.dockwidget = fooDockWidget(None)

    def tearDown(self):
        """Runs after each test."""
        self.dockwidget = None

    def test_dockwidget_ok(self):
        """Test we can click OK."""
        pass

if __name__ == "__main__":
    suite = unittest.makeSuite(fooDialogTest)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


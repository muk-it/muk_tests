###################################################################################
#
#    Copyright (c) 2017-2019 MuK IT GmbH.
#
#    This file is part of MuK Test Utils
#    (see https://mukit.at).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with this program. If not, see <http://www.gnu.org/licenses/>.
#
###################################################################################

import logging

from odoo.tests import common

_logger = logging.getLogger(__name__)


class HierarchyTestCase(common.TransactionCase):
    def test_hierarchy_restrict_path_names(self):
        record = self.env.ref("muk_test_utils.hierarchy_restrict_2")
        record = record.with_user(self.browse_ref("base.user_admin"))
        self.assertEqual(record.parent_path_names, "Child_01/")

    def test_hierarchy_sudo_path_names(self):
        record = self.env.ref("muk_test_utils.hierarchy_sudo_2")
        record = record.with_user(self.browse_ref("base.user_admin"))
        self.assertEqual(record.parent_path_names, "Root_01/Child_01/")

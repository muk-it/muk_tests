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
    def test_group_user_computation(self):
        group1 = self.env.ref("muk_test_utils.muk_test_utils_groups_1")
        group2 = self.env.ref("muk_test_utils.muk_test_utils_groups_2")
        self.assertEqual(set(group1.users.ids), {7, 2})
        self.assertEqual(set(group2.users.ids), {6, 7, 2})

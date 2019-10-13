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

from odoo import fields, models


class HierarchyTestRestrict(models.Model):

    _name = "muk_test_utils.hierarchy_restrict"
    _description = "Hierarchy Restrict Test"

    _inherit = ["muk_utils.mixins.hierarchy"]

    _parent_name = "parent_id"

    _parent_path_sudo = False
    _parent_path_store = False

    # ----------------------------------------------------------
    # Database
    # ----------------------------------------------------------

    name = fields.Char(string="Name", required=True, translate=True)

    parent_id = fields.Many2one(
        comodel_name="muk_test_utils.hierarchy_restrict",
        context="{'show_path': True}",
        string="Parent",
        ondelete="cascade",
        index=True,
    )

    child_ids = fields.One2many(
        comodel_name="muk_test_utils.hierarchy_restrict",
        inverse_name="parent_id",
        string="Childs",
    )


class HierarchyTestSudo(models.Model):

    _name = "muk_test_utils.hierarchy_sudo"
    _description = "Hierarchy Sudo Test"

    _inherit = ["muk_utils.mixins.hierarchy"]

    _parent_name = "parent_id"

    _parent_path_sudo = True
    _parent_path_store = True

    # ----------------------------------------------------------
    # Database
    # ----------------------------------------------------------

    name = fields.Char(string="Name", required=True, translate=True)

    parent_id = fields.Many2one(
        comodel_name="muk_test_utils.hierarchy_sudo",
        context="{'show_path': True}",
        string="Parent",
        ondelete="cascade",
        index=True,
    )

    child_ids = fields.One2many(
        comodel_name="muk_test_utils.hierarchy_sudo",
        inverse_name="parent_id",
        string="Childs",
    )

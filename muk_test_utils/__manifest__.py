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

{
    "name": "MuK Test Utils",
    "summary": """Test Utils""",
    "version": "13.0.1.0.0",
    "category": "Tests",
    "license": "LGPL-3",
    "author": "MuK IT",
    "website": "https://www.mukit.at",
    "contributors": ["Mathias Markl <mathias.markl@mukit.at>"],
    "depends": ["test_testing_utilities", "muk_utils"],
    "data": [
        "security/ir.model.access.csv",
        "views/menu.xml",
        "views/groups.xml",
        "views/hierarchy.xml",
        "data/muk_test_utils.groups.csv",
        "data/muk_test_utils.hierarchy_restrict.csv",
        "data/muk_test_utils.hierarchy_sudo.csv",
        "data/ir.rule.csv",
    ],
    "images": ["static/description/banner.png"],
    "application": False,
    "installable": True,
    "auto_install": False,
}

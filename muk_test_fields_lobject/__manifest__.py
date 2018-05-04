###################################################################################
# 
#    Copyright (C) 2017 MuK IT GmbH
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###################################################################################

{
    "name": "MuK Large Object Field Tests",
    "summary": """PGSQL Large Object Field Tests""",
    "version": "11.0.1.0.0",
    "category": "Tests",
    "license": "AGPL-3",
    "website": "http://www.mukit.at",
    "author": "MuK IT",
    "contributors": [
        "Mathias Markl <mathias.markl@mukit.at>",
    ],
    "depends": [
        "muk_fields_lobject",
        "muk_web_fields_lobject",
        "muk_web_preview_lobject",
    ],
    "data": [
        "security/ir.model.access.csv",
        "template/assets.xml",
        "data/data.xml",
        "views/menu.xml",
        "views/dummy.xml"
    ],
    "demo": [
    ],
    "qweb": [
        "static/src/xml/*.xml",
    ],
    "images": [
        "static/description/banner.png"
    ],
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    "application": False,
    "installable": True,
}
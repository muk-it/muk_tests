###################################################################################
#
#    Copyright (C) 2018 MuK IT GmbH
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

import logging

from odoo import models, fields

from odoo.addons.muk_dms_field.fields.dms_binary import DocumentBinary
from odoo.addons.muk_dms_field.fields.dms_many2one import DocumentMany2one

_logger = logging.getLogger(__name__)

class Dummy(models.Model):
    
    _name = 'muk_test_dms.dummy'
    
    def _get_file_name(self):
        return self.content_fname or "NewFile"
    
    def _get_file_directory(self):
        return self.env.ref("muk_dms.directory_01_demo").id
    
    content_fname = fields.Char(
        string="Filename")
    
    content = DocumentBinary(
        string="Data",
        filename=_get_file_name,
        directory=_get_file_directory)
    
    file = DocumentMany2one(
        comodel_name='muk_dms.file')


    
    
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

import os
import base64
import logging

from urllib.parse import urlunparse
from urllib.parse import urlparse
from urllib.parse import parse_qsl
from urllib.parse import urlencode

from odoo.tests import common

_path = os.path.dirname(os.path.dirname(__file__))
_logger = logging.getLogger(__name__)

class LargeObjectTestCase(common.HttpCase):
    
    def setUp(self):
        super(LargeObjectTestCase, self).setUp()
        self.dummy = self.env['muk_test_fields_lobject.dummy']

    def tearDown(self):
        super(LargeObjectTestCase, self).tearDown()
        
    def test_field(self):
        record = self.dummy.create({'content': b"\xff data"})
        human_size = record.with_context({'human_size': True}).content
        bin_size = record.with_context({'bin_size': True}).content
        oid = record.with_context({'oid': True}).content
        b64 = record.with_context({'base64': True}).content
        stream = record.with_context({'stream': True}).content
        checksum = record.with_context({'checksum': True}).content
        binary = record.with_context({}).content
        self.assertEqual(human_size, "6.00 bytes")
        self.assertEqual(bin_size, len(b"\xff data"))
        self.assertEqual(b64, b'/yBkYXRh')
        self.assertEqual(stream.seek(0, 2), len(b"\xff data"))
        self.assertEqual(checksum, "e4afeea27415f0f987dee52ea91f2787")
        self.assertEqual(binary, b'\xff data')
        self.assertTrue(oid)
        
    def test_file(self):
        with open(os.path.join(_path, 'tests/data', 'sample.png'), 'rb') as file:
            record = self.dummy.create({'content': file.read()})
            binary = record.with_context({}).content
            self.assertTrue(binary)
            
    def test_b64(self):
        with open(os.path.join(_path, 'tests/data', 'sample.png'), 'rb') as file:
            record = self.dummy.create({'content': base64.b64encode(file.read())})
            b64 = record.with_context({'base64': True}).content
            self.assertTrue(b64)
    
    def test_write(self):
        record = self.dummy.create({'content': b"\xff data_create"})
        self.assertEqual(record.content, b'\xff data_create')
        record.write({'content': b"\xff data_write"})
        self.assertEqual(record.content, b'\xff data_write')
        
    def test_copy(self):
        record = self.dummy.create({'content': b"\xff data"})
        self.assertEqual(record.content, b'\xff data')
        self.assertEqual(record.copy().content, b'\xff data')
        
    def test_unlink(self):
        count = self.dummy.search([], count=True)
        record = self.dummy.create({'content': b"\xff data"})
        self.assertEqual(self.dummy.search([], count=True), count + 1)
        record.unlink()
        self.assertEqual(self.dummy.search([], count=True), count)
        
    def test_http(self):
        status, headers, content = self.env['ir.http'].lobject_content(
            model='muk_test_fields_lobject.dummy',
            id=self.ref('muk_test_fields_lobject.dummy'), 
            field='content',
            filename="test",
            unique=True)
        self.assertEqual(status, 200)
        self.assertTrue(headers)
        self.assertTrue(content)
        
    def test_controller(self):
        self.authenticate('admin', 'admin')
        url = "/web/lobject"
        params = {'xmlid': 'muk_test_fields_lobject.dummy'}
        url_parts = list(urlparse(url))
        query = dict(parse_qsl(url_parts[4]))
        query.update(params)
        url_parts[4] = urlencode(query)
        url = urlunparse(url_parts)
        response = self.url_open(url)
        self.assertTrue(response)      
        self.assertEqual(response.content, self.dummy.browse(self.ref('muk_test_fields_lobject.dummy')).content)      
        
    def test_preview(self):
        self.phantom_js("/web",
                        "odoo.__DEBUG__.services['web_tour.tour'].run('lobject')",
                        "odoo.__DEBUG__.services['web_tour.tour'].tours.lobject.ready",
                        login="admin")
        
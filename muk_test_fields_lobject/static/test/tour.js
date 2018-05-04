/**********************************************************************************
* 
*    Copyright (C) 2017 MuK IT GmbH
*
*    This program is free software: you can redistribute it and/or modify
*    it under the terms of the GNU Affero General Public License as
*    published by the Free Software Foundation, either version 3 of the
*    License, or (at your option) any later version.
*
*    This program is distributed in the hope that it will be useful,
*    but WITHOUT ANY WARRANTY; without even the implied warranty of
*    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
*    GNU Affero General Public License for more details.
*
*    You should have received a copy of the GNU Affero General Public License
*    along with this program.  If not, see <http://www.gnu.org/licenses/>.
*
**********************************************************************************/

odoo.define('muk_test_fields_lobject.tour', function (require) {
'use strict';

var core = require("web.core");
var tour = require("web_tour.tour");
var base = require("web_editor.base");

var _t = core._t;

var name = 'lobject';

var options = {
    test: true,
    url: '/web',
    wait_for: base.ready()
};

var setps = [
	{
		content: 'open menu',
		trigger: 'a[data-menu-xmlid="muk_test_fields_lobject.main_menu_muk_test_fields_lobject"]',
		run: 'click',
	},
	{
		content: 'open row',
		trigger: 'tr.o_data_row',
		run: 'click',
	},
	{
		content: 'open preview',
		trigger: 'button.o_binary_preview',
		run: 'click',
	},
];

tour.register(name, options, setps);

});
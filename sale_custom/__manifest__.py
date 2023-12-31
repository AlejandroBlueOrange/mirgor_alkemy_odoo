# -*- encoding: utf-8 -*-
##############################################################################
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{

    'name': 'Sale Custom',

    'version': '1.1',

    'category': 'Sale',

    'summary': '',

    'author': 'BLUEORANGE GROUP S.R.L. (www.blueorange.com.ar) / NEXIT',

    'website': 'https://www.nexit.com.uy',

    'license': 'AGPL-3',

    'depends': [
        'sale'
    ],

    'data': [
      'security/ir.model.access.csv',
      'views/sale_order.xml',
      'wizard/sale_wizard_example.xml',
    ],

    'installable': True,

    'auto_install': False,

    'application': False,

    'description': '''
    ''',

}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
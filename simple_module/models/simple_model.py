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

from odoo import models, fields


class SimpleModel(models.Model):
    _name = 'simple.model'
    _description = 'Simple Model'
    
    name = fields.Char(string='Name', help='This is a record name', required=True, default=lambda x: 'Name', index=True)

    def return_name(self):
        return self.name

class InheritSimpleModel(models.Model):
    _inherit = 'simple.model'
    
    name = fields.Char(default=lambda x: 'Inherit Name')

    def return_name(self):
        res =  super().return_name()
        return res + "X"
    

class ClassicInheritSimpleModel(models.Model):
    _inherit = 'simple.model'
    _name = 'simple.model.inherit'
    
    name = fields.Char(default=lambda x: 'Inherit Name')

    def return_name(self):
        res =  super().return_name()
        return res + "X"

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
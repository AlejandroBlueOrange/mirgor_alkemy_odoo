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

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    custom_groups_field = fields.Char(string="Campo con groups", groups="sales_team.group_sale_manager")  
    
    custom_inv_read_field = fields.Char(string="Campo con invisible y readonly")

    is_not_group_proforma_sales = fields.Boolean(
        compute="compute_is_not_group_proforma_sales",
    )

    sale_order_line1_ids = fields.One2many(
        comodel_name='sale.order.line1',
        inverse_name='sale_order_id'
    )

    sale_order_line1_m2m_ids = fields.Many2many(
        comodel_name='sale.order.line1',
        relation='sale_order_line1_sale_order',
        column1='sale_order_id',
        comlumn2='sale_order_line1_id'
    )

    def compute_is_not_group_proforma_sales(self):
        for rec in self:
            rec.is_not_group_proforma_sales = not self.user_has_groups('sale.group_proforma_sales')

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
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


class SaleOrderLine(models.Model):
    _name = 'sale.order.line1'
    _description = 'Sale Order Line 1'

    product_id = fields.Many2one(
        comodel_name='product.product'
    )
    name = fields.Char(

    )

    sale_order_id = fields.Many2one(
        comodel_name='sale.order',
        ondelete='cascade',
        auto_join=True,
        check_company=True
    )

    #sale_order_client_id = fields.Many2one(
    #    related='sale_order_id.partner_id',
    #    readonly=False
    #)
    sale_client_order_ref = fields.Char(
        related='sale_order_id.client_order_ref',
        readonly=False
    )

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
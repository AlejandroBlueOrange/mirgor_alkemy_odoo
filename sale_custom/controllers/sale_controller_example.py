import json
from odoo import http
from odoo.http import request, route

class SaleControllerExample(http.Controller):
    @route('/sale_orders', methods=['GET'], type='http', auth='none', cors='*')
    def sale_orders(self , **kwargs):
        sale_order_ids = request.env['sale.order'].search([]).sale_order_to_json()
        data = json.dumps({
            'sale_order_ids': sale_order_ids,
        })
        headers = [('Content-Type', 'application/json'),
                   ('Cache-Control', 'no-store')]
        return request.make_response(data, headers)
    
    @route('/sale_orders', methods=['GET'], type='http', auth='public', cors='*')
    def sale_orders(self , **kwargs):
        sale_order_ids = request.env['sale.order'].search([]).sale_order_to_json()
        data = json.dumps({
            'sale_order_ids': sale_order_ids,
        })
        headers = [('Content-Type', 'application/json'),
                   ('Cache-Control', 'no-store')]
        return request.make_response(data, headers)

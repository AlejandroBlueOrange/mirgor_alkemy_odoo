#!/usr/bin/env python
# coding: utf-8

from odoo import api, SUPERUSER_ID, fields

def migrate(cr, installed_version):
    cr.execute("select id, custom_groups_field_migration from sale_order where custom_groups_field_migration is not null")
    orders = cr.dictfetchall()
    for order in orders:
        order_id = order['id']
        custom_groups_field_migration = order['custom_groups_field_migration']
        cr.execute("update sale_order set custom_groups_field_1 = '{}' where id = {}".format(custom_groups_field_migration, order_id))



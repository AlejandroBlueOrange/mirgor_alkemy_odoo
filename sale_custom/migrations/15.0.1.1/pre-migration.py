#!/usr/bin/env python
# coding: utf-8

def migrate(cr, installed_version):
    cr.execute("alter table sale_order add custom_groups_field_migration varchar")
    cr.execute("select id,custom_groups_field from sale_order where custom_groups_field is not null")
    orders = cr.dictfetchall()
    for order in orders:
        order_id = order['id']
        custom_groups_field = order['custom_groups_field']
        cr.execute("update sale_order set custom_groups_field_migration = '{}' where id = {}".format(custom_groups_field, order_id))

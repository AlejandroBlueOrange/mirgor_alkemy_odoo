from odoo import api, fields, models

class TestComputed(models.Model):
    _name = "test.computed"

    total = fields.Float(compute="_compute_total", store=True)#inverse="_inverse_total")
    amount = fields.Float()

    @api.depends("amount")
    def _compute_total(self):
        for record in self:
            record.total = 2.0 * record.amount

    def _inverse_total(self):
        for record in self:
            record.amount = record.total / 2.0


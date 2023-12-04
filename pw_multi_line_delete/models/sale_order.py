# -*- coding: utf-8 -*-
from odoo import models, fields


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def action_select_all(self):
        selected = self.order_line.filtered(lambda x: x.tobe_delete)
        self.order_line.write({'tobe_delete': not selected})

    def action_delete_all(self):
        self.order_line.filtered(lambda x: x.tobe_delete).sudo().unlink()

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    tobe_delete = fields.Boolean('Tobe Delete')

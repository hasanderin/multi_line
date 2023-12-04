# -*- coding: utf-8 -*-
from odoo import models, fields


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    def action_select_all(self):
        selected = self.order_line.filtered(lambda x: x.tobe_delete)
        self.order_line.write({'tobe_delete': not selected})

    def action_delete_all(self):
        self.order_line.filtered(lambda x: x.tobe_delete).sudo().unlink()

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    tobe_delete = fields.Boolean('Tobe Delete')

# -*- coding: utf-8 -*-
from odoo import models, fields


class StockPicking(models.Model):
    _inherit = "stock.picking"

    def action_select_all(self):
        selected = self.move_lines.filtered(lambda x: x.tobe_delete)
        self.move_lines.write({'tobe_delete': not selected})

    def action_delete_all(self):
        tobe_delete = self.move_lines.filtered(lambda x: x.tobe_delete)
        tobe_delete.write({'state': 'draft'})
        tobe_delete.unlink()

class StockMove(models.Model):
    _inherit = 'stock.move'

    tobe_delete = fields.Boolean('Tobe Delete')

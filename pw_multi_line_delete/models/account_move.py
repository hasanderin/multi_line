# -*- coding: utf-8 -*-
from odoo import models, fields


class AccountMove(models.Model):
    _inherit = "account.move"

    def action_select_all(self):
        selected = self.invoice_line_ids.filtered(lambda x: x.tobe_delete)
        self.invoice_line_ids.write({'tobe_delete': not selected})

    def action_delete_all(self):
        self.invoice_line_ids.filtered(lambda x: x.tobe_delete).sudo().with_context(check_move_validity=False).unlink()
        self.with_context(check_move_validity=False)._recompute_dynamic_lines(recompute_all_taxes=True, recompute_tax_base_amount=True)


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    tobe_delete = fields.Boolean('Tobe Delete')

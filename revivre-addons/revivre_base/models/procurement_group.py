# -*- coding: utf-8 -*-

from odoo import api, models
from odoo.tools.misc import split_every


class ProcurementGroup(models.Model):
    _inherit = "procurement.group"

    @api.model
    def _run_scheduler_tasks(self, use_new_cursor=False, company_id=False):
        """Redefine this function because ddmrp override the standard method to
        disable the possibility to automatically procure from orderpoints and
        to automatically reserve stock moves."""
        # Minimum stock rules
        domain = self._get_orderpoint_domain(company_id=company_id)
        orderpoints = self.env['stock.warehouse.orderpoint'].search(domain)
        # ensure that qty_* which depends on datetime.now() are correctly
        # recomputed
        orderpoints.sudo()._compute_qty_to_order()
        orderpoints.sudo()._procure_orderpoint_confirm(use_new_cursor=use_new_cursor, company_id=company_id, raise_user_error=False)
        if use_new_cursor:
            self._cr.commit()

        # Search all confirmed stock_moves and try to assign them
        domain = self._get_moves_to_assign_domain(company_id)
        moves_to_assign = self.env['stock.move'].search(domain, limit=None,
            order='priority desc, date asc, id asc')
        for moves_chunk in split_every(100, moves_to_assign.ids):
            self.env['stock.move'].browse(moves_chunk).sudo()._action_assign()
            if use_new_cursor:
                self._cr.commit()

        # Merge duplicated quants
        self.env['stock.quant']._quant_tasks()

        # line get from production_lot module method _run_scheduler_tasks
        self.env['stock.production.lot']._alert_date_exceeded()

        if use_new_cursor:
            self._cr.commit()

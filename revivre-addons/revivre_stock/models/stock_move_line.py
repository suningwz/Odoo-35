# -*- coding: utf-8 -*-

from odoo import api, models, fields

class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    shopfloor_picking_sequence = fields.Char(related="location_id.shopfloor_picking_sequence")
    qty_done_packs = fields.Char(compute='_compute_qty_done_packs')

    @api.depends("qty_done")
    def _compute_qty_done_packs(self):
        print('_compute_qty_done_packs', self)
        for rec in self:
            value = rec.move_id.product_id.product_qty_by_packaging_as_str(
                rec.qty_done,
                include_total_units=False,
                only_packaging=False,
            )
            rec.qty_done_packs = value

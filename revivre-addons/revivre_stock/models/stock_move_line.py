# -*- coding: utf-8 -*-

from odoo import api, models, fields

class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    shopfloor_picking_sequence = fields.Char(related="location_id.shopfloor_picking_sequence")
    qty_done_packs = fields.Char(compute='_compute_qty_done_packs')

    @api.depends("qty_done")
    def _compute_qty_done_packs(self):
        for rec in self: #TODO factorisation with get_qty_done_packs
            if rec.product_id:
                value = rec.move_id.product_id.product_qty_by_packaging_as_str(
                    rec.qty_done,
                    include_total_units=False,
                    only_packaging=False,
                )
                rec.qty_done_packs = value
            else:
                rec.qty_done_packs = ""

    def get_qty_done_packs(self, product_id, qty):
        if product_id:
            value = product_id.product_qty_by_packaging_as_str(
                qty,
                include_total_units=False,
                only_packaging=False,
            )
            return value
        else:
            return ""

    def _get_aggregated_product_quantities(self, **kwargs):
        aggregated_move_lines = super()._get_aggregated_product_quantities(**kwargs)
        for v in aggregated_move_lines.values():
            v['qty_done_packs'] = self.get_qty_done_packs(product_id=v['product'], qty=v['qty_done'])
            v['weight'] = round(v['qty_done'] * v['product'].weight, 2)
            v['weight_uom_id'] = v['product'].weight_uom_id
        print(aggregated_move_lines)
        return aggregated_move_lines
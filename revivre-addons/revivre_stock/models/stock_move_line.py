# -*- coding: utf-8 -*-

from odoo import api, models, fields


class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    shopfloor_picking_sequence = fields.Char(related="location_id.shopfloor_picking_sequence")

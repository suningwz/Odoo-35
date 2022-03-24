# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    price_unit_without_seller_vat = fields.Float('Unit Price HT', compute='_compute_price_unit_without_seller_vat')

    @api.depends('product_id.seller_vat_id', 'price_unit')
    def _compute_price_unit_without_seller_vat(self):
        for rec in self:
            if rec.product_id and rec.price_unit and rec.product_id.seller_vat_id and rec.product_id.seller_vat_id.amount > 0:
                rec.price_unit_without_seller_vat = rec.price_unit / (rec.product_id.seller_vat_id.amount / 100 + 1)
            else:
                rec.price_unit_without_seller_vat = False

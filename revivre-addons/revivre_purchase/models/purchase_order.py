# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    price_unit_without_seller_vat = fields.Float('Unit Price HT', compute='_compute_price_unit_without_seller_vat')
    package_price_without_taxes = fields.Float('Package Price HT', compute='_compute_package_price_without_taxes')
    price_unit = fields.Float(string='Unit Price', required=True, digits='Product Price')
    price_subtotal = fields.Monetary(compute='_compute_amount', string='Subtotal', store=True)


    @api.depends('product_id.seller_vat_id', 'price_unit')
    def _compute_price_unit_without_seller_vat(self):
        for rec in self:
            if rec.product_id and rec.price_unit and rec.product_id.seller_vat_id and rec.product_id.seller_vat_id.amount > 0:
                rec.price_unit_without_seller_vat = rec.price_unit / (rec.product_id.seller_vat_id.amount / 100 + 1)
            else:
                rec.price_unit_without_seller_vat = False

    @api.depends('price_unit_without_seller_vat', 'product_packaging')
    def _compute_package_price_without_taxes(self):
        for rec in self:
            if rec.price_unit_without_seller_vat and rec.product_packaging and rec.product_packaging.uom_id and rec.product_packaging.uom_id.factor_inv:
                rec.package_price_without_taxes = rec.price_unit_without_seller_vat * rec.product_packaging.uom_id.factor_inv
            else:
                rec.package_price_without_taxes = False


class PurchaseOrderLinePriceHistoryLine(models.TransientModel):
    _inherit = "purchase.order.line.price.history.line"

    product_packaging = fields.Many2one(related="purchase_order_line_id.product_packaging", string="Package")
    package_price_without_taxes = fields.Float(related="purchase_order_line_id.package_price_without_taxes", string="Package Price HT")

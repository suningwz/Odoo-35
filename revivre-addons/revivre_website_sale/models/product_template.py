# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    def get_expiring_lot(self, product_variant_ids, field_to_check):
        expiring_lot = False
        if field_to_check == 'use_date':
            expiring_lot = self.env['stock.production.lot'].search([('product_id', 'in', product_variant_ids.ids),
                                                                    ('product_qty', '>', 0.0),
                                                                    ('use_date', '>=', fields.Datetime.now())],
                                                                   order='use_date asc', limit=1)
        elif field_to_check == 'expiration_date':
            expiring_lot = self.env['stock.production.lot'].search([('product_id', 'in', product_variant_ids.ids),
                                                                    ('product_qty', '>', 0.0),
                                                                    ('expiration_date', '>=', fields.Datetime.now())],
                                                                   order='expiration_date asc', limit=1)

        return expiring_lot

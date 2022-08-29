# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    def (self, product_variant_ids, field_to_check):
        expiring_lot = False
        if field_to_check == 'use_date':
            expiring_lot_ids = self.env['stock.production.lot'].sudo().search([('product_id', 'in', product_variant_ids.ids),
                                                                    ('use_date', '>=', fields.Datetime.now())],
                                                                   order='use_date asc')
        elif field_to_check == 'expiration_date':
            expiring_lot_ids = self.env['stock.production.lot'].sudo().search([('product_id', 'in', product_variant_ids.ids),
                                                                    ('expiration_date', '>=', fields.Datetime.now())],
                                                                   order='expiration_date asc')

        for expiring_lot_id in expiring_lot_ids:
            if expiring_lot_id.sudo().product_qty > 0.0:
                return expiring_lot_id
        return expiring_lot

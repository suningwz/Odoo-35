# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    seller_vat_id = fields.Many2one('account.tax', 'Seller VAT')

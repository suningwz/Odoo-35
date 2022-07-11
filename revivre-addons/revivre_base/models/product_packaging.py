# -*- coding: utf-8 -*-

from odoo import api, models


class ProductPackaging(models.Model):
    _inherit = "product.packaging"
    _order = 'name asc'


from odoo import models


class AccountMoveLine(models.Model):
    _name = "account.move.line"
    _inherit = ["account.move.line", "product.qty_by_packaging.mixin"]

    _qty_by_pkg__qty_field_name = "quantity"


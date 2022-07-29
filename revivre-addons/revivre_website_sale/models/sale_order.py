# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    # def get_description_following_lines(self):
    #     res = super(SaleOrderLine, self).get_description_following_lines()
    #     if self.product_packaging and self.product_packaging.uom_id and self.product_packaging.uom_id.factor_inv > 1:
    #         res.append(_('Package of ') + str(int(self.product_packaging.uom_id.factor_inv)) + ' ' +
    #                    _('Number of Package : ') + str(int(self.product_uom_qty / self.product_packaging.uom_id.factor_inv if self.product_packaging.uom_id.factor_inv > 0 else 1)))
    #     return res


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    expected_customer_date = fields.Date()

    @api.depends('order_line.product_uom_qty', 'order_line.product_id')
    def _compute_cart_info(self):
        for order in self:
            cart_quantity = 0
            for line in order.website_order_line:
                if line.product_packaging:
                    cart_quantity += line.product_packaging_qty
                else:
                    cart_quantity += line.product_uom_qty
            order.cart_quantity = int(cart_quantity)
            order.only_services = all(l.product_id.type in ('service', 'digital') for l in order.website_order_line)

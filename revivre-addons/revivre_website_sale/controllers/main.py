# -*- coding: utf-8 -*-

import logging
from odoo import fields, http, SUPERUSER_ID, tools, _
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale

_logger = logging.getLogger(__name__)


class WebsiteSaleProductPackaging(WebsiteSale):

    @http.route(['/shop/cart/update_json'], type='json', auth="public", methods=['POST'], website=True, csrf=False)
    def cart_update_json(self, product_id, line_id=None, add_qty=None, set_qty=None, display=True):
        print('cart_update_json2', product_id, line_id, add_qty, set_qty, display)
        """This route is called when changing quantity from the cart or adding
        a product from the wishlist."""
        order = request.website.sale_get_order(force_create=1)
        if order.state != 'draft':
            request.website.sale_reset()
            return {}

        if line_id and set_qty != 0 and request.env['sale.order.line'].browse(line_id).product_packaging:
            line_obj_id = request.env['sale.order.line'].browse(line_id)
            order = request.website.sale_get_order()
            line_obj_id.product_packaging_qty = set_qty
            value = {'line_id': line_obj_id.id, 'quantity': line_obj_id.product_uom_qty, 'option_ids': []}
        else:
            value = order._cart_update(product_id=product_id, line_id=line_id, add_qty=add_qty, set_qty=set_qty)

            if not order.cart_quantity:
                request.website.sale_reset()
                return value

            order = request.website.sale_get_order()
            value['cart_quantity'] = order.cart_quantity

            if not display:
                return value

        value['website_sale.cart_lines'] = request.env['ir.ui.view']._render_template("website_sale.cart_lines", {
            'website_sale_order': order,
            'date': fields.Date.today(),
            'suggested_products': order._cart_accessories()
        })
        value['website_sale.short_cart_summary'] = request.env['ir.ui.view']._render_template("website_sale.short_cart_summary", {
            'website_sale_order': order,
        })
        return value
# -*- coding: utf-8 -*-
from odoo import http
# from odoo.addons.website_sale_wishlist.controllers.main import WebsiteSaleWishlist


# class WebsiteSaleWishlistProductPackaging(WebsiteSaleWishlist):

    # @http.route(['/shop/wishlist/add'], type='json', auth="public", website=True)
    # def add_to_wishlist(self, product_id, price=False, **kw):
    #     wish_id = super(WebsiteSaleWishlistProductPackaging, self).add_to_wishlist(product_id, price=False, **kw)
    #     if wish_id.product_id.packaging_ids:
    #         for pack in wish_id.product_id.packaging_ids:
    #             wish_id.product_packaging = pack
    #     return wish_id
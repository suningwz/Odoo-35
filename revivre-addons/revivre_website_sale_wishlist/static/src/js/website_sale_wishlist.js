odoo.define("revivre_website_sale_wishlist.revivre_wishlist", function (require) {
    "use strict";
    var publicWidget = require('web.public.widget');
    var wSaleUtils = require('website_sale.utils');

    publicWidget.registry.ProductWishlist.include({
        _addToCart: function (productID, qty_id, packagingID) {
            console.log('aaaaazzzz',productID, qty_id, packagingID)
            return this._rpc({
                route: "/shop/cart/update_json",
                params: {
                    product_id: parseInt(productID, 10),
                    add_qty: parseInt(qty_id, 10),
                    packaging_id: parseInt(packagingID, 10),
                    display: false,
                },

            }).then(function (data) {
                wSaleUtils.updateCartNavBar(data);
                wSaleUtils.showWarning(data.warning);
            });
        },
        _addOrMoveWish: function (e) {
            console.log(e)
            console.log('ouoiuoiu')
            var $navButton = $('header .o_wsale_my_cart').first();
            var tr = $(e.currentTarget).parents('tr');
            var product = tr.data('product-id');
            var wish = tr.data('wish-id');
            // var packaging = $('#tr.packaging_select option:selected').attr('pack-id')
            // var packaging = tr.find('.packaging_select option:selected').val();
            // var packaging = tr;
            var packaging = tr.find('.package_selector :selected').attr('pack-id');

            console.log(product)
            console.log(wish)
            console.log(packaging)

            $('.o_wsale_my_cart').removeClass('d-none');
            wSaleUtils.animateClone($navButton, tr, 25, 40);

            if ($('#b2b_wish').is(':checked')) {
                return this._addToCart(product, tr.find('add_qty').val() || 1, packaging);
            } else {
                var adding_deffered = this._addToCart(product, tr.find('add_qty').val() || 1, packaging);
                this._removeWish(e, adding_deffered);
                return adding_deffered;
            }
        },
    });
});
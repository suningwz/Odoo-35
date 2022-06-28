# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

import logging

_logger = logging.getLogger(__name__)


class MrpProduction(models.Model):
    """ Manufacturing Orders """
    _inherit = 'mrp.production'

    def _compute_description_mrp(self):
        html_data = '''<table class="table">
                        <thead>
                                <tr>
                                    <th>Product Name</th>
                                    <th>Product Description</th>
                                    <th>Quantity</th>
                                    <th>Unit pack</th>
                                    <th>Package to be delivered</th>
                                    <th>Subtotal</th>
                                </tr>
                        </thead>
                        <tbody>

                                            '''
        raw_data = ""
        for line in self.env['sale.order'].sudo().search([('name', '=', self.origin)]).order_line.filtered(
                lambda line: True if line.product_id.id == self.product_id.id else False):
            raw_data += "<tr><td>" + line.product_id.name + "</td><td>" + line.name + "</td><td>" + str(
                line.product_uom_qty) + "</td><td>" + str(line.product_packaging.name) + "</td><td>" + str(
                int(line.product_uom_qty / (
                    line.product_packaging.qty if line.product_packaging.qty > 0 else 1))) + " Packages</td><td>" + str(
                line.price_subtotal) + "</td></tr>"

        self.description_mrp = html_data + raw_data + "</tbody></table>"


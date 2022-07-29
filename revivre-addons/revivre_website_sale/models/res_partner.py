# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import datetime

from odoo import fields, models, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.model
    def get_delivery_date_shop(self, partner_id):
        print('get_delivery_date_shop', partner_id)
        partner = self.browse(partner_id)
        anytime_delivery = partner and partner.delivery_time_preference == "anytime"
        outgoing_picking = "outgoing_picking"
        print(partner, anytime_delivery, outgoing_picking)
        # if not partner or anytime_delivery or outgoing_picking:
        #     return "aaaaaa"
        if not partner.is_in_delivery_window(datetime.datetime.now()):
            return partner._scheduled_date_no_delivery_window_match_msg()
        return "coucou frero"
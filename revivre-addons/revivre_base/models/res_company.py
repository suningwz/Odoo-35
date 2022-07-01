# -*- coding: utf-8 -*-

from odoo import fields, models


class Company(models.Model):
    _inherit = 'res.company'

    alimhotel_logo = fields.Binary(string=" Alimhotel Logo")
    villages_logo = fields.Binary(string=" Tournees Villages Logo")
    comment_for_report = fields.Text('Comment For Report')

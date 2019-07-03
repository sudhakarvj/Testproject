# -*- coding: utf-8 -*-

from odoo import models, fields

class CreateOrder(models.Model):
    _inherit = 'onida_apps.order'

    payment_mode=fields.Selection([('online','Online Payment'),('COD','Cash on Delivery')],'Payment Mode')

# -*- coding: utf-8 -*-

from odoo import models, fields, api
import random
from random import randint
import string

class CreateProduct(models.Model):
    _name = 'onida_apps.product'
    _description="Product Creation"
    _inherit = ['mail.thread']
    _rec_name="product_name"

    product_name=fields.Char(required=True,track_visibility='always',copy=False)
    product_ref=fields.Char(track_visibility='always',index=True)
    product_id=fields.Many2one('onida_apps.order')
    barcode=fields.Char(track_visibility='always')
    price = fields.Monetary('Price', 'currency_id')
#     tax_ids=fields.Many2many('onida_apps.tax')
    tax_ids=fields.Many2one('onida_apps.tax')
    currency_id = fields.Many2one('res.currency')
    total_cost=fields.Float('Total Price',readonly=True)
    notes=fields.Text(translate=True)
    is_available = fields.Boolean('is Product available?')
    product_image=fields.Binary()
    product_id=fields.Many2one('onida_apps.order',ondelete="restrict")
    color=fields.Integer()

    @api.onchange('tax_ids')
    def on_change_price(self):
        for record in self:
            if record.tax_ids.tax_name=='service':
                record.total_cost=record.price+(record.price*0.15)
            elif record.tax_ids.tax_name=='CGST':
                record.total_cost=record.price+(record.price*0.12)
            elif record.tax_ids.tax_name=='SGST':
                record.total_cost=record.price+(record.price*0.09)
            elif record.tax_ids.tax_name=='sales':
                record.total_cost=record.price+(record.price*0.05)
            else:
                record.total_cost=record.price

    @api.multi
    def generate_barcode_no(self):
         
        for rec in self:
            self.write({
                        'barcode': ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(randint(12,15)))
    })


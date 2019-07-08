# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime

class CreateOrder(models.Model):
    _name = 'onida_apps.order'
    _description="Purchase Order"
    _inherit = ['mail.thread']
    _rec_name="customer_id"

    customer_id=fields.Many2one('onida_apps.customer',string="Customer", ondelete="restrict", required=True)
    customer_mobile=fields.Char(related='customer_id.mobile')
    customer_ref=fields.Char(track_visibility='always')
    date_order=fields.Datetime('Order Date', track_visibility='always',default=fields.Datetime.today)
    notes=fields.Text()
    product_ids=fields.Many2many('onida_apps.product')
    product_line_ids=fields.One2many('onida_apps.product','product_id')
    sequence_id = fields.Char('Sequence', readonly=True)

    @api.model
    def create(self, vals):
        seq = self.env['ir.sequence'].next_by_code('order.id') or '/'
        vals['sequence_id'] = seq
        return super(CreateOrder, self).create(vals)

# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Createinvoice(models.Model):
    _name = 'onida_apps.invoice'
    _description="Invoice generation"
    _inherit = ['mail.thread']
    _rec_name="invoice_no"

    invoice_no=fields.Integer(track_visibility='always')
    invoice_date=fields.Date()
    customer_id=fields.Many2one('onida_apps.customer',track_visibility='always',delegate=True,required=True)
    product_id=fields.Many2one('onida_apps.product', track_visibility='always',delegate=True,required=True)
    notes=fields.Text()

class TaxInformation(models.Model):
    _name = 'onida_apps.tax'
    _description="Tax info"
    _inherit = ['mail.thread']
    _rec_name='tax_name'

    tax_no=fields.Integer()
    tax_name=fields.Selection([('service','Service Tax'),('CGST','CGST'),('SGST','SGST'),('sales','Sales Tax')],'Tax',copy=False)
    tax_value=fields.Float('Tax Value(%)', (8, 2), default="0")
    notes=fields.Html('Description') 

    @api.onchange('tax_name')
    def on_change_taxname(self):
        if self.tax_name=='service':
            self.tax_value=15
        elif self.tax_name=='CGST':
            self.tax_value=12
        elif self.tax_name=='SGST':
            self.tax_value=9
        elif self.tax_name=='sales':
            self.tax_value=5
        else:
            self.tax_value=0

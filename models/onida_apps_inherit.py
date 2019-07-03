# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re

class CreateCustomer(models.Model):
    _inherit = 'onida_apps.customer'
    _description="Customer Creation Inheritance"

    phone=fields.Char('Phone')
    
    @api.onchange('email')
    def validate_mail(self):
       if self.email:
        match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', self.email)
        if match == None:
            raise ValidationError('Not a valid E-mail ID')

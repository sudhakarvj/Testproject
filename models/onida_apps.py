# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime
from odoo.exceptions import ValidationError

class CreateCustomer(models.Model):
    _name = 'onida_apps.customer'
    _description="Customer Creation"
    _inherit = ['mail.thread']
    _rec_name='customer_name'
    _sql_constraints=[('email_unique','UNIQUE(email)',"The email must be unique"),
                      ('age_check','CHECK(age>=18)',"The age must be above 18")]

    customer_name = fields.Char(required=True, translate=True, track_visibility='always', track_sequence=1)
    street_number=fields.Char("Address",help='House number')
    street_name=fields.Char(string='Street Name',help='Street Address')
    street_name2=fields.Char('Street Name 2')
    city=fields.Char()
    country=fields.Char()
    zip=fields.Char()
    dob=fields.Date('DOB',track_visibility='always')
    age = fields.Integer(compute="calculate_age", store=True)
    email=fields.Char('Email', track_visibility='always')
    mobile=fields.Char('Mobile', track_visibility='always')
    lang=fields.Selection([('tamil','Tamil'),('english','English'),('hindi','Hindi'),('french','French')],'Language')
    comment=fields.Text(track_visibility='always')
    customer_image=fields.Binary()

    @api.depends('dob')
    def calculate_age(self):
        for records in self:
            if records.dob:
                records.current_year = datetime.datetime.now().year
                records.birth_year = records.dob.year
                records.age =  records.current_year - records.dob.year

    @api.constrains('mobile')
    def _check_mobile(self):
        for record in self:
            if len(record.mobile)!=10:
                raise ValidationError("Please enter valid mobile number")
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
import random
import string
from datetime import timedelta


class Links(models.Model):
    _name = 'ponctual.links'
    _description = 'Ponctual Links'
    _rec_name = 'display_name'
    
    email = fields.Char(string='البريد الإلكتروني', required=True)
    link_uid = fields.Char(string='UID Link', compute='_compute_link_uid', store=True)
    created_at = fields.Datetime(string='تم إنشاؤه في', default=fields.Datetime.now)
    expired_at = fields.Datetime(string='تاريخ انتهاء الصلاحية', compute='_compute_expired_at')
    is_valid = fields.Boolean(string='هل الرابط صالح للاستخدام', compute='_compute_is_valid', default=False)
    is_used = fields.Boolean(string='هل تم استخدامه', default=False)
    is_still_active = fields.Boolean(string='هل تم استخدامه', default=True)


    def _compute_link_uid(self):
        for record in self:
            if not record.link_uid:
                characters = string.ascii_letters + string.digits
                random_string = ''.join(random.choices(characters, k=32))
                record.link_uid = random_string

    @api.depends('created_at', 'is_used')            
    def _compute_is_valid(self):
        for record in self:
            if record.created_at:
                record.is_valid = record.created_at + timedelta(days=1) > fields.Datetime.now() and not record.is_used and record.is_still_active
            else:
                record.is_valid = False
                
    @api.depends('created_at')
    def _compute_expired_at(self):
        for record in self:
            if record.created_at:
                record.expired_at = record.created_at + timedelta(days=1)
            else:
                record.expired_at = False
    
    def _get_customer_information(self):

        return {
            'customer_name':  self.email,  
            'customer_email': self.email,  
        }

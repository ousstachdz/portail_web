from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
import random
import string
from datetime import timedelta


class Links(models.Model):
    _name = 'ponctual.links'
    _description = 'Ponctual Links'
    _rec_name = 'display_name'
    
    display_name = fields.Char(string='Display Name', compute='_compute_display_name')
    email = fields.Char(string='البريد الإلكتروني', required=True)
    link = fields.Char(string='الرابط', compute='_compute_link')
    link_uid = fields.Char(string='UID Link', compute='_compute_link_uid', store=True)
    user_id = fields.Many2one('res.users', string='المسؤول عن إنشاء الرابط', default=lambda self: self.env.user, store=True, readonly=True)
    created_at = fields.Datetime(string='تم إنشاؤه في', default=fields.Datetime.now)
    expired_at = fields.Datetime(string='تاريخ انتهاء الصلاحية', compute='_compute_expired_at')
    is_valid = fields.Boolean(string='هل الرابط صالح للاستخدام', compute='_compute_is_valid', default=False)
    is_used = fields.Boolean(string='هل تم استخدامه', default=False)
    is_still_active = fields.Boolean(string='هل تم استخدامه', default=True)

    @api.depends('user_id')
    def _compute_display_name(self):
        for record in self:
            record.display_name = record.user_id.name

 
    @api.depends('link_uid')
    def _compute_link(self):
        for record in self:
            if record.link_uid:
                host = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
                record.link = f'{host}/portal-salam/{record.user_id.id}/{record.link_uid}'
             
    @api.depends('user_id')
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
         
    @api.model
    def create(self, vals):
        record = super(Links, self).create(vals)
        record._compute_link_uid()
        record._compute_link()
        return record

    def _check_is_valid_email(self):
        email = self.email
        if email and '@' in email and '.' in email.split('@')[-1]:
            return True
        else:
            raise ValidationError(_('Invalid email address. Please provide a valid email.'))

    def action_create_link(self):

        record = self.create({
            'email': self.email,
        })
        
        ctx = record._send_link_email()
                        
        return {
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'mail.compose.message',
            'target': 'new',
            'context': ctx,
        }

    def _send_link_email(self):
        self._check_is_valid_email()
        self.ensure_one()
        email_template = self.env['mail.template'].create({
            'name': 'Email Template',
            'model_id': self.env['ir.model']._get('ponctual.links').id,
            'subject': 'إكمال عملية التسجيل - ببنك السلام',
            'email_from': 'no_replay@alsalamalgeria.dz',
            'email_to': self.email,
            'body_html': f'''
        <div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; color: #333; direction: rtl;">
            <!-- Header with logo -->
            <div style="padding: 20px; text-align: center;   box-shadow: 0 2px 3px rgba(0, 0, 0, 0.05);">
                <img src="/portal_salam/static/src/img/logo.png" alt="شعار ببنك السلام" style="max-height: 150px;">
            </div>
            
            <!-- Main content -->
            <div style="padding: 30px 20px;">
                <h2 style="color: #045444;">السادة العملاء الكرام،</h2>
                
                <p>نشكركم لاختياركم <strong style="color: #045444;">ببنك السلام</strong> لخدماتكم المصرفية. نقدر ثقتكم في خدماتنا.</p>
                
                <p>لإكمال عملية التسجيل، يرجى الضغط على الرابط أدناه:</p>
                
                <div style="text-align: center; margin: 30px 0;">
                    <a href="{self.link}" style="background-color: #045444; color: white; padding: 12px 25px; 
                       text-decoration: none; border-radius: 4px; font-weight: bold; display: inline-block;">
                        إكمال عملية التسجيل
                    </a>
                </div>
                
                <p>هذا الرابط صالح لفترة محدودة. إذا لم تطلب هذا التسجيل، يرجى تجاهل هذه الرسالة.</p>
                
                <p>للحصول على المساعدة، يرجى الاتصال بخدمة العملاء على <a href="mailto:support@alsalamalgeria.dz" style="color: #045444;">support@alsalamalgeria.dz</a>.</p>
                
                <p>مع أطيب التحيات،<br>
                <strong>فريق ببنك السلام</strong></p>
            </div>
            
            <!-- Footer -->
            <div style="background-color: #f5f5f5; padding: 15px 20px; text-align: center; font-size: 12px;">
                <p>© 2023 ببنك السلام. جميع الحقوق محفوظة.</p>
                <p>العنوان: 233, شـارع اْحمـد واكـد دالـي ابراهيـم الجزائـر | الهاتف: </p>
            </div>
        </div>
        ''',
        })
        
        return{
            'default_model': 'ponctual.links',
            'default_res_ids': [self.ids[0]],
            'default_use_template': True,
            'default_template_id': email_template.id,
            'default_composition_mode': 'comment',
            'mark_so_as_sent': True,
            'force_email': True,
        }


    def action_resend_link(self):
        self.ensure_one()
        ctx = self._send_link_email()
                
        return {
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'mail.compose.message',
            'target': 'new',
            'context': ctx,
        }


    def action_deactivate_link(self):
        self.ensure_one()
        self.write({'is_still_active': False})
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'message': 'Link has been deactivated',
                'type': 'success',
                'next': {'type': 'ir.actions.act_window_close'},
            }
        }
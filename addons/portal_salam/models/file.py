from odoo import fields, models


class Document(models.Model):
    _name = 'fw.document'
    _description = 'Documents'

    document = fields.Binary(string='Document File', required=True)
    filename = fields.Char(string='Document',required=True)

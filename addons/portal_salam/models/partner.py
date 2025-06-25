from odoo import models, fields, api, _


class Partner(models.Model):
    _inherit = 'res.partner'

    nom_arabe = fields.Char(string='الاسم بالاحرف العربية')
    nrc = fields.Char(string='N.RC')
    nif = fields.Char(string='NIF')
    nis = fields.Char(string='NIS')
    date_creation = fields.Date(string='Date de création')
    branche = fields.Many2one('pw.agence', string='الفرع' )


class Partenaire(models.Model):
    _inherit = 'pw.partenaire'
    _description = 'Partenaire du client'

    lead_id = fields.Many2one('pw.lead')


class EquipeGestion(models.Model):
    _inherit = 'pw.gestion'
    _description = 'Equipe de gestion'

    lead_id = fields.Many2one('pw.lead')


class Taillefin(models.Model):
    _inherit = 'pw.taille'

    lead_id = fields.Many2one('pw.lead')


class SituationBancaire(models.Model):
    _inherit = 'pw.situation'

    lead_id = fields.Many2one('pw.lead')


class SituationFin(models.Model):
    _inherit = 'pw.situation.fin'

    lead_id = fields.Many2one('pw.lead')




class Fournisseur(models.Model):
    _inherit = 'pw.fournisseur'

    lead_id = fields.Many2one('pw.lead')


class Client(models.Model):
    _inherit = 'pw.client'

    lead_id = fields.Many2one('pw.lead')


class KycDetail(models.Model):
    _inherit = 'pw.kyc.details'

    lead_id = fields.Many2one('pw.lead')


class Companies(models.Model):
    _inherit = 'pw.companies'

    lead_id = fields.Many2one('pw.lead')


class DocChecker(models.Model):
    _inherit = 'pw.document.check'

    lead_id = fields.Many2one('pw.lead')


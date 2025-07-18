from matplotlib import pyplot as plt
from odoo import models, fields, api, _
from io import BytesIO
import numpy as np
import matplotlib
import base64

from odoo.exceptions import UserError

matplotlib.use('Agg')

list_ratio = [

    ('1', 'CA'),
    ('2', 'EBE'),
    ('3', 'EBE%'),
    ('4', 'RNC'),
    ('5', 'RNC%'),
    ('6', 'CAF'),
    ('7', 'CAF%'),
    ('8', 'Client en jours de CA'),
    ('9', 'Stock en jours d`achat'),
    ('10', 'Founisseur en jours de CA'),
    ('11', 'BFR'),
    ('12', 'BFR en jours de CA'),
    ('13', 'Endettement / TB'),
    ('14', 'FP / TB'),
]


class Lead(models.Model):
    _name = 'pw.lead'
    rec_name = 'display_name'
    _inherit = ["crm.lead",]
    display_name = fields.Char(string='oppertunity name', compute='_compute_display_name')

    date_creation = fields.Datetime(string='Date de création', default=fields.Datetime.now, readonly=True)
    branch = fields.Many2one('pw.agence', string='Agence')
    secteur = fields.Many2one('pw.secteur', string='Secteur d\'activité')
    activity = fields.Many2one('pw.activite', string='Activité en détails')
    demande_type = fields.Selection([('0', 'Entrer en relation'),
                                     ('1', 'Renouvellement'),
                                     ('2', 'Ponctuel')], string='Type de demande')
    product = fields.Selection([('0', 'Exploitation'),
                                ('1', 'Investissement'),
                                ('2', 'Leasing')], string='Type de ligne de credit')
    product_ids = fields.Many2many('pw.product', string='Lignes de credit')
    demande = fields.Many2one('pw.type.demande', string='الطلب')
    explanation = fields.Html(string='الغرض من الطلب')
    description_company = fields.Html(string='تعريف الشركة')
    montant_sollicite = fields.Float(string='Montant sollicité')
    file_tcr = fields.Binary(string='TCR N, N-1')
    file_tcr1 = fields.Binary(string='TCR N, N-1')
    file_actif = fields.Binary(string='Actif N, N-1')
    file_passif = fields.Binary(string='Passif N, N-1')
    tcr_id = fields.Many2one('import.ocr.tcr', 'TCR')
    passif_id = fields.Many2one('import.ocr.passif', 'Passif')
    actif_id = fields.Many2one('import.ocr.actif', 'Actif')
    visualisation = fields.Binary()
    resultat = fields.Float(string='Resultat Scoring')
    nif = fields.Char(string='NIF')
    rc = fields.Char(string='RC')
    nis = fields.Char(string='NIS')
    activity_code = fields.Char(string='رمز النشاط حسب السجل التجاري')
    activity_description = fields.Char(string='النشاط حسب السجل التجاري')
    branche = fields.Many2one('pw.agence', string='الفرع',
                              default=lambda self: self.env.user.partner_id.branche)
    num_compte = fields.Char(string='رقم الحساب')
    date_ouverture_compte = fields.Date(string='تاريخ فتح الحساب')
    date_debut = fields.Date(string='تاريخ تأسيس الشركة')
    demandes = fields.Many2many('pw.historique', string="تسهيلات الشركة")
    nom_arabe = fields.Char(string='الاسم بالاحرف العربية')
    nom_groupe = fields.Char(string='اسم الشركة')
    groupe = fields.Many2one('res.partner', string='المجموعة')
    classification = fields.Many2one(
        'pw.classification', string="تصنيف الشركة")
    adress_siege = fields.Char(string='عنوان المقر الاجتماعي')
    wilaya = fields.Many2one(
        'pw.wilaya', string='الولاية', related='branche.wilaya_id')
    date_inscription = fields.Date(string='تاريخ القيد في السجل التجاري')
    date_debut_activite = fields.Date(string='تاريخ بداية النشاط')
    activite = fields.Many2one(
        'pw.activite', string='النشاط الرئيسي حسب بنك الجزائر')
    activite_salam = fields.Many2one(
        'pw.activite.salam', string='النشاط الرئيسي حسب بنك السلام')
    activite_second = fields.Many2one(
        'pw.secteur', string='رمز النشاط الثانوي في السجل التجاري')
    activite_sec = fields.Char(string='رمز النشاط الثانوي في السجل التجاري')
    forme_jur = fields.Many2one('pw.forme.jur', string='الشكل القانوني')
    company_id = fields.Many2one(
        'res.company', default=lambda self: self.env.company)
    currency_id = fields.Many2one(
        'res.currency', related='company_id.currency_id')
    chiffre_affaire = fields.Monetary(
        string='راس المال الحالي KDA', currency_field='currency_id', )
    chiffre_affaire_creation = fields.Monetary(
        string='راس المال التاسيسي KDA', currency_field='currency_id', )

    apropos = fields.One2many(
        'pw.partenaire', 'lead_id', string='توزيع راس مال الشركة')
    gestion = fields.One2many('pw.gestion', 'lead_id', string='فريق التسيير')
    tailles = fields.One2many('pw.taille', 'lead_id',
                              string='حجم و هيكل التمويلات المطلوبة')
    fournisseurs = fields.One2many(
        'pw.fournisseur', 'lead_id', string='الموردون')
    clients = fields.One2many('pw.client', 'lead_id', string='الزبائن')
    situations = fields.One2many(
        'pw.situation', 'lead_id', string='الوضعية المالية')
    situations_fin = fields.One2many(
        'pw.situation.fin', 'lead_id', string='البيانات المالية المدققة للثلاث سنوات الأخيرة KDA')
    kyc = fields.One2many('pw.kyc.details', 'lead_id', string='اعرف عميلك KYC')
    companies = fields.One2many(
        'pw.companies', 'lead_id', string='معلومات حول الشركات ذات الصلة (KDA)')
    documents = fields.One2many(
        'pw.document.check', 'lead_id', string='الملفات')
    stage = fields.Selection([
                            ('step1', 'Step 1'),
                            ('step2', 'Step 2'),
                            ('step3', 'Step 3'),
                            ('step4', 'Step 4'),
                            ('step5', 'Step 5')], string='Stage', default='step1')

    tag_ids = fields.Many2many(
        'crm.tag',
        'pw_lead_tag_rel',  # Changed relation table name
        'lead_id',
        'tag_id',
        string='Tags'
    )

    @api.depends('demande')
    def _compute_display_name(self):
        for rec in self:
            if rec.demande:
                rec.display_name = rec.name + ' - ' + rec.demande.name
            else:
                rec.display_name = rec.name

    
    def calcul_ratio(self):
        for rec in self:
            if rec.tcr_id.state != 'valide' or rec.actif_id.state != 'valide' or rec.passif_id.state != 'valide':
                raise UserError('Vous devriez valider les bilans')
            else:
                if not rec.ratio_ids:
                    for index, item in list_ratio:
                        self.env['pw.ratio'].create({'lead': rec.id,
                                                      'ratio': index,
                                                      'name': item,
                                                      'montant_n': 0,
                                                      'montant_n1': 0,
                                                      })
                ratio_1 = rec.ratio_ids.filtered(lambda l: l.ratio == '1')
                tcr_7 = rec.tcr_id.tcr_lines.filtered(
                    lambda r: r.rubrique.sequence == 7)
                ratio_1.montant_n = tcr_7.montant_n
                ratio_1.montant_n1 = tcr_7.montant_n1

                ratio_2 = rec.ratio_ids.filtered(lambda l: l.ratio == '2')
                tcr_33 = rec.tcr_id.tcr_lines.filtered(
                    lambda r: r.rubrique.sequence == 33)
                ratio_2.montant_n = tcr_33.montant_n
                ratio_2.montant_n1 = tcr_33.montant_n1

                ratio_3 = rec.ratio_ids.filtered(lambda l: l.ratio == '3')
                ratio_3.montant_n = (
                    tcr_33.montant_n / tcr_7.montant_n) * 100 if tcr_7.montant_n != 0 else 0
                ratio_3.montant_n1 = (
                    tcr_33.montant_n1 / tcr_7.montant_n1) * 100 if tcr_7.montant_n1 != 0 else 0

                ratio_4 = rec.ratio_ids.filtered(lambda l: l.ratio == '4')
                tcr_50 = rec.tcr_id.tcr_lines.filtered(
                    lambda r: r.rubrique.sequence == 50)
                ratio_4.montant_n = tcr_50.montant_n
                ratio_4.montant_n1 = tcr_50.montant_n1

                ratio_5 = rec.ratio_ids.filtered(lambda l: l.ratio == '5')
                ratio_5.montant_n = (
                    tcr_50.montant_n / tcr_7.montant_n) * 100 if tcr_7.montant_n != 0 else 0
                ratio_5.montant_n1 = (
                    tcr_50.montant_n / tcr_7.montant_n) * 100 if tcr_7.montant_n1 != 0 else 0

                ratio_6 = rec.ratio_ids.filtered(lambda l: l.ratio == '6')
                tcr_36 = rec.tcr_id.tcr_lines.filtered(
                    lambda r: r.rubrique.sequence == 36)
                ratio_6.montant_n = tcr_50.montant_n + tcr_36.montant_n
                ratio_6.montant_n1 = tcr_50.montant_n1 + tcr_36.montant_n1

                ratio_7 = rec.ratio_ids.filtered(lambda l: l.ratio == '7')
                ratio_7.montant_n = (ratio_6.montant_n /
                                     tcr_36.montant_n) * 100
                ratio_7.montant_n1 = (
                    ratio_6.montant_n1 / tcr_36.montant_n1) * 100

                ratio_8 = rec.ratio_ids.filtered(lambda l: l.ratio == '8')
                actif_20 = rec.actif_id.actif_lines.filtered(
                    lambda r: r.rubrique.sequence == 20)
                ratio_8.montant_n = (actif_20.montant_n * 360) / \
                    tcr_7.montant_n if tcr_7.montant_n != 0 else 0
                ratio_8.montant_n1 = (
                    actif_20.montant_n1 * 360) / tcr_7.montant_n1 if tcr_7.montant_n1 != 0 else 0

                ratio_9 = rec.ratio_ids.filtered(lambda l: l.ratio == '9')
                tcr_12 = rec.tcr_id.tcr_lines.filtered(
                    lambda r: r.rubrique.sequence == 12)
                actif_18 = rec.actif_id.actif_lines.filtered(
                    lambda r: r.rubrique.sequence == 18)
                ratio_9.montant_n = (actif_18.montant_n * 360) / \
                    tcr_12.montant_n if tcr_12.montant_n != 0 else 0
                ratio_9.montant_n1 = (
                    actif_18.montant_n1 * 360) / tcr_12.montant_n1 if tcr_12.montant_n1 != 0 else 0

                ratio_10 = rec.ratio_ids.filtered(lambda l: l.ratio == '10')
                passif_20 = rec.passif_id.passif_lines.filtered(
                    lambda r: r.rubrique.sequence == 20)
                ratio_10.montant_n = (
                    passif_20.montant_n * 360) / tcr_7.montant_n if tcr_7.montant_n != 0 else 0
                ratio_10.montant_n1 = (
                    passif_20.montant_n1 * 360) / tcr_7.montant_n1 if tcr_7.montant_n1 != 0 else 0

                ratio_11 = rec.ratio_ids.filtered(lambda l: l.ratio == '11')
                ratio_11.montant_n = actif_20.montant_n + \
                    actif_18.montant_n - passif_20.montant_n
                ratio_11.montant_n1 = actif_20.montant_n1 + \
                    actif_18.montant_n1 - passif_20.montant_n1

                ratio_12 = rec.ratio_ids.filtered(lambda l: l.ratio == '12')
                ratio_12.montant_n = (
                    ratio_11.montant_n * 360) / tcr_7.montant_n if tcr_7.montant_n != 0 else 0
                ratio_12.montant_n1 = (
                    ratio_11.montant_n1 * 360) / tcr_7.montant_n1 if tcr_7.montant_n1 != 0 else 0

                ratio_13 = rec.ratio_ids.filtered(lambda l: l.ratio == '13')
                passif_14 = rec.passif_id.passif_lines.filtered(
                    lambda r: r.rubrique.sequence == 14)
                passif_23 = rec.passif_id.passif_lines.filtered(
                    lambda r: r.rubrique.sequence == 23)
                passif_25 = rec.passif_id.passif_lines.filtered(
                    lambda r: r.rubrique.sequence == 25)
                ratio_13.montant_n = ((passif_14.montant_n + passif_23.montant_n) /
                                      passif_25.montant_n) * 100 if passif_25.montant_n != 0 else 0
                ratio_13.montant_n1 = ((passif_14.montant_n1 + passif_23.montant_n1) /
                                       passif_25.montant_n1) * 100 if passif_25.montant_n1 != 0 else 0

                ratio_14 = rec.ratio_ids.filtered(lambda l: l.ratio == '14')
                passif_12 = rec.passif_id.passif_lines.filtered(
                    lambda r: r.rubrique.sequence == 12)
                ratio_14.montant_n = (
                    passif_12.montant_n / passif_25.montant_n) * 100 if passif_25.montant_n != 0 else 0
                ratio_14.montant_n1 = (
                    passif_12.montant_n1 / passif_25.montant_n1) * 100 if passif_25.montant_n1 != 0 else 0
                rec.create_viz3()

    def create_viz3(self):
        for rec in self:
            line1 = rec.ratio_ids.filtered(lambda r: r.ratio == '1')
            line2 = rec.ratio_ids.filtered(lambda r: r.ratio == '2')
            line3 = rec.ratio_ids.filtered(lambda r: r.ratio == '4')
            data1 = [line1.montant_n, line1.montant_n1]
            data2 = [line2.montant_n, line2.montant_n1]
            data3 = [line3.montant_n, line3.montant_n1]
            label1 = 'CA'
            label2 = 'EBE'
            label3 = 'RNC'
            year = ["N", "N-1"]
            fig, ax = plt.subplots()
            width = 0.12
            X_axis = np.arange(len(year))
            rects1 = ax.bar(X_axis - width, data1, width,
                            color="yellow", label=label1)
            rects2 = ax.bar(X_axis, data2, width, color="orange", label=label2)
            rects3 = ax.bar(X_axis + width, data3, width,
                            color="red", label=label3)
            ax.set_ylabel('Montant')
            ax.set_title('Montant par année')
            ax.set_xticks(X_axis + width, year)
            ax.legend(loc="lower left", bbox_to_anchor=(0.8, 1.0))
            fig.tight_layout()
            buf = BytesIO()
            plt.savefig(buf, format='jpeg', dpi=100)
            buf.seek(0)
            rec.visualisation = base64.b64encode(buf.getvalue())
            buf.close()

    def calcul_scoring(self):
        for rec in self:
            all_valid = True
            if not rec.original_capital:
                all_valid = False
            elif not rec.actionnariat:
                all_valid = False
            elif not rec.forme_jur:
                all_valid = False
            elif not rec.remp_succession:
                all_valid = False
            elif not rec.competence:
                all_valid = False
            elif not rec.experience:
                all_valid = False
            elif not rec.soutien_etatic:
                all_valid = False
            elif not rec.activite:
                all_valid = False
            elif not rec.influence_tech:
                all_valid = False
            elif not rec.anciennete:
                all_valid = False
            elif not rec.concurrence:
                all_valid = False
            elif not rec.source_appro:
                all_valid = False
            elif not rec.produit:
                all_valid = False
            elif not rec.flexibilite:
                all_valid = False
            elif not rec.sollicitude:
                all_valid = False
            elif not rec.situation:
                all_valid = False
            elif not rec.mouvement:
                all_valid = False
            elif not rec.garanties:
                all_valid = False
            elif not rec.incident:
                all_valid = False
            elif not rec.conduite:
                all_valid = False
            elif not rec.dette_fisc:
                all_valid = False
            elif not rec.source_remb:
                all_valid = False
            elif not rec.part_profil:
                all_valid = False
            if not all_valid:
                UserError('Vous devriez remplir tout les critères')
            if all_valid:
                result_qual = rec.original_capital.ponderation + rec.actionnariat.ponderation + \
                    rec.forme_jur.ponderation + rec.remp_succession.ponderation + \
                    rec.competence.ponderation + rec.experience.ponderation + \
                    rec.soutien_etatic.ponderation + rec.activite.ponderation + \
                    rec.influence_tech.ponderation + rec.anciennete.ponderation + \
                    rec.concurrence.ponderation + rec.source_appro.ponderation + \
                    rec.produit.ponderation + rec.flexibilite.ponderation + \
                    rec.sollicitude.ponderation + rec.situation.ponderation + \
                    rec.mouvement.ponderation + rec.garanties.ponderation + \
                    rec.incident.ponderation + rec.conduite.ponderation + \
                    rec.dette_fisc.ponderation + rec.source_remb.ponderation + \
                    rec.part_profil.ponderation
                rec.resultat = result_qual


class Ratio(models.Model):
    _name = 'pw.ratio'

    name = fields.Char(string='Ratio')
    ratio = fields.Selection(list_ratio, string='Ratio')
    montant_n = fields.Float(string='N')
    montant_n1 = fields.Float(string='N-1')
    lead = fields.Many2one('pw.lead')

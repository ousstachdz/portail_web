
from odoo import models, fields, api


LIST = [('1', 'طلب التسهيلات ممضي من طرف المفوض القانوني عن الشركة'),
          ('2', 'الميزانيات لثلاث سنوات السابقة مصادق عليها من طرف المدقق المحاس'),
          ('3',
           ' الميزانية الافتتاحية و الميزانية المتوقعة للسنة المراد تمويلها موقعة من طرف الشركة (حديثة النشأة)'),
          ('4', 'مخطط تمويل الاستغلال مقسم الى أرباع السنة للسنة المراد تمويلها'),
          ('5',
           ' المستندات و الوثائق المتعلقة بنشاط الشركة ( عقود، صفقات ،  طلبيات ، ... )'),
          ('6', 'محاضر الجمعيات العادية و الغير العادية للأشخاص المعنويين'),
          ('7', 'نسخة مصادق عليها من السجل التجاري'),
          ('8', 'نسخة مصادق عليها من القانون الأساسي للشركة'),
          ('9', 'مداولة الشركاء أو مجلس الإدارة لتفويض المسير لطلب القروض البنكية'),
          ('10', 'نسخة مصادق عليها من النشرة الرسمية للإعلانات القانونية'),
          ('11', 'نسخة طبق الأصل لعقد ملكية أو استئجار المحلات ذات الاستعمال المهني'),
          ('12',
           ' نسخة طبق الأصل للشهادات الضريبية و شبه الضريبية حديثة (أقل من ثلاثة أشهر)'),
          ('13', 'استمارة كشف مركزية المخاطر ممضية من طرف ممثل الشركة (نموذج مرفق)'),
          ('14', 'آخر تقرير مدقق الحسابات'),
          ('15', 'Actif, Passif, TCR (N, N-1)'),
          ('16', 'Actif, Passif, TCR (N-2, N-3)')
          ]





class Wilaya(models.Model):
    _name = 'pw.wilaya'
    _rec_name = 'domaine'
    name = fields.Char(string="الرمز")
    domaine = fields.Char(string='الولاية')
    description = fields.Char(string='الاسم')
    wilaya_arabe = fields.Char(string='اسم الولاية بالعربية')



class Agence(models.Model):
    _name = 'pw.agence'
    _description = "Liste des agences de la banque"
    _rec_name = 'ref'
    name = fields.Char(string='رمز الفرع', size=5)
    wilaya = fields.Char(string='الولاية')
    ref = fields.Char(string='الولاية', )
    commune = fields.Char(string="المجلس الشعبي البلدي")
    wilaya_id = fields.Many2one('pw.wilaya',compute='compute_ref')

    def compute_ref(self):
        for rec in self:
            wilaya = self.env['pw.wilaya'].search([('name', '=', rec.wilaya)])
            commune = self.env['pw.commune'].search([('name', '=', rec.commune),
                                                     ('domaine', '=', rec.wilaya)])
            print(wilaya)
            print(commune)
            print(commune.description)
            if wilaya:

                rec.wilaya_id = wilaya.id
            else:
                rec.wilaya_id = False
            if commune:
                print(commune.description)
                if not rec.ref:
                    rec.ref = rec.name + '-' + commune.description

    def create_folder(self):
        for rec in self:
            folder = self.env['documents.folders'].search([('branch', '=', rec.id), ('client', '=', False)])
            if not folder:
                folder = self.env['documents.folders'].create({'branch': rec.id,
                                                               'name': rec.ref})

            clients = self.env['res.partner'].search([('branche', '=', rec.id)])
            for client in clients:
                client_folder = self.env['documents.folders'].search([('parent_folder_id', '=', folder.id),
                                                                        ('client', '=', client.id)])
                if not client_folder:
                    client_folder = self.env['documents.folders'].create({'branch': rec.id,
                                                                   'name': client.num_compte,
                                                                   'parent_folder_id': folder.id,
                                                                   'client': client.id})



class Secteur(models.Model):
    _name = 'pw.secteur'
    _description = 'Liste des secteurs'

    name = fields.Char(string='Secondary activity')
    activity = fields.Many2one('pw.activite', string='Main activity')



class Activity(models.Model):
    _name = 'pw.activite'
    _description = 'Liste des activités'
    _rec_name = 'domaine'

    name = fields.Char(string='الرمز')
    domaine = fields.Char(string='النشاط')
    description = fields.Char(string='Description')


class Product(models.Model):
    _name = 'pw.product'
    _description = 'Liste des produits de la banque'

    name = fields.Char(string='منتجات المصرف')
    for_branch = fields.Boolean(string='للفرع')


class TypeDemande(models.Model):
    _name = 'pw.type.demande'
    _description = 'Liste des types de demandes'

    name = fields.Char(string='نوع الطلب')


class Garanties(models.Model):
    _name = 'pw.garanties'

    name = fields.Char(string='الشروط و الضمانات')



class Historique(models.Model):
    _name = 'pw.historique'
    _description = 'Hisotorique du client'

    type = fields.Many2one('pw.type.demande', string='نوع التسهيلات الممنوحة')
    date = fields.Date(string='تاريخ الرخصة')
    date_fin = fields.Date(string='صالحة لغاية')
    montant = fields.Float(string='المبلغ')
    garanties = fields.Many2one('pw.garanties', string='الشروط و الضمانات')


class ClassificationEntreprise(models.Model):
    _name = 'pw.classification'
    _description = "Classification de l'entreprise"

    name = fields.Char(string='تصنيف الشركة')


class ActivitieSalam(models.Model):
    _name = 'pw.activite.salam'

    name = fields.Char(string='النشاط')


class FormeJuridique(models.Model):
    _name = 'pw.forme.jur'
    _description = 'Lignes des formes juridiques'

    name = fields.Char(string='الشكل القانوني')


class Partenaire(models.Model):
    _name = 'pw.partenaire'
    _description = 'Partenaire du client'

    nom_partenaire = fields.Char(string='اسم الشريك/المالك')
    age = fields.Date(string='تاريخ التاسيس/الميلاد')
    pourcentage = fields.Float(string='نسبة الحصة')
    statut_partenaire = fields.Char(string='صفة الشريك')
    nationalite = fields.Many2one('res.country', string='الجنسية', default=lambda self: self.env['res.country'].search([('code', '=', 'DZ')], limit=1))
    etape_id = fields.Integer(string='pw.etape')


class Fournisseur(models.Model):
    _name = 'pw.fournisseur'
    _description = 'fournisseur'


    etape_id = fields.Integer(string='pw.etape')
    name = fields.Char(string='الاسم')
    country = fields.Many2one('res.country', string='البلد')
    type_payment = fields.Many2many('pw.type.payment', string='طريقة السداد')


class SituationBancaire(models.Model):
    _name = 'pw.situation'
    _description = 'Situation bancaire et obligations envers autrui'

    banque = fields.Many2one('pw.banque', string='البنك')
    type_fin = fields.Many2one('pw.fin.banque', string='نوع التمويل')
    montant = fields.Float(string='المبلغ KDA')
    montant_dollar = fields.Float(string='المبلغ $', compute='compute_dollar')
    encours = fields.Float(string='المبلغ المستغل KDA')
    encours_dollar = fields.Float(string='المبلغ المستغل $', compute='compute_dollar')
    garanties = fields.Text(string='الضمانات الممنوحة')
    etape_id = fields.Integer(string='pw.etape')

    def compute_dollar(self):
        for rec in self:
            taux_change = rec.etape_id.workflow.states.filtered(lambda l:l.sequence == 2).taux_change or 1
            rec.montant_dollar = rec.montant / taux_change
            rec.encours_dollar = rec.encours / taux_change


class SituationFinanciere(models.Model):
    _name = 'pw.situation.fin'
    _description = 'Situation financière'

    type = fields.Char(string='السنة')
    sequence = fields.Integer(string='Sequence')
    year1 = fields.Float(string='N')
    year2 = fields.Float(string='N-1')
    year3 = fields.Float(string='N-2')
    etape_id = fields.Integer(string='pw.etape')


class KycDetail(models.Model):
    _name = 'pw.kyc.details'
    _description = 'Line KYC'

    info = fields.Char(string='معلومات إضافية عن العميل')
    answer = fields.Selection([('oui', 'نعم'),
                               ('non', 'لا')], string='نعم/ لا')
    detail = fields.Char(string='التفاصيل')
    etape_id = fields.Integer(string='pw.etape')


class Companies(models.Model):
    _name = 'pw.companies'
    _description = 'Companies in relation'

    name = fields.Char(string='الشركة')
    date_creation = fields.Char(string='سنة التاسيس', size=4)
    activite = fields.Many2one('pw.activite', string='النشاط الرئيسي')
    chiffre_affaire = fields.Float(string='راس المال')
    n1_num_affaire = fields.Integer(string='رقم الاعمال N-1')
    n_num_affaire = fields.Integer(string='رقم الاعمال N')

    etape_id = fields.Integer(string='pw.etape')


class DocChecker(models.Model):
    _name = 'pw.document.check'
    _description = ' check documents'


    list_document = fields.Selection(selection=LIST, string='اسم الملف')
    list_doc = fields.Char(string='اسم الملف', required=True)
    document = fields.Binary(string='الملف',)
    filename = fields.Char(string='الاسم', compute='compute_filename', store=True)
    answer = fields.Selection([('oui', 'نعم'),
                               ('non', 'لا')], string='نعم/ لا')
    note = fields.Text(string='التعليق')
    etape_id = fields.Integer(string='pw.etape')
    checked = fields.Boolean(string='Checked', default=False)

    def open_document(self):
        for rec in self:
            view_id = self.env.ref('dept_pw.view_bilan_wizard_form').id
            context = dict(self.env.context or {})
            context['pdf_1'] = rec.document
            wizard = self.env['view.bilan.wizard'].create({'pdf_1': rec.document})
            return {
                'name': 'الصورة',
                'type': 'ir.actions.act_window',
                'view_mode': 'form',
                'res_model': 'view.bilan.wizard',
                'res_id': wizard.id,
                'view_id': view_id,
                'target': 'new',
                'context': context,
            }

    @api.model
    def create(self, vals):
        if 'list_document' in vals:
            for index, item in LIST:
                if index == vals['list_document']:
                    vals['filename'] = item
        return super(DocChecker, self).create(vals)



    @api.depends('list_document', 'list_doc')
    def compute_filename(self):
        for rec in self:
            if rec.list_document:
                for index, item in LIST:
                    if index == rec.list_document:
                        rec.filename = item
                        rec.list_doc = item
            else:
                rec.filename = rec.list_doc



class EquipeGestion(models.Model):
    _name = 'pw.gestion'
    _description = 'Equipe de gestion'

    name = fields.Char(string='السيد(ة)')
    job = fields.Char(string='المهنة')
    niveau_etude = fields.Char(string='المستوى الدراسي')
    age = fields.Integer(string='السن')
    experience = fields.Integer(string='الخبرة المهنية')
    etape_id = fields.Integer(string='pw.etape')




class Taillefin(models.Model):
    _name = 'pw.taille'
    _description = 'La taille et la structure du financement requis'

    type_demande = fields.Many2one('pw.product', string='نوع التسهيلات')
    type_demande_ids = fields.Many2many('pw.product', string='نوع التسهيلات')
    montant = fields.Float(string='المبلغ المطلوب')
    raison = fields.Char(string='الغرض من التمويل')
    garanties = fields.Many2many('pw.garanties', string='الضمانات المقترحة')
    preg = fields.Float(string='هامش الجدية')
    duree = fields.Integer(string='المدة (الايام)')
    etape_id = fields.Integer(string='pw.etape')



class Client(models.Model):
    _name = 'pw.client'
    _description = 'clients'

    etape_id = fields.Integer(string='pw.etape')
    name = fields.Char(string='الاسم')
    country = fields.Many2one('res.country', string='البلد', default=lambda self: self.env['res.country'].search([('code', '=', 'DZ')], limit=1))
    type_payment = fields.Many2many('pw.type.payment', string='طريقة السداد')


class TypePayment(models.Model):
    _name = 'pw.type.payment'
    _description = 'Type Payment'

    name = fields.Char(string='name')
    type = fields.Selection([('1', 'المورد'),
                             ('2', 'الزبون'),
                             ('3', 'الكل')])


class Country(models.Model):
    _inherit = 'res.country'

    to_show = fields.Boolean(string='To not show in workflow')

class Banque(models.Model):
    _name = 'pw.banque'

    name = fields.Char(string='Désignation', required=True, copy=False)
    code = fields.Char(string='Code', required=True, copy=False)


class FinancementBanque(models.Model):
    _name = 'pw.fin.banque'
    _description = 'autres type de financement'

    name = fields.Char(string='نوع التمويل')

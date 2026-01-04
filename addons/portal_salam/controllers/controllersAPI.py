from odoo import http, fields
from odoo.http import request
from datetime import timedelta
import json

import base64

import logging
logger = logging.getLogger(__name__)

List_items = [('1', 'هل العميل شخص مقرب سياسيا؟'),
              ('2', 'هل أحد الشركاء/المساهمين/مسير مقرب سياسيا؟'),
              ('3', 'هل العميل أو أحد الشركاء/المساهمين/مسير مقرب من البنك؟'),
              ('4', 'هل للعميل شركات زميلة / مجموعة؟'),
              ('5', 'المتعامل / أحد الشركاء مدرج ضمن القوائم السوداء'),
              ('6', 'المتعامل / أحد الشركاء مدرج ضمن قائمة الزبائن المتعثرين بمركزية المخاطر لبنك الجزائر')]
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

list_situation = [
    ('1', 'حقوق الملكية'),
    ('2', 'مجموع الميزانية'),
    ('3', 'رقم الأعمال'),
    ('4', 'صافي الارباح')
]


class OpportunityControllerAPI(http.Controller):

    @http.route(['/portal-salam/<string:link_uid>'], type='http', auth='public', website=True, csrf=True)
    def opportunity_api_form(self, link_uid, **kwargs):

        link = request.env['ponctual.links'].sudo().search(
            [ ('link_uid', '=', link_uid)], limit=1)


        if link:
            if link.is_valid:
              return request.render('portal_salam.opportunity_api_form', {})
        
        return request.render('portal_salam.opportunity_api_form_error_page', {})

    @http.route(['/opportunity/form_data'], type='http', auth='public',  csrf=True, methods=['GET'], cors='*')
    def opportunity_form(self, **kwargs):
        opportunity_id = kwargs.get('opportunity_id', 0)
        activities = request.env['pw.activite'].search([])
        activities = [{"id": activity.id, "name": activity.name}
                      for activity in activities]
        classifications = request.env['pw.classification'].search([])
        classifications = [{"id": classification.id, "name": classification.name}
                           for classification in classifications]

        demandes = request.env['pw.type.demande'].search([])
        demandes = [{"id": demande.id, "name": demande.name}
                    for demande in demandes]

        forme_jurs = request.env['pw.forme.jur'].search([])
        forme_jurs = [{"id": forme_jur.id, "name": forme_jur.name}
                      for forme_jur in forme_jurs]

        apropos_ids = request.env['pw.partenaire'].search(
            [('lead_id', '=', int(opportunity_id))])
        apropos_ids = [{"id": apropos_id.id, "name": apropos_id.name}
                       for apropos_id in apropos_ids]

        gestion_ids = request.env['pw.gestion'].search(
            [('lead_id', '=', int(opportunity_id))])
        gestion_ids = [{"id": gestion_id.id, "name": gestion_id.name}
                       for gestion_id in gestion_ids]

        taille_ids = request.env['pw.taille'].search(
            [('lead_id', '=', int(opportunity_id))])
        taille_ids = [{"id": taille_id.id, "name": taille_id.name}
                      for taille_id in taille_ids]

        situation_ids = request.env['pw.situation'].search(
            [('lead_id', '=', int(opportunity_id))])
        situation_ids = [{"id": situation_id.id, "name": situation_id.name}
                         for situation_id in situation_ids]

        fournisseur_ids = request.env['pw.fournisseur'].search(
            [('lead_id', '=', int(opportunity_id))])
        fournisseur_ids = [{"id": fournisseur_id.id, "name": fournisseur_id.name}
                           for fournisseur_id in fournisseur_ids]

        client_ids = request.env['pw.client'].search(
            [('lead_id', '=', int(opportunity_id))])
        client_ids = [{"id": client_id.id, "name": client_id.name}
                      for client_id in client_ids]

        company_ids = request.env['pw.companies'].search(
            [('lead_id', '=', int(opportunity_id))])
        company_ids = [{"id": company_id.id, "name": company_id.name}
                       for company_id in company_ids]

        nationalites = request.env['res.country'].search(
            [('to_show', '=', False)])
        nationalites = [{"id": nationality.id, "name": nationality.name}
                        for nationality in nationalites]

        garanties = request.env['pw.garanties'].search([])
        garanties = [{"id": garantie.id, "name": garantie.name}
                     for garantie in garanties]

        type_demande_ids = request.env['pw.product'].search(
            [('for_branch', '=', True)])
        type_demande_ids = [{"id": type_demande_id.id, "name": type_demande_id.name}
                            for type_demande_id in type_demande_ids]
        banque_ids = request.env['pw.banque'].search([])
        banque_ids = [{"id": banque_id.id, "name": banque_id.name}
                      for banque_id in banque_ids]
        type_fin_ids = request.env['pw.fin.banque'].search([])
        type_fin_ids = [{"id": type_fin_id.id, "name": type_fin_id.name}
                        for type_fin_id in type_fin_ids]

        type_payment_ids = request.env['pw.type.payment'].search([])
        type_payment_ids = [{"id": type_payment_id.id, "name": type_payment_id.name}
                            for type_payment_id in type_payment_ids]

        if opportunity_id != 0:
            opportunity = request.env['pw.lead'].sudo().browse(int(opportunity_id))
        else:
            opportunity = False
        situation_fin = request.env['pw.situation.fin'].search(
            [('lead_id', '=', int(opportunity_id))])

        values = {
            'step': opportunity.stage if opportunity else 'step1',
            'opportunity_id': opportunity_id if opportunity_id else 0,
            'activities': activities,
            'nationalites': nationalites,
            'classifications': classifications,
            'demandes': demandes,
            'forme_jurs': forme_jurs,
            'banque_ids': banque_ids,
            'type_fin_ids': type_fin_ids,
            'apropos_ids': apropos_ids,
            'gestion_ids': gestion_ids,
            'taille_ids': taille_ids,
            'kyc_ids': List_items,
            'situation_ids': situation_ids,
            'fournisseur_ids': fournisseur_ids,
            'client_ids': client_ids,
            'company_ids': company_ids,
            'garanties_ids': garanties,
            'answers': [('oui', 'نعم'),
                        ('non', 'لا')],
            'type_demande_ids': type_demande_ids,
            'type_payment_ids': type_payment_ids,
        }

        for index, fin in enumerate(situation_fin):
            values[f'fin{index+1}_1'] = fin.year1
            values[f'fin{index+1}_2'] = fin.year2
            values[f'fin{index+1}_3'] = fin.year3
        for index, fin in enumerate(situation_fin):
            values[f'fin{index+1}_1'] = fin.year1
            values[f'fin{index+1}_2'] = fin.year2
            values[f'fin{index+1}_3'] = fin.year3

        return request.make_response(
            json.dumps(values, default=str),
            headers={'Content-Type': 'application/json'}
        )

    @http.route(['/opportunity/form_data/save'], type='http', auth='public', methods=['POST'], website=True, csrf=False, cors='*')
    def opportunity_submit(self, **post):
        try:
            data = json.loads(request.httprequest.data)
            def handle_empty_date(field):
                return field if field else None
            link_hash = data.get('link_hash')
            
            link = request.env['ponctual.links'].sudo().search(
             [ ('link_uid', '=', link_hash)], limit=1)

            # if not link.is_valid:
            #     logger.exception('error: Invalid link')
            #     return request.render('portal_salam.opportunity_api_form_error_page', {})

            lead_values = {

	            'link_hash' : data.get('link_hash'),
                'name': data.get('name'),
                'phone': data.get('phone'),
                'email_from': data.get('email_from'),
                'adress_siege': data.get('adress_siege'),
                'nif': data.get('nif'),
                'rc': data.get('rc'),
                'num_compte': data.get('num_compte'),
                'date_ouverture_compte': handle_empty_date(data.get('date_ouverture_compte')),
                'date_debut': handle_empty_date(data.get('date_debut')),
                'nom_arabe': data.get('nom_arabe'),
                'date_debut_activite': handle_empty_date(data.get('date_debut_activite')),
                'activity_code': data.get('activity_code'),
                'activity_description': data.get('activity_description'),
                'activite_sec': data.get('activite_sec'),
                'classification': int(data.get('classification')) if data.get('classification') else None,
                'forme_jur': int(data.get('forme_jur')) if data.get('forme_jur') else None,
                'chiffre_affaire': float(data.get('chiffre_affaire')) if data.get('chiffre_affaire') else 0.0,
                'chiffre_affaire_creation': float(data.get('chiffre_affaire_creation')) if data.get('chiffre_affaire_creation') else 0.0,
                'demande': int(data.get('demande')) if data.get('demande') else None,
                'explanation': data.get('explanation'),
                'description_company': data.get('description_company'),
            }

            opportunity = request.env['pw.lead'].sudo().create(lead_values)
            documents = []

            document_dict = {
                item[0]: item[1]
                for item in LIST
            }

            documents_values = {
                f'document_{i}': data.get(f'document_{i}')
                for i in range(1, 17)
            }

            for key, document_id in documents_values.items():
                logger.info(f"Processing key: {key}, value: {document_id}")

                if not (key.startswith('document_') and document_id):
                    logger.info(f"Skipping {key}: empty or invalid")
                    continue

                try:
                    document_id = int(document_id)
                except (ValueError, TypeError):
                    logger.error(f"Invalid document ID for {key}: {document_id}")
                    continue

                # Fetch uploaded document
                document = request.env['fw.document'].sudo().browse(document_id)

                if not document.exists():
                    logger.error(f"fw.document not found for ID {document_id}")
                    continue

                list_document_id = key.split('_')[1]

                documents.append({
                    'list_document': list_document_id,
                    'list_doc': document_dict.get(list_document_id, ''),
                    'document': document.document,     
                    'lead_id': opportunity.id,
                })

                logger.info(f"Document {document_id} linked successfully")
            

            if documents:
                if not opportunity.documents:
                    request.env['pw.document.check'].sudo().create(documents)
                else:
                    for doc in documents:
                        exist_doc = opportunity.documents.filtered(
                            lambda l: l.list_document == doc['list_document']
                        )
                        if exist_doc:
                            exist_doc.write(doc)
                        else:
                            request.env['pw.document.check'].sudo().create(doc)
            logger.info(f"############################################## \n Document linked to opportunity successfully")

            partner_ids, gestion_ids, taille_ids, fournisseur_ids, client_ids, situation_ids, company_ids = [
            ], [], [], [], [], [], []

            for partner in data.get('partners', []):
                partner_values = {
                    'nom_partenaire': partner.get('nom_partenaire'),
                    'age': partner.get('age'),
                    'pourcentage': partner.get('pourcentage'),
                    'statut_partenaire': partner.get('statut_partenaire'),
                    'nationalite': request.env['res.country'].sudo().browse(int(partner.get('country'))).id if partner.get('country') else None,
                    'lead_id': opportunity.id
                }
                partner_record = request.env['pw.partenaire'].sudo().create(
                    partner_values)
                partner_ids.append(partner_record.id)

            for manager in data.get('managers', []):
                gestion_values = {
                    'name': manager.get('name'),
                    'job': manager.get('job'),
                    'niveau_etude': manager.get('niveau_etude'),
                    'age': int(manager.get('age')),
                    'experience': int(manager.get('experience')),
                    'lead_id': opportunity.id
                }
                gestion_record = request.env['pw.gestion'].sudo().create(
                    gestion_values)
                gestion_ids.append(gestion_record.id)

            for taille in data.get('tailles', []):
                taille_values = {
                    'type_demande': request.env['pw.product'].sudo().search([('name', '=', taille['type_demande']['name'])], limit=1).id,
                    'montant': float(taille.get('montant', 0.0)),
                    'raison': taille.get('raison'),
                    'preg': float(taille.get('preg', 0.0)),
                    'duree': int(taille.get('duree', 0)),
                    'garanties': [(6, 0, [int(garantie_id) for garantie_id in taille.get('garanties', [])])],
                    'lead_id': opportunity.id
                }
                taille_record = request.env['pw.taille'].sudo().create(taille_values)
                taille_ids.append(taille_record.id)

            for situation in data.get('situationTailles', []):
                situation_values = {
                    'banque': request.env['pw.banque'].sudo().browse(int(situation['banque']['id'])).id if situation.get('banque') else None,
                    'type_fin': request.env['pw.fin.banque'].sudo().browse(int(situation['typeFin']['id'])).id if situation.get('typeFin') else None,
                    'montant': float(situation.get('situationMontant')),
                    'encours': float(situation.get('situationEncours')),
                    'garanties': ", ".join([g['name'] for g in situation.get('situationGaranties', [])]),
                    'lead_id': opportunity.id
                }
                situation_record = request.env['pw.situation'].sudo().create(
                    situation_values)
                situation_ids.append(situation_record.id)

            for supplier in data.get('suppliers', []):
                supplier_values = {
                    'name': supplier.get('name'),
                    'country': request.env['res.country'].sudo().browse(int(supplier.get('country'))).id if supplier.get('country') else None,
                    'type_payment': [(6, 0, [int(payment_id) for payment_id in supplier.get('selectedPayments', [])])],
                    'lead_id': opportunity.id
                }
                supplier_record = request.env['pw.fournisseur'].sudo().create(
                    supplier_values)
                fournisseur_ids.append(supplier_record.id)

            # companies
            for company in data.get('companies', []):
                company_values = {
                    'name': company.get('name'),
                    'date_creation': company.get('fond_date'),
                    'chiffre_affaire': company.get('capital'),
                    'n1_num_affaire': company.get('n1'),
                    'n_num_affaire': company.get('n'),
                }
                company_record = request.env['pw.companies'].sudo().create(company_values)
                company_ids.append(company_record.id)

            
            for client in data.get('clients', []):
                client_values = {
                    'name': client.get('name'),
                    'country': request.env['res.country'].sudo().browse(int(client.get('country'))).id if client.get('country') else None,
                    'type_payment': [(6, 0, [int(payment_id) for payment_id in client.get('selectedPayments', [])])],
                    'lead_id': opportunity.id
                }
                client_record = request.env['pw.client'].sudo().create(client_values)
                client_ids.append(client_record.id)
            answers = {}
            details = {}
            infos = {}
            list_items_dict = {item[0]: item[1] for item in List_items}
            for key, value in data.get('kyc', []):
                if key.startswith('answer_'):
                    try:
                        record_id = int(key.split('_')[1])
                        answers[record_id] = value
                    except ValueError:
                        continue
                elif key.startswith('detail_'):
                    try:
                        record_id = int(key.split('_')[1])
                        details[record_id] = value
                    except ValueError:
                        continue
                elif key.startswith('info_'):
                    try:
                        record_id = int(key.split('_')[1])
                        infos[record_id] = value
                    except ValueError:
                        continue

            records_to_create = []

            for record_id in answers.keys():
                record = {
                    'answer': answers[record_id],
                    'detail': details.get(record_id, ''),
                    'info': list_items_dict.get(str(record_id), ''),
                    'lead_id': opportunity.id
                }
                records_to_create.append(record)
            if records_to_create:
                request.env['pw.kyc.details'].sudo().create(records_to_create)

            try:
                opportunity.sudo().write({
                    'apropos': [(6, 0, partner_ids)],
                    'gestion': [(6, 0, gestion_ids)],
                    'tailles': [(6, 0, taille_ids)],
                    'fournisseurs': [(6, 0, fournisseur_ids)],
                    'clients': [(6, 0, client_ids)],
                    'situations': [(6, 0, situation_ids)],
                    'companies': [(6, 0, company_ids)],

                })
            except Exception as e:
                logger.exception(f"Error updating opportunity with related records: {e}")
                return request.make_response(
                    json.dumps({'error': 'Failed to update opportunity with related records', 'details': str(e)}),
                    headers={'Content-Type': 'application/json'},
                    status=500
                )
            

            return request.make_response(
                json.dumps({'message': 'Data saved successfully',
                           'lead_id':''}),
                headers={'Content-Type': 'application/json'}
            )

        except Exception as e:
            logger.exception("Error saving opportunity data: %s" % str(e))
            return request.make_response(
                json.dumps(
                    {'error': 'Failed to save data', 'details': str(e)}),
                headers={'Content-Type': 'application/json'},
                status=500
            )

    @http.route(['/opportunity/login'], type='http', auth='public', website=True, csrf=True)
    def opportunity_login_form(self, **kwargs):
        return request.render('portal_salam.opportunity_login_form', {})

    @http.route(['/opportunity/get_oopportunites'], type='http', auth='public', csrf=True, methods=['GET'], cors='*')
    def get_opportunities(self, **kwargs):

        all_opportunities = request.env['pw.lead'].sudo().search([])

        return request.make_response(
            json.dumps({
                'opportunities': [
                    {
                        'id': str(opp.id),
			            'link_hash' : str(opp.link_hash),
                        'name': str(opp.name),
                        'display_name': str(opp.display_name),
                        'date_creation': str(opp.date_creation),
                        'name': str(opp.name),
                        'phone': str(opp.phone),
                        'email_from': str(opp.email_from),
                        'adress_siege': str(opp.adress_siege),
                        'nif': str(opp.nif),
                        'rc': str(opp.rc),
                        'num_compte': str(opp.num_compte),
                        'date_ouverture_compte': str(opp.date_ouverture_compte),
                        'date_debut': str(opp.date_debut),
                        'nom_arabe': str(opp.nom_arabe),
                        'date_debut_activite': str(opp.date_debut_activite),
                        'activity_code': str(opp.activity_code),
                        'activity_description': str(opp.activity_description),
                        'explanation': str(opp.explanation),
                        'description_company': str(opp.description_company),
                        'activite_sec': str(opp.activite_sec),
                        'forme_jur': int(opp.forme_jur.id),
                        'demande': int(opp.demande.id),
                        'apropos': [
                            {
                                'id': str(partner.id),
                                'nom_partenaire': str(partner.nom_partenaire),
                                'age': str(partner.age),
                                'pourcentage': float(partner.pourcentage)/100,
                                'statut_partenaire': str(partner.statut_partenaire),
                                'nationalite': int(partner.nationalite.id) if partner.nationalite else None,
                            } for partner in opp.apropos],

                        'gestion': [
                            {
                                'id': str(gestion.id), 
                                'name': str(gestion.name),
                                'job': str(gestion.job),
                                'niveau_etude': str(gestion.niveau_etude),
                                'age': int(gestion.age),
                                'experience': int(gestion.experience)
                            } for gestion in opp.gestion],

                        'tailles': [
                            {
                                'id': str(tailles.id), 
                                'type_demande': request.env['pw.product'].sudo().search([('name', '=', tailles.type_demande.name)], limit=1).id,
                                'montant': float(tailles.montant),
                                'raison': str(tailles.raison),
                                 'preg': float(tailles.preg)/100,
                                'duree': int(tailles.duree),
                                'garanties': [{'id': str(garantie.id)} for garantie in tailles.garanties],
                                
                            } for tailles in opp.tailles],

                        'fournisseurs': [
                            {
                                'id': str(fournisseurs.id), 
                                'name': str(fournisseurs.name),
                                'country': request.env['res.country'].sudo().browse(int(fournisseurs.country)).id if fournisseurs.country else None,
                                'type_payment': [{'id': int(payment_id.id)} for payment_id in fournisseurs.type_payment],

                            } for fournisseurs in opp.fournisseurs],

                        'clients': [ 
                            {
                                'id': str(clients.id), 
                                'name': str(clients.name),
                                'country': request.env['res.country'].sudo().browse(int(clients.country)).id if clients.country else None,
                                'type_payment': [{'id': int(payment_id.id)} for payment_id in clients.type_payment],

                            } for clients in opp.clients],

                        'situations': [
                            {
                                'id': str(situations.id),
                                'banque': int(situations.banque.id),
                                'type_fin': int(situations.type_fin.id),
                                'montant': float(situations.montant),
                                'encours': float(situations.encours),
                                'garanties': str(situations.garanties) if situations.garanties else '',
                            
                            } for situations in opp.situations],

                        'companies': [
                            {
                                'id': str(companies.id), 
                                'name': str(companies.name),
                                'date_creation': str(companies.date_creation) ,
                                'chiffre_affaire': float(companies.chiffre_affaire) ,
                                'n1_num_affaire': int(companies.n1_num_affaire) ,
                                'n_num_affaire': int(companies.n_num_affaire) ,
                                } for companies in opp.companies],
                        'documents': [
                            {
                                'id': str(doc.id), 
                                'list_document': str(doc.list_document),
                                'list_doc': str(doc.list_doc),
                                'document': base64.b64encode(doc.document).decode() if doc.document else '',


                            } for doc in opp.documents],
                    
                    } for opp in all_opportunities]
            }),
            headers={'Content-Type': 'application/json'}
        )

    @http.route(['/opportunity/confirm_get_opportunities'], type='http', auth='public', methods=['POST'], website=True, csrf=False, cors='*')
    def confirm_get_opportunities(self, **kwargs):
        try:
            data = json.loads(request.httprequest.data)
            ids = data.get('ids', [])
            for id in ids:
                opportunity = request.env['pw.lead'].sudo().browse(int(id))
                if opportunity:
                    opportunity.sudo().unlink()
                    logger.info(f"Deleting opportunity with ID: {opportunity.id}")
            logger.info("Opportunities confirmed and deleted successfully.")
            return request.make_response(
                        json.dumps({
                            "confirm":"Confirmed",
                        }),                
                headers={'Content-Type': 'application/json'}
            )
        except Exception as e:
            logger.exception("Error fetching opportunities: %s" % str(e))
            return request.make_response(
                json.dumps({'error': 'Failed', 'details': str(e)}),
                headers={'Content-Type': 'application/json'},
                status=500
            )
        
# class WebsiteRedirect(http.Controller):

#     @http.route(['/web/login','/web/database/manager',], type='http', auth='public', website=True)
#     def homepage_redirect(self):
#         return request.redirect('/')

import re



class LinksController(http.Controller):

    @http.route(['/link/create'], type='http', auth='public', methods=['POST'], website=True, csrf=False, cors='*')
    def link_create(self, **post):
        try:
            data = json.loads(request.httprequest.data)
            email = data.get('email')
            link_hash = data.get('link_hash')
            if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
                return request.make_response(
                    json.dumps(
                        {'error': 'Invalid email', 'details': f"{email} is not valid email!"}),
                    headers={'Content-Type': 'application/json'},
                    status=400
                )

            link = request.env['ponctual.links'].sudo().create({
                'email':email,
                'link_uid':link_hash
            })

        
            return request.make_response(
                json.dumps(
                    {'status': 200, 'details':'Link created succefully' }),
                headers={'Content-Type': 'application/json'},
                status=200
            )

        except Exception as e:
            print("Error saving link data: %s" % str(e))
            return request.make_response(
                json.dumps(
                    {'error': 'Failed to save data', 'details': str(e)}),
                headers={'Content-Type': 'application/json'},
                status=500
            )

        

    @http.route(
        '/upload_document',
        auth='none',
        type='http',
        methods=['POST', 'OPTIONS'],
        csrf=False,
        cors='*')
    def upload_document(self, **post):
        """
        Receives a file and creates fw.document
        """

        uploaded_file = post.get('file')

        if not uploaded_file:
            return request.make_json_response(
                {'error': 'No file provided'},
                status=400
            )

        # Read file
        file_content = uploaded_file.read()
        filename = uploaded_file.filename

        # Create record
        document = request.env['fw.document'].sudo().create({
            'document': base64.b64encode(file_content),
            'filename': filename,
        })

        return request.make_json_response({
            'id': document.id
        })

    @http.route(
        '/delete_document',
        auth='none',
        type='http',
        methods=['POST', 'OPTIONS'],
        csrf=False,
        cors='*'
    )
    def delete_document(self, **post):
        """
        Deletes an uploaded fw.document by ID
        """

        document_id = post.get('id')

        if not document_id:
            return request.make_json_response(
                {'error': 'No document ID provided'},
                status=400
            )

        try:
            document_id = int(document_id)
        except (ValueError, TypeError):
            return request.make_json_response(
                {'error': 'Invalid document ID'},
                status=400
            )

        document = request.env['fw.document'].sudo().browse(document_id)

        if not document.exists():
            return request.make_json_response(
                {'error': 'Document not found'},
                status=404
            )

        document.unlink()

        return request.make_json_response({
            'success': True,
            'id': document_id
        })

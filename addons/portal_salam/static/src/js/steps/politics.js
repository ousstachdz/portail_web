class Politics extends Component {
  static props = ['state']

  setup() {
    this.state = useState({
      isValiddatePoliticsCoockis: false,
      isValiddatePoliticsDataUsege: false,
      showPopupCoockis: false,
      showPopupDataUsege: false,
    })
  }

  accept() {
    const { state } = this.props
    if (this.state.isValiddatePoliticsCoockis && this.state.isValiddatePoliticsDataUsege) {
      if (state.step < 1) {
        state.step += 1
      }
    }
  }

  openPopupDataUsege() {
    this.state.showPopupDataUsege = true
  }
  openPopupCoockis() {
    this.state.showPopupCoockis = true
  }

  closePopup() {
    this.state.showPopupCoockis = false
    this.state.showPopupDataUsege = false
  }

  static template = xml/* xml */ `
    <div class="p-4 text-right" dir="rtl">
      <h2 class="text-xl font-bold mb-3">سياسة الاستخدام</h2>
      
      <div class="space-y-3 mb-4">
        <label class="flex items-center space-x-2 space-x-reverse py-2">
          <input type="checkbox"
                 t-model="state.isValiddatePoliticsCoockis"
                 class="w-4 h-4 ms-2"/>
          <span>أوافق على استخدام ملفات تعريف الارتباط (cookies)
           <a href="#" t-on-click.prevent="openPopupCoockis" class="text-blue-600 hover:underline">
           اقرأ المزيد
          </a></span>
        </label>

        <br/>

        <label class="flex items-center space-x-2 space-x-reverse py-2">
          <input type="checkbox"
                 t-model="state.isValiddatePoliticsDataUsege"
                 class="w-4 h-4 ms-2"/>
          <span>أوافق على سياسة حمايـة المعطيـات الشخصيـة<a href="#" t-on-click.prevent="openPopupDataUsege" class="text-blue-600 hover:underline">
            اقرأ المزيد
          </a></span>
        </label>
      </div>

      <t t-if="state.isValiddatePoliticsCoockis &amp;&amp; state.isValiddatePoliticsDataUsege">
        <button type="button" class="btn btn-primary" t-on-click="accept">
          ابدأ
        </button>
      </t>

      <!-- Coockis -->
      <t t-if="state.showPopupCoockis">
        <div class="pop-up-policy fflex items-center justify-center bg-black bg-opacity-50 z-50">
          <div class="bg-white rounded-lg shadow-lg p-6 max-w-lg w-full text-right  p-4" dir="rtl">
          <div class="cookie-policy p-4">
                <div dir="ltr">
                <h3>Politique des cookies</h3>

                <h4>Qu’est-ce qu’un cookie ?</h4>
                <p>Les cookies sont de petits fichiers texte téléchargés sur votre ordinateur ou d'autres appareils connectés à Internet, tels que les smartphones et les tablettes, lorsque vous visitez un site web. Leur fonction principale est de reconnaître votre appareil lors de vos futures visites.</p>

                <p>Ces fichiers textes ont diverses utilités, notamment la sauvegarde de vos préférences, la mesure de votre activité en ligne, et l'amélioration de votre expérience en tant qu'utilisateur. Il est important de noter que la plupart des cookies ne renferment pas d'informations permettant de vous identifier personnellement, mais plutôt des données plus générales, comme votre localisation approximative ou la façon dont vous accédez et utilisez nos sites web.</p>

                <h4>Quels types de cookies sont utilisés par Al Salam ALGERIA?</h4>
                <p>En règle générale, nos cookies remplissent trois fonctions différentes :</p>
                <ul>
                    <li>Assurer le bon fonctionnement de nos sites web : Certains cookies sont essentiels pour garantir le fonctionnement adéquat de nos sites. Par exemple, nous utilisons des cookies pour vérifier que les pages affichées correspondent à votre emplacement, ou pour détecter les liens rompus et résoudre d'autres problèmes techniques sur le site web.</li>
                    <li>Analyser le comportement des visiteurs : Nos cookies sont utilisés pour analyser la manière dont nos visiteurs interagissent avec nos sites web et surveiller leurs performances. Cela nous permet de maintenir une expérience de qualité en veillant à ce que notre contenu et notre mise en page restent pertinents pour vous. Par exemple, ces cookies nous aident à identifier les pages et les liens les plus populaires, ainsi que ceux qui ne répondent pas aux attentes de nos visiteurs en termes d'informations.</li>
                    <li>Optimisation et personnalisation : Les cookies sont également utilisés pour améliorer les pages web que vous consultez et personnaliser le contenu que nous vous proposons sur toutes nos plateformes numériques, en fonction de notre compréhension de vos préférences.</li>
                </ul>


<table class="table table-bordered">
  <tr>
    <th colspan="5">Cookies exploités</th>
  </tr>
  <tr>
    <th>Intitulé du cookie</th>
    <th>Utilité</th>
    <th>Domaine</th>
    <th>Durée de conservation</th>
    <th>Responsable de traitement</th>
  </tr>

  <tr>
    <td>1</td>
    <td>Cookie interne utilisé pour le bon fonctionnement du site QuickCredit.</td>
    <td>quickcredit.alsalamalgeria.com</td>
    <td>13 mois</td>
    <td>Al Salam Bank ALGERIA</td>
  </tr>

  <tr>
    <td>frontend_lang</td>
    <td>Stocke la langue d’affichage de l’utilisateur (ex. en_US).</td>
    <td>quickcredit.alsalamalgeria.com</td>
    <td>13 mois</td>
    <td>Al Salam Bank ALGERIA</td>
  </tr>

  <tr>
    <td>session_id</td>
    <td>Identifiant de session pour l’utilisateur connecté afin de maintenir la session active.</td>
    <td>quickcredit.alsalamalgeria.com</td>
    <td>5 jours</td>
    <td>Al Salam Bank ALGERIA</td>
  </tr>

  <tr>
    <td>tz</td>
    <td>Stocke le fuseau horaire de l’utilisateur (ex. Africa/Lagos).</td>
    <td>quickcredit.alsalamalgeria.com</td>
    <td>Session</td>
    <td>Al Salam Bank ALGERIA</td>
  </tr>
</table>
                <h4>Quels types d’information peuvent être stockés dans un cookie ?</h4>
                <p>Les informations stockées par les cookies déposés sur votre appareil peuvent avoir trait aux éléments suivants, dans la limite de leur durée de conservation :</p>
                <ul>
                    <li>Les pages web que vous avez visitées en utilisant cet appareil ;</li>
                    <li>Les publicités sur lesquelles vous avez cliqué ;</li>
                    <li>Le type de navigateur que vous utilisez ;</li>
                    <li>Votre adresse IP ;</li>
                    <li>Et toute autre information que vous avez fournie sur notre Site/Application.</li>
                </ul>
                <p>Les cookies peuvent contenir des données à caractère personnel couvertes par notre (lien vers notice)</p>

                <h4>Comment gérer les cookies ?</h4>
                <p>À tout moment, vous avez la possibilité d'autoriser, de bloquer ou de supprimer les cookies, ainsi que d'effacer vos données de navigation depuis votre navigateur. Pour ce faire, veuillez consulter les options et les instructions fournies par le navigateur que vous utilisez.</p>

                <p>Il est également envisageable de restreindre l'installation de cookies par des sites web tiers sur votre ordinateur, afin d'éviter la collecte de données et d'enregistrements de votre activité de navigation.</p>

                <p>. Si vous optez pour le refus des cookies, certaines fonctionnalités et services de nos sites web peuvent ne pas fonctionner correctement.</p>

                <p>Vous pouvez soit :</p>
                <ul>
                    <li>Ajuster les réglages de votre navigateur afin qu'il vous notifie lors de la réception d'un cookie, vous donnant ainsi la possibilité de décider de l'accepter ou de le refuser ; ou</li>
                    <li>Configurer votre navigateur de manière à refuser automatiquement tous les cookies.</li>
                </ul>

                <p>Pour obtenir davantage de détails concernant notre traitement des informations personnelles, veuillez-vous référer à la notice relative à la protection des données à caractère personnel à travers le lien &lt;Boutton&gt;.</p>

                <h4>Le contenue du cadran qui s’affiche lors du l’ouverture du site</h4>
                <p>Al Salam Bank Algeria utilise des « cookies » pour assurer le bon fonctionnement et la sécurité du site, améliorer votre expérience, personnaliser les publicités et les contenus en fonction de votre navigation et de votre profil, réaliser des statistiques et mesures d'audiences afin d’évaluer la performance de ces publicités et contenus.</p>

                <p>Certains de ces cookies sont soumis à votre consentement. Vous pouvez exprimer votre choix de manière globale, ou paramétrer vos préférences par finalité de cookies. Vous pouvez modifier ces choix à tout moment.</p>

                <p>Accédez à notre charte cookies en cliquant « Gestion des cookies »</p>
                </div>

                <hr/>

                <h3>يستخدم مصرف السلام الجزائر "ملفات تعريف الارتباط"</h3>
                <p>يستخدم مصرف السلام الجزائر "ملفات تعريف الارتباط" لضمان حسن سير الموقع وأمنه، وتحسين تجربتك، وتخصيص الإعلانات والمحتوى بناءً على تصفحك وملفك الشخصي، وإجراء الإحصائيات وقياسات الجمهور من أجل "تقييم أداء هذه الخدمات". الإعلانات والمحتوى.</p>

                <p>تخضع بعض ملفات تعريف الارتباط هذه لموافقتك. كما يمكنك التعبير عن اختيارك بكل حرية، أو تكوين تفضيلاتك حسب غرض ملفات تعريف الارتباط. يمكنك تغيير هذه الاختيارات في أي وقت.</p>

                <p>يمكنك الوصول إلى ميثاق ملفات تعريف الارتباط الخاص بنا بالنقر على "إدارة ملفات تعريف الارتباط"</p>

                <hr/>

                <h3>ملفات تعريف الارتباط</h3>
                <p>ملفات تعريف الارتباط هي ملفات نصية صغيرة يتم تنزيلها على جهاز الكمبيوتر الخاص بك أو أجهزة أخرى متصلة بالإنترنت، مثل الهواتف الذكية والأجهزة اللوحية، عند زيارتك لموقع ويب. وظيفتها الرئيسية هي التعرف على جهازك خلال زياراتك المستقبلية.</p>

                <p>تحمل هذه الملفات النصية مجموعة متنوعة من الاستخدامات، بما في ذلك الاحتفاظ بتفضيلاتك، وقياس نشاطك على الإنترنت، وتحسين تجربتك كمستخدم. من المهم ملاحظة أن معظم ملفات تعريف الارتباط لا تحتوي على معلومات تمكن من تحديد هويتك شخصيًا، بل تحمل بدلاً من ذلك معلومات عامة أكثر، مثل موقعك التقريبي أو كيفية الوصول إلى مواقعنا واستخدامها.</p>

                <h4>أنواع ملفات تعريف الارتباط التي يستخدمها مصرف السلام الجزائر</h4>
                <p>بشكل عام، تقوم ملفات تعريف الارتباط الخاصة بنا بأداء ثلاث وظائف مختلفة:</p>
                <ul>
                    <li>ضمان عمل مواقعنا الإلكترونية بشكل صحيح: تعتبر بعض ملفات تعريف الارتباط ضرورية لضمان عمل مواقعنا بشكل صحيح. على سبيل المثال، نستخدم ملفات تعريف الارتباط للتحقق من أن الصفحات المعروضة تتوافق مع موقعك، أو لاكتشاف الروابط المكسورة وحل مشاكل تقنية أخرى على الموقع الإلكتروني.</li>
                    <li>تحليل سلوك الزوار: تستخدم ملفات تعريف الارتباط لدينا لتحليل كيفية تفاعل زوارنا مع مواقعنا الإلكترونية ومراقبة أدائها. وهذا يساعدنا على الحفاظ على تجربة ذات جودة عالية عن طريق التأكد من أن محتوانا وتصميمنا ما زالا ذات صلة بك. على سبيل المثال، تساعدنا هذه الملفات في تحديد الصفحات والروابط الأكثر شعبية، بالإضافة إلى تلك التي لا تلبي توقعات زوارنا من حيث المعلومات.</li>
                    <li>تحسين وتخصيص: تستخدم ملفات تعريف الارتباط أيضًا لتحسين الصفحات التي تتصفحها وتخصيص المحتوى الذي نقدمه على جميع منصاتنا الرقمية، استنادًا إلى فهمنا لتفضيلاتك.</li>
                </ul>

<table class="table table-bordered"  dir="rtl">
  <tr>
    <th colspan="5">ملفات تعريف الارتباط المستعملة</th>
  </tr>
  <tr>
    <th>اسم الملف</th>
    <th>الاستعمال</th>
    <th>المجال</th>
    <th>مدة الاحتفاظ</th>
    <th>مسؤول المعالجة</th>
  </tr>

  <tr>
    <td>1</td>
    <td>ملف داخلي يُستخدم لضمان الأداء السليم لموقع QuickCredit.</td>
    <td>quickcredit.alsalamalgeria.com</td>
    <td>13 شهرا</td>
    <td>مصرف السلام الجزائر</td>
  </tr>

  <tr>
    <td>frontend_lang</td>
    <td>يُستخدم لتخزين لغة واجهة المستخدم (مثل en_US).</td>
    <td>quickcredit.alsalamalgeria.com</td>
    <td>13 شهرا</td>
    <td>مصرف السلام الجزائر</td>
  </tr>

  <tr>
    <td>session_id</td>
    <td>يُستخدم لتحديد جلسة المستخدم والحفاظ عليها أثناء التصفح.</td>
    <td>quickcredit.alsalamalgeria.com</td>
    <td>خمسة أيام</td>
    <td>مصرف السلام الجزائر</td>
  </tr>

  <tr>
    <td>tz</td>
    <td>يُستخدم لتخزين المنطقة الزمنية للمستخدم (مثل Africa/Lagos).</td>
    <td>quickcredit.alsalamalgeria.com</td>
    <td>طوال مدة الجلسة</td>
    <td>مصرف السلام الجزائر</td>
  </tr>
</table>


                <h4>ما هي أنواع المعلومات التي يمكن تخزينها في ملف تعريف الارتباط؟</h4>
                <p>قد تتعلق المعلومات المخزنة بواسطة ملفات تعريف الارتباط الموضوعة على جهازك بالعناصر التالية، في حدود فترة الاحتفاظ بها:</p>
                <ul>
                    <li>صفحات الويب التي قمت بزيارتها باستخدام هذا الجهاز.</li>
                    <li>الإعلانات التي قمت بتصفحها عليها.</li>
                    <li>نوع المتصفح الذي تستخدمه.</li>
                    <li>عنوان IP الخاص بك.</li>
                    <li>وأي معلومات أخرى تقدمها على موقعنا/تطبيقنا.</li>
                </ul>
                <p>قد تحتوي ملفات تعريف الارتباط على بيانات شخصية يغطيها (رابط للإشعار)</p>

                <h4>كيفية إدارة ملفات تعريف الارتباط</h4>
                <p>يمكنك في أي وقت السماح، أو حظر، أو حذف ملفات تعريف الارتباط، وكذلك مسح بيانات تصفحك من متصفح الإنترنت الخاص بك. للقيام بذلك، يُرجى الاطلاع على الخيارات والتعليمات المقدمة من قبل المتصفح الذي تستخدمه.</p>

                <p>كما يمكنك أيضاً تقييد تثبيت ملفات تعريف الارتباط من قبل مواقع الويب من طرف ثالث على جهاز الكمبيوتر الخاص بك، لتجنب جمع البيانات وتسجيل نشاط تصفحك.</p>

                <p>إذا قررت رفض ملفات تعريف الارتباط، قد تتعطل بعض الوظائف والخدمات على مواقع الويب الخاصة بنا.</p>

                <p>حيث يمكنك إما：</p>
                <ul>
                    <li>ضبط إعدادات متصفحك ليعلمك عند تلقي ملف تعريف الارتباط، مما يتيح لك اختيار قبوله أو رفضه؛</li>
                    <li>ضبط متصفحك لرفض ملفات تعريف الارتباط تلقائيًا.</li>
                </ul>

                <p>للحصول على مزيد من التفاصيل حول معالجتنا للمعلومات الشخصية، يُرجى الرجوع إلى الإشعار المتعلق بحماية المعطيات الشخصية عبر الرابط التالي: [رابط الإشعار]</p>
                </div>

            <div class="text-left mt-4">
              <button type="button" class="btn btn-secondary" t-on-click="closePopup">
                إغلاق
              </button>
            </div>
          </div>
        </div>
      </t>

            <!-- DataUsege -->
      <t t-if="state.showPopupDataUsege">
        <div class="pop-up-policy flex items-center justify-center bg-black bg-opacity-50 z-50">
          <div class="bg-white rounded-lg shadow-lg p-6 max-w-lg w-full text-right  p-4" dir="rtl">
          
          <div class="policy-container  p-4">
                <div dir="ltr">
                    <h3>À propos de cette Politique</h3>
                    <p>Al Salam Bank Algeria, en sa qualité d’établissement bancaire, construit avec ses clients des relations fortes et durables, fondées sur une confiance réciproque.</p>
                    <p>Afin de préserver cette confiance, nous faisons de la sécurité et de la protection de vos données personnelles une priorité inconditionnelle.</p>
                    <p>Dans cette perspective, Al Salam Bank Algeria respecte la loi 18-07 relative à la protection des personnes physiques dans le traitement des données à caractère personnel</p>
                    <p>L’objectif de cette Politique est de vous informer sur notre approche en ce qui concerne la collecte, l'utilisation et la préservation de vos données à caractère personnel ainsi que sur vos droits et les voies de contacts ou de recours mis à votre disposition. Notre engagement absolu est d'assurer la confidentialité de votre vie privée et de garantir votre sécurité lorsque vous interagissez avec nos services. Nous vous invitons vivement à lire et à examiner attentivement ce document pour avoir une meilleure compréhension du traitement de vos données.</p>
                    <p>Cette Politique s’adresse et s’applique aux clients et prospects particuliers de Al Salam Bank Algeria, employés, les tiers et les candidats, ainsi qu’aux personnes en lien avec nos clients (Membre de la famille du client, héritier/ayant-droit du client, Associé ou Actionnaire de société cliente; Bénéficiaire effectif, Créancier, Propriétaire ou bailleur, Donneur d’ordre ou bénéficiaire d’un paiement désigné, représentant légal Co-emprunteur, garant ou caution un mandataire ou un signataire autorisé, un contact désigné et Les prestataires de service externes et sous-traitants)</p>

                    <h4>Type de Données collectées</h4>
                    <p>Nous pouvons être amenés à collecter les types de données suivantes:</p>
                    <ul>
                        <li>Vos Données d’état civil et Informations d’identification (nom, prénom(s), genre, date de naissance, signatures…) ;</li>
                        <li>Vos coordonnées de contact (adresse postale, adresse e-mail, numéro de téléphone, etc);</li>
                        <li>Vos Données relatives à la situation économique, financière et fiscale;</li>
                        <li>Vos coordonnées bancaires ;</li>
                        <li>Vos données liées aux produits et services souscrits (coordonnées bancaires, Produits et services détenus et utilisés (crédit, assurance, épargne et investissements, leasing…), numéro de carte, virements, antécédents de crédit, incidents de paiement) ………..</li>
                        <li>Données issues des correspondances et communications entre vous et la Banque (appels téléphoniques, des entretiens, messagerie électronique, messageries instantanées, communications sur les réseaux sociaux ou tout autre type de communication) …………</li>
                        <li>Informations sur votre carrière professionnelle et performance (postes occupés, historique de l’emploi, rapports de performance, etc.) ;</li>
                        <li>Des données relatives à une autorisation de travail (pour les salariés étrangers) ;</li>
                        <li>Des données relatives à vos formations et expériences professionnelles et à vos compétences liées au poste à pourvoir en cas de candidature (compétences linguistiques, techniques, etc.) ;</li>
                        <li>Des Coordonnées des personnes à prévenir en cas d’urgence ;</li>
                        <li>Des Données nécessaires à la lutte contre la fraude, le blanchiment d'argent et le financement du terrorisme ;</li>
                        <li>Des Données d'utilisation (des informations sur la manière dont vous utilisez nos services, y compris l'adresse IP, le navigateur et les informations sur l'appareil) ;</li>
                        <li>Des Cookies (pour améliorer votre expérience de navigation et recueillir des données analytiques;</li>
                        <li>Contenu généré par l'utilisateur : Tout contenu que vous soumettez sur notre plateforme.</li>
                        <li>Des données concernant l’objet de votre passage dans les locaux d’Al Salam Bank Algeria;</li>
                        <li>Les Données d’enregistrements de la vidéo-surveillance lors de vos passages au niveau de nos locaux ;</li>
                        <li>Enregistrement de votre itinéraire à l'intérieur des locaux d’Al Salam Bank Algeria;</li>
                        <li>Lorsque cela est nécessaire, et uniquement après l'obtention de votre consentement explicite, Al Salam Bank Algeria peut être amenée à collecter des données sensibles, notamment les données de santé.</li>
                        <li>Ces données personnelles sont collectées soit directement auprès de vous ou indirectement à travers d’autres sources publiques.</li>
                    </ul>

                    <h4>Utilisation de vos données</h4>
                    <p>Les finalités de la collecte de vos données sont :</p>
                    <p>Dans le cadre du respect d'obligations légales et règlementaires auxquelles Al Salam Bank Algeria est soumise :</p>
                    <ul>
                        <li>L'accomplissement des contrôles fiscaux et les obligations de notification</li>
                        <li>La réponse à des demandes potentielles émanant d'une autorité publique ou judiciaire dûment habilitée ;</li>
                        <li>La lutte contre le blanchiment d’argent et le financement du terrorisme</li>
                        <li>La gestion du risque opérationnel (par exemple la sécurité des réseaux informatiques et des transactions) ……</li>
                    </ul>
                    <p>Dans le cadre de votre relation contractuelle comme :</p>
                    <ul>
                        <li>La passation, la gestion et l'exécution de vos contrats avec Al Salam Bank Algeria;</li>
                        <li>La gestion commerciale des clients et à la prospection commerciale à travers notamment des actions de fidélisation, du suivi et d'amélioration de la qualité de la relation client (enquêtes de satisfaction, e-mails, SMS, communication sur les réseaux sociaux, toute autre communication, …) ;</li>
                        <li>La gestion de la relation avec la Banque :</li>
                        <li>L’ouverture, clôture et la gestion des comptes et/ou des services et produits souscrits ;</li>
                        <li>Le traitement des réclamations ;</li>
                        <li>La gestion et la maitrise des risques ;</li>
                        <li>Le recouvrement de créance ;</li>
                        <li>La gestion des incidents de paiement.</li>
                        <li>Fourniture de services ;</li>
                        <li>La gestion de notre système d'information ;</li>
                        <li>La personnalisation de nos offres ;</li>
                        <li>Gestion administrative du personnel de la banque et suivi de la carrière professionnelle ;</li>
                        <li>La génération des statistiques et l’anonymisation des données dans le but d'améliorer le processus de recrutement ;</li>
                        <li>Mise à disposition d’outils informatiques, de téléphonie, et gestion des accès à nos services et systèmes d’information ;</li>
                        <li>Aménagement d’un environnement de travail approprié notamment pour les personnes à mobilité réduite ;</li>
                        <li>Garantir la sécurité des personnes et des équipements par l’identification des intervenants lors de l’accès aux ressources et aux installations d’Al Salam Bank Algeria;</li>
                        <li>Protéger les droits d’Al Salam Bank Algeria (par exemple pour se défendre dans le cas d’un litige) ;</li>
                        <li>Communication (répondre à vos demandes, envoyer des mises à jour et fournir un support) ;</li>
                        <li>Analyser le comportement des utilisateurs et améliorer nos services ;</li>
                        <li>A des fins Marketing et l’amélioration de la qualité des services (envoi des documents promotionnels) ;</li>
                        <li>La gestion et l’exécution des processus internes, tels que, les rendez-vous</li>
                    </ul>

                    <h4>Partage de Données</h4>
                    <p>Dans le cadre de nos missions, Nous pouvons partager vos données avec :</p>
                    <ul>
                        <li>Des prestataires de services tiers de confiance, pour des fonctions essentielles ;</li>
                        <li>Lorsque la loi l'exige ou pour protéger nos droits.</li>
                        <li>Des autorités judiciaires, financières, fiscales, administratives, des autorités ou des établissements ou institutions publics à qui nous sommes tenus de divulguer des données personnelles.</li>
                        <li>Certaines professions réglementées telles que des avocats, des notaires, des experts ou des commissaires aux comptes lorsque des circonstances l’imposent (transaction, litige, audit, etc.</li>
                        <li>Les organes et les entités du groupe auxquelles appartient Al Salam Bank Algeria.</li>
                    </ul>

                    <h4>Sécurité des Données</h4>
                    <p>Afin de protéger vos données collectées, des mesures de sécurité physiques, techniques et organisationnelles appropriées sont misent en place pour prévenir toute perte, utilisation abusive, accès non autorisé, divulgation ou altération de vos données.</p>

                    <h4>Conservation des Données</h4>
                    <p>Nous conservons vos données personnelles pendant toute la durée de la relation tant que vous utiliserez nos produits et services. Elles pourront être conservées au-delà de la relation, notamment pour nous conformer à la réglementation applicable, pour faire valoir nos droits ou défendre nos intérêts, afin d’accomplir les finalités pour lesquelles vos données personnelles ont été recueillies.</p>

                    <h4>Vos Droits</h4>
                    <p>Conformément à la Loi 18-07 (Article 32 à 37), vous disposez des droits suivants :</p>
                    <ul>
                        <li>Droit à l’information (dans les conditions de l’article 32 et 33 de la loi 18-07) ;</li>
                        <li>Droit d’accès (dans les conditions de l’article 34 de la loi 18-07);</li>
                        <li>Droit de rectification (dans les conditions de l’article 35 de la loi 18-07);</li>
                        <li>Droit d’opposition (dans les conditions de l’article 36 de la loi 18-07);</li>
                        <li>Interdiction de la prospection directe (dans les conditions de l’article 37 de la loi 18-07).</li>
                    </ul>
                    <p>Vous pouvez exercer l’un de vos droits énumérés ci-dessus, en écrivant au responsable de traitement dont les coordonnées sont énumérées ci-dessous.</p>
                    <p>Toute demande doit être accompagnée de la photocopie d’un justificatif d’identité, faute de quoi elle ne pourra être traitée.</p>

                    <h4>Nous contacter</h4>
                    <p>Pour plus d’information, clarification relative à cette politique, ou utilisation de l’un de vos droits, Veuillez prendre contact avec le Représentant du Responsable de Traitement à l'adresse e-mail suivante :</p>
                    <p>AL SALAM BANK ALGERIA ;</p>
                    <p>233, Rue Ahmed OUAKED, Dely Ibrahim ALGER ALGERIE</p>
                    <p>Privacy@alsalamalgeria.com</p>
                    <p>En utilisant nos services, vous consentez aux termes de cette Politique de Protection des Données à Caractère Personnel.</p>
                </div>
                    <h3>سياسة حماية المعطيات الشخصية</h3>
                    <p>يقوم مصرف السلام الجزائر، بصفته مؤسسة مصرفية، ببناء علاقات قوية ودائمة مع عملائه، على أساس الثقة المتبادلة.</p>
                    <p>وللحفاظ على هذه الثقة، فإننا نجعل من أمن وحماية بياناتك الشخصية أولوياتنا القصوى.</p>
                    <p>ومن هذا المنطلق، يمتثل مصرف السلام الجزائر للقانون 18-07 المتعلق بحماية الأشخاص الطبيعيين في مجال معالجة المعطيات ذات الطابع الشخصي.</p>
                    <p>الهدف من هذه السياسة هو إعلامك بالنهج الذي نتبعه فيما يتعلق بجمع بياناتك الشخصية واستخدامها والحفاظ عليها بالإضافة إلى حقوقك ووسائل الاتصال المتاحة لك. التزامنا المطلق هو ضمان خصوصيتك وتأمين بياناتك الشخصية عند التفاعل مع خدماتنا. نحن ندعوك لقراءة ومراجعة هذه الوثيقة بعناية للحصول على فهم أفضل لعملية معالجة بياناتك.</p>
                    <p>هذه السياسة موجهة ومطبقة على العملاء الأفراد والعملاء الأفراد المحتملين لمصرف السلام الجزائر والموظفين والأطراف الثالثة والمرشحين، وكذلك الأشخاص ذوي الصلة بعملائنا (عائلة العميل، وريث/مستفيد من العميل، شريك أو مساهم في شركة لها علاقة عمل مع المصرف، المالك المستفيد، الدائن، المالك أو المؤجر، صاحب الشأن أو المستفيد من دفعة معينة، الممثل القانوني، المقترض المشارك، الضامن، الوكيل أو المفوض بالتوقيع، جهة الاتصال المعينة ومقدمي الخدمات الخارجية والمقاولين من الباطن)</p>

                    <h4>المعطيات المجمعة</h4>
                    <p>قد نقوم بجمع الفئات التالية من البيانات:</p>
                    <ul>
                        <li>بيانات الحالة المدنية الخاصة بك ومعلومات عن الهوية (اللقب، الاسم، الجنس، تاريخ الميلاد، التوقيعات، وما إلى ذلك)؛</li>
                        <li>تفاصيل الاتصال الخاصة بك (العنوان البريدي، عنوان البريد الإلكتروني، رقم الهاتف، وما إلى ذلك)؛</li>
                        <li>بياناتك المتعلقة بالوضع الاقتصادي والمالي والضريبي.</li>
                        <li>تفاصيل البنك الخاص بك ;</li>
                        <li>بياناتك المتعلقة بالمنتجات والخدمات المشتركة فيها (التفاصيل المصرفية، المنتجات والخدمات المحتفظ بها والمستخدمة (الائتمان، التأمين، الادخار والاستثمار، التأجير، إلخ)، رقم البطاقة، التحويلات، التاريخ الائتماني، حوادث الدفع) ………</li>
                        <li>البيانات من المراسلات والاتصالات بينك وبين المصرف (المكالمات الهاتفية، المقابلات، الرسائل الإلكترونية، الرسائل الفورية، الاتصالات على شبكات التواصل الاجتماعي أو أي نوع آخر من الاتصالات) …………</li>
                        <li>معلومات عن حياتك المهنية وأدائك (المناصب التي شغلتها، وتاريخ التوظيف، وتقارير الأداء، وما إلى ذلك).</li>
                        <li>البيانات المتعلقة بترخيص العمل (للموظفين الأجانب).</li>
                        <li>البيانات المتعلقة بتدريبك وخبرتك المهنية ومهاراتك المتعلقة بالوظيفة التي سيتم شغلها في حالة تقديم الطلب (المهارات اللغوية والتقنية وما إلى ذلك).</li>
                        <li>تفاصيل الاتصال بالأشخاص الذين سيتم إعلامهم في حالة الطوارئ.</li>
                        <li>البيانات اللازمة لمكافحة الاحتيال وغسل الأموال وتمويل الإرهاب.</li>
                        <li>بيانات الاستخدام (معلومات حول كيفية استخدامك لخدماتنا، بما في ذلك عنوان IP والمتصفح ومعلومات الجهاز)؛</li>
                        <li>المحتوى الذي ينشئه المستخدم: أي محتوى ترسله إلى منصتنا.</li>
                        <li>البيانات المتعلقة بغرض زيارتك لمقر مصرف السلام الجزائر.</li>
                        <li>مراقبة الفيديو وتسجيل البيانات أثناء زياراتك لمقراتنا.</li>
                        <li>تسجيل خط سير زياراتكم داخل مقر مصرف السلام الجزائر.</li>
                        <li>عند الضرورة، وفقط بعد الحصول على موافقتك الصريحة، يجوز لمصرف السلام الجزائر جمع بيانات حساسة، بما في ذلك البيانات الصحية.</li>
                        <li>يتم جمع هذه البيانات الشخصية إما مباشرة منك أو بشكل غير مباشر من خلال مصادر عامة أخرى ذات صلة</li>
                    </ul>

                    <h4>معالجة المعطيات</h4>
                    <p>الغرض من جمع بياناتك هي:</p>
                    <ol>
                        <li>1. في إطار احترام الالتزامات القانونية والتنظيمية التي يخضع لها مصرف السلام الجزائر:</li>
                    </ol>
                    <ul>
                        <li>أ. الانتهاء من عمليات التدقيق الضريبي والتزامات الإخطار</li>
                        <li>ب. الاستجابة للطلبات المحتملة من سلطة عامة أو قضائية مرخصة؛</li>
                        <li>ج. مكافحة غسل الأموال وتمويل الإرهاب</li>
                        <li>د. إدارة المخاطر التشغيلية (مثل أمن شبكات الكمبيوتر والمعاملات)……</li>
                    </ul>
                    <p>2. كجزء من علاقتك التعاقدية مثل:</p>
                    <ul>
                        <li>أ. إبرام وإدارة وتنفيذ عقودكم مع مصرف السلام الجزائر؛</li>
                        <li>ب. الإدارة التجارية للعملاء والتنقيب التجاري، لا سيما من خلال إجراءات الولاء، ومراقبة وتحسين جودة علاقات العملاء (استطلاعات الرضا، ورسائل البريد الإلكتروني، والرسائل النصية القصيرة، والتواصل على الشبكات الاجتماعية، وأي اتصالات أخرى، ...)؛</li>
                        <li>3. إدارة العلاقة مع المصرف:</li>
                        <li>أ. فتح، غلق، تسيير الحسابات و/أو الخدمات والمنتجات المشتركة؛</li>
                        <li>ب. معالجة الشكاوى؛</li>
                        <li>ج. إدارة المخاطر والسيطرة عليها؛</li>
                        <li>د. تسديد التمويلان المختلفة؛</li>
                        <li>ه. إدارة حوادث الدفع.</li>
                        <li>4. تقديم الخدمات.</li>
                        <li>5. إدارة نظامنا المعلوماتي.</li>
                        <li>6. تخصيص العروض التسويقية للمتعاملين.</li>
                        <li>7. التنظيم الإداري لموظفي المصرف ومتابعة السيرة المهنية.</li>
                        <li>8.القيام بالإحصائيات وتشفير البيانات من أجل تحسين عملية التوظيف؛</li>
                        <li>9. توفير أدوات تكنولوجيا المعلومات والاتصال الهاتفي، وإدارة الوصول إلى خدماتنا وأنظمة المعلومات لدينا؛</li>
                        <li>10. توفير بيئة عمل مناسبة خاصة للأشخاص ذوي القدرة المحدودة على الحركة.</li>
                        <li>11. ضمان سلامة الأشخاص والمعدات من خلال تحديد أصحاب المصلحة عند الوصول إلى موارد ومرافق مصرف السلام الجزائر؛</li>
                        <li>12. حماية حقوق مصرف السلام الجزائر (على سبيل المثال الدفاع عن حقوق المصرف في حالة حدوث نزاع).</li>
                        <li>13. التواصل معكم (الاستجابة لطلباتك وإرسال التحديثات وتقديم الدعم)؛</li>
                    </ul>

                    <h4>مشاركة المعطيات</h4>
                    <p>كجزء من مهامنا، قد نشارك بياناتك الشخصية مع:</p>
                    <ul>
                        <li>مقدمو خدمات طرف ثالث موثوق فيهم للوظائف الأساسية.</li>
                        <li>عندما يقتضي القانون ذلك أو لحماية حقوق الحقوق.</li>
                        <li>السلطات القضائية، المالية، الضريبية، الإدارية والهيئات العامة أو المؤسسات التي يلزم علينا قانونا الكشف لها عن بياناتكم الشخصية.</li>
                        <li>بعض المهن الخاضعة للتنظيم مثل المحامين، الموثقين، الخبراء أو محافظي الحسابات عندما تتطلب الظروف ذلك (المعاملات، التقاضي، التدقيق، وما إلى ذلك).</li>
                        <li>الهيئات والمؤسسات التابعة للمجموعة التي ينتمي إليها مصرف السلام الجزائر،</li>
                    </ul>

                    <h4>أمن البيانات</h4>
                    <p>من أجل حماية بياناتك التي تم جمعها، يتم وضع تدابير أمنية مادية وتقنية وتنظيمية مناسبة لمنع أي فقدان أو سوء استخدام أو وصول غير مصرح به أو الكشف عن بياناتك أو تغييرها.</p>

                    <h4>الاحتفاظ بالبيانات</h4>
                    <p>لتحقيق الأغراض التي تم جمع بياناتك الشخصية من أجلها فإننا نحتفظ ببياناتك طوال مدة العلاقة طالما أنك تستخدم منتجاتنا وخدماتنا. وقد يتم الاحتفاظ بها بعد انتهاء علاقة العمل، لا سيما للامتثال للوائح المعمول بها، أو لتأكيد حقوقنا أو الدفاع عن مصالحنا.</p>

                    <h4>حقوقك</h4>
                    <p>وفقًا للقانون 18-07 (المواد من 32 إلى 37)، تتمتع بالحقوق التالية:</p>
                    <ul>
                        <li>الحق في الحصول على المعلومات (وفقا لأحكام المادتين 32 و 33 من القانون 18-07).</li>
                        <li>الحق الوصول (وفقا لشروط المادة 34 من القانون 18-07)؛</li>
                        <li>الحق التصحيح (وفقا لشروط المادة 35 من القانون 18-07).</li>
                        <li>الالحق المعارضة (بموجب شروط المادة 36 من القانون 18-07).</li>
                        <li>حظر الاستكشاف المباشر (طبقا لشروط المادة 37 من القانون 18-07).</li>
                    </ul>
                    <p>يمكنكم ممارسة أي من الحقوق المذكورة أعلاه عن طريق التواصل مع ممثل مسؤول المعالجة عبر قنوات التواصل أدناه. يجب أن يكون طلبكم مصحوبًا بنسخة من وثيقة إثبات الهوية، لتتم معالجته.</p>

                    <h4>الاتصال بنا</h4>
                    <p>لمزيد من المعلومات أو التوضيحات المتعلقة بهذه السياسة أو لاستخدام أحد حقوقكم الواردة أعلاه، يرجى الاتصال بممثل مسؤول معالجة المعطيات لمصرف السلام الجزائرعلى عنوان البريد الإلكتروني التالي:</p>
                    <p>مصرف السلام الجزائر ،</p>
                    <p>233 , شارع أحمد واكد، دالي إبراهيم الجزائر</p>
                    <p>Privacy@alsalamalgeria.com</p>
                    <p>باستخدامك لخدمات المصرف، فإنك توافق على شروط سياسة حماية البيانات الشخصية.</p>
                </div>

            <div class="text-left mt-4">
              <button type="button" class="btn btn-secondary" t-on-click="closePopup">
                إغلاق
              </button>
            </div>
          </div>
        </div>
      </t>
    </div>
  `
}

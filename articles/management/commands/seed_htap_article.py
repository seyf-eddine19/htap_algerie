from django.core.management.base import BaseCommand
from django.utils import timezone

from articles.models import (
    Article,
    ArticleCategory,
    ArticleTranslation,
    ArticleBlock,
)


class Command(BaseCommand):
    help = "Create English Article - Chronic Thromboembolic Pulmonary Hypertension"

    def handle(self, *args, **options):

        # ==============================================================
        # CATEGORY
        # ==============================================================

        category, _ = ArticleCategory.objects.get_or_create(
            slug="htap",
            defaults={
                "name": "PAH",
                "is_active": True,
                "order": 1,
            },
        )

        # ==============================================================
        # ARTICLE
        # ==============================================================

        # article, _ = Article.objects.get_or_create(
        #     slug="chronic-thromboembolic-pulmonary-hypertension",
        #     defaults={
        #         "category": category,
        #         "author": "HTAP Algérie",
        #         "status": Article.Status.PUBLISHED,
        #         "is_featured": False,
        #         "published_at": timezone.now(),
        #     },
        # )

        article, _ = Article.objects.get_or_create(
            slug="chronic-thromboembolic-pulmonary-hypertension",
            defaults={
                "category": category,
                "author": "HTAP Algérie",
                "status": Article.Status.PUBLISHED,
                "is_featured": False,
                "published_at": timezone.now(),
            },
        )

        # ==============================================================
        # TRANSLATION
        # ==============================================================

        translation, created = ArticleTranslation.objects.get_or_create(
            article=article,
            language="en",
            defaults={
                "title": "Chronic Thromboembolic Pulmonary Hypertension",
                "excerpt": (
                    "Information about chronic thromboembolic pulmonary "
                    "hypertension, its management and interventional treatment."
                ),
                "meta_title": (
                    "Chronic Thromboembolic Pulmonary Hypertension | "
                    "HTAP Algérie"
                ),
                "meta_description": (
                    "Information about chronic thromboembolic pulmonary "
                    "hypertension and its interventional management."
                ),
            },
        )

        # ==============================================================
        # BLOCKS
        # ==============================================================

        blocks = [

            # ==========================================================
            # INTRODUCTION
            # ==========================================================

            {
                "type": "heading",
                "title": (
                    "Chronic Thromboembolic Pulmonary Hypertension"
                ),
            },

            {
                "type": "heading",
                "title": (
                    "Updates on Chronic Thromboembolic Pulmonary Hypertension"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Click on the icon to download."
                ),
            },

            # ==========================================================
            # PULMONARY ANGIOPLASTY
            # ==========================================================

            {
                "type": "heading",
                "title": (
                    "Pulmonary Angioplasty at HEGP"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Letter from the Pulmonary Hypertension Reference Centre "
                    "to the HTaPFrance patient association:"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Message from the coordinator of the Reference Centre "
                    "addressed to patients concerned by chronic "
                    "thromboembolic pulmonary hypertension."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Thank you for your question addressed to Marc Humbert "
                    "regarding the performance of pulmonary angioplasties "
                    "at centres that are not identified by our pulmonary "
                    "hypertension care network."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "We confirm that the Reference Centre has designated "
                    "one centre for medical, surgical and interventional "
                    "management through pulmonary endarterectomy and/or "
                    "pulmonary angioplasty. This includes the Pulmonary "
                    "Hypertension Reference Centre at the Bicêtre site, "
                    "AP-HP, and the Marie Lannelongue site."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "A centre has also been designated for interventional "
                    "management through pulmonary angioplasty: the "
                    "Rhône-Alpes competence centre, at the Grenoble site."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "It is necessary to limit the number of centres "
                    "responsible for medical, surgical and interventional "
                    "management through pulmonary endarterectomy and/or "
                    "pulmonary angioplasty in order to have experienced "
                    "medical and surgical teams performing a sufficient "
                    "number of procedures and familiar with the treatments "
                    "and their complications."
                ),
            },

            # ==========================================================
            # MULTIDISCIPLINARY MEETING
            # ==========================================================

            {
                "type": "heading",
                "title": (
                    "Multidisciplinary discussion of chronic "
                    "thromboembolic pulmonary hypertension"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "All cases of chronic thromboembolic pulmonary "
                    "hypertension must be discussed during a "
                    "multidisciplinary consultation meeting in the presence "
                    "of pulmonary hypertension specialists, a specialised "
                    "radiologist, a pulmonary angioplasty specialist, "
                    "and a thoracic surgeon performing pulmonary "
                    "endarterectomy surgery."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "These meetings are organised in person or by "
                    "videoconference every Tuesday from 9:00 a.m. to "
                    "11:00 a.m. at Bicêtre Hospital."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Each case receives a report determining the best "
                    "therapeutic strategy, which may include surgery, "
                    "angioplasty, and/or medical treatment."
                ),
            },

            # ==========================================================
            # REFERENCE CENTRE
            # ==========================================================

            {
                "type": "paragraph",
                "text": (
                    "The Reference Centre does not support other initiatives "
                    "for medical, surgical and interventional management "
                    "through pulmonary endarterectomy and/or pulmonary "
                    "angioplasty."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "We leave it to you to distribute this information "
                    "to your members."
                ),
            },

            # ==========================================================
            # AUTHORS / SIGNATORIES
            # ==========================================================

            {
                "type": "paragraph",
                "text": (
                    "Best regards,"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Marc Humbert, Coordinator of the Pulmonary Hypertension "
                    "Reference Centre"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Gérald Simonneau, Scientific Director of the Chronic "
                    "Thromboembolic Pulmonary Hypertension Programme"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Elie Fadel, Surgical Director of the Chronic "
                    "Thromboembolic Pulmonary Hypertension Programme"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Xavier Jaïs, Medical Director of the Chronic "
                    "Thromboembolic Pulmonary Hypertension Programme"
                ),
            },

        ]

        # ==============================================================
        # CREATE BLOCKS
        # ==============================================================


        for order, block in enumerate(blocks, start=1):

            ArticleBlock.objects.create(
                translation=translation,
                block_type=block["type"],
                order=order,
                title=block.get("title", ""),
                text=block.get("text", ""),
                image=block.get("image", ""),
                image_caption=block.get("image_caption", ""),
            )

        # ==============================================================
        # SUCCESS
        # ==============================================================

        self.stdout.write(
            self.style.SUCCESS(
                "English article created successfully."
            )
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"Article ID: {article.pk}"
            )
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"Translation ID: {translation.pk}"
            )
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"Blocks created: {len(blocks)}"
            )
        )


        translation = ArticleTranslation.objects.create(
            article=article,
            language="ar",
            title="ارتفاع ضغط الدم الرئوي الخثاري الصمّي المزمن",
            excerpt=(
                "معلومات حول ارتفاع ضغط الدم الرئوي الخثاري الصمّي المزمن، "
                "وتدبيره والعلاجات التدخلية والجراحية المتاحة."
            ),
            meta_title=(
                "ارتفاع ضغط الدم الرئوي الخثاري الصمّي المزمن | HTAP Algérie"
            ),
            meta_description=(
                "معلومات حول ارتفاع ضغط الدم الرئوي الخثاري الصمّي المزمن، "
                "والخيارات العلاجية والتدخلية والجراحية."
            ),
        )

        blocks = [

            # ==========================================================
            # INTRODUCTION
            # ==========================================================

            {
                "type": "heading",
                "title": (
                    "ارتفاع ضغط الدم الرئوي الخثاري الصمّي المزمن"
                ),
            },

            {
                "type": "heading",
                "title": (
                    "ارتفاع ضغط الدم الرئوي الخثاري الصمّي المزمن"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "ارتفاع ضغط الدم الرئوي الخثاري الصمّي المزمن "
                    "(HTP-TEC) هو شكل من أشكال ارتفاع ضغط الدم الرئوي "
                    "المرتبط بوجود خثرات دموية وانسدادات مزمنة في "
                    "الشرايين الرئوية."
                ),
            },

            # ==========================================================
            # DOCUMENT
            # ==========================================================

            {
                "type": "paragraph",
                "text": (
                    "آخر المستجدات في ارتفاع ضغط الدم الرئوي الخثاري "
                    "الصمّي المزمن"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "اضغط على الأيقونة لتحميل الوثيقة."
                ),
            },

            # ==========================================================
            # ANGIOPLASTY
            # ==========================================================

            {
                "type": "heading",
                "title": (
                    "رأب الأوعية الرئوية في مستشفى HEGP"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "رسالة من مركز الإحالة لارتفاع ضغط الدم الرئوي "
                    "إلى جمعية المرضى HTaPFrance."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "رسالة منسق مركز الإحالة إلى المرضى المعنيين "
                    "بارتفاع ضغط الدم الرئوي الخثاري الصمّي المزمن."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "شكرًا على سؤالكم الموجه إلى Marc Humbert بشأن "
                    "إجراء رأب الأوعية الرئوية في مراكز غير محددة "
                    "ضمن شبكة التكفل بارتفاع ضغط الدم الرئوي."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "نؤكد لكم أن مركز الإحالة قد حدد مركزًا للتكفل "
                    "الطبي والجراحي والتداخلي، من خلال استئصال "
                    "بطانة الشرايين الرئوية و/أو رأب الأوعية الرئوية، "
                    "وهو مركز الإحالة لارتفاع ضغط الدم الرئوي في "
                    "موقع Bicêtre التابع لـ AP-HP وموقع Marie Lannelongue."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "كما تم تحديد مركز للتكفل التداخلي عن طريق رأب "
                    "الأوعية الرئوية، وهو مركز الكفاءات في منطقة "
                    "Rhône-Alpes، في موقع Grenoble."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "ومن الضروري الحد من عدد المراكز التي تتولى "
                    "التكفل الطبي والجراحي والتداخلي عن طريق "
                    "استئصال بطانة الشرايين الرئوية و/أو رأب "
                    "الأوعية الرئوية، وذلك لضمان توفر فرق طبية "
                    "وجراحية ذات خبرة، تجري عددًا كافيًا من هذه "
                    "الإجراءات وتملك خبرة جيدة في العلاجات "
                    "ومضاعفاتها."
                ),
            },

            # ==========================================================
            # MULTIDISCIPLINARY MEETING
            # ==========================================================

            {
                "type": "heading",
                "title": (
                    "اجتماع التشاور متعدد التخصصات"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "يجب مناقشة جميع حالات ارتفاع ضغط الدم الرئوي "
                    "الخثاري الصمّي المزمن خلال اجتماع تشاور متعدد "
                    "التخصصات، بحضور اختصاصيي ارتفاع ضغط الدم الرئوي، "
                    "وطبيب أشعة متخصص، واختصاصي في رأب الأوعية "
                    "الرئوية، وجراح صدر يمارس جراحة استئصال بطانة "
                    "الشرايين الرئوية."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "تُنظم هذه الاجتماعات حضوريًا أو عبر تقنية "
                    "الاجتماع المرئي كل يوم ثلاثاء من الساعة "
                    "09:00 إلى 11:00 في مستشفى Bicêtre."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "وتحصل كل حالة على تقرير يحدد أفضل استراتيجية "
                    "علاجية، سواء كانت الجراحة أو رأب الأوعية "
                    "الرئوية أو العلاج الدوائي أو الجمع بينها."
                ),
            },

            # ==========================================================
            # CENTER POSITION
            # ==========================================================

            {
                "type": "paragraph",
                "text": (
                    "لا يدعم مركز الإحالة مبادرات أخرى للتكفل "
                    "الطبي والجراحي والتداخلي عن طريق استئصال "
                    "بطانة الشرايين الرئوية و/أو رأب الأوعية الرئوية."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "نترك لكم مهمة تعميم هذه المعلومات على أعضائكم."
                ),
            },

            # ==========================================================
            # SIGNATURE
            # ==========================================================

            {
                "type": "paragraph",
                "text": (
                    "مع خالص التحية،"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Marc Humbert، منسق مركز الإحالة لارتفاع ضغط الدم الرئوي\n"
                    "Gérald Simonneau، المدير العلمي لبرنامج ارتفاع ضغط الدم "
                    "الرئوي الخثاري الصمّي المزمن\n"
                    "Elie Fadel، المسؤول الجراحي عن برنامج ارتفاع ضغط الدم "
                    "الرئوي الخثاري الصمّي المزمن\n"
                    "Xavier Jaïs، المسؤول الطبي عن برنامج ارتفاع ضغط الدم "
                    "الرئوي الخثاري الصمّي المزمن"
                ),
            },

        ]

        # ==============================================================
        # CREATE BLOCKS
        # ==============================================================

        for order, block in enumerate(blocks, start=1):

            ArticleBlock.objects.create(
                translation=translation,
                block_type=block["type"],
                order=order,
                title=block.get("title", ""),
                text=block.get("text", ""),
                image=block.get("image", ""),
                image_caption=block.get("image_caption", ""),
            )

        self.stdout.write(
            self.style.SUCCESS(
                "Arabic translation created successfully."
            )
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"Article ID: {article.pk}"
            )
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"Translation ID: {translation.pk}"
            )
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"Blocks created: {len(blocks)}"
            )
        )


        translation = ArticleTranslation.objects.create(
            article=article,
            language="fr",
            title="L'HTAP thromboembolique chronique",
            excerpt=(
                "Informations sur l'hypertension pulmonaire "
                "thromboembolique chronique, sa prise en charge et "
                "les différentes options thérapeutiques."
            ),
            meta_title=(
                "L'HTAP thromboembolique chronique | HTAP Algérie"
            ),
            meta_description=(
                "Informations sur l'hypertension pulmonaire "
                "thromboembolique chronique et sa prise en charge "
                "médicale, chirurgicale et interventionnelle."
            ),
        )

        blocks = [

            # ==========================================================
            # INTRODUCTION
            # ==========================================================

            {
                "type": "heading",
                "title": (
                    "L'HYPERTENSION PULMONAIRE THROMBOEMBOLIQUE CHRONIQUE"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "L'hypertension pulmonaire thromboembolique chronique "
                    "(HTP-TEC) est une forme d'hypertension pulmonaire "
                    "associée à la présence de caillots sanguins persistants "
                    "et d'obstructions chroniques des artères pulmonaires."
                ),
            },

            # ==========================================================
            # DOCUMENT / ACTUALITES
            # ==========================================================

            {
                "type": "heading",
                "title": "Actualités dans l’HTP-TEC",
            },

            {
                "type": "paragraph",
                "text": (
                    "CV29_QDND_Actualités_dans_l'HTP-TEC_V00"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Cliquer sur l'icône pour télécharger."
                ),
            },

            # ==========================================================
            # ANGIOPLASTIES
            # ==========================================================

            {
                "type": "heading",
                "title": "Angioplasties pulmonaires à l'HEGP",
            },

            {
                "type": "paragraph",
                "text": (
                    "Lettre du Centre de Référence de l'hypertension "
                    "pulmonaire à l'association de patients HTaPFrance."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Message du coordonnateur du Centre de Référence "
                    "à l'adresse des patients concernés par une "
                    "Hypertension Pulmonaire Thrombo-embolique chronique."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Merci pour votre question adressée à Marc Humbert "
                    "concernant la réalisation d’angioplasties pulmonaires "
                    "dans des sites non identifiés par notre réseau de "
                    "prise en charge de l’hypertension pulmonaire."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Nous vous confirmons que le Centre de Référence "
                    "a désigné un Centre pour la prise en charge "
                    "médico-chirurgicale et interventionnelle par "
                    "endartériectomie pulmonaire et/ou angioplastie "
                    "pulmonaire : le Centre de Référence de "
                    "l’hypertension pulmonaire, site de Bicêtre, "
                    "AP-HP, et site Marie Lannelongue."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Un Centre a également été désigné pour la prise "
                    "en charge interventionnelle par angioplastie "
                    "pulmonaire : le centre de compétences Rhône-Alpes, "
                    "site de Grenoble."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Il est nécessaire de limiter le nombre de Centres "
                    "pour la prise en charge médico-chirurgicale et "
                    "interventionnelle par endartériectomie pulmonaire "
                    "et/ou angioplastie pulmonaire afin de disposer "
                    "d’équipes médico-chirurgicales expérimentées "
                    "pratiquant un nombre suffisant de gestes et "
                    "connaissant bien les traitements et leurs "
                    "complications."
                ),
            },

            # ==========================================================
            # REUNION MULTIDISCIPLINAIRE
            # ==========================================================

            {
                "type": "heading",
                "title": "Réunion de concertation pluridisciplinaire",
            },

            {
                "type": "paragraph",
                "text": (
                    "Tous les cas d’hypertension pulmonaire "
                    "thrombo-embolique chronique doivent être discutés "
                    "au cours d’une réunion de concertation "
                    "pluri-disciplinaire en présence de spécialistes "
                    "de l’hypertension pulmonaire, d’un radiologue "
                    "spécialisé, d’un spécialiste en angioplastie "
                    "pulmonaire et d’un chirurgien thoracique pratiquant "
                    "la chirurgie d’endartériectomie pulmonaire."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Ces réunions sont organisées en présentiel ou "
                    "par vidéoconférence tous les mardis de 9h à 11h "
                    "à l’Hôpital Bicêtre."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Chaque cas bénéficie d’un compte-rendu statuant "
                    "sur la meilleure stratégie thérapeutique : "
                    "chirurgie, angioplastie et/ou traitement médical."
                ),
            },

            # ==========================================================
            # POSITION DU CENTRE
            # ==========================================================

            {
                "type": "paragraph",
                "text": (
                    "Le Centre de Référence ne soutient pas d’autres "
                    "initiatives pour la prise en charge "
                    "médico-chirurgicale et interventionnelle par "
                    "endartériectomie pulmonaire et/ou angioplastie "
                    "pulmonaire."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Nous vous laissons diffuser cette information "
                    "auprès de vos adhérents."
                ),
            },

            # ==========================================================
            # SIGNATURE
            # ==========================================================

            {
                "type": "paragraph",
                "text": "Amitiés,",
            },

            {
                "type": "paragraph",
                "text": (
                    "Marc Humbert, coordonnateur du Centre de Référence "
                    "de l’hypertension pulmonaire\n"
                    "Gérald Simonneau, directeur scientifique du "
                    "programme hypertension pulmonaire "
                    "thrombo-embolique chronique\n"
                    "Elie Fadel, responsable chirurgical du programme "
                    "hypertension pulmonaire thrombo-embolique chronique\n"
                    "Xavier Jaïs, responsable médical du programme "
                    "hypertension pulmonaire thrombo-embolique chronique"
                ),
            },

        ]

        # ==============================================================
        # CREATE BLOCKS
        # ==============================================================

        for order, block in enumerate(blocks, start=1):

            ArticleBlock.objects.create(
                translation=translation,
                block_type=block["type"],
                order=order,
                title=block.get("title", ""),
                text=block.get("text", ""),
                image=block.get("image", ""),
                image_caption=block.get("image_caption", ""),
            )

        self.stdout.write(
            self.style.SUCCESS(
                "French article created successfully."
            )
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"Article ID: {article.pk}"
            )
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"Translation ID: {translation.pk}"
            )
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"Blocks created: {len(blocks)}"
            )
        )
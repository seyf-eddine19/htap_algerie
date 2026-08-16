from django.core.management.base import BaseCommand
from django.utils import timezone

from articles.models import (
    Article,
    ArticleCategory,
    ArticleTranslation,
    ArticleBlock,
)


class Command(BaseCommand):
    help = "Create Article - HTAP associées"

    def handle(self, *args, **options):

        # ==============================================================
        # CATEGORY
        # ==============================================================

        category, _ = ArticleCategory.objects.get_or_create(
            slug="htap",
            defaults={
                "name": "HTAP",
                "is_active": True,
                "order": 1,
            },
        )

        # ==============================================================
        # ARTICLE
        # ==============================================================

        article = Article.objects.create(
            category=category,
            author="HTAP Algérie",
            status=Article.Status.PUBLISHED,
            is_featured=False,
            published_at=timezone.now(),
            slug="htap-associees",
        )

        # ==============================================================
        # FRENCH TRANSLATION
        # ==============================================================

        translation = ArticleTranslation.objects.create(
            article=article,
            language="fr",
            title="HTAP associées",
            excerpt=(
                "Informations sur les différentes formes d'hypertension "
                "artérielle pulmonaire associées à d'autres maladies, "
                "notamment les connectivites, l'hypertension portale, "
                "le VIH et les cardiopathies congénitales."
            ),
            meta_title="HTAP associées | HTAP Algérie",
            meta_description=(
                "Découvrez les différentes formes d'HTAP associées, "
                "notamment à la connectivite, à l'hypertension portale, "
                "au VIH et aux cardiopathies congénitales."
            ),
        )

        # ==============================================================
        # BLOCKS
        # ==============================================================

        blocks = [

            # ==========================================================
            # HTAP ASSOCIÉE À UNE CONNECTIVITE
            # ==========================================================

            {
                "type": "heading",
                "title": "HTAP associée à une Connectivite",
            },

            {
                "type": "paragraph",
                "text": (
                    "Maladie due au dérèglement du système immunitaire "
                    "qui porte atteinte au tissu de soutien de l’organisme, "
                    "le tissu conjonctif."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Représente 15,3 % des HTAP du groupe 1."
                ),
            },

            {
                "type": "heading",
                "title": "Sclérodermie systémique (ScS)",
            },

            {
                "type": "paragraph",
                "text": (
                    "La sclérodermie est une maladie auto-immune qui affecte "
                    "tout le tissu conjonctif. Elle est caractérisée avant "
                    "tout par le durcissement et l’épaississement de la peau."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "La ScS est caractérisée par la fibrose (fabrication "
                    "excessive de collagène) de la peau, des vaisseaux sanguins "
                    "mais aussi des organes internes (appareil gastro-intestinal, "
                    "les poumons, le cœur, les reins)."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "La sclérodermie systémique représente environ 11 % de "
                    "l’ensemble des causes d’HTAP, soit 600 à 800 patients."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Le symptôme : le phénomène de Raynaud (doigts devenant "
                    "blancs, froids et parfois insensibles ou engourdis) est "
                    "le premier signe de la ScS."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Trois mécanismes s’associent pour augmenter les résistances "
                    "vasculaires pulmonaires au cours de l’HTAP associée à la "
                    "ScS : la vasoconstriction, le remodelage vasculaire "
                    "pulmonaire et les phénomènes de thrombose in situ."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Le traitement repose sur l’association de mesures générales, "
                    "du traitement conventionnel et, chez les patients en classe "
                    "fonctionnelle NYHA II, III ou IV, de l’adjonction d’une "
                    "molécule agissant sur l’une des trois voies métaboliques "
                    "de l’endothéline, du NO ou de la prostacycline."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Les recommandations internationales sont de réaliser un "
                    "dépistage de l’HTAP de manière annuelle chez tout patient "
                    "atteint de ScS."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Ce dépistage doit reposer sur l’échocardiographie et des "
                    "épreuves fonctionnelles respiratoires, ce qui permet la "
                    "mise en place précoce d'un traitement adapté."
                ),
            },

            {
                "type": "heading",
                "title": "Lupus érythémateux systémique",
            },

            {
                "type": "heading",
                "title": "Connectivite mixte (syndrome de Sharp)",
            },

            {
                "type": "paragraph",
                "text": (
                    "Télécharger le document HTAP-Sclérodermie au format PDF."
                ),
            },

            # ==========================================================
            # HTAP ASSOCIÉE À UNE HYPERTENSION PORTALE
            # ==========================================================

            {
                "type": "heading",
                "title": "HTAP associée à une Hypertension Portale",
            },

            {
                "type": "heading",
                "title": "L’HYPERTENSION PORTOPULMONAIRE",
            },

            {
                "type": "paragraph",
                "text": (
                    "Par Laurent Savale (1) et Vincent Cottin (2)\n\n"
                    "Service de pneumologie – Centre de Référence de "
                    "l’hypertension pulmonaire sévère, Hôpital Bicêtre, "
                    "AP-HP, Le Kremlin Bicêtre, France.\n\n"
                    "Hospices Civils de Lyon, Hôpital Louis Pradel, "
                    "Service de pneumologie – Centre de Référence national "
                    "des maladies pulmonaires rares et Centre de Compétences "
                    "de l’hypertension artérielle pulmonaire, Lyon, France ; "
                    "Université de Lyon, Université Claude Bernard Lyon I, "
                    "INRA, UMR754 INRA-Vetagrosup EPHE IFR 128, Lyon, France."
                ),
            },

            # ==========================================================
            # INTRODUCTION HTPoP
            # ==========================================================

            {
                "type": "heading",
                "title": "Introduction",
            },

            {
                "type": "paragraph",
                "text": (
                    "Les anomalies pulmonaires sont fréquentes chez les "
                    "patients atteints de maladies hépatiques. Ainsi, les "
                    "deux tiers des patients évalués en vue d’une transplantation "
                    "hépatique se plaignent de dyspnée (essoufflement)."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Certaines de ces anomalies respiratoires sont en rapport "
                    "avec des maladies pulmonaires spécifiques mais indépendantes "
                    "de l’atteinte hépatique (bronchopneumopathie chronique "
                    "obstructive, asthme…), alors que d’autres sont directement "
                    "la conséquence de l’insuffisance hépatique."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Ainsi, l’existence d’une maladie hépatique peut avoir des "
                    "conséquences néfastes sur le système vasculaire pulmonaire."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "L'hypertension portopulmonaire (HTPoP) est définie comme "
                    "une hypertension artérielle pulmonaire (HTAP) qui se "
                    "développe dans un contexte d’hypertension portale."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Le plus souvent, l’hypertension portale est la conséquence "
                    "d’une cirrhose. L’HTPoP est intégrée dans le groupe 1 de "
                    "la classification de l’hypertension pulmonaire, car elle "
                    "est caractérisée par des mécanismes physiopathologiques "
                    "qui sont semblables à d'autres formes d'HTAP."
                ),
            },

            # ==========================================================
            # EPIDEMIOLOGIE
            # ==========================================================

            {
                "type": "heading",
                "title": "Épidémiologie",
            },

            {
                "type": "paragraph",
                "text": (
                    "L’association entre hypertension portale et HTAP est bien "
                    "établie et elle est reconnue comme une association « très "
                    "probable »."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Chez les patients atteints d’une maladie hépatique avec "
                    "hypertension portale, l’hypertension pulmonaire modérée "
                    "et peu symptomatique (pression artérielle pulmonaire "
                    "moyenne ou PAPm < 35 mmHg, débit cardiaque élevé) est "
                    "fréquente ; elle est liée essentiellement au syndrome "
                    "hyperkinétique (élévation du débit cardiaque) responsable "
                    "d’une élévation « passive » de la pression artérielle "
                    "pulmonaire, les résistances vasculaires pulmonaires (RVP) "
                    "restant normales ou basses."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "À côté de ces élévations passives de la PAP, il existe "
                    "de vraies HTAP, moins fréquentes, liées au remodelage "
                    "vasculaire par prolifération cellulaire comme on le voit "
                    "dans l’HTAP idiopathique (sans cause identifiée)."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "On estime que 2 % environ des patients présentant une "
                    "maladie hépatique avancée présenteraient une HTPoP. "
                    "La fréquence de l’HTPoP atteindrait 3 % à 5 % des patients "
                    "présentant une maladie hépatique sévère, et 6 % des "
                    "patients en attente de transplantation hépatique."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Un délai moyen de 4 à 7 ans est observé entre le diagnostic "
                    "d’hypertension portale et celui d’HTPoP."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Sur les dernières données du registre français de l’HTAP, "
                    "l’HTPoP représenterait environ 17 % des causes d’HTAP en "
                    "France, soit la troisième cause des HTAP du groupe 1."
                ),
            },

            # ==========================================================
            # DEFINITION / DIAGNOSTIC
            # ==========================================================

            {
                "type": "heading",
                "title": "De la définition au diagnostic",
            },

            {
                "type": "paragraph",
                "text": (
                    "Le diagnostic d’HTPoP repose sur l’association de deux éléments :"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "1. Une HTAP, elle-même définie par une pression artérielle "
                    "pulmonaire (PAP) moyenne mesurée au cathétérisme cardiaque "
                    "droit supérieure ou égale à 25 mmHg au repos. "
                    "L’hypertension pulmonaire est ici précapillaire (due à une "
                    "anomalie vasculaire pulmonaire), avec une PAP d’occlusion "
                    "(estimation de la pression capillaire moyenne) inférieure "
                    "ou égale à 15 mmHg ; le débit cardiaque est normal ou "
                    "diminué, et les résistances vasculaires pulmonaires sont élevées."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "2. Une hypertension portale, avec ou sans maladie hépatique. "
                    "En effet, l’HTPoP survient indépendamment de la cause et "
                    "de la gravité de l’hypertension portale."
                ),
            },

            # ==========================================================
            # PHYSIOPATHOLOGIE
            # ==========================================================

            {
                "type": "heading",
                "title": "Physiopathologie",
            },

            {
                "type": "paragraph",
                "text": (
                    "Les lésions vasculaires pulmonaires observées chez les "
                    "malades atteints d’HTPoP sont comparables à celles observées "
                    "chez les malades atteints d’HTAP idiopathique."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "La maladie hépatique aboutit par différents mécanismes à "
                    "une agression de la circulation pulmonaire qui, chez certains "
                    "patients prédisposés, peut favoriser l’apparition d’un "
                    "remodelage vasculaire et l’installation progressive d’une HTAP."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "En cas de cirrhose, il est constaté un défaut de synthèse "
                    "hépatique de facteurs inhibant la prolifération des vaisseaux "
                    "(dits « anti-angiogéniques »). À l’inverse, la cirrhose "
                    "favoriserait l’augmentation de la prolifération cellulaire "
                    "vasculaire pulmonaire par le biais de médiateurs libérés "
                    "dans la circulation pulmonaire."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "L’augmentation du débit sanguin pulmonaire due à "
                    "l’hypertension portale pourrait participer à l’activation "
                    "de l’endothélium pulmonaire par un mécanisme de « shear "
                    "stress » (lésions par cisaillement)."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Enfin, les modifications de la circulation abdominale "
                    "provoquées par l’hypertension portale et les anomalies de "
                    "la fonction hépatique dues à la cirrhose favorisent le "
                    "passage dans la circulation sanguine de bactéries d’origine "
                    "digestive, puis le recrutement et l’activation de cellules "
                    "inflammatoires dans la circulation artérielle pulmonaire."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Il est probable qu’une prédisposition génétique encore "
                    "non identifiée explique que seule une minorité des patients "
                    "atteints d’hypertension portale développent une HTPoP."
                ),
            },

            # ==========================================================
            # MANIFESTATIONS CLINIQUES
            # ==========================================================

            {
                "type": "heading",
                "title": "Manifestations cliniques",
            },

            {
                "type": "paragraph",
                "text": (
                    "Le principal symptôme est représenté par la dyspnée d’effort, "
                    "d’intensité variable. Toutefois la dyspnée peut manquer "
                    "initialement chez les patients dont l’activité physique "
                    "est limitée, ou être intriquée avec la gêne liée à la "
                    "présence anormale de liquide dans la cavité abdominale "
                    "(l’ascite)."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "La dyspnée s’aggrave progressivement, et peut s’accompagner "
                    "de douleurs thoraciques atypiques ou de syncopes d’effort "
                    "(qui représentent un critère clinique de gravité)."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Il peut exister à l’examen clinique des signes "
                    "d’insuffisance ventriculaire droite. Ces signes cliniques "
                    "viennent s’ajouter à ceux propres à la maladie hépatique "
                    "sous-jacente."
                ),
            },

            # ==========================================================
            # EXAMENS COMPLEMENTAIRES
            # ==========================================================

            {
                "type": "heading",
                "title": "Examens complémentaires",
            },

            {
                "type": "heading",
                "title": "1. Rechercher l’hypertension pulmonaire par une échographie cardiaque",
            },

            {
                "type": "paragraph",
                "text": (
                    "L’échographie cardiaque trans-thoracique est l’examen de "
                    "référence pour orienter vers une HTPoP. Elle est nécessaire "
                    "en cas d’essoufflement ou d’insuffisance cardiaque droite "
                    "chez un patient présentant une hypertension portale, et "
                    "doit être réalisée systématiquement au cours du bilan "
                    "pré-transplantation hépatique."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Elle permet l’estimation de la pression artérielle "
                    "pulmonaire systolique d’après la vitesse maximale du flux "
                    "de régurgitation tricuspide au doppler."
                ),
            },

            {
                "type": "heading",
                "title": "2. Affirmer l’HTAP par le cathétérisme cardiaque droit",
            },

            {
                "type": "paragraph",
                "text": (
                    "Un cathétérisme cardiaque droit doit être réalisé lorsqu’une "
                    "HTAP est suspectée à l’échographie cardiaque, en particulier "
                    "si la PAP systolique est estimée à plus de 50 mmHg."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Ce diagnostic est souvent déterminant dans le contexte "
                    "d’une maladie hépatique avancée car l’HTAP expose à un "
                    "risque opératoire et post-opératoire accru en cas de "
                    "transplantation hépatique."
                ),
            },

            {
                "type": "heading",
                "title": "3. Autres examens utiles",
            },

            {
                "type": "paragraph",
                "text": (
                    "La radiographie thoracique peut montrer une hypertrophie "
                    "des artères pulmonaires, ainsi qu’une dilatation des "
                    "cavités cardiaques droites."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Un test de marche de 6 minutes est réalisé pour évaluer "
                    "de façon reproductible l’incapacité fonctionnelle associée "
                    "à l’HTPoP."
                ),
            },

            # ==========================================================
            # TRAITEMENT
            # ==========================================================

            {
                "type": "heading",
                "title": "Traitement",
            },

            {
                "type": "paragraph",
                "text": (
                    "La stratégie thérapeutique employée dans la prise en "
                    "charge de l’HTPoP est globalement similaire à celle de "
                    "l’HTAP idiopathique avec néanmoins des considérations "
                    "spécifiques du fait de la maladie hépatique associée."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Les patients atteints de cirrhose n’ont pas pu être inclus "
                    "dans la plupart des études prospectives ayant évalué les "
                    "traitements spécifiques de l’HTAP idiopathique."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Cependant, l’expérience acquise dans les centres de prise "
                    "en charge de l’HTAP et les données rétrospectives recueillies "
                    "dans la littérature semblent montrer une bonne efficacité "
                    "des traitements au moins sur les données fonctionnelles et "
                    "hémodynamiques avec globalement une bonne tolérance."
                ),
            },

            # ==========================================================
            # TRAITEMENT CONVENTIONNEL
            # ==========================================================

            {
                "type": "heading",
                "title": "Traitement « conventionnel » de l’HTAP",
            },

            {
                "type": "paragraph",
                "text": (
                    "Chez les malades atteints de cirrhose, les anticoagulants "
                    "ne sont habituellement pas administrés lorsqu’il existe "
                    "une insuffisance hépatocellulaire sévère et/ou une baisse "
                    "des plaquettes favorisée par l’hypertension portale."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Le traitement par ß-bloquants (bêta-bloquants), indiqué très "
                    "fréquemment chez les patients cirrhotiques pour prévenir "
                    "les hémorragies digestives par rupture de varices "
                    "œsophagiennes, peut être néfaste car il diminue le débit cardiaque."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Un traitement diurétique est conseillé en cas d’œdème "
                    "des membres inférieurs ou d’élévation de la pression de "
                    "l’oreillette droite au cathétérisme."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "L’oxygénothérapie est recommandée s’il existe un défaut "
                    "d’oxygénation qui peut aggraver l’HTAP."
                ),
            },

            # ==========================================================
            # TRAITEMENTS SPECIFIQUES
            # ==========================================================

            {
                "type": "heading",
                "title": "Traitements spécifiques de l’HTAP",
            },

            {
                "type": "paragraph",
                "text": (
                    "Les traitements spécifiques de l’HTAP sont assez largement "
                    "utilisés au cours de l’HTPoP."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Le traitement par administration intraveineuse continue "
                    "d’époprosténol (prostacycline-Flolan®) améliore la dyspnée "
                    "et l’hémodynamique."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "C’est le traitement de choix en cas de classe fonctionnelle "
                    "IV ou pour permettre la transplantation hépatique ultérieure "
                    "(bridge therapy)."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Ce traitement contraignant expose néanmoins à des "
                    "complications infectieuses locales et générales liées à "
                    "la voie veineuse centrale permanente."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Une amélioration clinique a également été montrée avec "
                    "des analogues stables de la prostacycline administrés par "
                    "voie inhalée (iloprost-Ventavis®) ou sous-cutanée continue "
                    "(treprostinil-Remodulin®), mais on dispose de peu de données "
                    "à long terme."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "L’utilisation des antagonistes des récepteurs de "
                    "l’endothéline-1 (bosentan-Tracleer®, ambrisentan-Volibris®) "
                    "est limitée dans le contexte de l’HTPoP par leur toxicité "
                    "hépatique potentielle."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Néanmoins, l’utilisation du bosentan, ou de l’ambrisentan "
                    "(dont l’hépatotoxicité serait moindre), est possible chez "
                    "les patients présentant une cirrhose peu évoluée ou une "
                    "hypertension portale sans cirrhose."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Une vigilance particulière est nécessaire pour s’assurer "
                    "de l’absence d’aggravation de la fonction hépatique lorsque "
                    "cette classe thérapeutique est utilisée."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Les inhibiteurs de la phosphodiestérase 5 "
                    "(sildénafil-Revatio®, tadalafil-Adcirca®) peuvent être "
                    "utilisés avec une bonne tolérance habituelle chez les "
                    "patients présentant une HTPoP."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Néanmoins, ce traitement serait en théorie susceptible "
                    "d’aggraver indirectement l’hypertension portale, justifiant "
                    "une évaluation individuelle du bénéfice thérapeutique."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Une évaluation précise du bénéfice du traitement doit être "
                    "conduite individuellement, 3 à 4 mois après l’introduction "
                    "du traitement."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Les bénéfices escomptés comportent une amélioration de la "
                    "dyspnée (idéalement de classe fonctionnelle I ou II sous "
                    "traitement), une amélioration de la distance parcourue "
                    "en 6 minutes (plus de 450 à 500 mètres), et une amélioration "
                    "hémodynamique (diminution des résistances vasculaires "
                    "pulmonaires, normalisation du débit cardiaque)."
                ),
            },

            # ==========================================================
            # TRANSPLANTATION HEPATIQUE
            # ==========================================================

            {
                "type": "heading",
                "title": "Transplantation hépatique",
            },

            {
                "type": "paragraph",
                "text": (
                    "L’HTPoP n’est pas en soi une indication de transplantation "
                    "hépatique bien que quelques cas d’amélioration après "
                    "transplantation aient été rapportés."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "En revanche, lorsqu’il existe une indication de "
                    "transplantation hépatique du fait de la gravité de la "
                    "maladie hépatique elle-même, il est établi que l’HTAP sévère "
                    "(PAPm > 35 mmHg et résistances vasculaires pulmonaires "
                    "> 250 dyn.s.cm-5) est une contre-indication."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Il a été possible toutefois, dans certains cas, de diminuer "
                    "la pression artérielle pulmonaire par les dérivés de la "
                    "prostacycline permettant d’effectuer dans un second temps "
                    "une transplantation hépatique dans de bonnes conditions "
                    "de sécurité."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "L’évolution de l’HTPoP après transplantation hépatique est "
                    "souvent imprévisible notamment chez les patients ayant eu "
                    "besoin d’un traitement médical de l’HTAP avant transplantation "
                    "hépatique."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Il convient de surveiller ces patients de manière rapprochée "
                    "en période péri-opératoire afin d’ajuster les traitements."
                ),
            },

            # ==========================================================
            # CONCLUSION HTPoP
            # ==========================================================

            {
                "type": "heading",
                "title": "Conclusion",
            },

            {
                "type": "paragraph",
                "text": (
                    "L’HTPoP représente la 3ième cause d’HTAP en France. Elle "
                    "est retrouvée chez près de 6 % des patients en attente de "
                    "transplantation hépatique."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Sa fréquence justifie son dépistage chez tout patient "
                    "atteint d’une maladie hépatique et qui présente une gêne "
                    "respiratoire inexpliquée ainsi que chez tous les patients "
                    "qui doivent être inscrits sur liste de transplantation hépatique."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "La prise en charge de l’HTPoP est globalement similaire à "
                    "celle de l’HTAP idiopathique avec néanmoins des considérations "
                    "spécifiques liées à la maladie hépatique sous-jacente."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "L’HTPoP peut en revanche compliquer l’accès à la transplantation "
                    "hépatique et doit faire l’objet dans ce cas d’une prise en "
                    "charge multidisciplinaire associant pneumologue spécialiste "
                    "de l’HTAP et hépatologue."
                ),
            },

            # ==========================================================
            # HTAP ASSOCIÉE AU VIH
            # ==========================================================

            {
                "type": "heading",
                "title": "HTAP associée au VIH",
            },

            {
                "type": "paragraph",
                "text": (
                    "L'HTAP est une manifestation rare de l'infection à VIH, "
                    "indépendante du degré d'immunodépression mais aggrave "
                    "considérablement le pronostic des patients séropositifs atteints."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Elle peut toucher tous les groupes à risque d'infection "
                    "par le VIH mais les toxicomanes sont les plus fréquemment "
                    "concernés puisqu'ils représentent 40 à 60 % de l'ensemble "
                    "des malades."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "L'HTAP est diagnostiquée en moyenne 2,5 à 3 ans après la "
                    "découverte de la séropositivité mais elle peut également "
                    "la révéler ce qui justifie de faire réaliser une sérologie "
                    "VIH dans le bilan initial de toute HTAP d'allure idiopathique."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "La présentation clinique est identique à celle de l'HTAP "
                    "idiopathique et le diagnostic (cathétérisme cardiaque droit) "
                    "est réalisé de la même façon."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Le traitement des HTAP réfractaires malgré un traitement "
                    "conventionnel optimal (limitation des efforts, anticoagulation "
                    "orale, diurétiques et oxygène si nécessaire) associe "
                    "généralement traitement par antirétroviraux (trithérapie) "
                    "et époprosténol même si ce traitement, qui exige un matériel "
                    "veineux implantable, est inutilisable chez le toxicomane "
                    "non sevré et comporte un risque infectieux à prendre en "
                    "compte en cas d'immunodépression."
                ),
            },

            # ==========================================================
            # HTAP ASSOCIÉE À UNE CARDIOPATHIE CONGÉNITALE
            # ==========================================================

            {
                "type": "heading",
                "title": "HTAP associée à une Cardiopathie Congénitale",
            },

            {
                "type": "paragraph",
                "text": (
                    "Les cardiopathies congénitales représentent 13 % des cas "
                    "d’HTAP."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Les cardiopathies congénitales sont parmi les malformations "
                    "congénitales (c’est-à-dire acquises pendant le développement "
                    "embryonnaire, durant la grossesse) les plus fréquentes, "
                    "avec une incidence d’environ 8 sur 1000 naissances."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "60 % de ces anomalies sont caractérisées par un shunt "
                    "gauche-droit. C’est à ces dernières qu’est associée le "
                    "plus fréquemment l’HTAP."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Téléchargez la brochure Cardiopathies congénitales et "
                    "HTAP en PDF."
                ),
            },

            # ==========================================================
            # CTA
            # ==========================================================

            {
                "type": "heading",
                "title": "Prendre un RDV",
            },
        ]

        # ==============================================================
        # CREATE ARTICLE BLOCKS
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
        # SUCCESS MESSAGES
        # ==============================================================

        self.stdout.write(
            self.style.SUCCESS(
                "Article 'HTAP associées' created successfully."
            )
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"Article ID: {article.pk}"
            )
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"Blocks created: {len(blocks)}"
            )
        )


        # ==============================================================
        # TRANSLATION
        # ==============================================================

        translation, _ = ArticleTranslation.objects.get_or_create(
            article=article,
            language="ar",
            defaults={
                "title": "ارتفاع ضغط الدم الشرياني الرئوي المرتبط بأمراض أخرى",
                "excerpt": (
                    "معلومات حول أشكال ارتفاع ضغط الدم الشرياني الرئوي "
                    "المرتبطة بأمراض النسيج الضام وارتفاع ضغط الدم البابي "
                    "وفيروس نقص المناعة البشرية وأمراض القلب الخلقية."
                ),
                "meta_title": (
                    "ارتفاع ضغط الدم الشرياني الرئوي المرتبط بأمراض أخرى "
                    "| HTAP Algérie"
                ),
                "meta_description": (
                    "معلومات حول ارتفاع ضغط الدم الشرياني الرئوي المرتبط "
                    "بأمراض النسيج الضام وارتفاع ضغط الدم البابي وفيروس "
                    "نقص المناعة البشرية وأمراض القلب الخلقية."
                ),
            },
        )

        # ==============================================================
        # BLOCKS
        # ==============================================================

        blocks = [

            # ==========================================================
            # CONNECTIVITE
            # ==========================================================

            {
                "type": "heading",
                "title": "ارتفاع ضغط الدم الشرياني الرئوي المرتبط بأمراض النسيج الضام",
            },

            {
                "type": "paragraph",
                "text": (
                    "هو مرض ناتج عن اضطراب في جهاز المناعة، ويؤثر في "
                    "النسيج الداعم للجسم، المعروف باسم النسيج الضام."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "يمثل هذا النوع حوالي 15.3% من حالات ارتفاع ضغط الدم "
                    "الشرياني الرئوي ضمن المجموعة الأولى."
                ),
            },

            {
                "type": "heading",
                "title": "التصلب الجهازي (Sclérodermie systémique - ScS)",
            },

            {
                "type": "paragraph",
                "text": (
                    "التصلب الجهازي هو مرض مناعي ذاتي يؤثر في النسيج الضام "
                    "بشكل عام، ويتميز بشكل أساسي بتصلب وسماكة الجلد."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "يتميز التصلب الجهازي بحدوث تليف، أي إنتاج مفرط للكولاجين، "
                    "في الجلد والأوعية الدموية وكذلك في الأعضاء الداخلية، "
                    "مثل الجهاز الهضمي والرئتين والقلب والكليتين."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "يمثل التصلب الجهازي حوالي 11% من جميع أسباب ارتفاع ضغط "
                    "الدم الشرياني الرئوي، أي ما يقارب 600 إلى 800 مريض."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "تُعد ظاهرة رينو، التي تصبح فيها الأصابع بيضاء وباردة "
                    "وأحيانًا فاقدة للإحساس أو مخدرة، أول علامة للتصلب الجهازي."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "تتضافر ثلاثة آليات لزيادة المقاومة الوعائية الرئوية "
                    "في ارتفاع ضغط الدم الشرياني الرئوي المرتبط بالتصلب الجهازي: "
                    "تقبض الأوعية، وإعادة تشكيل الأوعية الرئوية، وحدوث "
                    "الخثار داخل الأوعية."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "يعتمد العلاج على الجمع بين الإجراءات العامة والعلاج "
                    "التقليدي، وعند المرضى المصنفين ضمن الفئة الوظيفية "
                    "NYHA II أو III أو IV، يمكن إضافة دواء يعمل على أحد "
                    "المسارات الأيضية الثلاثة: الإندوثيلين أو أكسيد النتريك "
                    "أو البروستاسيكلين."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "توصي الإرشادات الدولية بإجراء تحرٍ سنوي للكشف عن "
                    "ارتفاع ضغط الدم الشرياني الرئوي لدى جميع المرضى "
                    "المصابين بالتصلب الجهازي."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "يجب أن يعتمد هذا التحري على تخطيط صدى القلب واختبارات "
                    "وظائف التنفس، مما يسمح ببدء العلاج المناسب في وقت مبكر."
                ),
            },

            {
                "type": "heading",
                "title": "الذئبة الحمامية الجهازية",
            },

            {
                "type": "heading",
                "title": "مرض النسيج الضام المختلط (متلازمة شارب)",
            },

            # ==========================================================
            # PORTAL HYPERTENSION
            # ==========================================================

            {
                "type": "heading",
                "title": "ارتفاع ضغط الدم الشرياني الرئوي المرتبط بارتفاع ضغط الدم البابي",
            },

            {
                "type": "heading",
                "title": "ارتفاع ضغط الدم الرئوي البابي",
            },

            {
                "type": "paragraph",
                "text": (
                    "تُعد الاضطرابات الرئوية شائعة لدى المرضى المصابين "
                    "بأمراض الكبد. فحوالي ثلثي المرضى الذين يتم تقييمهم "
                    "من أجل زراعة الكبد يشكون من ضيق التنفس."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "ترتبط بعض هذه الاضطرابات بأمراض رئوية محددة ومستقلة "
                    "عن إصابة الكبد، مثل مرض الانسداد الرئوي المزمن والربو، "
                    "بينما تكون اضطرابات أخرى نتيجة مباشرة لقصور الكبد."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "وبالتالي، يمكن لوجود مرض كبدي أن يكون له تأثيرات "
                    "سلبية على الجهاز الوعائي الرئوي."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "يُعرّف ارتفاع ضغط الدم الرئوي البابي بأنه ارتفاع ضغط "
                    "الدم الشرياني الرئوي الذي يتطور في سياق وجود ارتفاع "
                    "ضغط الدم البابي. وغالبًا ما يكون ارتفاع ضغط الدم البابي "
                    "ناتجًا عن تشمع الكبد."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "ويُدرج ارتفاع ضغط الدم الرئوي البابي ضمن المجموعة الأولى "
                    "من تصنيف ارتفاع ضغط الدم الرئوي، لأنه يتميز بآليات "
                    "فيزيولوجية مرضية مشابهة لأشكال أخرى من ارتفاع ضغط الدم "
                    "الشرياني الرئوي."
                ),
            },

            # ==========================================================
            # EPIDEMIOLOGY
            # ==========================================================

            {
                "type": "heading",
                "title": "الوبائيات",
            },

            {
                "type": "paragraph",
                "text": (
                    "إن العلاقة بين ارتفاع ضغط الدم البابي وارتفاع ضغط الدم "
                    "الشرياني الرئوي معروفة جيدًا، وتُعتبر من الارتباطات "
                    "المحتملة جدًا."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "لدى المرضى المصابين بمرض كبدي مصحوب بارتفاع ضغط الدم "
                    "البابي، قد يكون ارتفاع ضغط الدم الرئوي المعتدل قليل "
                    "الأعراض شائعًا. ويرتبط ذلك بشكل أساسي بمتلازمة فرط "
                    "الديناميكية الدموية، أي ارتفاع النتاج القلبي، مما يؤدي "
                    "إلى ارتفاع سلبي في ضغط الدم الشرياني الرئوي."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "إلى جانب هذه الارتفاعات السلبية في الضغط الرئوي، توجد "
                    "حالات حقيقية من ارتفاع ضغط الدم الشرياني الرئوي، وهي "
                    "أقل شيوعًا، وترتبط بإعادة تشكيل الأوعية الدموية نتيجة "
                    "تكاثر الخلايا كما يحدث في ارتفاع ضغط الدم الشرياني "
                    "الرئوي مجهول السبب."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "يُقدّر أن حوالي 2% من المرضى المصابين بمرض كبدي متقدم "
                    "يعانون من ارتفاع ضغط الدم الرئوي البابي."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "وقد تصل النسبة إلى 3% إلى 5% لدى المرضى المصابين "
                    "بمرض كبدي شديد، وإلى حوالي 6% لدى المرضى المنتظرين "
                    "لزراعة الكبد."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "ويُلاحظ متوسط فترة تتراوح بين 4 و7 سنوات بين تشخيص "
                    "ارتفاع ضغط الدم البابي وتشخيص ارتفاع ضغط الدم الرئوي البابي."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "ووفقًا لبيانات السجل الفرنسي لارتفاع ضغط الدم الشرياني "
                    "الرئوي، يمثل ارتفاع ضغط الدم الرئوي البابي حوالي 17% "
                    "من أسباب ارتفاع ضغط الدم الشرياني الرئوي في فرنسا، "
                    "وهو السبب الثالث ضمن المجموعة الأولى."
                ),
            },

            # ==========================================================
            # DIAGNOSIS
            # ==========================================================

            {
                "type": "heading",
                "title": "من التعريف إلى التشخيص",
            },

            {
                "type": "paragraph",
                "text": (
                    "يعتمد تشخيص ارتفاع ضغط الدم الرئوي البابي على وجود عنصرين:"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "• وجود ارتفاع ضغط الدم الشرياني الرئوي، والذي يُعرّف "
                    "بمتوسط ضغط شرياني رئوي يتم قياسه بواسطة قسطرة القلب "
                    "اليمنى ويكون مساويًا أو أكبر من 25 ملم زئبق أثناء الراحة. "
                    "ويكون ارتفاع الضغط الرئوي هنا قبل الشعيرات الدموية، "
                    "مع ضغط انسداد رئوي يساوي أو يقل عن 15 ملم زئبق، "
                    "ويكون النتاج القلبي طبيعيًا أو منخفضًا، بينما تكون "
                    "المقاومة الوعائية الرئوية مرتفعة."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "• وجود ارتفاع ضغط الدم البابي، مع أو بدون وجود مرض كبدي. "
                    "إذ يمكن أن يحدث ارتفاع ضغط الدم الرئوي البابي بغض النظر "
                    "عن سبب ارتفاع ضغط الدم البابي وشدته."
                ),
            },

            # ==========================================================
            # PATHOPHYSIOLOGY
            # ==========================================================

            {
                "type": "heading",
                "title": "الفيزيولوجيا المرضية",
            },

            {
                "type": "paragraph",
                "text": (
                    "إن الآفات الوعائية الرئوية التي تُلاحظ لدى المرضى "
                    "المصابين بارتفاع ضغط الدم الرئوي البابي تشبه تلك "
                    "الملاحظة لدى المرضى المصابين بارتفاع ضغط الدم الشرياني "
                    "الرئوي مجهول السبب."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "يمكن لمرض الكبد، من خلال عدة آليات، أن يؤدي إلى إصابة "
                    "الدورة الدموية الرئوية، والتي قد تؤدي لدى بعض الأشخاص "
                    "المهيئين إلى إعادة تشكيل الأوعية الدموية وظهور ارتفاع "
                    "ضغط الدم الشرياني الرئوي تدريجيًا."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "في حالة تشمع الكبد، يحدث نقص في تصنيع عوامل كبدية "
                    "تثبط تكاثر الأوعية الدموية، والمعروفة بالعوامل "
                    "المضادة لتكوين الأوعية."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "وعلى العكس، قد يؤدي تشمع الكبد إلى زيادة تكاثر الخلايا "
                    "الوعائية الرئوية من خلال وسطاء يتم إطلاقهم في الدورة "
                    "الدموية الرئوية."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "كما قد تساهم زيادة تدفق الدم الرئوي الناتجة عن ارتفاع "
                    "ضغط الدم البابي في تنشيط بطانة الأوعية الرئوية من خلال "
                    "آلية إجهاد القص."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "وأخيرًا، فإن التغيرات التي تصيب الدورة الدموية البطنية "
                    "بسبب ارتفاع ضغط الدم البابي واضطرابات وظائف الكبد "
                    "الناتجة عن تشمع الكبد قد تسهّل انتقال البكتيريا ذات "
                    "المصدر الهضمي إلى الدورة الدموية، ثم تجنيد وتنشيط "
                    "الخلايا الالتهابية في الدورة الشريانية الرئوية."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "ومن المحتمل أن وجود استعداد وراثي لم يتم تحديده بعد "
                    "يفسر سبب إصابة أقلية فقط من المرضى المصابين بارتفاع "
                    "ضغط الدم البابي بارتفاع ضغط الدم الرئوي البابي."
                ),
            },

            # ==========================================================
            # CLINICAL MANIFESTATIONS
            # ==========================================================

            {
                "type": "heading",
                "title": "المظاهر السريرية",
            },

            {
                "type": "paragraph",
                "text": (
                    "يتمثل العرض الرئيسي في ضيق التنفس أثناء الجهد، "
                    "وتختلف شدته من شخص إلى آخر."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "ومع ذلك، قد لا يظهر ضيق التنفس في البداية لدى المرضى "
                    "الذين يكون نشاطهم البدني محدودًا، أو قد يختلط مع "
                    "الأعراض الناتجة عن وجود كمية غير طبيعية من السوائل "
                    "في تجويف البطن، أي الاستسقاء."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "يتفاقم ضيق التنفس تدريجيًا، وقد يصاحبه ألم صدري غير "
                    "نموذجي أو نوبات إغماء أثناء الجهد، والتي تُعد علامة "
                    "سريرية على شدة المرض."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "وقد تظهر أثناء الفحص السريري علامات قصور البطين الأيمن، "
                    "بالإضافة إلى العلامات الخاصة بمرض الكبد الأساسي."
                ),
            },

            # ==========================================================
            # EXAMS
            # ==========================================================

            {
                "type": "heading",
                "title": "الفحوصات الإضافية",
            },

            {
                "type": "heading",
                "title": "1. البحث عن ارتفاع ضغط الدم الرئوي بواسطة تخطيط صدى القلب",
            },

            {
                "type": "paragraph",
                "text": (
                    "يُعد تخطيط صدى القلب عبر جدار الصدر الفحص المرجعي "
                    "للاشتباه في ارتفاع ضغط الدم الرئوي البابي."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "وهو ضروري عند وجود ضيق التنفس أو قصور القلب الأيمن "
                    "لدى مريض يعاني من ارتفاع ضغط الدم البابي، كما يجب "
                    "إجراؤه بشكل منهجي ضمن تقييم المريض قبل زراعة الكبد."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "ويسمح بتقدير الضغط الشرياني الرئوي الانقباضي اعتمادًا "
                    "على السرعة القصوى لتدفق الارتجاع ثلاثي الشرفات باستخدام "
                    "الدوبلر."
                ),
            },

            {
                "type": "heading",
                "title": "2. تأكيد ارتفاع ضغط الدم الشرياني الرئوي بواسطة قسطرة القلب اليمنى",
            },

            {
                "type": "paragraph",
                "text": (
                    "يجب إجراء قسطرة القلب اليمنى عندما يُشتبه في وجود "
                    "ارتفاع ضغط الدم الشرياني الرئوي بواسطة تخطيط صدى القلب، "
                    "وخاصة عندما يُقدّر الضغط الرئوي الانقباضي بأكثر من "
                    "50 ملم زئبق."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "ويكتسب هذا التشخيص أهمية خاصة في سياق المرض الكبدي "
                    "المتقدم، لأن ارتفاع ضغط الدم الشرياني الرئوي يزيد "
                    "من المخاطر الجراحية وما بعد الجراحة في حالة زراعة الكبد."
                ),
            },

            {
                "type": "heading",
                "title": "3. فحوصات أخرى مفيدة",
            },

            {
                "type": "paragraph",
                "text": (
                    "يمكن أن تُظهر صورة الصدر بالأشعة السينية تضخم الشرايين "
                    "الرئوية وكذلك توسع حجرات القلب اليمنى."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "كما يُجرى اختبار المشي لمدة 6 دقائق لتقييم العجز "
                    "الوظيفي المرتبط بارتفاع ضغط الدم الرئوي البابي "
                    "بطريقة قابلة للتكرار."
                ),
            },

            # ==========================================================
            # TREATMENT
            # ==========================================================

            {
                "type": "heading",
                "title": "العلاج",
            },

            {
                "type": "paragraph",
                "text": (
                    "تتشابه الاستراتيجية العلاجية المستخدمة في علاج ارتفاع "
                    "ضغط الدم الرئوي البابي بشكل عام مع علاج ارتفاع ضغط "
                    "الدم الشرياني الرئوي مجهول السبب، مع وجود اعتبارات "
                    "خاصة بسبب المرض الكبدي المصاحب."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "لم يتمكن مرضى تشمع الكبد من المشاركة في معظم الدراسات "
                    "المستقبلية التي قيّمت العلاجات النوعية لارتفاع ضغط الدم "
                    "الشرياني الرئوي مجهول السبب."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "ومع ذلك، تشير الخبرة المكتسبة في مراكز علاج ارتفاع "
                    "ضغط الدم الشرياني الرئوي والبيانات المنشورة إلى فعالية "
                    "جيدة للعلاجات، على الأقل من حيث المؤشرات الوظيفية "
                    "والديناميكية الدموية، مع تحمل جيد بشكل عام."
                ),
            },

            {
                "type": "heading",
                "title": "العلاج التقليدي لارتفاع ضغط الدم الشرياني الرئوي",
            },

            {
                "type": "paragraph",
                "text": (
                    "لدى المرضى المصابين بتشمع الكبد، لا تُعطى مضادات التخثر "
                    "عادةً عندما يكون هناك قصور كبدي خلوي شديد و/أو انخفاض "
                    "في عدد الصفائح الدموية بسبب ارتفاع ضغط الدم البابي."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "وقد يكون العلاج بحاصرات بيتا، الذي يُستخدم بشكل متكرر "
                    "لدى مرضى تشمع الكبد للوقاية من النزيف الهضمي الناتج "
                    "عن تمزق دوالي المريء، ضارًا لأنه يقلل النتاج القلبي."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "ويُنصح باستخدام العلاج المدر للبول عند وجود وذمة "
                    "في الأطراف السفلية أو ارتفاع ضغط الأذين الأيمن أثناء "
                    "قسطرة القلب."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "كما يُوصى بالعلاج بالأكسجين عند وجود نقص في أكسجة الدم "
                    "يمكن أن يؤدي إلى تفاقم ارتفاع ضغط الدم الشرياني الرئوي."
                ),
            },

            {
                "type": "heading",
                "title": "العلاجات النوعية لارتفاع ضغط الدم الشرياني الرئوي",
            },

            {
                "type": "paragraph",
                "text": (
                    "تُستخدم العلاجات النوعية لارتفاع ضغط الدم الشرياني "
                    "الرئوي على نطاق واسع نسبيًا في حالات ارتفاع ضغط الدم "
                    "الرئوي البابي."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "يحسن العلاج المستمر عبر الوريد بالإيبوبروستينول "
                    "من ضيق التنفس والديناميكا الدموية. ويُعد علاجًا "
                    "مفضلًا في حالة الفئة الوظيفية IV أو للسماح بإجراء "
                    "زراعة الكبد لاحقًا."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "إلا أن هذا العلاج يتطلب وجود وصول وريدي مركزي دائم، "
                    "مما قد يعرض المريض لمضاعفات التهابية موضعية وعامة."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "كما أظهرت نظائر البروستاسيكلين المستقرة، التي تُعطى "
                    "بالاستنشاق أو بشكل مستمر تحت الجلد، تحسنًا سريريًا، "
                    "لكن البيانات طويلة الأمد لا تزال محدودة."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "ويكون استخدام مضادات مستقبلات الإندوثيلين-1 محدودًا "
                    "في سياق ارتفاع ضغط الدم الرئوي البابي بسبب احتمال "
                    "حدوث سمية كبدية."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "ومع ذلك، يمكن استخدام بعض هذه العلاجات لدى المرضى "
                    "المصابين بتشمع كبدي غير متقدم أو ارتفاع ضغط الدم البابي "
                    "دون وجود تشمع، مع ضرورة مراقبة وظائف الكبد بعناية."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "يمكن استخدام مثبطات الفوسفوديستيراز 5 مثل السيلدينافيل "
                    "والتادالافيل، مع تحمل جيد عادة لدى المرضى المصابين "
                    "بارتفاع ضغط الدم الرئوي البابي."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "ويجب تقييم الفائدة العلاجية بشكل فردي بعد مرور "
                    "3 إلى 4 أشهر من بدء العلاج."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "وتشمل الفوائد المتوقعة تحسن ضيق التنفس، ويفضل الوصول "
                    "إلى الفئة الوظيفية I أو II، وتحسن المسافة المقطوعة "
                    "خلال 6 دقائق لتتجاوز 450 إلى 500 متر، وتحسن المؤشرات "
                    "الديناميكية الدموية."
                ),
            },

            # ==========================================================
            # LIVER TRANSPLANT
            # ==========================================================

            {
                "type": "heading",
                "title": "زراعة الكبد",
            },

            {
                "type": "paragraph",
                "text": (
                    "لا يُعد ارتفاع ضغط الدم الرئوي البابي بحد ذاته "
                    "سببًا لإجراء زراعة الكبد، رغم تسجيل بعض حالات التحسن "
                    "بعد الزراعة."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "ولكن عندما تكون زراعة الكبد ضرورية بسبب شدة المرض "
                    "الكبدي نفسه، فإن ارتفاع ضغط الدم الشرياني الرئوي "
                    "الشديد يمثل مانعًا لإجراء الزراعة."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "وقد أمكن في بعض الحالات خفض الضغط الشرياني الرئوي "
                    "باستخدام مشتقات البروستاسيكلين، مما سمح بإجراء زراعة "
                    "الكبد لاحقًا في ظروف أكثر أمانًا."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "ويكون تطور ارتفاع ضغط الدم الرئوي البابي بعد زراعة "
                    "الكبد غير متوقع في كثير من الأحيان، وخاصة لدى المرضى "
                    "الذين احتاجوا إلى علاج طبي لارتفاع ضغط الدم الشرياني "
                    "الرئوي قبل الزراعة."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "ولهذا يجب مراقبة هؤلاء المرضى عن قرب خلال الفترة "
                    "المحيطة بالجراحة لتعديل العلاجات عند الحاجة."
                ),
            },

            # ==========================================================
            # CONCLUSION
            # ==========================================================

            {
                "type": "heading",
                "title": "الخلاصة",
            },

            {
                "type": "paragraph",
                "text": (
                    "يمثل ارتفاع ضغط الدم الرئوي البابي السبب الثالث "
                    "لارتفاع ضغط الدم الشرياني الرئوي في فرنسا، ويُلاحظ "
                    "لدى نحو 6% من المرضى المنتظرين لزراعة الكبد."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "وتبرر هذه النسبة ضرورة التحري عنه لدى كل مريض مصاب "
                    "بمرض كبدي ويعاني من ضيق تنفس غير مفسر، وكذلك لدى جميع "
                    "المرضى الذين يجب إدراجهم على قائمة زراعة الكبد."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "وتتشابه رعاية ارتفاع ضغط الدم الرئوي البابي بشكل عام "
                    "مع رعاية ارتفاع ضغط الدم الشرياني الرئوي مجهول السبب، "
                    "مع وجود اعتبارات خاصة مرتبطة بمرض الكبد الأساسي."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "وقد يؤدي ارتفاع ضغط الدم الرئوي البابي إلى تعقيد "
                    "الوصول إلى زراعة الكبد، ولذلك يتطلب في هذه الحالة "
                    "رعاية متعددة التخصصات تجمع بين اختصاصي أمراض الرئة "
                    "المتخصص في ارتفاع ضغط الدم الشرياني الرئوي واختصاصي الكبد."
                ),
            },

            # ==========================================================
            # HIV
            # ==========================================================

            {
                "type": "heading",
                "title": "ارتفاع ضغط الدم الشرياني الرئوي المرتبط بفيروس نقص المناعة البشرية",
            },

            {
                "type": "paragraph",
                "text": (
                    "يُعد ارتفاع ضغط الدم الشرياني الرئوي من المظاهر النادرة "
                    "لعدوى فيروس نقص المناعة البشرية، وهو مستقل عن درجة "
                    "نقص المناعة، لكنه يؤدي إلى تفاقم كبير في إنذار المرضى "
                    "المصابين بالفيروس."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "يمكن أن يصيب جميع الفئات المعرضة لخطر الإصابة بفيروس "
                    "نقص المناعة البشرية، إلا أن الأشخاص الذين يتعاطون "
                    "المخدرات كانوا الأكثر شيوعًا ضمن الحالات المذكورة "
                    "في المصدر."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "يُشخّص ارتفاع ضغط الدم الشرياني الرئوي في المتوسط بعد "
                    "2.5 إلى 3 سنوات من اكتشاف إيجابية المصل، لكنه قد يكون "
                    "أيضًا سببًا في اكتشاف العدوى، ولذلك يُنصح بإجراء اختبار "
                    "فيروس نقص المناعة البشرية ضمن التقييم الأولي لأي حالة "
                    "يُشتبه في أنها ارتفاع ضغط دم شرياني رئوي مجهول السبب."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "تكون الصورة السريرية مشابهة لارتفاع ضغط الدم الشرياني "
                    "الرئوي مجهول السبب، ويتم التشخيص بالطريقة نفسها، "
                    "أي بواسطة قسطرة القلب اليمنى."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "في الحالات التي لا تستجيب للعلاج التقليدي الأمثل، "
                    "يمكن أن يجمع العلاج بين مضادات الفيروسات القهقرية "
                    "والإيبوبروستينول، مع مراعاة المخاطر المرتبطة بالوصول "
                    "الوريدي المركزي والحالة المناعية للمريض."
                ),
            },

            # ==========================================================
            # CONGENITAL HEART DISEASE
            # ==========================================================

            {
                "type": "heading",
                "title": "ارتفاع ضغط الدم الشرياني الرئوي المرتبط بأمراض القلب الخلقية",
            },

            {
                "type": "paragraph",
                "text": (
                    "تمثل أمراض القلب الخلقية حوالي 13% من حالات ارتفاع "
                    "ضغط الدم الشرياني الرئوي."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "وتُعد أمراض القلب الخلقية من أكثر التشوهات الخلقية "
                    "شيوعًا، أي التشوهات التي تحدث أثناء التطور الجنيني "
                    "خلال الحمل، حيث تبلغ نسبة حدوثها حوالي 8 حالات لكل "
                    "1000 ولادة."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "وتتميز 60% من هذه التشوهات بوجود تحويلة دموية من "
                    "اليسار إلى اليمين، وهي الحالات التي يرتبط بها "
                    "ارتفاع ضغط الدم الشرياني الرئوي بشكل أكثر شيوعًا."
                ),
            },

            # ==========================================================
            # CTA
            # ==========================================================

            {
                "type": "heading",
                "title": "تحميل كتيب أمراض القلب الخلقية وارتفاع ضغط الدم الشرياني الرئوي بصيغة PDF",
            },

            {
                "type": "heading",
                "title": "Prendre un RDV",
            },
        ]

        # ==============================================================
        # CREATE BLOCKS
        # ==============================================================

        # Supprimer les anciens blocs de cette traduction
        ArticleBlock.objects.filter(
            translation=translation
        ).delete()

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
                "Arabic article created successfully."
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


        # ==============================================================
        # TRANSLATION
        # ==============================================================

        translation, _ = ArticleTranslation.objects.get_or_create(
            article=article,
            language="en",
            defaults={
                "title": "Associated PAH",
                "excerpt": (
                    "Information about pulmonary arterial hypertension "
                    "associated with connective tissue disease, portal "
                    "hypertension, HIV infection and congenital heart disease."
                ),
                "meta_title": "Associated PAH | HTAP Algérie",
                "meta_description": (
                    "Learn about pulmonary arterial hypertension associated "
                    "with connective tissue disease, portal hypertension, "
                    "HIV infection and congenital heart disease."
                ),
            },
        )

        # ==============================================================
        # BLOCKS
        # ==============================================================

        blocks = [

            # ==========================================================
            # ASSOCIATED PAH - CONNECTIVE TISSUE DISEASE
            # ==========================================================

            {
                "type": "heading",
                "title": "PAH associated with connective tissue disease",
            },

            {
                "type": "paragraph",
                "text": (
                    "Connective tissue disease is caused by a dysfunction "
                    "of the immune system that affects the supporting tissue "
                    "of the body, known as connective tissue."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "It represents approximately 15.3% of group 1 PAH."
                ),
            },

            {
                "type": "heading",
                "title": "Systemic sclerosis (SSc)",
            },

            {
                "type": "paragraph",
                "text": (
                    "Systemic sclerosis is an autoimmune disease that affects "
                    "connective tissue throughout the body. It is characterized "
                    "primarily by hardening and thickening of the skin."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Systemic sclerosis is characterized by fibrosis "
                    "(excessive production of collagen) affecting the skin, "
                    "blood vessels and internal organs, including the "
                    "gastrointestinal tract, lungs, heart and kidneys."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Systemic sclerosis represents approximately 11% of all "
                    "causes of PAH, corresponding to approximately 600 to "
                    "800 patients."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "The Raynaud phenomenon, in which the fingers become "
                    "white, cold and sometimes numb or insensitive, is often "
                    "the first sign of systemic sclerosis."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Three mechanisms contribute to increased pulmonary "
                    "vascular resistance in PAH associated with systemic "
                    "sclerosis: vasoconstriction, pulmonary vascular remodeling "
                    "and in-situ thrombosis."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Treatment is based on a combination of general measures "
                    "and conventional treatment. In patients in NYHA functional "
                    "class II, III or IV, a drug acting on one of the three "
                    "major metabolic pathways — endothelin, nitric oxide (NO) "
                    "or prostacyclin — may be added."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "International recommendations call for annual screening "
                    "for PAH in every patient with systemic sclerosis."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Screening should be based on echocardiography and "
                    "pulmonary function tests, allowing early initiation "
                    "of appropriate treatment."
                ),
            },

            {
                "type": "heading",
                "title": "Systemic lupus erythematosus",
            },

            {
                "type": "heading",
                "title": "Mixed connective tissue disease (Sharp syndrome)",
            },

            {
                "type": "paragraph",
                "text": (
                    "Download the PAH-Scleroderma document in PDF format."
                ),
            },

            # ==========================================================
            # PORTAL HYPERTENSION
            # ==========================================================

            {
                "type": "heading",
                "title": "PAH associated with portal hypertension",
            },

            {
                "type": "heading",
                "title": "Portopulmonary hypertension",
            },

            {
                "type": "paragraph",
                "text": (
                    "By Laurent Savale and Vincent Cottin."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Pulmonology Department – Reference Center for Severe "
                    "Pulmonary Hypertension, Bicêtre Hospital, AP-HP, "
                    "Le Kremlin-Bicêtre, France."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Hospices Civils de Lyon, Louis Pradel Hospital, "
                    "Pulmonology Department – National Reference Center "
                    "for Rare Pulmonary Diseases and Competence Center "
                    "for Pulmonary Arterial Hypertension, Lyon, France."
                ),
            },

            {
                "type": "heading",
                "title": "Introduction",
            },

            {
                "type": "paragraph",
                "text": (
                    "Pulmonary abnormalities are common in patients with "
                    "liver disease. Approximately two thirds of patients "
                    "being evaluated for liver transplantation report "
                    "dyspnea (shortness of breath)."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Some of these respiratory abnormalities are related to "
                    "specific pulmonary diseases that are independent of "
                    "liver disease, such as chronic obstructive pulmonary "
                    "disease or asthma, while others are directly related "
                    "to liver failure."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Therefore, the presence of liver disease can have "
                    "adverse effects on the pulmonary vascular system."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Portopulmonary hypertension (PoPH) is defined as "
                    "pulmonary arterial hypertension developing in the "
                    "context of portal hypertension."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Portal hypertension is most commonly caused by cirrhosis. "
                    "Portopulmonary hypertension is included in group 1 of "
                    "the pulmonary hypertension classification because it "
                    "has pathophysiological mechanisms similar to other "
                    "forms of PAH."
                ),
            },

            # ==========================================================
            # EPIDEMIOLOGY
            # ==========================================================

            {
                "type": "heading",
                "title": "Epidemiology",
            },

            {
                "type": "paragraph",
                "text": (
                    "The association between portal hypertension and PAH is "
                    "well established and is recognized as a highly probable "
                    "association."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "In patients with liver disease and portal hypertension, "
                    "moderate and mildly symptomatic pulmonary hypertension "
                    "(mean pulmonary arterial pressure below 35 mmHg with "
                    "high cardiac output) is common."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "It is mainly related to a hyperkinetic syndrome, with "
                    "increased cardiac output causing a passive elevation "
                    "of pulmonary arterial pressure while pulmonary vascular "
                    "resistance remains normal or low."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "In addition to these passive elevations in pulmonary "
                    "arterial pressure, true PAH can occur. It is less common "
                    "and is related to vascular remodeling caused by cellular "
                    "proliferation, as seen in idiopathic PAH."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Approximately 2% of patients with advanced liver disease "
                    "are estimated to develop portopulmonary hypertension."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "The frequency of portopulmonary hypertension may reach "
                    "3% to 5% among patients with severe liver disease and "
                    "approximately 6% among patients awaiting liver "
                    "transplantation."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "An average delay of 4 to 7 years is observed between "
                    "the diagnosis of portal hypertension and the diagnosis "
                    "of portopulmonary hypertension."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "According to data from the French PAH registry, "
                    "portopulmonary hypertension accounted for approximately "
                    "17% of PAH causes in France and represented the third "
                    "most common cause of group 1 PAH."
                ),
            },

            # ==========================================================
            # DIAGNOSIS
            # ==========================================================

            {
                "type": "heading",
                "title": "From definition to diagnosis",
            },

            {
                "type": "paragraph",
                "text": (
                    "The diagnosis of portopulmonary hypertension is based "
                    "on the combination of two elements:"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "• Pulmonary arterial hypertension, defined by a mean "
                    "pulmonary arterial pressure measured by right heart "
                    "catheterization of at least 25 mmHg at rest. The "
                    "pulmonary hypertension is precapillary, caused by an "
                    "abnormality of the pulmonary vasculature, with a pulmonary "
                    "artery wedge pressure of 15 mmHg or less. Cardiac output "
                    "is normal or reduced and pulmonary vascular resistance "
                    "is elevated.\n\n"
                    "• Portal hypertension, with or without liver disease. "
                    "Portopulmonary hypertension can occur independently of "
                    "the cause and severity of portal hypertension."
                ),
            },

            # ==========================================================
            # PATHOPHYSIOLOGY
            # ==========================================================

            {
                "type": "heading",
                "title": "Pathophysiology",
            },

            {
                "type": "paragraph",
                "text": (
                    "The pulmonary vascular lesions observed in patients "
                    "with portopulmonary hypertension are similar to those "
                    "observed in patients with idiopathic PAH."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Liver disease can affect the pulmonary circulation "
                    "through several mechanisms. In predisposed patients, "
                    "these mechanisms may promote vascular remodeling and "
                    "the progressive development of PAH."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "In cirrhosis, there is reduced hepatic production of "
                    "factors that inhibit vascular proliferation, known as "
                    "anti-angiogenic factors. Conversely, cirrhosis may "
                    "promote increased pulmonary vascular cell proliferation "
                    "through mediators released into the pulmonary circulation."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Increased pulmonary blood flow caused by portal hypertension "
                    "may contribute to activation of the pulmonary endothelium "
                    "through a shear-stress mechanism."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Finally, changes in abdominal circulation caused by portal "
                    "hypertension and abnormalities in liver function caused "
                    "by cirrhosis promote the passage of bacteria originating "
                    "from the digestive tract into the bloodstream, followed "
                    "by recruitment and activation of inflammatory cells in "
                    "the pulmonary arterial circulation."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "It is likely that an as-yet unidentified genetic "
                    "predisposition explains why only a minority of patients "
                    "with portal hypertension develop portopulmonary hypertension."
                ),
            },

            # ==========================================================
            # CLINICAL MANIFESTATIONS
            # ==========================================================

            {
                "type": "heading",
                "title": "Clinical manifestations",
            },

            {
                "type": "paragraph",
                "text": (
                    "The main symptom is exertional dyspnea of variable severity."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "However, dyspnea may initially be absent in patients "
                    "whose physical activity is limited, or it may be confused "
                    "with discomfort caused by abnormal accumulation of fluid "
                    "in the abdominal cavity (ascites)."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Dyspnea gradually worsens and may be accompanied by "
                    "atypical chest pain or exertional syncope, which is "
                    "considered a clinical marker of severity."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Clinical examination may reveal signs of right ventricular "
                    "failure. These clinical signs are added to those caused "
                    "by the underlying liver disease."
                ),
            },

            # ==========================================================
            # COMPLEMENTARY TESTS
            # ==========================================================

            {
                "type": "heading",
                "title": "Additional examinations",
            },

            {
                "type": "heading",
                "title": "1. Screening for pulmonary hypertension by echocardiography",
            },

            {
                "type": "paragraph",
                "text": (
                    "Transthoracic echocardiography is the reference examination "
                    "for screening for portopulmonary hypertension."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "It is necessary when a patient with portal hypertension "
                    "has shortness of breath or right heart failure and should "
                    "be performed routinely as part of the pre-liver-transplant "
                    "assessment."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "It allows estimation of systolic pulmonary arterial "
                    "pressure based on the maximum velocity of tricuspid "
                    "regurgitation measured by Doppler."
                ),
            },

            {
                "type": "heading",
                "title": "2. Confirming PAH by right heart catheterization",
            },

            {
                "type": "paragraph",
                "text": (
                    "Right heart catheterization should be performed when "
                    "PAH is suspected on echocardiography, particularly when "
                    "systolic pulmonary arterial pressure is estimated to "
                    "be above 50 mmHg."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "This diagnosis is often crucial in advanced liver disease "
                    "because PAH increases the operative and postoperative "
                    "risk associated with liver transplantation."
                ),
            },

            {
                "type": "heading",
                "title": "3. Other useful examinations",
            },

            {
                "type": "paragraph",
                "text": (
                    "A chest X-ray may show enlargement of the pulmonary "
                    "arteries and dilation of the right cardiac chambers."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "A six-minute walk test is performed to reproducibly "
                    "assess the functional limitation associated with "
                    "portopulmonary hypertension."
                ),
            },

            # ==========================================================
            # TREATMENT
            # ==========================================================

            {
                "type": "heading",
                "title": "Treatment",
            },

            {
                "type": "paragraph",
                "text": (
                    "The therapeutic strategy used to manage portopulmonary "
                    "hypertension is generally similar to that used for "
                    "idiopathic PAH, with specific considerations because "
                    "of the associated liver disease."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Patients with cirrhosis were not included in most "
                    "prospective studies evaluating specific treatments "
                    "for idiopathic PAH."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "However, experience from specialized PAH centers and "
                    "retrospective data from the literature suggest that "
                    "these treatments are effective, at least in terms of "
                    "functional and hemodynamic parameters, and are generally "
                    "well tolerated."
                ),
            },

            # ==========================================================
            # CONVENTIONAL TREATMENT
            # ==========================================================

            {
                "type": "heading",
                "title": "Conventional treatment of PAH",
            },

            {
                "type": "paragraph",
                "text": (
                    "In patients with cirrhosis, anticoagulants are generally "
                    "not administered when severe liver-cell dysfunction "
                    "and/or a reduction in platelet count caused by portal "
                    "hypertension is present."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Beta-blocker treatment, frequently prescribed in "
                    "cirrhotic patients to prevent gastrointestinal bleeding "
                    "from ruptured esophageal varices, may be harmful because "
                    "it reduces cardiac output."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Diuretic treatment is recommended in cases of lower-limb "
                    "edema or increased right atrial pressure measured during "
                    "catheterization."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Oxygen therapy is recommended when impaired oxygenation "
                    "is present and may worsen PAH."
                ),
            },

            # ==========================================================
            # SPECIFIC TREATMENTS
            # ==========================================================

            {
                "type": "heading",
                "title": "Specific PAH treatments",
            },

            {
                "type": "paragraph",
                "text": (
                    "Specific PAH treatments are widely used in portopulmonary "
                    "hypertension."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Continuous intravenous administration of epoprostenol "
                    "(prostacyclin – Flolan) improves dyspnea and hemodynamic "
                    "parameters."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "It is the treatment of choice in functional class IV "
                    "patients or when treatment is intended to allow subsequent "
                    "liver transplantation (bridge therapy)."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "However, this treatment is demanding and carries a risk "
                    "of local and systemic infectious complications related "
                    "to the permanent central venous access."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Clinical improvement has also been demonstrated with "
                    "stable prostacyclin analogues administered by inhalation "
                    "(iloprost – Ventavis) or by continuous subcutaneous "
                    "infusion (treprostinil – Remodulin), although long-term "
                    "data remain limited."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "The use of endothelin-1 receptor antagonists "
                    "(bosentan – Tracleer, ambrisentan – Volibris) is limited "
                    "in portopulmonary hypertension because of their potential "
                    "liver toxicity."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Nevertheless, bosentan or ambrisentan, whose liver toxicity "
                    "may be lower, can be considered in patients with mild "
                    "cirrhosis or portal hypertension without cirrhosis."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Particular care is required to ensure that liver function "
                    "does not deteriorate when this class of treatment is used."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Phosphodiesterase-5 inhibitors such as sildenafil "
                    "(Revatio) and tadalafil (Adcirca) can generally be used "
                    "with good tolerance in patients with portopulmonary "
                    "hypertension."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "However, these treatments could theoretically worsen "
                    "portal hypertension indirectly, making an individual "
                    "assessment of the therapeutic benefit necessary."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "A precise assessment of treatment benefit should be "
                    "performed individually 3 to 4 months after treatment "
                    "is initiated."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Expected benefits include improvement in dyspnea, ideally "
                    "to functional class I or II, improvement in the distance "
                    "walked during six minutes to more than 450–500 meters, "
                    "and hemodynamic improvement, including reduced pulmonary "
                    "vascular resistance and normalization of cardiac output."
                ),
            },

            # ==========================================================
            # LIVER TRANSPLANTATION
            # ==========================================================

            {
                "type": "heading",
                "title": "Liver transplantation",
            },

            {
                "type": "paragraph",
                "text": (
                    "Portopulmonary hypertension is not itself an indication "
                    "for liver transplantation, although several cases of "
                    "improvement after transplantation have been reported."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "However, when liver transplantation is indicated because "
                    "of the severity of the liver disease itself, severe PAH "
                    "(mean pulmonary arterial pressure above 35 mmHg and "
                    "pulmonary vascular resistance above 250 dyn·s·cm⁻⁵) "
                    "is considered a contraindication."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "In some cases, pulmonary arterial pressure can be reduced "
                    "using prostacyclin derivatives, allowing liver transplantation "
                    "to be performed subsequently under safer conditions."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "The course of portopulmonary hypertension after liver "
                    "transplantation is often unpredictable, particularly in "
                    "patients who required medical PAH treatment before "
                    "transplantation."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "These patients should therefore be closely monitored "
                    "during the perioperative period so that treatment can "
                    "be adjusted appropriately."
                ),
            },

            # ==========================================================
            # CONCLUSION
            # ==========================================================

            {
                "type": "heading",
                "title": "Conclusion",
            },

            {
                "type": "paragraph",
                "text": (
                    "Portopulmonary hypertension is the third most common "
                    "cause of PAH in France. It is found in approximately "
                    "6% of patients awaiting liver transplantation."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Its frequency justifies screening in every patient with "
                    "liver disease who has unexplained respiratory symptoms, "
                    "as well as in all patients being considered for liver "
                    "transplantation."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Management of portopulmonary hypertension is generally "
                    "similar to that of idiopathic PAH, although specific "
                    "considerations related to the underlying liver disease "
                    "must be taken into account."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Portopulmonary hypertension may complicate access to "
                    "liver transplantation and therefore requires multidisciplinary "
                    "management involving a pulmonologist specializing in "
                    "PAH and a hepatologist."
                ),
            },

            # ==========================================================
            # HIV
            # ==========================================================

            {
                "type": "heading",
                "title": "PAH associated with HIV infection",
            },

            {
                "type": "paragraph",
                "text": (
                    "PAH is a rare manifestation of HIV infection. It is "
                    "independent of the degree of immunosuppression but can "
                    "considerably worsen the prognosis of affected HIV-positive "
                    "patients."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "It can affect all groups at risk of HIV infection. "
                    "People who inject drugs have historically been among "
                    "the most frequently affected groups."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "PAH is diagnosed on average 2.5 to 3 years after HIV "
                    "infection is discovered, but it can also reveal the "
                    "infection. This is why HIV testing is recommended as "
                    "part of the initial assessment of apparently idiopathic PAH."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "The clinical presentation is similar to that of idiopathic "
                    "PAH, and diagnosis is performed in the same way, including "
                    "right heart catheterization."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "For PAH that remains refractory despite optimal conventional "
                    "treatment, including limitation of physical exertion, "
                    "oral anticoagulation when appropriate, diuretics and "
                    "oxygen when necessary, treatment generally combines "
                    "antiretroviral therapy with epoprostenol."
                ),
            },

            # ==========================================================
            # CONGENITAL HEART DISEASE
            # ==========================================================

            {
                "type": "heading",
                "title": "PAH associated with congenital heart disease",
            },

            {
                "type": "paragraph",
                "text": (
                    "Congenital heart diseases account for approximately "
                    "13% of PAH cases."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Congenital heart diseases are among the most common "
                    "congenital malformations, meaning abnormalities acquired "
                    "during embryonic development and pregnancy, with an "
                    "incidence of approximately 8 cases per 1,000 births."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Approximately 60% of these abnormalities are characterized "
                    "by a left-to-right shunt. PAH is most frequently associated "
                    "with these conditions."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Download the brochure: Congenital Heart Disease and PAH "
                    "in PDF format."
                ),
            },

            # ==========================================================
            # CTA
            # ==========================================================

            {
                "type": "heading",
                "title": "Make an appointment",
            },
        ]

        # ==============================================================
        # CREATE BLOCKS
        # ==============================================================

        # Remove existing blocks if this translation was previously created.
        ArticleBlock.objects.filter(
            translation=translation
        ).delete()

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
                "Associated PAH article created successfully."
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
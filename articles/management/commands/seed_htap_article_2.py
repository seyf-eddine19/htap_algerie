from django.core.management.base import BaseCommand
from django.utils import timezone

from articles.models import (
    Article,
    ArticleCategory,
    ArticleTranslation,
    ArticleBlock,
)


class Command(BaseCommand):
    help = "Create Article 02 - Diagnostic de l'HTAP"

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
            slug="diagnostic-htap",
        )

        # ==============================================================
        # TRANSLATION
        # ==============================================================

        translation = ArticleTranslation.objects.create(
            article=article,
            language="fr",
            title="Diagnostic de l'HTAP",
            excerpt=(
                "Découvrez les différentes classifications de l'hypertension "
                "pulmonaire, les examens permettant d'évaluer le fonctionnement "
                "du cœur et des poumons et les examens utilisés pour diagnostiquer "
                "et déterminer la cause de l'HTAP."
            ),
            meta_title="Diagnostic de l'HTAP | HTAP Algérie",
            meta_description=(
                "Informations sur le diagnostic de l'HTAP, les classifications "
                "de l'hypertension pulmonaire, les examens cardiaques et "
                "respiratoires et le cathétérisme cardiaque."
            ),
        )

        # ==============================================================
        # BLOCKS
        # ==============================================================

        blocks = [

            # ==========================================================
            # CLASSIFICATION
            # ==========================================================

            {
                "type": "heading",
                "title": "Les différentes classifications de l'hypertension pulmonaire",
            },

            {
                "type": "paragraph",
                "text": (
                    "L'HTAP peut avoir différentes origines et différentes "
                    "conséquences d'une personne à l'autre."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Les médecins proposent souvent un classement dans "
                    "différentes catégories."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Une classification de l'HTAP en fonction des causes "
                    "à l'origine de la maladie."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "L'origine du ralentissement de la circulation du sang "
                    "à l'intérieur des poumons peut être multiple."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Connaître l'origine de l'HTAP permet de choisir le "
                    "traitement le plus adapté à chaque personne."
                ),
            },

            {
                "type": "heading",
                "title": (
                    "Classification des Hypertensions Pulmonaires "
                    "(4th PH World Symposium – Dana Point, Californie – Février 2008)"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Il existe une classification suivant les causes où "
                    "l'HTAP est divisée en 5 catégories, elles-mêmes "
                    "découpées en sous-catégories."
                ),
            },

            # ==========================================================
            # GROUP 1
            # ==========================================================

            {
                "type": "heading",
                "title": "Hypertension Artérielle Pulmonaire – groupe 1",
            },

            {
                "type": "heading",
                "title": "HTAP dite idiopathique",
            },

            {
                "type": "paragraph",
                "text": (
                    "Désigne une HTAP qui survient de façon isolée, sans "
                    "raison ou circonstance favorisante connue."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Anciennement appelée HTAP primitive."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "La majorité des HTAP entre dans cette catégorie."
                ),
            },

            {
                "type": "heading",
                "title": "HTAP dite héréditaire",
            },

            {
                "type": "paragraph",
                "text": (
                    "Liée à la mutation d'un gène, le plus souvent le gène "
                    "BMPR2, avec un risque de transmission familiale."
                ),
            },

            {
                "type": "heading",
                "title": "HTAP induite par médicaments ou toxiques",
            },

            {
                "type": "paragraph",
                "text": (
                    "Liée essentiellement à une consommation de drogues et "
                    "de médicaments coupe-faim (anorexigènes) dérivés "
                    "d'amphétamines."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Fenfluramine et dérivés : Isoméride retiré du marché en 1997.\n"
                    "Benfluorex : Médiator retiré du marché en novembre 2009.\n"
                    "Attention aux dérivés type méthamphétamine "
                    "(stupéfiants type « ecstasy »)."
                ),
            },

            {
                "type": "heading",
                "title": (
                    "HTAP associée à une connectivite, à une hypertension "
                    "portale, à une cardiopathie congénitale, à une infection "
                    "par le VIH, autres"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Autres maladies pouvant être associées : maladies de "
                    "la thyroïde, maladie de Gaucher, maladie de l'hémoglobine, "
                    "maladie de Rendu-Osler…"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Certaines maladies sont des conditions favorisant l'HTAP."
                ),
            },

            {
                "type": "heading",
                "title": "HTP persistante du nouveau-né",
            },

            {
                "type": "paragraph",
                "text": (
                    "Dans laquelle les artérioles ne se dilatent pas à la "
                    "naissance comme elles devraient le faire normalement."
                ),
            },

            # ==========================================================
            # GROUP 1'
            # ==========================================================

            {
                "type": "heading",
                "title": (
                    "Maladie veino-occlusive pulmonaire et hémangiome "
                    "capillaire pulmonaire – groupe 1'"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Associée à une pathologie veineuse ou des vaisseaux "
                    "capillaires, qui affecte en fait les veines et veinules "
                    "pulmonaires et non les artérioles mais qui donne les "
                    "mêmes symptômes."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "C’est une forme très rare de l’HTAP."
                ),
            },

            # ==========================================================
            # GROUP 2
            # ==========================================================

            {
                "type": "heading",
                "title": (
                    "Hypertension Pulmonaire associée à une cardiopathie "
                    "gauche – groupe 2"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Lorsqu’elle est la conséquence d'une maladie ou "
                    "malformation du cœur gauche."
                ),
            },

            # ==========================================================
            # GROUP 3
            # ==========================================================

            {
                "type": "heading",
                "title": (
                    "Hypertension Pulmonaire associée à une maladie pulmonaire "
                    "et/ou une hypoxémie chronique – groupe 3"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Bronchopathie pulmonaire chronique obstructive (BPCO), "
                    "syndrome d'apnée du sommeil, maladies interstitielles "
                    "pulmonaires, exposition chronique aux hautes altitudes."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Lorsqu’elle est associée à des maladies respiratoires "
                    "responsables d'une mauvaise aération du sang."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "En général ce type d'HTAP est modéré (s'accompagne "
                    "rarement de conséquences graves)."
                ),
            },

            # ==========================================================
            # GROUP 4
            # ==========================================================

            {
                "type": "heading",
                "title": (
                    "Hypertension Pulmonaire post-embolique chronique – groupe 4"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Lorsque les artères des poumons se bouchent avec des "
                    "petits caillots de sang, ces caillots s'organisent et "
                    "obstruent définitivement les vaisseaux."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "La chirurgie peut guérir complètement ces patients "
                    "(endartériectomie pulmonaire)."
                ),
            },

            # ==========================================================
            # GROUP 5
            # ==========================================================

            {
                "type": "heading",
                "title": (
                    "Hypertension Pulmonaire de mécanisme multifactoriel "
                    "ou incertain – groupe 5"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Sarcoïdose, histiocytose X, lymphangiomyomatose, "
                    "compression des vaisseaux pulmonaires."
                ),
            },

            # ==========================================================
            # FUNCTIONAL CLASSIFICATION
            # ==========================================================

            {
                "type": "paragraph",
                "text": (
                    "L'HTAP peut avoir différentes origines et différentes "
                    "conséquences d'une personne à l'autre."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Les médecins proposent souvent un classement dans "
                    "différentes catégories."
                ),
            },

            {
                "type": "heading",
                "title": (
                    "Une classification de l'HTAP en fonction de ses "
                    "conséquences sur la santé"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "L'HTAP peut être classée en 4 classes suivant ses "
                    "manifestations les plus courantes (plus la classe est "
                    "élevée, plus les manifestations de l'HTAP sont importantes)."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "On parle de classes fonctionnelles."
                ),
            },

            {
                "type": "image",
                "image": "articles/source/231.png",
                "image_caption": "Classification fonctionnelle de l'HTAP.",
            },

            # ==========================================================
            # EXAMS HEART / LUNGS
            # ==========================================================

            {
                "type": "heading",
                "title": (
                    "Les examens pour mesurer le fonctionnement du cœur "
                    "et des poumons"
                ),
            },

            # ----------------------------------------------------------
            # CATHETERISM
            # ----------------------------------------------------------

            {
                "type": "heading",
                "title": "Le cathétérisme cardiaque",
            },

            {
                "type": "paragraph",
                "text": (
                    "Le cathétérisme doit rester l'examen de référence dans "
                    "le diagnostic de l'HTAP. C'est la raison pour laquelle "
                    "nous lui consacrons un chapitre dédié."
                ),
            },

            # ----------------------------------------------------------
            # ECG
            # ----------------------------------------------------------

            {
                "type": "heading",
                "title": "L'électro-cardiogramme",
            },

            {
                "type": "paragraph",
                "text": (
                    "Des électrodes sont placées sur le torse pour mesurer "
                    "l'activité électrique du cœur afin d'illustrer sur un "
                    "graphe le rythme et l'intensité des contractions du cœur."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Cet examen peut illustrer des signes d'hypertrophie du "
                    "ventricule droit du cœur (le ventricule droit augmente "
                    "de volume en raison du sang qui s'accumule en amont "
                    "des poumons)."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "L'électrocardiogramme peut être fait allongé(e) ou pendant "
                    "un effort sur un tapis roulant (ou un vélo d'appartement)."
                ),
            },

            # ----------------------------------------------------------
            # CHEST X-RAY
            # ----------------------------------------------------------

            {
                "type": "heading",
                "title": "La radiographie pulmonaire",
            },

            {
                "type": "paragraph",
                "text": (
                    "Une photographie des poumons est réalisée à l'aide de "
                    "rayons X. Sur l'image, on peut reconnaître des signes "
                    "caractéristiques d'une augmentation du volume "
                    "(dilatation) des artères pulmonaires."
                ),
            },

            # ----------------------------------------------------------
            # ECHOCARDIOGRAM
            # ----------------------------------------------------------

            {
                "type": "heading",
                "title": (
                    "L'échographie cardiaque (ou échocardiogramme)"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Un émetteur est placé sur la poitrine pour envoyer des "
                    "ondes sonores (des ultrasons que l'homme ne peut pas "
                    "entendre) vers le cœur."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Ces ondes « rebondissent » (par échos) sur le cœur et "
                    "peuvent être à nouveau captées à l'extérieur."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Ces ondes permettent alors d'obtenir des images des "
                    "battements du cœur (sur papier ou vidéo). Ces images "
                    "permettent de mesurer la taille du cœur et l'épaisseur "
                    "du muscle cardiaque."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Cet examen peut illustrer une augmentation du volume "
                    "du ventricule droit (hypertrophie et dilatation)."
                ),
            },

            # ----------------------------------------------------------
            # PFT
            # ----------------------------------------------------------

            {
                "type": "heading",
                "title": "Les épreuves fonctionnelles respiratoires (EFR)",
            },

            {
                "type": "paragraph",
                "text": (
                    "Il s'agit d'examens classiques pour mesurer les principales "
                    "caractéristiques de la respiration (telle que la quantité "
                    "d'air qui est échangée avec l'extérieur)."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Les EFR font appel à plusieurs types d'instruments de "
                    "mesure. Le plus souvent il s'agit de respirer (inspirer) "
                    "ou de souffler (expirer) par une embouchure reliée à "
                    "un tuyau."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Le tuyau est connecté à une machine où des courbes sont "
                    "réalisées sur un écran pour illustrer les caractéristiques "
                    "de votre respiration."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "En général, il faut se boucher le nez à l'aide d'un "
                    "pince-nez pour que l'air passe entièrement par l'instrument."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Souvent les personnes qui souffrent d'HTAP échangent "
                    "moins d'air avec l'extérieur."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Ces tests peuvent permettre au médecin de dépister "
                    "certaines maladies respiratoires comme une bronchite "
                    "chronique ou une fibrose pulmonaire."
                ),
            },

            # ==========================================================
            # WALK TEST
            # ==========================================================

            {
                "type": "heading",
                "title": "Le test de Marche",
            },

            {
                "type": "paragraph",
                "text": (
                    "Il s'agit de mesurer la distance qu'un sujet peut "
                    "parcourir en marchant normalement pendant 6 minutes."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Le plus souvent il s'agit de faire des allers-retours "
                    "dans un couloir de 50 mètres."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Cet examen permet de mesurer si l'on doit faire des "
                    "pauses ou si la personne est essoufflée."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Parfois, un petit appareil appelé oxymètre de pouls "
                    "est placé au bout du doigt pour mesurer si le sang est "
                    "suffisamment oxygéné pendant l'effort."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Le test de marche est utile en matière de suivi pour "
                    "savoir si l'HTAP s'améliore ou non en fonction de "
                    "votre traitement."
                ),
            },

            {
                "type": "heading",
                "title": (
                    "En quoi consiste le test de marche et que permet-il "
                    "d'apprécier ?"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Le test de marche consiste à mesurer la distance "
                    "maximale parcourue en marchant normalement sur une "
                    "période de 6 minutes."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Dans des conditions normales, chez une personne "
                    "n'ayant pas d'HTAP, cette distance est de plus de "
                    "600 mètres."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "En pratique, le test de marche permet d'évaluer de "
                    "façon assez précise la classe fonctionnelle où se "
                    "situe le patient :"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Classe IV : de 0 à 250 mètres\n"
                    "Classe III : de 250 à 450 mètres\n"
                    "Classe II : de 450 à 550 mètres\n"
                    "Classe I : de 550 à 600 mètres"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Attention : ces valeurs ne sont données qu'à titre "
                    "indicatif et sont évaluées par le médecin en fonction "
                    "de chaque personne (selon l'âge, caractéristiques "
                    "corporelles...)."
                ),
            },

            # ==========================================================
            # WALK TEST IMAGES
            # ==========================================================

            {
                "type": "image",
                "image": "articles/source/4.jpg",
                "image_caption": "Illustration du test de marche.",
            },

            {
                "type": "image",
                "image": "articles/source/3.jpg",
                "image_caption": "Illustration du test de marche.",
            },

            {
                "type": "image",
                "image": "articles/source/1.jpg",
                "image_caption": "Illustration du test de marche.",
            },

            {
                "type": "image",
                "image": "articles/source/2.jpg",
                "image_caption": "Illustration du test de marche.",
            },

            {
                "type": "image",
                "image": "articles/source/4.gif",
                "image_caption": "Illustration du test de marche.",
            },

            # ==========================================================
            # CARDIAC CATHETERIZATION
            # ==========================================================

            {
                "type": "heading",
                "title": (
                    "L'examen pour diagnostiquer l'HTAP : "
                    "le cathétérisme cardiaque"
                ),
            },

            {
                "type": "heading",
                "title": "Réalisation",
            },

            {
                "type": "paragraph",
                "text": (
                    "Cet examen est généralement pratiqué à l'aide d'un "
                    "cathéter pulmonaire (sonde) de type Swan Ganz qui "
                    "permet la mesure de :"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "• la pression artérielle pulmonaire ;\n"
                    "• la pression auriculaire gauche ;\n"
                    "• la pression auriculaire droite ;\n"
                    "• le débit sanguin pulmonaire ;\n"
                    "• l'analyse des gaz du sang veineux."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Ces mesures sont utiles à l'établissement d'un pronostic."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Une petite sonde est introduite à partir d'une veine "
                    "dite fémorale (située en haut des cuisses au niveau du "
                    "pli de l'aine), ou bien à partir de la veine sous-clavière "
                    "(située dans le creux juste au-dessus de la clavicule), "
                    "ou encore à partir de la veine jugulaire (située à la "
                    "face latérale du cou) pour remonter jusqu'au cœur puis "
                    "jusqu'aux artères pulmonaires."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Cette sonde permet de mesurer la pression du sang à "
                    "l'intérieur des artères pulmonaires."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Il s'agit d'un examen clé pour savoir si on a ou pas "
                    "une HTAP."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Il peut ensuite être réalisé régulièrement pour savoir "
                    "si le traitement est efficace (ce traitement vise à "
                    "réduire la pression du sang dans les artères)."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Dans l'HTAP : le profil hémodynamique moyen est "
                    "caractérisé par :"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "• une pression artérielle pulmonaire dépassant en moyenne "
                    "le triple de la limite supérieure de la normale,\n"
                    "• un faible (ou « bas ») débit cardiaque,\n"
                    "• une pression auriculaire gauche normale,\n"
                    "• une pression auriculaire droite à la limite supérieure "
                    "de la normale."
                ),
            },

            {
                "type": "image",
                "image": "articles/source/htap32.jpg",
                "image_caption": "Illustration du cathétérisme cardiaque.",
            },

            # ==========================================================
            # CAUSE EXAMS
            # ==========================================================

            {
                "type": "heading",
                "title": (
                    "Les examens pour déterminer la cause de l'HTAP"
                ),
            },

            # ----------------------------------------------------------
            # PULMONARY ANGIOGRAPHY
            # ----------------------------------------------------------

            {
                "type": "heading",
                "title": "L'angiographie pulmonaire",
            },

            {
                "type": "paragraph",
                "text": (
                    "Un liquide opaque aux rayons X est injecté dans les "
                    "veines, puis une radiographie est rapidement réalisée "
                    "pour obtenir une image du cœur et des artères pulmonaires."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Cet examen permet de visualiser les artères pulmonaires "
                    "droite et gauche."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Cet examen peut permettre de vérifier que l’HTAP n’est "
                    "pas due à des caillots bouchant les artères pulmonaires."
                ),
            },

            # ----------------------------------------------------------
            # LUNG SCINTIGRAPHY
            # ----------------------------------------------------------

            {
                "type": "heading",
                "title": "La scintigraphie pulmonaire",
            },

            {
                "type": "paragraph",
                "text": (
                    "Une substance radioactive est injectée dans les veines, "
                    "puis un scanner des poumons est rapidement réalisé pour "
                    "mesurer le déplacement de la radioactivité dans les poumons."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Cet examen permet de visualiser si la circulation du "
                    "sang est ralentie ou devenue impossible dans des parties "
                    "des poumons en raison de caillots qui bouchent certaines "
                    "petites artères."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Cet examen permet de savoir si l'HTAP est due ou non "
                    "à la formation de caillots de sang dans les poumons."
                ),
            },

            {
                "type": "image",
                "image": "articles/source/1.jpg",
                "image_caption": "Illustration de la scintigraphie pulmonaire.",
            },

            {
                "type": "image",
                "image": "articles/source/2.jpg",
                "image_caption": "Illustration de la scintigraphie pulmonaire.",
            },

            # ----------------------------------------------------------
            # EFR
            # ----------------------------------------------------------

            {
                "type": "heading",
                "title": "Les EFR",
            },

            {
                "type": "paragraph",
                "text": (
                    "Les épreuves fonctionnelles respiratoires peuvent "
                    "identifier certaines maladies respiratoires "
                    "(bronchite chronique…)."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Dans ce cas, cela peut permettre d'identifier une "
                    "HTAP dite à « hypoxie chronique »."
                ),
            },

            # ----------------------------------------------------------
            # AUTOIMMUNE DISEASE
            # ----------------------------------------------------------

            {
                "type": "heading",
                "title": "La recherche d'une maladie auto-immune",
            },

            {
                "type": "paragraph",
                "text": (
                    "Des analyses d'une prise de sang sont effectuées pour "
                    "rechercher s'il y a ou non dans le sang des marqueurs "
                    "caractéristiques de maladies auto-immunes qui pourraient "
                    "être associées à l'HTAP."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Il peut s'agir d'une sclérodermie, d'un lupus érythémateux "
                    "disséminé, de maladies thyroïdiennes auto-immunes…"
                ),
            },

            # ----------------------------------------------------------
            # BIOPSY
            # ----------------------------------------------------------

            {
                "type": "heading",
                "title": "La biopsie",
            },

            {
                "type": "paragraph",
                "text": (
                    "Si les examens précédemment cités ne permettent pas de "
                    "déterminer l'origine de l'HTAP, il est utile de réaliser "
                    "une biopsie."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Il s'agit de prélever sous anesthésie quelques cellules "
                    "de poumons qui seront analysées au microscope pour "
                    "permettre de définir l'origine de l'HTAP."
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
                "Article 'Diagnostic de l'HTAP' created successfully."
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

        translation = ArticleTranslation.objects.create(
            article=article,
            language="ar",
            title="تشخيص ارتفاع ضغط الدم الشرياني الرئوي",
            excerpt=(
                "التعرف على تصنيفات ارتفاع ضغط الدم الرئوي، "
                "والفحوصات المستخدمة لتشخيص ارتفاع ضغط الدم الشرياني الرئوي "
                "وتحديد أسبابه."
            ),
            meta_title="تشخيص ارتفاع ضغط الدم الشرياني الرئوي | HTAP Algérie",
            meta_description=(
                "معلومات حول تشخيص ارتفاع ضغط الدم الشرياني الرئوي، "
                "تصنيفاته، الفحوصات المستخدمة لتقييم القلب والرئتين، "
                "والفحوصات التي تساعد على تحديد سبب المرض."
            ),
        )

        blocks = [

            # ==========================================================
            # INTRODUCTION
            # ==========================================================

            {
                "type": "heading",
                "title": (
                    "تشخيص ارتفاع ضغط الدم الشرياني الرئوي"
                ),
            },

            {
                "type": "heading",
                "title": (
                    "التصنيفات المختلفة لارتفاع ضغط الدم الرئوي"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "يمكن أن تكون لارتفاع ضغط الدم الشرياني الرئوي "
                    "أسباب مختلفة وعواقب مختلفة من شخص إلى آخر."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "غالبًا ما يقترح الأطباء تصنيف المرض ضمن فئات مختلفة."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "يمكن تصنيف ارتفاع ضغط الدم الشرياني الرئوي "
                    "وفقًا للأسباب التي أدت إلى ظهور المرض."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "يمكن أن يكون سبب تباطؤ تدفق الدم داخل الرئتين متعددًا."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "إن معرفة سبب ارتفاع ضغط الدم الشرياني الرئوي "
                    "تساعد على اختيار العلاج الأنسب لكل شخص."
                ),
            },

            # ==========================================================
            # CLASSIFICATION
            # ==========================================================

            {
                "type": "heading",
                "title": (
                    "تصنيف ارتفاع ضغط الدم الرئوي "
                    "(الندوة العالمية الرابعة لارتفاع ضغط الدم الرئوي "
                    "– دانا بوينت، كاليفورنيا – فبراير 2008)"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "يوجد تصنيف يعتمد على الأسباب، حيث يُقسّم ارتفاع "
                    "ضغط الدم الرئوي إلى خمس فئات، تنقسم بدورها إلى "
                    "فئات فرعية."
                ),
            },

            # ==========================================================
            # GROUP 1
            # ==========================================================

            {
                "type": "heading",
                "title": (
                    "ارتفاع ضغط الدم الشرياني الرئوي – المجموعة الأولى"
                ),
            },

            {
                "type": "heading",
                "title": (
                    "ارتفاع ضغط الدم الشرياني الرئوي مجهول السبب"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "يشير إلى ارتفاع ضغط الدم الشرياني الرئوي الذي يظهر "
                    "بشكل معزول، دون وجود سبب أو ظرف محفز معروف."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "كان يُعرف سابقًا باسم ارتفاع ضغط الدم الشرياني "
                    "الرئوي الأولي."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "وتندرج غالبية حالات ارتفاع ضغط الدم الشرياني الرئوي "
                    "ضمن هذه الفئة."
                ),
            },

            {
                "type": "heading",
                "title": (
                    "ارتفاع ضغط الدم الشرياني الرئوي الوراثي"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "يرتبط بحدوث طفرة في أحد الجينات، وغالبًا ما يكون "
                    "ذلك في جين BMPR2، مع وجود خطر انتقال المرض داخل الأسرة."
                ),
            },

            {
                "type": "heading",
                "title": (
                    "ارتفاع ضغط الدم الشرياني الرئوي الناجم عن الأدوية أو المواد السامة"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "يرتبط بشكل أساسي باستهلاك بعض المخدرات وبعض الأدوية "
                    "المثبطة للشهية (مضادات فقدان الشهية) المشتقة من الأمفيتامينات."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "فينفلورامين ومشتقاته: إيزوميريد، الذي تم سحبه من السوق سنة 1997."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "بنفلوريكس: ميدياتور، الذي تم سحبه من السوق في نوفمبر 2009."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "تنبيه إلى المشتقات من نوع الميثامفيتامين "
                    "(المخدرات مثل «الإكستاسي»)."
                ),
            },

            {
                "type": "heading",
                "title": (
                    "ارتفاع ضغط الدم الشرياني الرئوي المرتبط بأمراض أخرى"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "يمكن أن يرتبط ارتفاع ضغط الدم الشرياني الرئوي "
                    "بأمراض النسيج الضام، أو ارتفاع ضغط الدم البابي، "
                    "أو أمراض القلب الخلقية، أو الإصابة بفيروس نقص المناعة "
                    "البشرية، أو أمراض أخرى مثل أمراض الغدة الدرقية، "
                    "ومرض غوشيه، وأمراض الهيموغلوبين، ومرض راندو-أوسلر."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "تُعد بعض الأمراض من الحالات التي قد تهيئ لظهور "
                    "ارتفاع ضغط الدم الشرياني الرئوي."
                ),
            },

            {
                "type": "heading",
                "title": (
                    "ارتفاع ضغط الدم الرئوي المستمر عند حديثي الولادة"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "تكون فيه الشُعيرات أو الشُرينات الرئوية غير قادرة "
                    "على التوسع عند الولادة كما ينبغي أن يحدث بشكل طبيعي."
                ),
            },

            # ==========================================================
            # GROUP 1'
            # ==========================================================

            {
                "type": "heading",
                "title": (
                    "مرض الانسداد الوريدي الرئوي والورم الوعائي الشعيري الرئوي "
                    "– المجموعة 1'"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "يرتبط بمرض يصيب الأوردة أو الأوعية الشعرية، ويؤثر "
                    "في الواقع على الأوردة والأوردة الدقيقة الرئوية "
                    "وليس على الشُرينات، لكنه يؤدي إلى الأعراض نفسها."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "وهو شكل نادر جدًا من ارتفاع ضغط الدم الشرياني الرئوي."
                ),
            },

            # ==========================================================
            # GROUP 2
            # ==========================================================

            {
                "type": "heading",
                "title": (
                    "ارتفاع ضغط الدم الرئوي المرتبط بأمراض القلب الأيسر "
                    "– المجموعة الثانية"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "يحدث عندما يكون ارتفاع ضغط الدم الرئوي نتيجة "
                    "مرض أو تشوه في الجزء الأيسر من القلب."
                ),
            },

            # ==========================================================
            # GROUP 3
            # ==========================================================

            {
                "type": "heading",
                "title": (
                    "ارتفاع ضغط الدم الرئوي المرتبط بأمراض الرئة "
                    "و/أو نقص الأكسجة المزمن – المجموعة الثالثة"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "مثل مرض الانسداد الرئوي المزمن (BPCO)، "
                    "ومتلازمة انقطاع التنفس أثناء النوم، "
                    "وأمراض الرئة الخلالية، والتعرض المزمن للمرتفعات."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "يحدث عندما يكون ارتفاع ضغط الدم الرئوي مرتبطًا "
                    "بأمراض تنفسية مسؤولة عن سوء أكسجة الدم."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "بشكل عام، يكون هذا النوع من ارتفاع ضغط الدم الرئوي "
                    "معتدلًا، ونادرًا ما تكون له عواقب خطيرة."
                ),
            },

            # ==========================================================
            # GROUP 4
            # ==========================================================

            {
                "type": "heading",
                "title": (
                    "ارتفاع ضغط الدم الرئوي المزمن التالي للانصمام "
                    "– المجموعة الرابعة"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "يحدث عندما تنسد شرايين الرئتين بجلطات دموية صغيرة، "
                    "ثم تتنظم هذه الجلطات وتؤدي إلى انسداد دائم للأوعية."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "يمكن للجراحة أن تشفي هؤلاء المرضى بشكل كامل "
                    "(استئصال بطانة الشريان الرئوي)."
                ),
            },

            # ==========================================================
            # GROUP 5
            # ==========================================================

            {
                "type": "heading",
                "title": (
                    "ارتفاع ضغط الدم الرئوي ذو الآلية متعددة العوامل "
                    "أو غير المؤكدة – المجموعة الخامسة"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "مثل الساركويد، وكثرة المنسجات X، "
                    "والورم العضلي اللمفي، وانضغاط الأوعية الرئوية."
                ),
            },

            # ==========================================================
            # FUNCTIONAL CLASSIFICATION
            # ==========================================================

            {
                "type": "paragraph",
                "text": (
                    "يمكن أن تكون لارتفاع ضغط الدم الشرياني الرئوي "
                    "أسباب مختلفة وعواقب مختلفة من شخص إلى آخر."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "وغالبًا ما يقترح الأطباء تصنيف المرض ضمن فئات مختلفة."
                ),
            },

            {
                "type": "heading",
                "title": (
                    "تصنيف ارتفاع ضغط الدم الشرياني الرئوي "
                    "وفقًا لتأثيراته على الصحة"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "يمكن تصنيف ارتفاع ضغط الدم الشرياني الرئوي إلى "
                    "أربع درجات وفقًا لأكثر مظاهره شيوعًا. وكلما ارتفعت "
                    "الدرجة، كانت مظاهر المرض أكثر أهمية."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "ويُطلق على هذه الدرجات اسم الفئات الوظيفية."
                ),
            },

            {
                "type": "image",
                "image": "articles/source/231.png",
                "image_caption": (
                    "الفئات الوظيفية لارتفاع ضغط الدم الشرياني الرئوي."
                ),
            },

            # ==========================================================
            # HEART AND LUNG TESTS
            # ==========================================================

            {
                "type": "heading",
                "title": (
                    "الفحوصات المستخدمة لقياس وظيفة القلب والرئتين"
                ),
            },

            {
                "type": "heading",
                "title": "قسطرة القلب",
            },

            {
                "type": "paragraph",
                "text": (
                    "تبقى قسطرة القلب الفحص المرجعي في تشخيص ارتفاع ضغط "
                    "الدم الشرياني الرئوي. ولهذا السبب نخصص لها فصلًا خاصًا."
                ),
            },

            {
                "type": "heading",
                "title": "تخطيط كهربية القلب",
            },

            {
                "type": "paragraph",
                "text": (
                    "توضع أقطاب على الصدر لقياس النشاط الكهربائي للقلب، "
                    "وذلك لعرض إيقاع وقوة انقباضات القلب على رسم بياني."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "يمكن لهذا الفحص أن يُظهر علامات تضخم البطين الأيمن "
                    "للقلب، حيث يزداد حجم البطين الأيمن نتيجة تراكم الدم "
                    "في الاتجاه السابق للرئتين."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "يمكن إجراء تخطيط كهربية القلب أثناء الاستلقاء أو "
                    "أثناء بذل جهد على جهاز المشي أو الدراجة الثابتة."
                ),
            },

            # ==========================================================
            # CHEST X-RAY
            # ==========================================================

            {
                "type": "heading",
                "title": "الأشعة السينية للصدر",
            },

            {
                "type": "paragraph",
                "text": (
                    "يتم تصوير الرئتين باستخدام الأشعة السينية. "
                    "ويمكن في الصورة التعرف على علامات مميزة لزيادة "
                    "حجم أو توسع الشرايين الرئوية."
                ),
            },

            # ==========================================================
            # ECHOCARDIOGRAPHY
            # ==========================================================

            {
                "type": "heading",
                "title": "تصوير القلب بالموجات فوق الصوتية (الإيكو)",
            },

            {
                "type": "paragraph",
                "text": (
                    "يوضع جهاز على الصدر لإرسال موجات صوتية، وهي موجات "
                    "فوق صوتية لا يستطيع الإنسان سماعها، باتجاه القلب."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "ترتد هذه الموجات عن القلب على شكل أصداء ويمكن التقاطها "
                    "مرة أخرى من خارج الجسم."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "تسمح هذه الموجات بالحصول على صور لحركات القلب، "
                    "على الورق أو في شكل فيديو."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "تسمح هذه الصور بقياس حجم القلب وسماكة عضلة القلب."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "يمكن لهذا الفحص أن يُظهر زيادة حجم البطين الأيمن "
                    "(تضخمًا وتوسعًا)."
                ),
            },

            # ==========================================================
            # PULMONARY FUNCTION TESTS
            # ==========================================================

            {
                "type": "heading",
                "title": "اختبارات وظائف التنفس (EFR)",
            },

            {
                "type": "paragraph",
                "text": (
                    "هي فحوصات تقليدية لقياس الخصائص الرئيسية للتنفس، "
                    "مثل كمية الهواء التي يتم تبادلها مع الوسط الخارجي."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "تستخدم اختبارات وظائف التنفس عدة أنواع من أجهزة القياس. "
                    "وفي أغلب الأحيان، يُطلب من الشخص أن يستنشق أو يزفر "
                    "من خلال قطعة فموية متصلة بأنبوب."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "يكون الأنبوب متصلًا بجهاز تظهر عليه منحنيات على الشاشة "
                    "لتوضيح خصائص التنفس."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "عادةً ما يجب إغلاق الأنف باستخدام مشبك الأنف حتى يمر "
                    "الهواء بالكامل عبر الجهاز."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "غالبًا ما يتبادل الأشخاص المصابون بارتفاع ضغط الدم "
                    "الشرياني الرئوي كمية أقل من الهواء مع الوسط الخارجي."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "يمكن لهذه الاختبارات أن تساعد الطبيب على اكتشاف بعض "
                    "أمراض الجهاز التنفسي، مثل التهاب الشعب الهوائية المزمن "
                    "أو تليف الرئة."
                ),
            },

            # ==========================================================
            # WALK TEST
            # ==========================================================

            {
                "type": "heading",
                "title": "اختبار المشي",
            },

            {
                "type": "paragraph",
                "text": (
                    "يهدف هذا الاختبار إلى قياس المسافة التي يستطيع الشخص "
                    "قطعها أثناء المشي بشكل طبيعي لمدة ست دقائق."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "غالبًا ما يتم ذلك من خلال المشي ذهابًا وإيابًا "
                    "في ممر يبلغ طوله 50 مترًا."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "يسمح هذا الفحص بتقييم الحاجة إلى التوقف للراحة "
                    "ومعرفة ما إذا كان الشخص يعاني من ضيق في التنفس."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "أحيانًا يوضع جهاز صغير يسمى مقياس التأكسج النبضي "
                    "على طرف الإصبع لقياس ما إذا كان الدم يحصل على كمية "
                    "كافية من الأكسجين أثناء الجهد."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "يُعد اختبار المشي مفيدًا في المتابعة لمعرفة ما إذا كان "
                    "ارتفاع ضغط الدم الشرياني الرئوي يتحسن أم لا وفقًا للعلاج."
                ),
            },

            {
                "type": "heading",
                "title": (
                    "ما هو اختبار المشي وما الذي يسمح بتقييمه؟"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "يتكون اختبار المشي من قياس أقصى مسافة يمكن قطعها "
                    "بالمشي بشكل طبيعي خلال فترة ست دقائق."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "في الظروف الطبيعية، لدى شخص لا يعاني من ارتفاع ضغط "
                    "الدم الشرياني الرئوي، تكون هذه المسافة أكثر من 600 متر."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "عمليًا، يسمح اختبار المشي بتقييم الفئة الوظيفية "
                    "التي ينتمي إليها المريض بدرجة جيدة من الدقة:"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "الفئة IV: من 0 إلى 250 مترًا\n"
                    "الفئة III: من 250 إلى 450 مترًا\n"
                    "الفئة II: من 450 إلى 550 مترًا\n"
                    "الفئة I: من 550 إلى 600 متر."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "تنبيه: هذه القيم إرشادية فقط، ويتم تقييمها من قبل الطبيب "
                    "وفقًا لكل شخص، وبحسب العمر والخصائص الجسدية وغيرها."
                ),
            },

            # ==========================================================
            # WALK TEST IMAGES
            # ==========================================================

            {
                "type": "image",
                "image": "articles/source/4.jpg",
                "image_caption": "اختبار المشي.",
            },

            {
                "type": "image",
                "image": "articles/source/3.jpg",
                "image_caption": "اختبار المشي.",
            },

            {
                "type": "image",
                "image": "articles/source/1.jpg",
                "image_caption": "اختبار المشي.",
            },

            {
                "type": "image",
                "image": "articles/source/2.jpg",
                "image_caption": "اختبار المشي.",
            },

            {
                "type": "image",
                "image": "articles/source/4.gif",
                "image_caption": "اختبار المشي.",
            },

            # ==========================================================
            # CARDIAC CATHETERIZATION
            # ==========================================================

            {
                "type": "heading",
                "title": (
                    "الفحص المستخدم لتشخيص ارتفاع ضغط الدم الشرياني الرئوي: "
                    "قسطرة القلب"
                ),
            },

            {
                "type": "heading",
                "title": "إجراء الفحص",
            },

            {
                "type": "paragraph",
                "text": (
                    "يُجرى هذا الفحص عادةً باستخدام قسطرة رئوية، "
                    "أو مسبار من نوع Swan-Ganz، يسمح بقياس:"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "• ضغط الدم في الشرايين الرئوية،\n"
                    "• ضغط الأذين الأيسر،\n"
                    "• ضغط الأذين الأيمن،\n"
                    "• تدفق الدم الرئوي،\n"
                    "• تحليل غازات الدم الوريدي."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "تساعد هذه القياسات في تحديد التوقعات المستقبلية "
                    "لمسار المرض."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "يتم إدخال مسبار صغير عبر وريد يسمى الوريد الفخذي "
                    "(الموجود في أعلى الفخذ عند مستوى ثنية الأربية)، "
                    "أو عبر الوريد تحت الترقوة (الموجود في التجويف "
                    "فوق الترقوة مباشرة)، أو عبر الوريد الوداجي "
                    "(الموجود على الجانب الجانبي من الرقبة)، ثم يتم "
                    "توجيهه حتى يصل إلى القلب ثم إلى الشرايين الرئوية."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "يسمح هذا المسبار بقياس ضغط الدم داخل الشرايين الرئوية."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "ويُعد هذا الفحص أساسيًا لمعرفة ما إذا كان الشخص "
                    "مصابًا بارتفاع ضغط الدم الشرياني الرئوي أم لا."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "ويمكن إجراؤه بعد ذلك بشكل منتظم لمعرفة ما إذا كان "
                    "العلاج فعالًا أم لا، إذ يهدف العلاج إلى خفض ضغط الدم "
                    "داخل الشرايين الرئوية."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "في حالة ارتفاع ضغط الدم الشرياني الرئوي، يتميز "
                    "النمط الديناميكي الدموي المتوسط بما يلي:"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "• ضغط شرياني رئوي يتجاوز في المتوسط ثلاثة أضعاف "
                    "الحد الأعلى للقيمة الطبيعية،\n"
                    "• انخفاض أو «تدفق قلبي منخفض»،\n"
                    "• ضغط أذيني أيسر طبيعي،\n"
                    "• ضغط أذيني أيمن عند الحد الأعلى الطبيعي."
                ),
            },

            {
                "type": "image",
                "image": "articles/source/htap32.jpg",
                "image_caption": (
                    "قسطرة القلب في تشخيص ارتفاع ضغط الدم الشرياني الرئوي."
                ),
            },

            # ==========================================================
            # TESTS TO DETERMINE THE CAUSE
            # ==========================================================

            {
                "type": "heading",
                "title": (
                    "الفحوصات المستخدمة لتحديد سبب ارتفاع ضغط الدم "
                    "الشرياني الرئوي"
                ),
            },

            {
                "type": "heading",
                "title": "تصوير الأوعية الرئوية",
            },

            {
                "type": "paragraph",
                "text": (
                    "يتم حقن مادة ظليلة تظهر في الأشعة السينية داخل الأوردة، "
                    "ثم تُجرى صورة بالأشعة بسرعة للحصول على صورة للقلب "
                    "والشرايين الرئوية."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "يسمح هذا الفحص برؤية الشريانين الرئويين الأيمن والأيسر."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "ويمكن أن يساعد هذا الفحص على التأكد من أن ارتفاع ضغط "
                    "الدم الشرياني الرئوي ليس ناتجًا عن جلطات تسد الشرايين الرئوية."
                ),
            },

            # ==========================================================
            # LUNG SCINTIGRAPHY
            # ==========================================================

            {
                "type": "heading",
                "title": "المسح الرئوي بالنظائر المشعة",
            },

            {
                "type": "paragraph",
                "text": (
                    "يتم حقن مادة مشعة داخل الأوردة، ثم يتم إجراء تصوير "
                    "سريع للرئتين لقياس حركة المادة المشعة داخل الرئتين."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "يسمح هذا الفحص بمعرفة ما إذا كان تدفق الدم قد تباطأ "
                    "أو أصبح مستحيلًا في بعض أجزاء الرئتين بسبب جلطات "
                    "تسد بعض الشرايين الصغيرة."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "يساعد هذا الفحص على معرفة ما إذا كان ارتفاع ضغط الدم "
                    "الشرياني الرئوي ناتجًا أم لا عن تكوّن جلطات دموية في الرئتين."
                ),
            },

            {
                "type": "image",
                "image": "articles/source/1.jpg",
                "image_caption": "المسح الرئوي.",
            },

            {
                "type": "image",
                "image": "articles/source/2.jpg",
                "image_caption": "المسح الرئوي.",
            },

            # ==========================================================
            # EFR
            # ==========================================================

            {
                "type": "heading",
                "title": "اختبارات وظائف التنفس (EFR)",
            },

            {
                "type": "paragraph",
                "text": (
                    "يمكن لاختبارات وظائف التنفس أن تكشف بعض أمراض الجهاز "
                    "التنفسي، مثل التهاب الشعب الهوائية المزمن."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "وفي هذه الحالة، يمكن أن تساعد في تحديد ارتفاع ضغط "
                    "الدم الشرياني الرئوي المرتبط بـ«نقص الأكسجة المزمن»."
                ),
            },

            # ==========================================================
            # AUTOIMMUNE DISEASE
            # ==========================================================

            {
                "type": "heading",
                "title": "البحث عن مرض مناعي ذاتي",
            },

            {
                "type": "paragraph",
                "text": (
                    "يتم إجراء تحاليل لعينة من الدم للبحث عن وجود أو عدم "
                    "وجود مؤشرات مميزة لأمراض المناعة الذاتية، والتي قد "
                    "تكون مرتبطة بارتفاع ضغط الدم الشرياني الرئوي."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "يمكن أن تشمل هذه الأمراض تصلب الجلد، والذئبة الحمامية "
                    "الجهازية، وأمراض الغدة الدرقية المناعية الذاتية."
                ),
            },

            # ==========================================================
            # BIOPSY
            # ==========================================================

            {
                "type": "heading",
                "title": "الخزعة",
            },

            {
                "type": "paragraph",
                "text": (
                    "إذا لم تسمح الفحوصات السابقة بتحديد سبب ارتفاع ضغط "
                    "الدم الشرياني الرئوي، فقد يكون من المفيد إجراء خزعة."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "تتمثل الخزعة في أخذ بعض خلايا الرئة تحت التخدير، "
                    "ثم تحليلها تحت المجهر للمساعدة على تحديد سبب "
                    "ارتفاع ضغط الدم الشرياني الرئوي."
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
                f"Article created successfully: {article}"
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

        translation = ArticleTranslation.objects.create(
            article=article,
            language="en",
            title="Diagnosis of Pulmonary Arterial Hypertension",
            excerpt=(
                "Understanding the different classifications of pulmonary "
                "hypertension, the tests used to diagnose pulmonary arterial "
                "hypertension, and the examinations used to determine its causes."
            ),
            meta_title=(
                "Diagnosis of Pulmonary Arterial Hypertension | HTAP Algérie"
            ),
            meta_description=(
                "Information about the diagnosis of pulmonary arterial "
                "hypertension, its classifications, tests used to assess "
                "heart and lung function, and examinations used to determine "
                "the cause of the disease."
            ),
        )

        blocks = [

            # ==========================================================
            # INTRODUCTION
            # ==========================================================

            {
                "type": "heading",
                "title": (
                    "Diagnosis of Pulmonary Arterial Hypertension"
                ),
            },

            {
                "type": "heading",
                "title": (
                    "The Different Classifications of Pulmonary Hypertension"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Pulmonary arterial hypertension can have different "
                    "origins and different consequences from one person "
                    "to another."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Doctors often classify the disease into different categories."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Pulmonary arterial hypertension can be classified "
                    "according to the causes responsible for the disease."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "The cause of the slowing of blood circulation inside "
                    "the lungs can be multiple."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Knowing the origin of pulmonary arterial hypertension "
                    "makes it possible to choose the treatment best suited "
                    "to each person."
                ),
            },

            # ==========================================================
            # CLASSIFICATION
            # ==========================================================

            {
                "type": "heading",
                "title": (
                    "Classification of Pulmonary Hypertension "
                    "(4th World Symposium on Pulmonary Hypertension "
                    "– Dana Point, California – February 2008)"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "There is a classification based on the causes, in which "
                    "pulmonary hypertension is divided into five categories, "
                    "which are themselves divided into subcategories."
                ),
            },

            # ==========================================================
            # GROUP 1
            # ==========================================================

            {
                "type": "heading",
                "title": (
                    "Pulmonary Arterial Hypertension – Group 1"
                ),
            },

            {
                "type": "heading",
                "title": (
                    "Idiopathic Pulmonary Arterial Hypertension"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Refers to pulmonary arterial hypertension that occurs "
                    "in isolation, without any known cause or known "
                    "predisposing circumstance."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "It was formerly called primary pulmonary arterial hypertension."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "The majority of pulmonary arterial hypertension cases "
                    "fall into this category."
                ),
            },

            {
                "type": "heading",
                "title": (
                    "Hereditary Pulmonary Arterial Hypertension"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "It is linked to a mutation in a gene, most often the "
                    "BMPR2 gene, with a risk of familial transmission."
                ),
            },

            {
                "type": "heading",
                "title": (
                    "Pulmonary Arterial Hypertension Induced by Drugs or Toxins"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "It is mainly associated with the use of drugs and "
                    "appetite-suppressant medicines (anorexigenic drugs) "
                    "derived from amphetamines."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Fenfluramine and derivatives: Isomeride, withdrawn "
                    "from the market in 1997."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Benfluorex: Mediator, withdrawn from the market "
                    "in November 2009."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Caution with methamphetamine-type derivatives "
                    "(illicit drugs such as ecstasy)."
                ),
            },

            {
                "type": "heading",
                "title": (
                    "Pulmonary Arterial Hypertension Associated with Other Diseases"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Pulmonary arterial hypertension may be associated "
                    "with connective tissue disease, portal hypertension, "
                    "congenital heart disease, HIV infection, or other "
                    "conditions such as thyroid diseases, Gaucher disease, "
                    "hemoglobin disorders, and Rendu-Osler disease."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Some diseases are conditions that can predispose "
                    "a person to pulmonary arterial hypertension."
                ),
            },

            {
                "type": "heading",
                "title": (
                    "Persistent Pulmonary Hypertension of the Newborn"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "In this condition, the pulmonary arterioles do not "
                    "dilate at birth as they normally should."
                ),
            },

            # ==========================================================
            # GROUP 1'
            # ==========================================================

            {
                "type": "heading",
                "title": (
                    "Pulmonary Veno-Occlusive Disease and Pulmonary "
                    "Capillary Hemangiomatosis – Group 1'"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "This condition is associated with disease affecting "
                    "the veins or capillary vessels. It actually affects "
                    "the pulmonary veins and venules rather than the "
                    "arterioles, but produces the same symptoms."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "It is a very rare form of pulmonary arterial hypertension."
                ),
            },

            # ==========================================================
            # GROUP 2
            # ==========================================================

            {
                "type": "heading",
                "title": (
                    "Pulmonary Hypertension Associated with Left Heart Disease "
                    "– Group 2"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "It occurs when pulmonary hypertension is the consequence "
                    "of a disease or malformation of the left side of the heart."
                ),
            },

            # ==========================================================
            # GROUP 3
            # ==========================================================

            {
                "type": "heading",
                "title": (
                    "Pulmonary Hypertension Associated with Lung Disease "
                    "and/or Chronic Hypoxemia – Group 3"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Examples include chronic obstructive pulmonary disease "
                    "(COPD), sleep apnea syndrome, interstitial lung diseases, "
                    "and chronic exposure to high altitudes."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "It occurs when pulmonary hypertension is associated "
                    "with respiratory diseases responsible for inadequate "
                    "oxygenation of the blood."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "In general, this type of pulmonary hypertension is "
                    "moderate and is rarely associated with serious consequences."
                ),
            },

            # ==========================================================
            # GROUP 4
            # ==========================================================

            {
                "type": "heading",
                "title": (
                    "Chronic Thromboembolic Pulmonary Hypertension "
                    "– Group 4"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "This occurs when the arteries of the lungs become "
                    "blocked by small blood clots. These clots organize "
                    "and permanently obstruct the vessels."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Surgery can completely cure these patients "
                    "(pulmonary endarterectomy)."
                ),
            },

            # ==========================================================
            # GROUP 5
            # ==========================================================

            {
                "type": "heading",
                "title": (
                    "Pulmonary Hypertension with Multifactorial or "
                    "Unclear Mechanisms – Group 5"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Examples include sarcoidosis, histiocytosis X, "
                    "lymphangioleiomyomatosis, and compression of "
                    "the pulmonary vessels."
                ),
            },

            # ==========================================================
            # FUNCTIONAL CLASSIFICATION
            # ==========================================================

            {
                "type": "paragraph",
                "text": (
                    "Pulmonary arterial hypertension can have different "
                    "origins and different consequences from one person "
                    "to another."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Doctors often classify the disease into different categories."
                ),
            },

            {
                "type": "heading",
                "title": (
                    "Classification of Pulmonary Arterial Hypertension "
                    "According to Its Impact on Health"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Pulmonary arterial hypertension can be classified "
                    "into four classes according to its most common "
                    "manifestations. The higher the class, the more "
                    "significant the manifestations of the disease."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "These are referred to as functional classes."
                ),
            },

            {
                "type": "image",
                "image": "articles/source/231.png",
                "image_caption": (
                    "Functional classes of pulmonary arterial hypertension."
                ),
            },

            # ==========================================================
            # HEART AND LUNG TESTS
            # ==========================================================

            {
                "type": "heading",
                "title": (
                    "Tests Used to Assess Heart and Lung Function"
                ),
            },

            {
                "type": "heading",
                "title": "Cardiac Catheterization",
            },

            {
                "type": "paragraph",
                "text": (
                    "Cardiac catheterization remains the reference test "
                    "for the diagnosis of pulmonary arterial hypertension. "
                    "For this reason, a dedicated section is devoted to it."
                ),
            },

            {
                "type": "heading",
                "title": "Electrocardiogram",
            },

            {
                "type": "paragraph",
                "text": (
                    "Electrodes are placed on the chest to measure the "
                    "electrical activity of the heart and display the "
                    "rhythm and intensity of heart contractions on a graph."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "This examination can show signs of right ventricular "
                    "hypertrophy. The right ventricle increases in size "
                    "because blood accumulates upstream of the lungs."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "An electrocardiogram can be performed while lying down "
                    "or during exercise on a treadmill or stationary bicycle."
                ),
            },

            # ==========================================================
            # CHEST X-RAY
            # ==========================================================

            {
                "type": "heading",
                "title": "Chest X-Ray",
            },

            {
                "type": "paragraph",
                "text": (
                    "An image of the lungs is obtained using X-rays. "
                    "The image may show characteristic signs of an increase "
                    "in the size or dilation of the pulmonary arteries."
                ),
            },

            # ==========================================================
            # ECHOCARDIOGRAPHY
            # ==========================================================

            {
                "type": "heading",
                "title": "Cardiac Ultrasound (Echocardiogram)",
            },

            {
                "type": "paragraph",
                "text": (
                    "A device is placed on the chest to send sound waves "
                    "(ultrasound, which cannot be heard by humans) toward "
                    "the heart."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "These waves bounce off the heart and can be detected "
                    "again outside the body."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "The waves make it possible to obtain images of the "
                    "heart's movements, either on paper or as video."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "These images make it possible to measure the size "
                    "of the heart and the thickness of the heart muscle."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "This examination can show an increase in the size "
                    "of the right ventricle (hypertrophy and dilation)."
                ),
            },

            # ==========================================================
            # PULMONARY FUNCTION TESTS
            # ==========================================================

            {
                "type": "heading",
                "title": "Pulmonary Function Tests (PFTs)",
            },

            {
                "type": "paragraph",
                "text": (
                    "These are standard examinations used to measure "
                    "the main characteristics of breathing, such as "
                    "the amount of air exchanged with the outside."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Pulmonary function tests use several types of measuring "
                    "instruments. Most often, the person is asked to inhale "
                    "or exhale through a mouthpiece connected to a tube."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "The tube is connected to a machine that displays "
                    "curves on a screen to illustrate the characteristics "
                    "of breathing."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Generally, the nose must be closed with a nose clip "
                    "so that all the air passes through the instrument."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "People with pulmonary arterial hypertension often "
                    "exchange less air with the outside."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "These tests can help the doctor detect certain "
                    "respiratory diseases, such as chronic bronchitis "
                    "or pulmonary fibrosis."
                ),
            },

            # ==========================================================
            # WALK TEST
            # ==========================================================

            {
                "type": "heading",
                "title": "The Walking Test",
            },

            {
                "type": "paragraph",
                "text": (
                    "This test measures the distance a person can walk "
                    "normally during six minutes."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Most often, the person walks back and forth along "
                    "a 50-meter corridor."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "This examination makes it possible to determine "
                    "whether the person needs to take breaks and whether "
                    "they become short of breath."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Sometimes, a small device called a pulse oximeter "
                    "is placed on the fingertip to measure whether the "
                    "blood is sufficiently oxygenated during exercise."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "The walking test is useful for follow-up to determine "
                    "whether pulmonary arterial hypertension is improving "
                    "or not depending on the treatment."
                ),
            },

            {
                "type": "heading",
                "title": (
                    "What Does the Walking Test Involve and What Does It Assess?"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "The walking test consists of measuring the maximum "
                    "distance that can be covered by walking normally "
                    "over a six-minute period."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Under normal conditions, in a person without pulmonary "
                    "arterial hypertension, this distance is more than 600 meters."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "In practice, the walking test provides a fairly accurate "
                    "assessment of the patient's functional class:"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Class IV: 0 to 250 meters\n"
                    "Class III: 250 to 450 meters\n"
                    "Class II: 450 to 550 meters\n"
                    "Class I: 550 to 600 meters."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Warning: these values are provided for guidance only "
                    "and are assessed by the doctor according to each person, "
                    "including age, physical characteristics, and other factors."
                ),
            },

            # ==========================================================
            # WALK TEST IMAGES
            # ==========================================================

            {
                "type": "image",
                "image": "articles/source/4.jpg",
                "image_caption": "Walking test.",
            },

            {
                "type": "image",
                "image": "articles/source/3.jpg",
                "image_caption": "Walking test.",
            },

            {
                "type": "image",
                "image": "articles/source/1.jpg",
                "image_caption": "Walking test.",
            },

            {
                "type": "image",
                "image": "articles/source/2.jpg",
                "image_caption": "Walking test.",
            },

            {
                "type": "image",
                "image": "articles/source/4.gif",
                "image_caption": "Walking test.",
            },

            # ==========================================================
            # CARDIAC CATHETERIZATION
            # ==========================================================

            {
                "type": "heading",
                "title": (
                    "The Examination Used to Diagnose Pulmonary Arterial "
                    "Hypertension: Cardiac Catheterization"
                ),
            },

            {
                "type": "heading",
                "title": "Procedure",
            },

            {
                "type": "paragraph",
                "text": (
                    "This examination is generally performed using a "
                    "pulmonary catheter (Swan-Ganz catheter), which makes "
                    "it possible to measure:"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "• pulmonary arterial pressure,\n"
                    "• left atrial pressure,\n"
                    "• right atrial pressure,\n"
                    "• pulmonary blood flow,\n"
                    "• venous blood gas analysis."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "These measurements are useful for establishing a prognosis."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "A small catheter is introduced through a vein called "
                    "the femoral vein, located at the top of the thigh near "
                    "the groin, or through the subclavian vein, located in "
                    "the hollow just above the collarbone, or through the "
                    "jugular vein, located on the side of the neck."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "The catheter is advanced through the heart and then "
                    "into the pulmonary arteries."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "This catheter makes it possible to measure the pressure "
                    "of the blood inside the pulmonary arteries."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "It is a key examination for determining whether or not "
                    "a person has pulmonary arterial hypertension."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "It can subsequently be performed regularly to determine "
                    "whether the treatment is effective. The aim of treatment "
                    "is to reduce blood pressure in the pulmonary arteries."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "In pulmonary arterial hypertension, the average "
                    "hemodynamic profile is characterized by:"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "• pulmonary arterial pressure exceeding, on average, "
                    "three times the upper limit of normal,\n"
                    "• low cardiac output,\n"
                    "• normal left atrial pressure,\n"
                    "• right atrial pressure at the upper limit of normal."
                ),
            },

            {
                "type": "image",
                "image": "articles/source/htap32.jpg",
                "image_caption": (
                    "Cardiac catheterization in the diagnosis of pulmonary "
                    "arterial hypertension."
                ),
            },

            # ==========================================================
            # TESTS TO DETERMINE THE CAUSE
            # ==========================================================

            {
                "type": "heading",
                "title": (
                    "Examinations Used to Determine the Cause "
                    "of Pulmonary Arterial Hypertension"
                ),
            },

            {
                "type": "heading",
                "title": "Pulmonary Angiography",
            },

            {
                "type": "paragraph",
                "text": (
                    "A contrast liquid that is visible on X-rays is injected "
                    "into the veins, followed quickly by an X-ray to obtain "
                    "an image of the heart and pulmonary arteries."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "This examination makes it possible to visualize "
                    "the right and left pulmonary arteries."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "It can help determine whether pulmonary arterial "
                    "hypertension is caused by blood clots blocking "
                    "the pulmonary arteries."
                ),
            },

            # ==========================================================
            # LUNG SCINTIGRAPHY
            # ==========================================================

            {
                "type": "heading",
                "title": "Lung Scintigraphy",
            },

            {
                "type": "paragraph",
                "text": (
                    "A radioactive substance is injected into the veins, "
                    "and a lung scan is then performed to measure the "
                    "movement of radioactivity through the lungs."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "This examination makes it possible to determine "
                    "whether blood circulation has slowed or become "
                    "impossible in parts of the lungs because clots "
                    "are blocking some of the small arteries."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "This examination helps determine whether pulmonary "
                    "arterial hypertension is caused by the formation "
                    "of blood clots in the lungs."
                ),
            },

            {
                "type": "image",
                "image": "articles/source/1.jpg",
                "image_caption": "Lung scintigraphy.",
            },

            {
                "type": "image",
                "image": "articles/source/2.jpg",
                "image_caption": "Lung scintigraphy.",
            },

            # ==========================================================
            # PFT
            # ==========================================================

            {
                "type": "heading",
                "title": "Pulmonary Function Tests (PFTs)",
            },

            {
                "type": "paragraph",
                "text": (
                    "Pulmonary function tests can identify certain "
                    "respiratory diseases, such as chronic bronchitis."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "In this case, they can help identify pulmonary arterial "
                    "hypertension associated with chronic hypoxia."
                ),
            },

            # ==========================================================
            # AUTOIMMUNE DISEASE
            # ==========================================================

            {
                "type": "heading",
                "title": "Testing for an Autoimmune Disease",
            },

            {
                "type": "paragraph",
                "text": (
                    "Blood tests are performed to determine whether there "
                    "are characteristic markers of autoimmune diseases "
                    "that could be associated with pulmonary arterial hypertension."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "These may include scleroderma, systemic lupus "
                    "erythematosus, and autoimmune thyroid diseases."
                ),
            },

            # ==========================================================
            # BIOPSY
            # ==========================================================

            {
                "type": "heading",
                "title": "Biopsy",
            },

            {
                "type": "paragraph",
                "text": (
                    "If the examinations described above do not make it "
                    "possible to determine the cause of pulmonary arterial "
                    "hypertension, a biopsy may be useful."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "A biopsy involves taking a small sample of lung cells "
                    "under anesthesia. The cells are then analyzed under "
                    "a microscope to help determine the cause of pulmonary "
                    "arterial hypertension."
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
                f"Article created successfully: {article}"
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
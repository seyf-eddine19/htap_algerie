from django.core.management.base import BaseCommand
from django.utils import timezone

from articles.models import (
    Article,
    ArticleCategory,
    ArticleTranslation,
    ArticleBlock,
)


class Command(BaseCommand):
    help = "Create Article - Génétique et HTAP"

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

        # article = Article.objects.create(
        #     category=category,
        #     author="HTAP Algérie",
        #     status=Article.Status.PUBLISHED,
        #     is_featured=False,
        #     published_at=timezone.now(),
        #     slug="genetique-et-htap",
        # )
        
        article, _ = Article.objects.get_or_create(
            slug="genetique-et-htap",
            defaults={
                "category": category,
                "author": "HTAP Algérie",
                "status": Article.Status.PUBLISHED,
                "is_featured": False,
                "published_at": timezone.now(),
            },
        )

        # ==============================================================
        # FRENCH TRANSLATION
        # ==============================================================

        translation = ArticleTranslation.objects.create(
            article=article,
            language="fr",
            title="Génétique et HTAP",
            excerpt=(
                "Comprendre le rôle de la génétique dans l'hypertension "
                "artérielle pulmonaire, les mutations impliquées, leur "
                "transmission et le conseil génétique."
            ),
            meta_title="Génétique et HTAP | HTAP Algérie",
            meta_description=(
                "Informations sur la génétique et l'hypertension artérielle "
                "pulmonaire, les gènes de prédisposition, la transmission "
                "génétique et le conseil génétique."
            ),
        )

        # ==============================================================
        # BLOCKS
        # ==============================================================

        blocks = [

            # ==========================================================
            # INTRODUCTION — LA GÉNÉTIQUE EN IMAGES
            # ==========================================================

            {
                "type": "heading",
                "title": "La génétique en images",
            },

            {
                "type": "paragraph",
                "text": (
                    "Chaque individu est constitué de plusieurs millions "
                    "de cellules. Chaque cellule contient à l’intérieur de "
                    "son noyau 46 chromosomes organisés en 23 paires "
                    "(Figure 1)."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Chaque paire de chromosomes est constituée d’un "
                    "chromosome hérité de sa mère, et d’un chromosome "
                    "hérité de son père. Les chromosomes sont donc tous "
                    "en double exemplaire."
                ),
            },

            {
                "type": "paragraph",
                "text": "Figure 1 : La cellule",
            },

            {
                "type": "image",
                "image": "articles/source/fig01.gif",
                "image_caption": "Figure 1 : La cellule.",
            },

            {
                "type": "paragraph",
                "text": (
                    "Chaque chromosome est constitué de plusieurs gènes "
                    "(représentés de différentes couleurs sur la Figure 2), "
                    "et chaque gène possède une fonction bien définie "
                    "(couleur des yeux, formation des poumons, taille, …) "
                    "(Figure 2). Tous les hommes possèdent 30 000 gènes "
                    "différents. Plusieurs gènes sont nécessaires à la "
                    "création d’un organe."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Figure 2 : Exemple de trois paires de chromosomes "
                    "différentes"
                ),
            },

            {
                "type": "image",
                "image": "articles/source/fig02.gif",
                "image_caption": (
                    "Figure 2 : Exemple de trois paires de chromosomes différentes."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "On peut imaginer qu’un gène est une encyclopédie "
                    "(Figure 3) contenant le mode d’emploi pour fabriquer "
                    "une protéine (molécule active) qui aura une fonction "
                    "importante pour la cellule et donc pour l’individu."
                ),
            },

            {
                "type": "paragraph",
                "text": "Figure 3 : Les gènes",
            },

            {
                "type": "image",
                "image": "articles/source/fig_3.gif",
                "image_caption": "Figure 3 : Les gènes.",
            },

            {
                "type": "paragraph",
                "text": (
                    "Une anomalie génétique (ou mutation) est une erreur "
                    "dans ce mode d’emploi (Figure 4). L’information "
                    "contenue dans l’encyclopédie sera donc erronée, "
                    "et la protéine créée ne sera pas fonctionnelle. "
                    "Certaines anomalies génétiques ne créent pas de maladie."
                ),
            },

            {
                "type": "paragraph",
                "text": "Figure 4 : Les anomalies génétiques",
            },

            {
                "type": "image",
                "image": "articles/source/fig04.gif",
                "image_caption": "Figure 4 : Les anomalies génétiques.",
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
                    "considérablement le pronostic des patients séropositifs "
                    "atteints. Elle peut toucher tous les groupes à risque "
                    "d'infection par le VIH mais les toxicomanes sont les "
                    "plus fréquemment concernés puisqu'ils représentent "
                    "40 à 60 % de l'ensemble des malades."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "L'HTAP est diagnostiquée en moyenne 2,5 à 3 ans après "
                    "la découverte de la séropositivité mais elle peut "
                    "également la révéler ce qui justifie de faire réaliser "
                    "une sérologie VIH dans le bilan initial de toute HTAP "
                    "d'allure idiopathique."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "La présentation clinique est identique à celle de "
                    "l'HTAP idiopathique et le diagnostic (cathétérisme "
                    "cardiaque droit) réalisé de la même façon."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Le traitement des HTAP réfractaires malgré un traitement "
                    "conventionnel optimal (limitation des efforts, "
                    "anticoagulation orale, diurétiques et oxygène si "
                    "nécessaire) associe généralement traitement par "
                    "antirétroviraux (trithérapie) et époprosténol même si "
                    "ce traitement, qui exige un matériel veineux implantable, "
                    "est inutilisable chez le toxicomane non sevré et comporte "
                    "un risque infectieux à prendre en compte en cas "
                    "d'immunodépression."
                ),
            },

            # ==========================================================
            # ANOMALIES GÉNÉTIQUES
            # ==========================================================

            {
                "type": "heading",
                "title": (
                    "Les anomalies génétiques impliquées dans la survenue "
                    "de l’HTAP"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "La première forme familiale de la maladie a été décrite "
                    "par Dresdale et al. en 1954. En 2000, deux équipes "
                    "(Lane et al. & Deng et al.) identifient la première "
                    "mutation (ou anomalie génétique) sur le gène BMPR2 "
                    "responsable de la maladie. Ce gène est localisé sur "
                    "le chromosome 2 (Figure 5)."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "En 2001 et 2003, l'observation du développement d'une "
                    "HTAP chez les patients atteints de la maladie de "
                    "Rendu-Osler (dont les gènes ALK1 et endogline étaient "
                    "connus pour être responsables de cette maladie), "
                    "ont permis d'identifier deux nouveaux gènes de "
                    "prédisposition à l'HTAP."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "En 2012, il a été identifié un nouveau gène de "
                    "prédisposition à l'HTAP : Cavéoline-1. Des anomalies "
                    "de ce gène sont très rares puisqu'elles n'ont été "
                    "identifiées à l'heure actuelle que dans deux familles."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Plus récemment, en 2013, l'implication d'un nouveau "
                    "gène KCNK3 a été démontrée dans le développement de "
                    "l'HTAP. Ainsi, plusieurs gènes impliqués dans le "
                    "développement de l'HTAP ont été identifiés. Cependant, "
                    "les mutations sur le gène BMPR2 sont de loin les "
                    "plus fréquentes."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Figure 5 : Caryotype humain. Le génome humain est "
                    "composé de 23 paires de chromosomes. Chaque paire "
                    "est composée d’un chromosome paternel et d’un chromosome "
                    "maternel. Le gène BMPR2 est localisé sur le chromosome 2. "
                    "Chaque être humain possède donc deux copies de ce gène "
                    "(un sur chaque chromosome 2). Une anomalie sur un de "
                    "ces deux gènes va donner un risque à la personne de "
                    "développer une HTAP."
                ),
            },

            {
                "type": "image",
                "image": "articles/source/fig05.jpg",
                "image_caption": (
                    "Figure 5 : Caryotype humain et localisation du gène BMPR2."
                ),
            },

            # ==========================================================
            # FONCTION DES GÈNES
            # ==========================================================

            {
                "type": "heading",
                "title": (
                    "Fonction des gènes de prédisposition à l'HTAP"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Les gènes de prédisposition à l'HTAP interviennent "
                    "dans la régulation de la croissance des cellules des "
                    "artères pulmonaires. Les mutations de ces gènes peuvent "
                    "entraîner une multiplication anormale des cellules des "
                    "artères pulmonaires, ce qui va boucher les vaisseaux. "
                    "Les personnes porteuses d'une mutation sur un de ces "
                    "gènes vont être prédisposées à faire une HTAP."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Des mutations d’un des gènes de prédisposition à l'HTAP "
                    "sont trouvées chez :"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "• 20 % des patients atteints d'HTAP idiopathique "
                    "(patients n’ayant pas d’autre maladie associée pouvant "
                    "causer une HTAP et pas de parent atteint d’HTAP),\n\n"
                    "• 85 % des patients ayant une HTAP familiale "
                    "(au moins deux personnes atteintes de la maladie "
                    "dans une même famille)."
                ),
            },

            # ==========================================================
            # TRANSMISSION GÉNÉTIQUE DE L'HTAP
            # ==========================================================

            {
                "type": "heading",
                "title": "La transmission génétique de l'HTAP",
            },

            {
                "type": "paragraph",
                "text": (
                    "Étant donné que nous avons tous nos chromosomes en "
                    "double exemplaire (un chromosome hérité de notre mère, "
                    "et un chromosome hérité de notre père), nous avons "
                    "tous 2 gènes BMPR2, 2 gènes ALK1 et 2 gènes KCNK3... "
                    "(Figure 6)."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Lors de sa conception, un enfant va récupérer, pour "
                    "chaque paire de chromosomes, un des deux chromosomes "
                    "de son père et un des deux chromosomes de sa mère."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Ainsi, lorsqu’un parent est porteur d’une anomalie "
                    "génétique sur un de ces gènes, chacun de ses enfants "
                    "a un risque sur deux (soit 50 % de risque) d’être "
                    "porteur de l’anomalie génétique familiale."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "En effet, l’enfant peut récupérer du parent porteur "
                    "de l’anomalie génétique soit le chromosome ayant le "
                    "gène muté, soit le chromosome ayant le gène non muté "
                    "(Figure 6)."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Dans sa forme héréditaire, l’HTAP est une maladie dite :\n\n"
                    "• de transmission autosomique (peut toucher les femmes "
                    "et les hommes),\n\n"
                    "• dominante, ce qui signifie qu’une seule anomalie "
                    "génétique va donner un risque à la personne de développer "
                    "la maladie,\n\n"
                    "• de pénétrance incomplète, ce qui signifie qu’une personne "
                    "peut être porteuse de l’anomalie génétique mais ne jamais "
                    "développer la maladie."
                ),
            },

            {
                "type": "image",
                "image": "articles/source/Genetique.jpg",
                "image_caption": (
                    "Illustration de la transmission génétique de l'HTAP."
                ),
            },

            # ==========================================================
            # BMPR2
            # ==========================================================

            {
                "type": "paragraph",
                "text": (
                    "En effet, et en ce qui concerne le gène BMPR2 :"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "• les hommes porteurs d'une anomalie génétique sur "
                    "le gène BMPR2 ont un risque d'environ 14 % de développer "
                    "la maladie, et ont donc 86 % de chance de ne jamais "
                    "être atteints.\n\n"
                    "• les femmes porteuses d'une anomalie génétique sur "
                    "le gène BMPR2 ont un risque d'environ 42 % de développer "
                    "la maladie, et ont donc 58 % de chance de ne jamais "
                    "être atteintes."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Le risque de développer une HTAP pour les personnes "
                    "porteuses d'une mutation des gènes KCNK3, Cavéoline-1, "
                    "ALK1 et Endogline n'est pas connu précisément pour le "
                    "moment car ces anomalies concernent très peu de personnes."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Les descendants des personnes porteuses d'une anomalie "
                    "génétique (malade ou non malade) peuvent également "
                    "être porteurs de cette anomalie génétique."
                ),
            },

            # ==========================================================
            # RISQUE GÉNÉTIQUE
            # ==========================================================

            {
                "type": "heading",
                "title": (
                    "Un risque génétique variable en fonction des "
                    "sous-groupes d'HTAP"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "L'HTAP peut être due à une maladie associée "
                    "(hypertension portale, VIH, cardiopathie congénitale, "
                    "connectivites) mais elle peut aussi ne pas avoir de "
                    "cause apparente. Le risque génétique n'est pas le même "
                    "pour chaque sous-groupe d'HTAP. Le dépistage génétique "
                    "est par conséquent différent selon les cas : forme "
                    "familiale, idiopathique ou associée à d'autres maladies."
                ),
            },

            # ==========================================================
            # HTAP FAMILIALE
            # ==========================================================

            {
                "type": "heading",
                "title": "HTAP familiale",
            },

            {
                "type": "paragraph",
                "text": (
                    "Dans notre centre de référence, une mutation sur un "
                    "des gènes de prédisposition à l'HTAP (BMPR2, KCNK3, "
                    "Cavéoline-1, ALK1, Endogline) est identifiée chez 85 % "
                    "des patients atteints d’une HTAP familiale."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Dans 15 % des cas, il n'est pas possible d'identifier "
                    "d’anomalie génétique car, dans les conditions techniques "
                    "actuelles, il est possible de passer à côté d'une mutation "
                    "et il peut exister également d'autres gènes responsables "
                    "de la maladie et qui restent à découvrir."
                ),
            },

            # ==========================================================
            # HTAP IDIOPATHIQUE
            # ==========================================================

            {
                "type": "heading",
                "title": (
                    "HTAP idiopathique (anciennement primitive)"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "La maladie s'est dans ce cas développée chez des personnes "
                    "qui n'avaient pas de facteur de risque particulier "
                    "(pas de prise d'anorexigène ni de connectivite, "
                    "d’hypertension portale, de cardiopathie congénitale)."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Une étude effectuée par l’équipe de Bicêtre a montré "
                    "que 20 % des patients souffrant d'HTAP idiopathique "
                    "sont porteurs d’une anomalie génétique sur un des gènes "
                    "de prédisposition (BMPR2, KCNK3, Cavéoline-1, ALK1, "
                    "Endogline)."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Il est important de préciser que la distinction entre "
                    "les patients atteints d’HTAP familiale et les patients "
                    "atteints d’HTAP idiopathique porteurs d’une mutation, "
                    "est artificielle puisque qu’il s’agit dans les deux cas "
                    "de la forme héréditaire de la maladie."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Un patient atteint d’HTAP idiopathique avec une mutation "
                    "sur le gène BMPR2 peut être le premier cas d’HTAP décrit "
                    "dans une famille à risque. Les discussions récentes "
                    "plaident en faveur du terme HTAP « héréditaire » pour "
                    "décrire cette forme génétique de la maladie."
                ),
            },

            # ==========================================================
            # HTAP ASSOCIÉES
            # ==========================================================

            {
                "type": "heading",
                "title": "HTAP associées",
            },

            {
                "type": "paragraph",
                "text": (
                    "Dans le cas d'une HTAP associée à la prise d'un médicament "
                    "coupe-faim (médicaments pour maigrir), environ 10 % des "
                    "patients présentent une mutation du gène BMPR2."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Dans l'ensemble de toutes les autres maladies auxquelles "
                    "est associée l'HTAP (hypertension portale, VIH, cardiopathie "
                    "congénitale, connectivites), il n'existe pas de mutation "
                    "des gènes de prédisposition à l'HTAP identifiée à l'heure "
                    "actuelle."
                ),
            },

            # ==========================================================
            # RENDU-OSLER
            # ==========================================================

            {
                "type": "heading",
                "title": "HTAP et maladie de Rendu-Osler",
            },

            {
                "type": "paragraph",
                "text": (
                    "La maladie de Rendu-Osler est caractérisée par des "
                    "anomalies des vaisseaux et en particulier des fistules "
                    "artério-veineuses qui peuvent être pulmonaires."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Il a été montré que les personnes porteuses d’une "
                    "mutation sur un gène impliqué dans la maladie de "
                    "Rendu-Osler (ACVRL1 ou Endogline) peuvent développer "
                    "une HTAP."
                ),
            },

            # ==========================================================
            # RISQUE POUR LES APPARENTÉS
            # ==========================================================

            {
                "type": "heading",
                "title": "Risque pour les apparentés",
            },

            {
                "type": "paragraph",
                "text": (
                    "Lorsqu’une anomalie génétique a été identifiée chez "
                    "un patient, ses apparentés peuvent être porteurs de "
                    "cette même anomalie génétique. Ils ont donc un risque "
                    "de développer une HTAP."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Ces personnes peuvent avoir connaissance de leur statut "
                    "génétique (porteur ou non porteur de la mutation familiale) "
                    "en effectuant un test génétique."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Ainsi, parmi les personnes non malades ayant un parent "
                    "porteur d’une mutation sur le gène BMPR2 :"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "• les hommes porteurs d'une mutation génétique sur le "
                    "gène BMPR2 ont un risque estimé de 14 % de développer "
                    "la maladie et 86 % de chance de ne jamais la développer. "
                    "Leurs descendants peuvent également être porteurs de "
                    "cette anomalie génétique.\n\n"
                    "• les femmes porteuses d'une mutation génétique sur le "
                    "gène BMPR2 ont un risque estimé de 42 % de développer "
                    "la maladie et donc 58 % de chance de ne jamais la "
                    "développer. Leurs descendants peuvent également être "
                    "porteurs de cette anomalie génétique.\n\n"
                    "• les personnes non porteuses de la mutation n’ont pas "
                    "de risque particulier vis-à-vis de la maladie, tout "
                    "comme leurs enfants."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Le risque de développer une HTAP pour les personnes "
                    "porteuses d'une mutation des gènes KCNK3, Cavéoline-1, "
                    "ALK1 et Endogline n'est pas connu précisément pour le "
                    "moment car ces anomalies concernent très peu de personnes."
                ),
            },

            # ==========================================================
            # CONSEIL GÉNÉTIQUE
            # ==========================================================

            {
                "type": "heading",
                "title": "Le conseil génétique",
            },

            {
                "type": "paragraph",
                "text": (
                    "Une consultation de génétique est proposée systématiquement "
                    "à l’ensemble des patients atteints d’HTAP idiopathique, "
                    "d’HTAP familiale, ou associée à la prise d’un médicament "
                    "coupe-faim."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Elle est également accessible à tous les apparentés des "
                    "patients ayant une mutation sur un des gènes de "
                    "prédisposition à l'HTAP (BMPR2, KCNK3, Cavéoline-1, "
                    "ALK1, Endogline)."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Durant les 12 dernières années, plus de 500 patients "
                    "atteints d'HTAP ainsi que plus de 200 apparentés ont "
                    "été vus en consultation de génétique."
                ),
            },

            # ==========================================================
            # DÉROULEMENT DE LA CONSULTATION
            # ==========================================================

            {
                "type": "heading",
                "title": "Le déroulement de la consultation de génétique",
            },

            {
                "type": "paragraph",
                "text": (
                    "Lors de la première consultation de génétique, nous "
                    "expliquons aux personnes le mécanisme de la maladie, "
                    "la transmission génétique, le risque d’être porteur "
                    "d’une anomalie génétique sur un des gènes de "
                    "prédisposition à l'HTAP (BMPR2, KCNK3, Cavéoline-1, "
                    "ALK1, Endogline) et le risque pour les apparentés "
                    "d’être atteints de la maladie."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Au terme de cette première consultation, le test "
                    "génétique est proposé en soulignant les inconvénients "
                    "et les avantages de connaître son statut génétique, "
                    "et le fait qu’ils peuvent suspendre leur démarche "
                    "de manière temporaire ou définitive à n’importe quelle "
                    "étape de la procédure."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "S’ils souhaitent faire le test, un consentement éclairé "
                    "est alors signé, et la prise de sang est effectuée."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Lorsque l’analyse est terminée (4 à 6 mois pour la "
                    "première personne testée dans la famille et 1 mois "
                    "pour les autres), une lettre est envoyée à la personne, "
                    "l’informant de la disponibilité de son résultat et "
                    "mentionnant le fait qu’il peut dès à présent prendre "
                    "rendez-vous pour en avoir connaissance."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Lors de la deuxième consultation de génétique, les "
                    "personnes reçoivent de la conseillère le résultat "
                    "ainsi que les informations adaptées."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Au terme de cette deuxième consultation, un prélèvement "
                    "de confirmation est effectué, et la confirmation est "
                    "remise aux personnes lors d’une troisième consultation."
                ),
            },

            # ==========================================================
            # MVO
            # ==========================================================

            {
                "type": "heading",
                "title": "Maladie veino-occlusive pulmonaire (MVO)",
            },

            {
                "type": "paragraph",
                "text": (
                    "La MVO est une forme rare d’hypertension pulmonaire "
                    "caractérisée par une atteinte prédominante des petites "
                    "veines pulmonaires (à la différence de l'HTAP qui touche "
                    "plutôt les petites artères pulmonaires)."
                ),
            },

            # ==========================================================
            # MVO ET EIF2AK4
            # ==========================================================

            {
                "type": "heading",
                "title": "MVO et mutations du gène EIF2AK4",
            },

            {
                "type": "paragraph",
                "text": (
                    "Deux mutations sur les deux gènes appelés EIF2AK4 "
                    "(1 hérité du père et 1 hérité de la mère) sont trouvées chez :"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "• environ 25 % des patients atteints de MVO sporadique "
                    "(patients n’ayant pas d’autre maladie associée pouvant "
                    "causer une MVO et pas de parents atteints de MVO),\n\n"
                    "• la quasi-totalité des patients ayant une MVO familiale "
                    "(au moins deux personnes atteintes de la maladie dans "
                    "une même famille)."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Les personnes porteuses de mutations sur leurs deux "
                    "gènes EIF2AK4 (= pas de EIF2AK4 fonctionnel) vont être "
                    "prédisposées à développer une MVO."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "En revanche, les connaissances actuelles laissent "
                    "supposer que les personnes porteuses d’une seule mutation "
                    "sur un seul gène EIF2AK4 n’auraient pas de risque de "
                    "développer une MVO."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Figure 7 : Caryotype humain. Le génome humain est composé "
                    "de 23 paires de chromosomes. Chaque paire est composée "
                    "d’un chromosome paternel et d’un chromosome maternel. "
                    "Le gène EIF2AK4 est localisé sur le chromosome 15. "
                    "Chaque être humain possède donc deux copies de ce gène "
                    "(un sur chaque chromosome 15). Une anomalie sur les "
                    "deux gènes va donner un risque à la personne de "
                    "développer une MVO."
                ),
            },

            # ==========================================================
            # TRANSMISSION MVO
            # ==========================================================

            {
                "type": "heading",
                "title": "La transmission génétique de la MVO",
            },

            {
                "type": "paragraph",
                "text": (
                    "Étant donné que nous avons tous nos chromosomes en "
                    "double exemplaire (un chromosome hérité de notre mère, "
                    "et un chromosome hérité de notre père), nous avons "
                    "tous 2 gènes EIF2AK4 (Figure 8)."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Lors de sa conception, un enfant va récupérer, pour "
                    "chaque paire de chromosomes, un des deux chromosomes "
                    "de son père et un des deux chromosomes de sa mère."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Ainsi, lorsque les deux parents sont porteurs d’une "
                    "seule anomalie génétique sur un des gènes EIF2AK4, "
                    "chacun de leurs enfants a un risque sur quatre "
                    "(soit 25 % de risque) d’être porteur de deux mutations "
                    "EIF2AK4."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "En effet, l’enfant peut récupérer des parents porteurs "
                    "de l’anomalie génétique soit le chromosome ayant le "
                    "gène EIF2AK4 muté, soit le chromosome ayant le gène "
                    "EIF2AK4 non muté. Quatre possibilités sont alors "
                    "possibles comme montré sur la Figure 8."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Figure 8 : Transmission des mutations EIF2AK4"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Lorsqu’une personne est porteuse de deux anomalies "
                    "génétiques du gène EIF2AK4, ses enfants seront "
                    "obligatoirement porteurs d’une seule anomalie génétique "
                    "comme le montre la figure 7, ce qui ne suffit pas à "
                    "prédisposer pour la MVO."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Une mutation sur le gène EIF2AK4 est très rare dans "
                    "la population générale. Il existe donc peu de risque "
                    "que le deuxième parent soit porteur d’une mutation "
                    "de ce gène, donc peu de risque qu’un enfant ait deux "
                    "mutations du gène EIF2AK4."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Ceci est différent en cas de consanguinité, car le "
                    "deuxième parent pourrait être porteur de l’anomalie "
                    "génétique familiale."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Figure 9 : Transmission d’un parent malade aux enfants"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Dans sa forme héréditaire, la MVO est une maladie dite :\n\n"
                    "• de transmission autosomique (peut toucher les femmes "
                    "et les hommes),\n\n"
                    "• récessive, ce qui signifie qu’il faut être porteur "
                    "de deux anomalies sur les deux gènes EIF2AK4 pour avoir "
                    "un risque de développer la maladie."
                ),
            },

            {
                "type": "image",
                "image": "articles/source/MVO.png",
                "image_caption": (
                    "Illustration de la maladie veino-occlusive pulmonaire."
                ),
            },

            {
                "type": "image",
                "image": "articles/source/888.png",
                "image_caption": (
                    "Illustration de la transmission génétique de la MVO."
                ),
            },

            {
                "type": "image",
                "image": "articles/source/777.png",
                "image_caption": (
                    "Illustration de la transmission génétique de la MVO."
                ),
            },

            # ==========================================================
            # CONSEIL GÉNÉTIQUE — MVO
            # ==========================================================

            {
                "type": "heading",
                "title": "Le conseil génétique",
            },

            {
                "type": "paragraph",
                "text": (
                    "Une consultation de génétique est proposée systématiquement "
                    "à l’ensemble des patients atteints de MVO ayant ou non "
                    "une histoire familiale de MVO."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Elle est également accessible à tous les frères et sœurs "
                    "des patients ayant deux mutations sur leurs gènes EIF2AK4."
                ),
            },

            {
                "type": "heading",
                "title": "Le déroulement de la consultation de génétique",
            },

            {
                "type": "paragraph",
                "text": (
                    "Lors de la première consultation de génétique, nous "
                    "expliquons aux personnes le mécanisme de la maladie, "
                    "la transmission génétique, le risque d’être porteur "
                    "d’anomalies génétiques sur le gène EIF2AK4 et le risque "
                    "pour les apparentés d’être atteints de la maladie."
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
                "Article 'Génétique et HTAP' created successfully."
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


        translation, created = ArticleTranslation.objects.get_or_create(
            article=article,
            language="ar",
            defaults={
                "title": "الوراثة وارتفاع ضغط الدم الشرياني الرئوي",
                "excerpt": (
                    "فهم دور العوامل الوراثية في ارتفاع ضغط الدم الشرياني الرئوي، "
                    "والطفرات الجينية، وطرق انتقال المرض والاستشارة الوراثية."
                ),
                "meta_title": (
                    "الوراثة وارتفاع ضغط الدم الشرياني الرئوي | HTAP Algérie"
                ),
                "meta_description": (
                    "معلومات حول الوراثة وارتفاع ضغط الدم الشرياني الرئوي، "
                    "والجينات المرتبطة بالمرض، وانتقاله الوراثي والاستشارة الوراثية."
                ),
            },
        )

        # Avoid duplicate blocks when running the command again.
        ArticleBlock.objects.filter(
            translation=translation
        ).delete()

        blocks = [

            # ==========================================================
            # INTRODUCTION
            # ==========================================================

            {
                "type": "heading",
                "title": "الوراثة وارتفاع ضغط الدم الشرياني الرئوي",
            },

            {
                "type": "heading",
                "title": "الوراثة بالصور",
            },

            {
                "type": "paragraph",
                "text": (
                    "يتكون كل فرد من عدة ملايين من الخلايا. تحتوي كل خلية "
                    "داخل نواتها على 46 كروموسومًا منظمة في 23 زوجًا "
                    "(الشكل 1)."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "يتكون كل زوج من الكروموسومات من كروموسوم موروث من الأم "
                    "وكروموسوم موروث من الأب. لذلك توجد الكروموسومات في "
                    "نسختين."
                ),
            },

            {
                "type": "paragraph",
                "text": "الشكل 1: الخلية.",
            },

            {
                "type": "image",
                "image": "articles/source/fig01.gif",
                "image_caption": "الشكل 1: الخلية.",
            },

            {
                "type": "paragraph",
                "text": (
                    "يتكون كل كروموسوم من عدة جينات، ممثلة بألوان مختلفة "
                    "في الشكل 2، ولكل جين وظيفة محددة (مثل لون العينين، "
                    "وتكوين الرئتين، والطول وغيرها). يمتلك الإنسان حوالي "
                    "30 ألف جين مختلف. وتحتاج عملية تكوين عضو ما إلى عدة جينات."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "الشكل 2: مثال على ثلاثة أزواج مختلفة من الكروموسومات."
                ),
            },

            {
                "type": "image",
                "image": "articles/source/fig02.gif",
                "image_caption": (
                    "الشكل 2: مثال على ثلاثة أزواج مختلفة من الكروموسومات."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "يمكن تشبيه الجين بموسوعة تحتوي على تعليمات تصنيع بروتين "
                    "وهو جزيء فعال يؤدي وظيفة مهمة داخل الخلية وبالتالي داخل "
                    "جسم الإنسان."
                ),
            },

            {
                "type": "paragraph",
                "text": "الشكل 3: الجينات.",
            },

            {
                "type": "image",
                "image": "articles/source/fig_3.gif",
                "image_caption": "الشكل 3: الجينات.",
            },

            {
                "type": "paragraph",
                "text": (
                    "الخلل الجيني أو الطفرة هو خطأ في هذه التعليمات. وبالتالي "
                    "قد تصبح المعلومات الموجودة في هذه «الموسوعة» غير صحيحة، "
                    "وقد لا يكون البروتين الناتج عن ذلك وظيفيًا. ومع ذلك، "
                    "فإن بعض التغيرات الجينية لا تسبب أي مرض."
                ),
            },

            {
                "type": "paragraph",
                "text": "الشكل 4: التغيرات الجينية.",
            },

            {
                "type": "image",
                "image": "articles/source/fig04.gif",
                "image_caption": "الشكل 4: التغيرات الجينية.",
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
                    "للعدوى بفيروس نقص المناعة البشرية، وهو مستقل عن درجة "
                    "نقص المناعة، لكنه يؤدي إلى تفاقم كبير في تشخيص وحالة "
                    "المرضى المصابين بالفيروس."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "يمكن أن يصيب المرض جميع الفئات المعرضة لخطر الإصابة "
                    "بفيروس نقص المناعة البشرية، إلا أن الأشخاص الذين يتعاطون "
                    "المخدرات بالحقن كانوا من أكثر الفئات المعنية في المصادر "
                    "القديمة، حيث كانوا يمثلون نسبة كبيرة من الحالات."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "يُشخّص ارتفاع ضغط الدم الشرياني الرئوي في المتوسط بعد "
                    "2.5 إلى 3 سنوات من اكتشاف الإصابة بفيروس نقص المناعة "
                    "البشرية، لكنه قد يكون أيضًا أول علامة تكشف الإصابة. "
                    "ولهذا يمكن أن يطلب الطبيب إجراء اختبار فيروس نقص المناعة "
                    "البشرية ضمن التقييم الأولي لبعض حالات ارتفاع ضغط الدم "
                    "الشرياني الرئوي مجهول السبب."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "تتشابه الصورة السريرية مع ارتفاع ضغط الدم الشرياني "
                    "الرئوي مجهول السبب، ويتم التشخيص بالطريقة نفسها، "
                    "ومن بينها قسطرة القلب اليمنى."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "في الحالات المقاومة للعلاج رغم تطبيق العلاج التقليدي "
                    "المناسب، يمكن أن يشمل العلاج مضادات الفيروسات القهقرية "
                    "وعلاجات مخصصة لارتفاع ضغط الدم الشرياني الرئوي، وذلك "
                    "وفق تقييم الطبيب المتخصص وحالة المريض."
                ),
            },

            # ==========================================================
            # GENETIC ANOMALIES
            # ==========================================================

            {
                "type": "heading",
                "title": "التغيرات الجينية المرتبطة بحدوث ارتفاع ضغط الدم الشرياني الرئوي",
            },

            {
                "type": "paragraph",
                "text": (
                    "تم وصف أول شكل عائلي من المرض من طرف Dresdale وزملائه "
                    "عام 1954. وفي عام 2000، حدد فريقان بحثيان أول طفرة، "
                    "أو تغير جيني، في جين BMPR2 المسؤول عن المرض. يقع هذا "
                    "الجين على الكروموسوم 2."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "وفي عامي 2001 و2003، ساهمت ملاحظة حدوث ارتفاع ضغط الدم "
                    "الشرياني الرئوي لدى مرضى داء Rendu-Osler، مع معرفة الجينات "
                    "المسؤولة عن هذا المرض، في تحديد جينين آخرين من جينات "
                    "الاستعداد للإصابة بالمرض."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "وفي عام 2012 تم تحديد جين آخر مرتبط بالاستعداد للإصابة "
                    "بارتفاع ضغط الدم الشرياني الرئوي، وهو Caveolin-1. "
                    "وتُعد التغيرات في هذا الجين نادرة جدًا."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "وفي عام 2013 تم إثبات مشاركة جين KCNK3 في تطور المرض. "
                    "وهكذا تم تحديد عدة جينات مرتبطة بحدوث ارتفاع ضغط الدم "
                    "الشرياني الرئوي، إلا أن الطفرات في جين BMPR2 تظل الأكثر شيوعًا."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "الشكل 5: النمط النووي البشري. يتكون الجينوم البشري من "
                    "23 زوجًا من الكروموسومات. يتكون كل زوج من كروموسوم أبوي "
                    "وكروموسوم أمومي. يقع جين BMPR2 على الكروموسوم 2. "
                    "وبالتالي يمتلك كل إنسان نسختين من هذا الجين، واحدة على "
                    "كل كروموسوم 2."
                ),
            },

            {
                "type": "image",
                "image": "articles/source/fig05.jpg",
                "image_caption": "الشكل 5: النمط النووي البشري وموقع جين BMPR2.",
            },

            # ==========================================================
            # FUNCTION OF GENES
            # ==========================================================

            {
                "type": "heading",
                "title": "وظيفة جينات الاستعداد للإصابة بارتفاع ضغط الدم الشرياني الرئوي",
            },

            {
                "type": "paragraph",
                "text": (
                    "تشارك جينات الاستعداد للإصابة بارتفاع ضغط الدم الشرياني "
                    "الرئوي في تنظيم نمو خلايا الشرايين الرئوية. وقد تؤدي "
                    "الطفرات في هذه الجينات إلى تكاثر غير طبيعي لخلايا "
                    "الشرايين الرئوية، مما قد يؤدي إلى تضيق الأوعية الدموية "
                    "وانسدادها."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "الأشخاص الذين يحملون طفرة في أحد هذه الجينات يكونون "
                    "أكثر استعدادًا للإصابة بارتفاع ضغط الدم الشرياني الرئوي."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "تم العثور على طفرات في أحد جينات الاستعداد لدى نحو 20% "
                    "من المرضى المصابين بارتفاع ضغط الدم الشرياني الرئوي "
                    "مجهول السبب، ونحو 85% من المرضى الذين لديهم شكل عائلي "
                    "من المرض."
                ),
            },

            # ==========================================================
            # TRANSMISSION
            # ==========================================================

            {
                "type": "heading",
                "title": "الانتقال الوراثي لارتفاع ضغط الدم الشرياني الرئوي",
            },

            {
                "type": "paragraph",
                "text": (
                    "بما أن لدينا جميعًا نسختين من كل كروموسوم، واحدة موروثة "
                    "من الأم وأخرى من الأب، فإن لدينا نسختين من جينات مثل "
                    "BMPR2 وALK1 وKCNK3."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "عند تكوّن الطفل، يرث لكل زوج من الكروموسومات كروموسومًا "
                    "واحدًا من الأب وكروموسومًا واحدًا من الأم. وعندما يكون "
                    "أحد الوالدين حاملًا لتغير جيني في أحد هذه الجينات، "
                    "فإن لكل طفل احتمالًا يبلغ 50% لوراثة التغير الجيني العائلي."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "قد يرث الطفل من الوالد الحامل للطفرة الكروموسوم الذي "
                    "يحمل الجين المتغير أو الكروموسوم الذي يحمل النسخة "
                    "غير المتغيرة."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "في الشكل الوراثي لارتفاع ضغط الدم الشرياني الرئوي، "
                    "يُعد المرض من الأمراض ذات الانتقال الجسدي، أي يمكن أن "
                    "يصيب النساء والرجال، وسائدًا، أي إن وجود تغير جيني واحد "
                    "قد يمنح الشخص قابلية للإصابة، مع نفوذية غير كاملة، "
                    "أي أن الشخص قد يكون حاملًا للتغير الجيني دون أن يصاب "
                    "بالمرض طوال حياته."
                ),
            },

            {
                "type": "image",
                "image": "articles/source/Génétique.jpg",
                "image_caption": "التوارث الجيني لارتفاع ضغط الدم الشرياني الرئوي.",
            },

            {
                "type": "paragraph",
                "text": (
                    "وبالنسبة إلى جين BMPR2، يُقدّر خطر الإصابة لدى الرجال "
                    "الحاملين لتغير جيني بنحو 14%، بينما يُقدّر لدى النساء "
                    "بنحو 42%. وهذه النسب تقديرات إحصائية وليست تنبؤًا "
                    "بمصير فرد معين."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "أما خطر الإصابة لدى الأشخاص الحاملين لطفرات في جينات "
                    "KCNK3 وCaveolin-1 وALK1 وEndoglin فلم يُحدد بدقة حتى الآن، "
                    "لأن هذه التغيرات نادرة جدًا."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "يمكن أيضًا لأبناء الأشخاص الحاملين لتغير جيني، سواء كانوا "
                    "مصابين بالمرض أم غير مصابين، أن يرثوا هذا التغير الجيني."
                ),
            },

            # ==========================================================
            # VARIABLE GENETIC RISK
            # ==========================================================

            {
                "type": "heading",
                "title": "خطر وراثي يختلف حسب مجموعات ارتفاع ضغط الدم الشرياني الرئوي",
            },

            {
                "type": "paragraph",
                "text": (
                    "قد يكون ارتفاع ضغط الدم الشرياني الرئوي مرتبطًا بمرض "
                    "آخر، مثل ارتفاع ضغط الدم البابي أو فيروس نقص المناعة "
                    "البشرية أو أمراض القلب الخلقية أو أمراض النسيج الضام، "
                    "كما قد يحدث دون سبب واضح."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "ولا يكون الخطر الوراثي متساويًا في جميع مجموعات المرض. "
                    "لذلك يختلف الفحص الجيني حسب الحالة، سواء كان المرض "
                    "عائليًا أو مجهول السبب أو مرتبطًا بمرض آخر."
                ),
            },

            # ==========================================================
            # FAMILIAL PAH
            # ==========================================================

            {
                "type": "heading",
                "title": "ارتفاع ضغط الدم الشرياني الرئوي العائلي",
            },

            {
                "type": "paragraph",
                "text": (
                    "في مركزنا المرجعي، يتم العثور على طفرة في أحد جينات "
                    "الاستعداد للإصابة بارتفاع ضغط الدم الشرياني الرئوي "
                    "(BMPR2 وKCNK3 وCaveolin-1 وALK1 وEndoglin) لدى نحو 85% "
                    "من المرضى المصابين بالشكل العائلي."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "وفي نحو 15% من الحالات لا يمكن تحديد تغير جيني، إذ قد "
                    "تفوت التقنيات الحالية بعض الطفرات، كما قد توجد جينات "
                    "أخرى مسؤولة عن المرض لم يتم اكتشافها بعد."
                ),
            },

            # ==========================================================
            # IDIOPATHIC
            # ==========================================================

            {
                "type": "heading",
                "title": "ارتفاع ضغط الدم الشرياني الرئوي مجهول السبب",
            },

            {
                "type": "paragraph",
                "text": (
                    "في هذه الحالة يتطور المرض لدى أشخاص لا توجد لديهم عوامل "
                    "خطر واضحة، مثل تناول أدوية كابحة للشهية أو وجود مرض "
                    "من أمراض النسيج الضام أو ارتفاع ضغط الدم البابي أو "
                    "مرض قلبي خلقي."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "أظهرت دراسة أجراها فريق Bicêtre أن نحو 20% من المرضى "
                    "المصابين بارتفاع ضغط الدم الشرياني الرئوي مجهول السبب "
                    "يحملون تغيرًا جينيًا في أحد جينات الاستعداد المعروفة."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "ومن المهم الإشارة إلى أن التمييز بين المرضى المصابين "
                    "بالشكل العائلي والمرضى المصابين بالشكل مجهول السبب "
                    "والحاملين لطفرة قد يكون اصطناعيًا، لأن الحالتين قد "
                    "تمثلان الشكل الوراثي للمرض."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "وقد يكون المريض المصاب بارتفاع ضغط الدم الشرياني الرئوي "
                    "مجهول السبب والحامل لطفرة في جين BMPR2 أول حالة يتم "
                    "تشخيصها في عائلته. ولذلك يُستخدم بشكل متزايد مصطلح "
                    "«ارتفاع ضغط الدم الشرياني الرئوي الوراثي» لوصف هذا الشكل."
                ),
            },

            # ==========================================================
            # ASSOCIATED PAH
            # ==========================================================

            {
                "type": "heading",
                "title": "ارتفاع ضغط الدم الشرياني الرئوي المرتبط بأمراض أخرى",
            },

            {
                "type": "paragraph",
                "text": (
                    "في حالات ارتفاع ضغط الدم الشرياني الرئوي المرتبط "
                    "باستخدام أدوية كابحة للشهية، وُجدت طفرة في جين BMPR2 "
                    "لدى نسبة من المرضى."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "أما في بقية الأمراض المرتبطة بارتفاع ضغط الدم الشرياني "
                    "الرئوي، مثل ارتفاع ضغط الدم البابي وفيروس نقص المناعة "
                    "البشرية وأمراض القلب الخلقية وأمراض النسيج الضام، فلم "
                    "يتم حتى الآن تحديد طفرات مؤكدة في جينات الاستعداد "
                    "المعروفة للمرض."
                ),
            },

            # ==========================================================
            # RENDU-OSLER
            # ==========================================================

            {
                "type": "heading",
                "title": "ارتفاع ضغط الدم الشرياني الرئوي ومرض Rendu-Osler",
            },

            {
                "type": "paragraph",
                "text": (
                    "يتميز مرض Rendu-Osler بوجود تغيرات في الأوعية الدموية، "
                    "ولا سيما الوصلات الشريانية الوريدية التي قد تكون موجودة "
                    "في الرئتين."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "وقد تبين أن الأشخاص الحاملين لطفرة في أحد الجينات "
                    "المرتبطة بمرض Rendu-Osler، مثل ACVRL1 أو Endoglin، "
                    "يمكن أن يصابوا بارتفاع ضغط الدم الشرياني الرئوي."
                ),
            },

            # ==========================================================
            # RELATIVES
            # ==========================================================

            {
                "type": "heading",
                "title": "الخطر بالنسبة إلى أفراد العائلة",
            },

            {
                "type": "paragraph",
                "text": (
                    "عندما يتم تحديد تغير جيني لدى أحد المرضى، فقد يكون "
                    "أفراد عائلته حاملين للتغير الجيني نفسه، وبالتالي قد "
                    "يكون لديهم خطر متزايد للإصابة بارتفاع ضغط الدم الشرياني "
                    "الرئوي. ويمكن معرفة الحالة الجينية من خلال اختبار جيني "
                    "مناسب."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "ومن بين الأشخاص غير المصابين الذين لديهم والد أو قريب "
                    "حامل لطفرة في جين BMPR2، يُقدّر خطر الإصابة لدى الرجال "
                    "الحاملين للطفرة بنحو 14%، بينما يُقدّر لدى النساء بنحو 42%."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "أما الأشخاص الذين لا يحملون الطفرة العائلية المحددة، "
                    "فلا يكون لديهم الخطر الوراثي الخاص بهذه الطفرة، وكذلك "
                    "لا يرث أطفالهم هذه الطفرة."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "ولا يزال خطر الإصابة لدى حاملي طفرات KCNK3 وCaveolin-1 "
                    "وALK1 وEndoglin غير محدد بدقة بسبب ندرة هذه التغيرات."
                ),
            },

            # ==========================================================
            # GENETIC COUNSELING
            # ==========================================================

            {
                "type": "heading",
                "title": "الاستشارة الوراثية",
            },

            {
                "type": "paragraph",
                "text": (
                    "تُقترح الاستشارة الوراثية بشكل منتظم للمرضى المصابين "
                    "بارتفاع ضغط الدم الشرياني الرئوي مجهول السبب أو العائلي، "
                    "وكذلك في بعض الحالات المرتبطة باستخدام أدوية كابحة "
                    "للشهية. كما يمكن أن تكون متاحة لأفراد عائلات المرضى "
                    "الذين تم تحديد طفرة لديهم في أحد جينات الاستعداد "
                    "المعروفة."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "خلال السنوات الاثنتي عشرة الماضية، تم استقبال أكثر من "
                    "500 مريض مصاب بارتفاع ضغط الدم الشرياني الرئوي وأكثر "
                    "من 200 فرد من عائلاتهم في إطار الاستشارة الوراثية."
                ),
            },

            # ==========================================================
            # GENETIC CONSULTATION PROCESS
            # ==========================================================

            {
                "type": "heading",
                "title": "كيفية إجراء الاستشارة الوراثية",
            },

            {
                "type": "paragraph",
                "text": (
                    "خلال الاستشارة الوراثية الأولى، يتم شرح آلية المرض "
                    "والانتقال الوراثي واحتمال حمل تغير جيني في أحد جينات "
                    "الاستعداد للإصابة بارتفاع ضغط الدم الشرياني الرئوي، "
                    "وكذلك خطر إصابة أفراد العائلة."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "بعد هذه الاستشارة الأولى، يمكن اقتراح الاختبار الجيني، "
                    "مع توضيح فوائد معرفة الحالة الجينية والسلبيات المحتملة. "
                    "ويحق للشخص تعليق الإجراءات مؤقتًا أو نهائيًا في أي مرحلة."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "إذا رغب الشخص في إجراء الاختبار، يتم توقيع الموافقة "
                    "المستنيرة ثم تُجرى عملية أخذ عينة الدم."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "بعد انتهاء التحليل، والذي قد يستغرق عدة أشهر للشخص "
                    "الأول الذي يتم اختباره في العائلة ووقتًا أقصر للأشخاص "
                    "الآخرين عند البحث عن الطفرة العائلية المعروفة، يتم "
                    "إبلاغ الشخص بتوفر النتيجة."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "خلال الاستشارة الوراثية الثانية، يتم شرح النتيجة "
                    "والمعلومات المناسبة للشخص من طرف الفريق المختص."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "وبعد ذلك قد يتم إجراء عينة تأكيدية، ثم تُسلّم النتيجة "
                    "المؤكدة خلال استشارة لاحقة."
                ),
            },

            # ==========================================================
            # MVO
            # ==========================================================

            {
                "type": "heading",
                "title": "المرض الوريدي الانسدادي الرئوي (MVO)",
            },

            {
                "type": "paragraph",
                "text": (
                    "المرض الوريدي الانسدادي الرئوي هو شكل نادر من ارتفاع "
                    "ضغط الدم الرئوي، يتميز بإصابة أساسية في الأوردة الرئوية "
                    "الصغيرة، على خلاف ارتفاع ضغط الدم الشرياني الرئوي الذي "
                    "يصيب بصورة أساسية الشرايين الرئوية الصغيرة."
                ),
            },

            {
                "type": "heading",
                "title": "المرض الوريدي الانسدادي الرئوي وطفرات جين EIF2AK4",
            },

            {
                "type": "paragraph",
                "text": (
                    "تم العثور على طفرات في نسختي جين EIF2AK4، واحدة موروثة "
                    "من الأب وأخرى من الأم، لدى نحو 25% من المرضى المصابين "
                    "بالشكل المتفرق من المرض الوريدي الانسدادي الرئوي."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "كما توجد هذه الطفرات لدى الغالبية العظمى من المرضى "
                    "المصابين بالشكل العائلي للمرض."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "الأشخاص الذين يحملون طفرات في نسختي جين EIF2AK4، أي "
                    "الذين لا يمتلكون نسخة وظيفية من الجين، يكونون أكثر "
                    "استعدادًا للإصابة بالمرض الوريدي الانسدادي الرئوي."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "أما الأشخاص الذين يحملون طفرة واحدة فقط في إحدى نسختي "
                    "جين EIF2AK4، فتشير المعارف الحالية إلى أن ذلك لا يكفي "
                    "بحد ذاته لزيادة خطر الإصابة بالمرض بشكل واضح."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "الشكل 7: النمط النووي البشري. يتكون الجينوم البشري من "
                    "23 زوجًا من الكروموسومات، ويتكون كل زوج من كروموسوم أبوي "
                    "وآخر أمومي. يقع جين EIF2AK4 على الكروموسوم 15، ولذلك "
                    "يمتلك كل إنسان نسختين من هذا الجين."
                ),
            },

            {
                "type": "image",
                "image": "articles/source/MVO.png",
                "image_caption": (
                    "المرض الوريدي الانسدادي الرئوي والاختلافات الجينية."
                ),
            },

            # ==========================================================
            # MVO TRANSMISSION
            # ==========================================================

            {
                "type": "heading",
                "title": "الانتقال الوراثي للمرض الوريدي الانسدادي الرئوي",
            },

            {
                "type": "paragraph",
                "text": (
                    "بما أن جميع الأشخاص يمتلكون نسختين من كل كروموسوم، "
                    "فإننا نمتلك نسختين من جين EIF2AK4، واحدة موروثة من الأم "
                    "وأخرى من الأب."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "عند تكوّن الطفل، يرث لكل زوج من الكروموسومات كروموسومًا "
                    "واحدًا من الأب وواحدًا من الأم."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "عندما يكون كلا الوالدين حاملًا لطفرة واحدة في جين "
                    "EIF2AK4، يكون لكل طفل احتمال يبلغ 25% لوراثة الطفرتين، "
                    "أي طفرة من كل والد."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "يمكن للطفل أن يرث من كل والد الكروموسوم الذي يحمل الجين "
                    "المتغير أو الكروموسوم الذي يحمل النسخة غير المتغيرة، "
                    "وبالتالي توجد أربع احتمالات وراثية."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "الشكل 8: انتقال طفرات EIF2AK4."
                ),
            },

            {
                "type": "image",
                "image": "articles/source/888.png",
                "image_caption": "الشكل 8: انتقال طفرات EIF2AK4.",
            },

            {
                "type": "paragraph",
                "text": (
                    "عندما يكون الشخص حاملًا لطفرتين في جين EIF2AK4، فإن "
                    "أطفاله سيرثون منه بالضرورة نسخة واحدة متغيرة من الجين، "
                    "لكن وجود طفرة واحدة لا يكفي عادةً لزيادة الاستعداد "
                    "للإصابة بالمرض."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "تُعد طفرة EIF2AK4 نادرة جدًا في عامة السكان، ولذلك يكون "
                    "احتمال أن يكون الوالد الآخر حاملًا لطفرة في الجين نفسه "
                    "منخفضًا. وقد يختلف هذا الاحتمال في حالات زواج الأقارب، "
                    "حيث يمكن أن يكون الوالد الآخر حاملًا للتغير الجيني "
                    "العائلي نفسه."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "الشكل 9: انتقال التغير الجيني من أحد الوالدين إلى الأطفال."
                ),
            },

            {
                "type": "image",
                "image": "articles/source/777.png",
                "image_caption": (
                    "الشكل 9: انتقال التغير الجيني من أحد الوالدين إلى الأطفال."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "في شكله الوراثي، يُعد المرض الوريدي الانسدادي الرئوي "
                    "مرضًا ذا انتقال جسدي، أي يمكن أن يصيب النساء والرجال، "
                    "ومتنحيًا، أي إن وجود تغيرين جينيين في نسختي EIF2AK4 "
                    "هو الذي يرتبط بخطر الإصابة بالمرض."
                ),
            },

            # ==========================================================
            # MVO GENETIC COUNSELING
            # ==========================================================

            {
                "type": "heading",
                "title": "الاستشارة الوراثية للمرض الوريدي الانسدادي الرئوي",
            },

            {
                "type": "paragraph",
                "text": (
                    "تُقترح الاستشارة الوراثية للمرضى المصابين بالمرض الوريدي "
                    "الانسدادي الرئوي، سواء كانت لديهم قصة عائلية للمرض أم لا."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "كما يمكن أن تكون الاستشارة متاحة لإخوة وأخوات المرضى "
                    "الذين تم تحديد طفرتين لديهم في جيني EIF2AK4."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "خلال الاستشارة الوراثية الأولى، يتم شرح آلية المرض "
                    "والانتقال الوراثي واحتمال حمل تغيرات جينية في جين "
                    "EIF2AK4، وكذلك المخاطر المحتملة بالنسبة إلى أفراد العائلة."
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

        translation, created = ArticleTranslation.objects.get_or_create(
            article=article,
            language="en",
            defaults={
                "title": "Genetics and Pulmonary Arterial Hypertension",
                "excerpt": (
                    "Understanding the role of genetics in pulmonary arterial "
                    "hypertension, genetic mutations, their transmission, and "
                    "genetic counseling."
                ),
                "meta_title": (
                    "Genetics and Pulmonary Arterial Hypertension | HTAP Algérie"
                ),
                "meta_description": (
                    "Information about genetics and pulmonary arterial hypertension, "
                    "predisposition genes, genetic transmission, and genetic counseling."
                ),
            },
        )

        # Avoid duplicate blocks when running the command again.
        ArticleBlock.objects.filter(
            translation=translation
        ).delete()

        blocks = [

            # ==========================================================
            # INTRODUCTION
            # ==========================================================

            {
                "type": "heading",
                "title": "Genetics and Pulmonary Arterial Hypertension",
            },

            {
                "type": "heading",
                "title": "Genetics in Pictures",
            },

            {
                "type": "paragraph",
                "text": (
                    "Each individual is made up of several million cells. Each cell "
                    "contains 46 chromosomes organized into 23 pairs inside its "
                    "nucleus (Figure 1)."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Each pair of chromosomes consists of one chromosome inherited "
                    "from the mother and one chromosome inherited from the father. "
                    "Therefore, chromosomes are present in two copies."
                ),
            },

            {
                "type": "paragraph",
                "text": "Figure 1: The cell.",
            },

            {
                "type": "image",
                "image": "articles/source/fig01.gif",
                "image_caption": "Figure 1: The cell.",
            },

            {
                "type": "paragraph",
                "text": (
                    "Each chromosome consists of several genes, represented by "
                    "different colors in Figure 2. Each gene has a specific function "
                    "(such as eye color, lung development, height, and others). "
                    "Humans have approximately 30,000 different genes. Several genes "
                    "are required for the formation of an organ."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Figure 2: Example of three different pairs of chromosomes."
                ),
            },

            {
                "type": "image",
                "image": "articles/source/fig02.gif",
                "image_caption": (
                    "Figure 2: Example of three different pairs of chromosomes."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "A gene can be compared to an encyclopedia containing instructions "
                    "for producing a protein, an active molecule that performs an "
                    "important function within the cell and therefore within the human body."
                ),
            },

            {
                "type": "paragraph",
                "text": "Figure 3: Genes.",
            },

            {
                "type": "image",
                "image": "articles/source/fig_3.gif",
                "image_caption": "Figure 3: Genes.",
            },

            {
                "type": "paragraph",
                "text": (
                    "A genetic abnormality, or mutation, is an error in these "
                    "instructions. As a result, the information contained in this "
                    "“encyclopedia” may be incorrect, and the resulting protein may "
                    "not be functional. However, some genetic changes do not cause disease."
                ),
            },

            {
                "type": "paragraph",
                "text": "Figure 4: Genetic abnormalities.",
            },

            {
                "type": "image",
                "image": "articles/source/fig04.gif",
                "image_caption": "Figure 4: Genetic abnormalities.",
            },

            # ==========================================================
            # HIV
            # ==========================================================

            {
                "type": "heading",
                "title": "Pulmonary Arterial Hypertension Associated with HIV",
            },

            {
                "type": "paragraph",
                "text": (
                    "Pulmonary arterial hypertension is a rare manifestation of "
                    "human immunodeficiency virus (HIV) infection. It is independent "
                    "of the degree of immunodeficiency but can significantly worsen "
                    "the prognosis of affected patients."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "It can affect all groups at risk of HIV infection. According to "
                    "older sources, people who inject drugs were among the groups "
                    "frequently affected and represented a significant proportion "
                    "of cases."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Pulmonary arterial hypertension is diagnosed on average 2.5 to "
                    "3 years after HIV infection is discovered, but it may also be "
                    "the first manifestation revealing the infection. Therefore, "
                    "HIV testing may be requested as part of the initial assessment "
                    "of some patients with apparently idiopathic pulmonary arterial hypertension."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "The clinical presentation is similar to that of idiopathic "
                    "pulmonary arterial hypertension, and diagnosis is performed in "
                    "the same way, including right heart catheterization."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "In cases resistant to treatment despite appropriate conventional "
                    "therapy, treatment may include antiretroviral therapy and specific "
                    "therapies for pulmonary arterial hypertension, according to the "
                    "assessment of the specialist and the patient's condition."
                ),
            },

            # ==========================================================
            # GENETIC ANOMALIES
            # ==========================================================

            {
                "type": "heading",
                "title": (
                    "Genetic Changes Associated with the Development "
                    "of Pulmonary Arterial Hypertension"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "The first familial form of the disease was described by Dresdale "
                    "and colleagues in 1954. In 2000, two research teams identified "
                    "the first mutation, or genetic change, in the BMPR2 gene "
                    "responsible for the disease. This gene is located on chromosome 2."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "In 2001 and 2003, observations of pulmonary arterial hypertension "
                    "in patients with Rendu-Osler disease, together with knowledge of "
                    "the genes responsible for that disease, led to the identification "
                    "of two additional pulmonary arterial hypertension predisposition genes."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "In 2012, another gene associated with predisposition to pulmonary "
                    "arterial hypertension was identified: Caveolin-1. Changes in this "
                    "gene are very rare."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "In 2013, the involvement of the KCNK3 gene in the development of "
                    "the disease was demonstrated. Several genes associated with the "
                    "development of pulmonary arterial hypertension have therefore been "
                    "identified, although mutations in the BMPR2 gene remain the most common."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Figure 5: Human karyotype. The human genome consists of 23 pairs "
                    "of chromosomes. Each pair consists of a paternal chromosome and "
                    "a maternal chromosome. The BMPR2 gene is located on chromosome 2. "
                    "Every person therefore has two copies of this gene, one on each "
                    "chromosome 2."
                ),
            },

            {
                "type": "image",
                "image": "articles/source/fig05.jpg",
                "image_caption": (
                    "Figure 5: Human karyotype and location of the BMPR2 gene."
                ),
            },

            # ==========================================================
            # FUNCTION OF GENES
            # ==========================================================

            {
                "type": "heading",
                "title": (
                    "Function of Genes Predisposing to Pulmonary Arterial Hypertension"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Genes that predispose to pulmonary arterial hypertension are "
                    "involved in regulating the growth of pulmonary artery cells. "
                    "Mutations in these genes may cause abnormal proliferation of "
                    "pulmonary artery cells, which can lead to narrowing and blockage "
                    "of the blood vessels."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "People carrying a mutation in one of these genes have an increased "
                    "predisposition to developing pulmonary arterial hypertension."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Mutations in one of the predisposition genes have been identified "
                    "in approximately 20% of patients with idiopathic pulmonary arterial "
                    "hypertension and approximately 85% of patients with familial disease."
                ),
            },

            # ==========================================================
            # TRANSMISSION
            # ==========================================================

            {
                "type": "heading",
                "title": "Genetic Transmission of Pulmonary Arterial Hypertension",
            },

            {
                "type": "paragraph",
                "text": (
                    "Because we all have two copies of each chromosome, one inherited "
                    "from our mother and one from our father, we have two copies of "
                    "genes such as BMPR2, ALK1, and KCNK3."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "When a child is conceived, they inherit one chromosome from the "
                    "father and one chromosome from the mother for each chromosome pair. "
                    "When one parent carries a genetic change in one of these genes, "
                    "each child has a 50% chance of inheriting the familial genetic change."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "The child may inherit either the chromosome carrying the altered "
                    "gene or the chromosome carrying the unchanged version from the "
                    "parent who carries the mutation."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "In its hereditary form, pulmonary arterial hypertension is an "
                    "autosomal disease, meaning that it can affect both women and men; "
                    "dominant, meaning that one genetic change may confer a risk of "
                    "developing the disease; and incompletely penetrant, meaning that "
                    "a person may carry the genetic change without ever developing the disease."
                ),
            },

            {
                "type": "image",
                "image": "articles/source/Génétique.jpg",
                "image_caption": (
                    "Genetic inheritance of pulmonary arterial hypertension."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "For the BMPR2 gene, the estimated risk of developing the disease "
                    "is approximately 14% for men carrying a genetic change and "
                    "approximately 42% for women carrying a genetic change. These are "
                    "statistical estimates and do not predict the outcome for a specific individual."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "The risk of developing the disease in people carrying mutations "
                    "in KCNK3, Caveolin-1, ALK1, or Endoglin has not yet been precisely "
                    "determined because these genetic changes are very rare."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Children of people carrying a genetic change, whether or not "
                    "they themselves have the disease, may also inherit the genetic change."
                ),
            },

            # ==========================================================
            # VARIABLE GENETIC RISK
            # ==========================================================

            {
                "type": "heading",
                "title": (
                    "Genetic Risk Varies According to the Pulmonary Arterial "
                    "Hypertension Subgroup"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Pulmonary arterial hypertension may be associated with another "
                    "condition, such as portal hypertension, HIV infection, congenital "
                    "heart disease, or connective tissue disease, or it may occur "
                    "without an apparent cause."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Genetic risk is not the same across all disease subgroups. "
                    "Therefore, genetic testing differs depending on the situation, "
                    "whether the disease is familial, idiopathic, or associated with another condition."
                ),
            },

            # ==========================================================
            # FAMILIAL PAH
            # ==========================================================

            {
                "type": "heading",
                "title": "Familial Pulmonary Arterial Hypertension",
            },

            {
                "type": "paragraph",
                "text": (
                    "At our reference center, a mutation in one of the genes "
                    "predisposing to pulmonary arterial hypertension (BMPR2, KCNK3, "
                    "Caveolin-1, ALK1, or Endoglin) is identified in approximately "
                    "85% of patients with the familial form."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "In approximately 15% of cases, no genetic change can be identified. "
                    "Current techniques may fail to detect certain mutations, and there "
                    "may also be other disease-causing genes that have not yet been discovered."
                ),
            },

            # ==========================================================
            # IDIOPATHIC
            # ==========================================================

            {
                "type": "heading",
                "title": "Idiopathic Pulmonary Arterial Hypertension",
            },

            {
                "type": "paragraph",
                "text": (
                    "In this situation, the disease develops in people who have no "
                    "obvious risk factors, such as the use of appetite-suppressant "
                    "medications, connective tissue disease, portal hypertension, "
                    "or congenital heart disease."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "A study conducted by the Bicêtre team showed that approximately "
                    "20% of patients with idiopathic pulmonary arterial hypertension "
                    "carry a genetic change in one of the known predisposition genes."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "It is important to note that the distinction between patients "
                    "with familial disease and patients with idiopathic disease who "
                    "carry a mutation may be artificial, because both situations may "
                    "represent the hereditary form of the disease."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "A patient with idiopathic pulmonary arterial hypertension who "
                    "carries a BMPR2 mutation may be the first diagnosed case in "
                    "their family. Therefore, the term “hereditary pulmonary arterial "
                    "hypertension” is increasingly used to describe this genetic form."
                ),
            },

            # ==========================================================
            # ASSOCIATED PAH
            # ==========================================================

            {
                "type": "heading",
                "title": "Pulmonary Arterial Hypertension Associated with Other Conditions",
            },

            {
                "type": "paragraph",
                "text": (
                    "In cases of pulmonary arterial hypertension associated with the "
                    "use of appetite-suppressant medications, BMPR2 mutations have "
                    "been identified in a proportion of patients."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "For other conditions associated with pulmonary arterial hypertension, "
                    "such as portal hypertension, HIV infection, congenital heart disease, "
                    "and connective tissue diseases, no confirmed mutations in the known "
                    "pulmonary arterial hypertension predisposition genes have been "
                    "identified to date."
                ),
            },

            # ==========================================================
            # RENDU-OSLER
            # ==========================================================

            {
                "type": "heading",
                "title": "Pulmonary Arterial Hypertension and Rendu-Osler Disease",
            },

            {
                "type": "paragraph",
                "text": (
                    "Rendu-Osler disease is characterized by abnormalities of the blood "
                    "vessels, particularly arteriovenous malformations, which may occur "
                    "in the lungs."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "People carrying a mutation in one of the genes associated with "
                    "Rendu-Osler disease, such as ACVRL1 or Endoglin, may develop "
                    "pulmonary arterial hypertension."
                ),
            },

            # ==========================================================
            # RELATIVES
            # ==========================================================

            {
                "type": "heading",
                "title": "Risk for Family Members",
            },

            {
                "type": "paragraph",
                "text": (
                    "When a genetic change is identified in a patient, family members "
                    "may carry the same genetic change and may therefore have an "
                    "increased risk of developing pulmonary arterial hypertension. "
                    "Their genetic status can be determined through appropriate genetic testing."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Among unaffected people who have a parent or relative carrying "
                    "a BMPR2 mutation, the estimated risk of developing the disease "
                    "is approximately 14% for men carrying the mutation and "
                    "approximately 42% for women carrying the mutation."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "People who do not carry the identified familial mutation do not "
                    "have the genetic risk associated with that specific mutation, "
                    "and their children do not inherit that mutation from them."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "The risk of developing the disease among carriers of KCNK3, "
                    "Caveolin-1, ALK1, and Endoglin mutations has not yet been precisely "
                    "determined because these genetic changes are rare."
                ),
            },

            # ==========================================================
            # GENETIC COUNSELING
            # ==========================================================

            {
                "type": "heading",
                "title": "Genetic Counseling",
            },

            {
                "type": "paragraph",
                "text": (
                    "Genetic counseling is routinely offered to patients with "
                    "idiopathic or familial pulmonary arterial hypertension, as well "
                    "as in certain cases associated with the use of appetite-suppressant "
                    "medications. It may also be available to family members of patients "
                    "in whom a mutation has been identified in one of the known "
                    "predisposition genes."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Over the past 12 years, more than 500 patients with pulmonary "
                    "arterial hypertension and more than 200 family members have "
                    "received genetic counseling."
                ),
            },

            # ==========================================================
            # GENETIC CONSULTATION PROCESS
            # ==========================================================

            {
                "type": "heading",
                "title": "How Genetic Counseling Works",
            },

            {
                "type": "paragraph",
                "text": (
                    "During the first genetic counseling consultation, the disease "
                    "mechanism, genetic transmission, the possibility of carrying a "
                    "genetic change in one of the pulmonary arterial hypertension "
                    "predisposition genes, and the potential risk to family members "
                    "are explained."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "After this first consultation, genetic testing may be proposed, "
                    "with an explanation of the benefits and potential disadvantages "
                    "of knowing one's genetic status. The person has the right to "
                    "temporarily or permanently stop the process at any stage."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "If the person wishes to undergo testing, informed consent is "
                    "signed and a blood sample is collected."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Once the analysis is completed, which may take several months "
                    "for the first person tested in a family and less time for other "
                    "family members when the familial mutation is already known, "
                    "the person is informed that the result is available."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "During the second genetic counseling consultation, the result "
                    "and appropriate information are explained by the specialist team."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "A confirmatory sample may then be collected, and the confirmed "
                    "result is provided during a subsequent consultation."
                ),
            },

            # ==========================================================
            # PVOD
            # ==========================================================

            {
                "type": "heading",
                "title": "Pulmonary Veno-Occlusive Disease (PVOD)",
            },

            {
                "type": "paragraph",
                "text": (
                    "Pulmonary veno-occlusive disease is a rare form of pulmonary "
                    "hypertension characterized primarily by involvement of the small "
                    "pulmonary veins, unlike pulmonary arterial hypertension, which "
                    "primarily affects the small pulmonary arteries."
                ),
            },

            {
                "type": "heading",
                "title": "Pulmonary Veno-Occlusive Disease and EIF2AK4 Mutations",
            },

            {
                "type": "paragraph",
                "text": (
                    "Mutations in both copies of the EIF2AK4 gene, one inherited "
                    "from the father and one from the mother, are found in approximately "
                    "25% of patients with sporadic pulmonary veno-occlusive disease."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "They are also found in the vast majority of patients with "
                    "the familial form of the disease."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "People carrying mutations in both copies of the EIF2AK4 gene, "
                    "meaning that they do not have a functional copy of the gene, "
                    "have a predisposition to developing pulmonary veno-occlusive disease."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "For people carrying only one mutation in one copy of EIF2AK4, "
                    "current knowledge suggests that this alone does not clearly "
                    "increase the risk of developing pulmonary veno-occlusive disease."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Figure 7: Human karyotype. The human genome consists of 23 pairs "
                    "of chromosomes. Each pair consists of a paternal and a maternal "
                    "chromosome. The EIF2AK4 gene is located on chromosome 15, so "
                    "every person has two copies of this gene."
                ),
            },

            {
                "type": "image",
                "image": "articles/source/MVO.png",
                "image_caption": (
                    "Pulmonary veno-occlusive disease and genetic changes."
                ),
            },

            # ==========================================================
            # PVOD TRANSMISSION
            # ==========================================================

            {
                "type": "heading",
                "title": "Genetic Transmission of Pulmonary Veno-Occlusive Disease",
            },

            {
                "type": "paragraph",
                "text": (
                    "Because everyone has two copies of each chromosome, we have "
                    "two copies of the EIF2AK4 gene, one inherited from the mother "
                    "and one from the father."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "When a child is conceived, they inherit one chromosome from "
                    "the father and one chromosome from the mother for each pair."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "When both parents carry one mutation in the EIF2AK4 gene, "
                    "each child has a 25% chance of inheriting both mutations, "
                    "one from each parent."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "The child may inherit from each parent either the chromosome "
                    "carrying the altered gene or the chromosome carrying the "
                    "unchanged version. Therefore, four genetic possibilities exist."
                ),
            },

            {
                "type": "paragraph",
                "text": "Figure 8: Transmission of EIF2AK4 mutations.",
            },

            {
                "type": "image",
                "image": "articles/source/888.png",
                "image_caption": "Figure 8: Transmission of EIF2AK4 mutations.",
            },

            {
                "type": "paragraph",
                "text": (
                    "When a person carries two mutations in the EIF2AK4 gene, "
                    "their children will necessarily inherit one altered copy "
                    "of the gene from them. However, carrying only one mutation "
                    "is generally not sufficient to increase the predisposition "
                    "to the disease."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "EIF2AK4 mutations are very rare in the general population. "
                    "Therefore, the likelihood that the other parent also carries "
                    "a mutation in the same gene is low. This probability may be "
                    "different in cases of consanguinity, where the other parent "
                    "may carry the same familial genetic change."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Figure 9: Transmission of a genetic change from one parent to children."
                ),
            },

            {
                "type": "image",
                "image": "articles/source/777.png",
                "image_caption": (
                    "Figure 9: Transmission of a genetic change from one parent to children."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "In its hereditary form, pulmonary veno-occlusive disease is "
                    "an autosomal disease, meaning that it can affect both women "
                    "and men, and is recessive, meaning that changes in both copies "
                    "of EIF2AK4 are associated with the risk of developing the disease."
                ),
            },

            # ==========================================================
            # PVOD GENETIC COUNSELING
            # ==========================================================

            {
                "type": "heading",
                "title": "Genetic Counseling for Pulmonary Veno-Occlusive Disease",
            },

            {
                "type": "paragraph",
                "text": (
                    "Genetic counseling is offered to patients with pulmonary "
                    "veno-occlusive disease, whether or not they have a family history "
                    "of the disease."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Counseling may also be available to the brothers and sisters "
                    "of patients in whom two EIF2AK4 mutations have been identified."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "During the first genetic counseling consultation, the disease "
                    "mechanism, genetic transmission, the possibility of carrying "
                    "genetic changes in the EIF2AK4 gene, and the potential risks "
                    "for family members are explained."
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
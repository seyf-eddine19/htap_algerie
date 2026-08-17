from django.core.management.base import BaseCommand
from django.utils import timezone

from articles.models import (
    Article,
    ArticleCategory,
    ArticleTranslation,
    ArticleBlock,
)


class Command(BaseCommand):
    help = "Create Article 01 - À propos d'HTAP"

    def handle(self, *args, **options):

        category, _ = ArticleCategory.objects.get_or_create(
            slug="htap",
            defaults={
                "name": "HTAP",
                "is_active": True,
                "order": 1,
            },
        )

        article = Article.objects.create(
            category=category,
            author="HTaP ALGERIA",
            status=Article.Status.PUBLISHED,
            is_featured=True,
            published_at=timezone.now(),
            slug="a-propos-htap",
        )

        translation = ArticleTranslation.objects.create(
            article=article,
            language="fr",
            title="À propos d'HTAP",
            excerpt=(
                "Comprendre ce qu'est l'hypertension artérielle pulmonaire, "
                "ses symptômes, ses causes et les personnes concernées."
            ),
            meta_title="À propos d'HTAP | HTaP ALGERIA",
            meta_description=(
                "Informations sur l'hypertension artérielle pulmonaire, "
                "ses symptômes, ses causes et les personnes concernées."
            ),
        )

        blocks = [

            # ==========================================================
            # INTRODUCTION
            # ==========================================================

            {
                "type": "heading",
                "title": (
                    "Qu'est-ce que l'hypertension artérielle pulmonaire "
                    "appelée HTAP ?"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "L'Hypertension Artérielle Pulmonaire, en abrégé HTAP, "
                    "est une maladie grave. Aujourd'hui, l'HTAP se soigne "
                    "avec des moyens efficaces mais souvent très contraignants. "
                    "Ainsi, pour mettre les meilleures chances de votre côté, "
                    "il convient d'adapter votre vie."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Cette rubrique d'information contient des explications "
                    "nécessaires pour vous aider et aider vos proches à "
                    "comprendre ce qu'est l'HTAP. Elle tentera de répondre "
                    "à vos principales interrogations et préoccupations."
                ),
            },

            {
                "type": "heading",
                "title": "Le nom HTAP renvoie aux initiales suivantes :",
            },

            {
                "type": "paragraph",
                "text": (
                    "HT = HyperTension\n"
                    "A = Artérielle\n"
                    "P = Pulmonaire"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "L'HTAP ou Hypertension artérielle pulmonaire est une "
                    "maladie qui perturbe la circulation du sang à "
                    "l'intérieur des poumons."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "L'HTAP est une maladie différente de l'hypertension "
                    "artérielle « classique », non uniquement pulmonaire, "
                    "correspondant au fait « d'avoir de la tension » qui "
                    "touche un grand nombre de personnes en Algérie."
                ),
            },

            # ==========================================================
            # SYMPTOMES
            # ==========================================================

            {
                "type": "heading",
                "title": "Quels sont les symptômes de la maladie ?",
            },

            {
                "type": "paragraph",
                "text": (
                    "Aux premiers stades de l’HTAP, les symptômes ressemblent "
                    "beaucoup à ceux d’autres affections du cœur et des poumons. "
                    "Ainsi, les deux signes les plus courants sont l’essoufflement "
                    "lors d’efforts physiques importants dans un premier temps "
                    "(footing, port d’une charge lourde…), puis plus courants "
                    "(monter un escalier, faire son lit, faire quelques pas…) "
                    "et la fatigue."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "L'HTAP se traduit par :"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "• de la fatigue et un essoufflement lors d'efforts physiques,\n"
                    "• un gonflement (œdème) des jambes et des pieds,\n"
                    "• un gonflement du foie, accompagné de douleur au niveau du foie,\n"
                    "• des douleurs au niveau du cœur,\n"
                    "• des palpitations (le cœur bat plus vite ou irrégulièrement)."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Lorsque l'HTAP progresse, elle peut s'accompagner :"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "• de signes traduisant un mauvais fonctionnement du cœur "
                    "(on parle d'insuffisance cardiaque : œdèmes des membres "
                    "inférieurs, essoufflement ou dyspnée, …),\n"
                    "• de malaises avec ou sans perte de connaissance suite "
                    "à un effort physique,\n"
                    "• de douleurs thoraciques,\n"
                    "• de crachats de sang,\n"
                    "• d'une modification de la voix (plus faible et un peu "
                    "modifiée) – syndrome d’Ortner,\n"
                    "• du syndrome de Raynaud (doigts devenant blancs, froids "
                    "et parfois insensibles ou engourdis),\n"
                    "• d'une coloration bleutée des lèvres et des doigts."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Si on regarde ce qui se passe à l'intérieur, l'HTAP est "
                    "une maladie qui se développe au niveau des poumons mais "
                    "qui a des répercussions rapides au niveau de l'artère "
                    "pulmonaire et du cœur."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Les symptômes sont peu spécifiques et peuvent être "
                    "associés à de nombreuses maladies du cœur et des poumons, "
                    "d’où le retard parfois du diagnostic."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "L’essoufflement ressenti par le patient permet d’évaluer "
                    "le niveau de gravité initiale de l’HTAP en référence à "
                    "la classification de la NYHA (New York Heart Association) "
                    "et de guider le choix du traitement."
                ),
            },

            # ==========================================================
            # CAUSES / RESPONSABLE
            # ==========================================================

            {
                "type": "heading",
                "title": "Qu'est-ce qui est responsable de l'HTAP ?",
            },

            {
                "type": "paragraph",
                "text": (
                    "L'HTAP est une hypertension. Par définition, cela indique "
                    "que la pression du sang à l'intérieur de l'artère pulmonaire "
                    "est anormalement élevée."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Normalement, la pression moyenne du sang dans l'artère "
                    "pulmonaire est de 14 mm de mercure (en abrégé Hg) "
                    "au repos."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "On considère qu'il y a hypertension artérielle pulmonaire "
                    "lorsque cette pression dépasse 25 mm Hg au repos."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Chronique et évolutive, l’HTAP est provoquée par un "
                    "rétrécissement du calibre des artères pulmonaires qui "
                    "relient le cœur aux poumons. Ceci oblige le cœur à "
                    "pousser plus fort d’où une augmentation de pression "
                    "et peut à la longue entraîner une insuffisance "
                    "cardiaque droite sévère."
                ),
            },

            # ==========================================================
            # IMAGE SCHEMA 1
            # ==========================================================

            {
                "type": "image",
                "image": "articles/source/schema1.jpg",
                "image_caption": "Schéma de l'hypertension artérielle pulmonaire.",
            },

            {
                "type": "image",
                "image": "articles/source/schema2.jpg",
                "image_caption": "Schéma de l'hypertension artérielle pulmonaire.",
            },

            {
                "type": "image",
                "image": "articles/source/schema3.jpg",
                "image_caption": "Schéma de l'hypertension artérielle pulmonaire.",
            },

            # ==========================================================
            # PRESSURE
            # ==========================================================

            {
                "type": "heading",
                "title": (
                    "Pourquoi la pression du sang augmente-t-elle "
                    "dans l'artère pulmonaire ?"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Chez les personnes qui souffrent d'HTAP, la circulation "
                    "du sang est freinée au niveau des poumons."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Ce phénomène a deux conséquences :"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "• en cas d'effort physique, les poumons ont des difficultés "
                    "pour augmenter l'aération du sang (d'où l'essoufflement : "
                    "on doit fournir plus d'efforts pour respirer),\n\n"
                    "• comme le sang circule mal au niveau des poumons, il a "
                    "tendance à s'accumuler avant les poumons (comme pour une "
                    "rivière où un arbre est tombé en travers : l'eau "
                    "s'accumule en amont). En s'accumulant, le sang fait "
                    "pression sur les éléments qui le contiennent : la pression "
                    "augmente dans l'artère pulmonaire et également au niveau "
                    "de la partie droite du cœur (en particulier le ventricule "
                    "droit du cœur)."
                ),
            },

            {
                "type": "image",
                "image": "articles/source/Untitled.png",
                "image_caption": "Illustration de la circulation pulmonaire.",
            },

            # ==========================================================
            # BLOOD FLOW
            # ==========================================================

            {
                "type": "heading",
                "title": "Comment le sang est-il freiné dans les poumons ?",
            },

            {
                "type": "paragraph",
                "text": (
                    "Dans 9 cas sur 10, le sang circule mal dans les poumons "
                    "parce que les petites artères des poumons se bouchent. "
                    "Les éléments qui peuvent boucher les petites artères "
                    "à l'intérieur des poumons sont, soit des petits caillots "
                    "de sang, soit des zones fibreuses."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Dans les autres cas, ce sont les petites veines pulmonaires "
                    "qui se bouchent (le plus souvent par de petits caillots "
                    "de sang). Le sang va alors s'accumuler au niveau des "
                    "petites artères des poumons et les poumons vont se mettre "
                    "à gonfler (on parle d'embolie pulmonaire)."
                ),
            },

            # ==========================================================
            # WHO IS AFFECTED
            # ==========================================================

            {
                "type": "heading",
                "title": "Qui est touché par l'HTAP ?",
            },

            {
                "type": "paragraph",
                "text": (
                    "L’HTAP est une maladie rare qui touche environ 15 personnes "
                    "sur un million. Elle touche les hommes et les femmes de "
                    "tous les âges et de tous les groupes ethniques. Elle est "
                    "cependant plus fréquente chez les femmes de 30 à 50 ans."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Comme beaucoup de maladies rares, l’HTAP reste encore "
                    "méconnue du grand public et parfois des médecins eux-mêmes."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Pourtant un diagnostic précoce permet, souvent d’influencer "
                    "favorablement l’évolution de la maladie grâce à des "
                    "traitements adaptés."
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
                f"Article created successfully: {article.title if hasattr(article, 'title') else article}"
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
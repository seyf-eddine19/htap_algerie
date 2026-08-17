from datetime import datetime

from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone
from django.utils.text import slugify

from activities.models import (
    Activity,
    ActivityBlock,
    ActivityImage,
    ActivityTranslation,
    ActivityType,
    Language,
)


class Command(BaseCommand):
    help = "Seed HTaP ALGERIA activities with multilingual content."

    @transaction.atomic
    def handle(self, *args, **options):
        activities = [
            {
                "slug": "world-pulmonary-hypertension-day",
                "type": ActivityType.CAMPAIGN,
                "location": "Algiers, Algeria",
                "start_date": datetime(2026, 5, 5, 10, 0),
                "end_date": datetime(2026, 5, 5, 17, 0),
                "featured": True,
                "translations": {
                    Language.ENGLISH: {
                        "title": "World Pulmonary Hypertension Day",
                        "excerpt": "An awareness day dedicated to increasing understanding of pulmonary hypertension and the challenges faced by patients and their families.",
                        "meta_title": "World Pulmonary Hypertension Day | HTaP ALGERIA",
                        "meta_description": "HTaP ALGERIA raises awareness about pulmonary hypertension and stands alongside patients and their families.",
                        "blocks": [
                            {
                                "type": ActivityBlock.BlockType.HEADING,
                                "title": "Raising awareness about pulmonary hypertension",
                            },
                            {
                                "type": ActivityBlock.BlockType.PARAGRAPH,
                                "text": "On World Pulmonary Hypertension Day, HTaP ALGERIA brings attention to a condition that can significantly affect the daily lives of patients and their families.",
                            },
                            {
                                "type": ActivityBlock.BlockType.PARAGRAPH,
                                "text": "Through awareness activities, information sharing and patient support, the association works to ensure that pulmonary hypertension receives greater recognition and that affected people are not left alone.",
                            },
                            {
                                "type": ActivityBlock.BlockType.QUOTE,
                                "title": "Our commitment",
                                "text": "Inform, raise awareness and support patients throughout their journey.",
                            },
                        ],
                    },
                    Language.FRENCH: {
                        "title": "Journée mondiale de l'Hypertension Artérielle Pulmonaire",
                        "excerpt": "Une journée de sensibilisation consacrée à la compréhension de l'Hypertension Artérielle Pulmonaire et aux difficultés vécues par les patients et leurs familles.",
                        "meta_title": "Journée mondiale de l'HTAP | HTaP ALGERIA",
                        "meta_description": "HTaP ALGERIA sensibilise à l'Hypertension Artérielle Pulmonaire et accompagne les patients et leurs familles.",
                        "blocks": [
                            {
                                "type": ActivityBlock.BlockType.HEADING,
                                "title": "Sensibiliser à l'Hypertension Artérielle Pulmonaire",
                            },
                            {
                                "type": ActivityBlock.BlockType.PARAGRAPH,
                                "text": "À l'occasion de la Journée mondiale de l'Hypertension Artérielle Pulmonaire, HTaP ALGERIA met en lumière une maladie qui peut profondément affecter la vie quotidienne des patients et de leurs familles.",
                            },
                            {
                                "type": ActivityBlock.BlockType.PARAGRAPH,
                                "text": "À travers ses actions de sensibilisation, d'information et de soutien, l'association œuvre pour une meilleure reconnaissance de l'HTAP et pour que les personnes concernées ne restent pas seules face à la maladie.",
                            },
                            {
                                "type": ActivityBlock.BlockType.QUOTE,
                                "title": "Notre engagement",
                                "text": "Informer, sensibiliser et accompagner les patients tout au long de leur parcours.",
                            },
                        ],
                    },
                    Language.ARABIC: {
                        "title": "اليوم العالمي لارتفاع ضغط الدم الشرياني الرئوي",
                        "excerpt": "يوم توعوي يهدف إلى التعريف بارتفاع ضغط الدم الشرياني الرئوي والتحديات التي يواجهها المرضى وعائلاتهم.",
                        "meta_title": "اليوم العالمي لارتفاع ضغط الدم الشرياني الرئوي | HTaP ALGERIA",
                        "meta_description": "تعمل جمعية HTaP ALGERIA على التوعية بارتفاع ضغط الدم الشرياني الرئوي ومرافقة المرضى وعائلاتهم.",
                        "blocks": [
                            {
                                "type": ActivityBlock.BlockType.HEADING,
                                "title": "التوعية بارتفاع ضغط الدم الشرياني الرئوي",
                            },
                            {
                                "type": ActivityBlock.BlockType.PARAGRAPH,
                                "text": "بمناسبة اليوم العالمي لارتفاع ضغط الدم الشرياني الرئوي، تسلط جمعية HTaP ALGERIA الضوء على مرض يمكن أن يؤثر بشكل كبير على الحياة اليومية للمرضى وعائلاتهم.",
                            },
                            {
                                "type": ActivityBlock.BlockType.PARAGRAPH,
                                "text": "من خلال أنشطة التوعية ونشر المعلومات ودعم المرضى، تعمل الجمعية من أجل تعزيز الوعي بالمرض ومساندة الأشخاص المتضررين وعائلاتهم.",
                            },
                            {
                                "type": ActivityBlock.BlockType.QUOTE,
                                "title": "التزامنا",
                                "text": "الإعلام والتوعية ومرافقة المرضى طوال مسارهم.",
                            },
                        ],
                    },
                },
            },
            {
                "slug": "patient-awareness-meeting-algiers",
                "type": ActivityType.MEETING,
                "location": "Birkhadem, Algiers, Algeria",
                "start_date": datetime(2026, 6, 12, 14, 0),
                "end_date": datetime(2026, 6, 12, 17, 0),
                "featured": False,
                "translations": {
                    Language.ENGLISH: {
                        "title": "Patient Awareness and Support Meeting",
                        "excerpt": "A meeting dedicated to listening to patients, sharing information and discussing the everyday challenges associated with pulmonary hypertension.",
                        "meta_title": "Patient Awareness and Support Meeting | HTaP ALGERIA",
                        "meta_description": "HTaP ALGERIA organizes patient awareness and support activities focused on information, listening and solidarity.",
                        "blocks": [
                            {
                                "type": ActivityBlock.BlockType.HEADING,
                                "title": "A space for listening and solidarity",
                            },
                            {
                                "type": ActivityBlock.BlockType.PARAGRAPH,
                                "text": "The meeting provides an opportunity for patients and families to come together, exchange experiences and discuss the challenges they may encounter in their daily lives.",
                            },
                            {
                                "type": ActivityBlock.BlockType.PARAGRAPH,
                                "text": "HTaP ALGERIA believes that listening to patients is an essential part of building meaningful support and improving awareness of pulmonary hypertension.",
                            },
                        ],
                    },
                    Language.FRENCH: {
                        "title": "Rencontre de sensibilisation et de soutien aux patients",
                        "excerpt": "Une rencontre consacrée à l'écoute des patients, au partage d'informations et aux difficultés quotidiennes liées à l'Hypertension Artérielle Pulmonaire.",
                        "meta_title": "Rencontre de soutien aux patients | HTaP ALGERIA",
                        "meta_description": "HTaP ALGERIA organise des rencontres de sensibilisation et de soutien axées sur l'information, l'écoute et la solidarité.",
                        "blocks": [
                            {
                                "type": ActivityBlock.BlockType.HEADING,
                                "title": "Un espace d'écoute et de solidarité",
                            },
                            {
                                "type": ActivityBlock.BlockType.PARAGRAPH,
                                "text": "Cette rencontre permet aux patients et aux familles de se réunir, de partager leurs expériences et d'échanger autour des difficultés rencontrées au quotidien.",
                            },
                            {
                                "type": ActivityBlock.BlockType.PARAGRAPH,
                                "text": "HTaP ALGERIA considère l'écoute des patients comme une composante essentielle d'un accompagnement humain et d'une meilleure sensibilisation à l'HTAP.",
                            },
                        ],
                    },
                    Language.ARABIC: {
                        "title": "لقاء للتوعية ودعم المرضى",
                        "excerpt": "لقاء مخصص للاستماع إلى المرضى وتبادل المعلومات ومناقشة التحديات اليومية المرتبطة بارتفاع ضغط الدم الشرياني الرئوي.",
                        "meta_title": "لقاء للتوعية ودعم المرضى | HTaP ALGERIA",
                        "meta_description": "تنظم جمعية HTaP ALGERIA لقاءات للتوعية ودعم المرضى تقوم على الإعلام والاستماع والتضامن.",
                        "blocks": [
                            {
                                "type": ActivityBlock.BlockType.HEADING,
                                "title": "فضاء للاستماع والتضامن",
                            },
                            {
                                "type": ActivityBlock.BlockType.PARAGRAPH,
                                "text": "يوفر هذا اللقاء فرصة للمرضى وعائلاتهم للاجتماع وتبادل التجارب والنقاش حول الصعوبات التي قد يواجهونها في حياتهم اليومية.",
                            },
                            {
                                "type": ActivityBlock.BlockType.PARAGRAPH,
                                "text": "تؤمن جمعية HTaP ALGERIA بأن الاستماع إلى المرضى يمثل جزءًا أساسيًا من بناء دعم حقيقي وتعزيز الوعي بارتفاع ضغط الدم الشرياني الرئوي.",
                            },
                        ],
                    },
                },
            },
            {
                "slug": "htap-algerie-medical-conference",
                "type": ActivityType.CONFERENCE,
                "location": "Algiers, Algeria",
                "start_date": datetime(2026, 9, 20, 9, 0),
                "end_date": datetime(2026, 9, 20, 16, 0),
                "featured": False,
                "translations": {
                    Language.ENGLISH: {
                        "title": "Pulmonary Hypertension Medical Conference",
                        "excerpt": "A professional meeting focused on knowledge sharing, awareness and discussion around pulmonary hypertension.",
                        "meta_title": "Pulmonary Hypertension Medical Conference | HTaP ALGERIA",
                        "meta_description": "A medical conference focused on pulmonary hypertension awareness, knowledge sharing and patient support.",
                        "blocks": [
                            {
                                "type": ActivityBlock.BlockType.HEADING,
                                "title": "Knowledge sharing and awareness",
                            },
                            {
                                "type": ActivityBlock.BlockType.PARAGRAPH,
                                "text": "This conference brings together stakeholders interested in pulmonary hypertension awareness and patient support.",
                            },
                            {
                                "type": ActivityBlock.BlockType.PARAGRAPH,
                                "text": "The objective is to encourage dialogue, share knowledge and strengthen the visibility of pulmonary hypertension within the community.",
                            },
                        ],
                    },
                    Language.FRENCH: {
                        "title": "Conférence médicale sur l'Hypertension Artérielle Pulmonaire",
                        "excerpt": "Une rencontre professionnelle consacrée au partage des connaissances, à la sensibilisation et aux échanges autour de l'HTAP.",
                        "meta_title": "Conférence médicale sur l'HTAP | HTaP ALGERIA",
                        "meta_description": "Une conférence consacrée à la sensibilisation, au partage des connaissances et au soutien des patients atteints d'HTAP.",
                        "blocks": [
                            {
                                "type": ActivityBlock.BlockType.HEADING,
                                "title": "Partage des connaissances et sensibilisation",
                            },
                            {
                                "type": ActivityBlock.BlockType.PARAGRAPH,
                                "text": "Cette conférence réunit les acteurs intéressés par la sensibilisation à l'HTAP et l'accompagnement des patients.",
                            },
                            {
                                "type": ActivityBlock.BlockType.PARAGRAPH,
                                "text": "L'objectif est d'encourager le dialogue, de partager les connaissances et de renforcer la visibilité de l'HTAP au sein de la communauté.",
                            },
                        ],
                    },
                    Language.ARABIC: {
                        "title": "مؤتمر طبي حول ارتفاع ضغط الدم الشرياني الرئوي",
                        "excerpt": "لقاء مهني يركز على تبادل المعارف والتوعية والنقاش حول ارتفاع ضغط الدم الشرياني الرئوي.",
                        "meta_title": "مؤتمر طبي حول ارتفاع ضغط الدم الشرياني الرئوي | HTaP ALGERIA",
                        "meta_description": "مؤتمر يركز على التوعية بارتفاع ضغط الدم الشرياني الرئوي وتبادل المعارف ودعم المرضى.",
                        "blocks": [
                            {
                                "type": ActivityBlock.BlockType.HEADING,
                                "title": "تبادل المعرفة والتوعية",
                            },
                            {
                                "type": ActivityBlock.BlockType.PARAGRAPH,
                                "text": "يجمع هذا المؤتمر مختلف الأطراف المهتمة بالتوعية بارتفاع ضغط الدم الشرياني الرئوي ودعم المرضى.",
                            },
                            {
                                "type": ActivityBlock.BlockType.PARAGRAPH,
                                "text": "يهدف اللقاء إلى تشجيع الحوار وتبادل المعارف وتعزيز الاهتمام بارتفاع ضغط الدم الشرياني الرئوي داخل المجتمع.",
                            },
                        ],
                    },
                },
            },
            {
                "slug": "htap-algerie-community-awareness-campaign",
                "type": ActivityType.CAMPAIGN,
                "location": "Algiers, Algeria",
                "start_date": datetime(2026, 10, 10, 10, 0),
                "end_date": datetime(2026, 10, 17, 18, 0),
                "featured": False,
                "translations": {
                    Language.ENGLISH: {
                        "title": "Pulmonary Hypertension Awareness Campaign",
                        "excerpt": "A community awareness campaign encouraging people to learn more about pulmonary hypertension and the importance of patient support.",
                        "meta_title": "Pulmonary Hypertension Awareness Campaign | HTaP ALGERIA",
                        "meta_description": "HTaP ALGERIA awareness campaign dedicated to pulmonary hypertension information and community solidarity.",
                        "blocks": [
                            {
                                "type": ActivityBlock.BlockType.HEADING,
                                "title": "Information can make a difference",
                            },
                            {
                                "type": ActivityBlock.BlockType.PARAGRAPH,
                                "text": "Awareness is an important part of helping patients and families better understand pulmonary hypertension.",
                            },
                            {
                                "type": ActivityBlock.BlockType.PARAGRAPH,
                                "text": "Through educational content and community activities, HTaP ALGERIA encourages dialogue and solidarity around the challenges faced by patients.",
                            },
                        ],
                    },
                    Language.FRENCH: {
                        "title": "Campagne de sensibilisation à l'Hypertension Artérielle Pulmonaire",
                        "excerpt": "Une campagne de sensibilisation destinée à mieux faire connaître l'HTAP et l'importance du soutien aux patients.",
                        "meta_title": "Campagne de sensibilisation à l'HTAP | HTaP ALGERIA",
                        "meta_description": "Campagne HTaP ALGERIA consacrée à l'information sur l'HTAP et à la solidarité avec les patients.",
                        "blocks": [
                            {
                                "type": ActivityBlock.BlockType.HEADING,
                                "title": "L'information peut faire la différence",
                            },
                            {
                                "type": ActivityBlock.BlockType.PARAGRAPH,
                                "text": "La sensibilisation constitue un élément important pour aider les patients et leurs familles à mieux comprendre l'Hypertension Artérielle Pulmonaire.",
                            },
                            {
                                "type": ActivityBlock.BlockType.PARAGRAPH,
                                "text": "À travers des contenus éducatifs et des actions de proximité, HTaP ALGERIA encourage le dialogue et la solidarité autour des difficultés vécues par les patients.",
                            },
                        ],
                    },
                    Language.ARABIC: {
                        "title": "حملة للتوعية بارتفاع ضغط الدم الشرياني الرئوي",
                        "excerpt": "حملة توعوية تهدف إلى التعريف بارتفاع ضغط الدم الشرياني الرئوي وأهمية دعم المرضى.",
                        "meta_title": "حملة التوعية بارتفاع ضغط الدم الشرياني الرئوي | HTaP ALGERIA",
                        "meta_description": "حملة توعوية من HTaP ALGERIA حول ارتفاع ضغط الدم الشرياني الرئوي والتضامن مع المرضى.",
                        "blocks": [
                            {
                                "type": ActivityBlock.BlockType.HEADING,
                                "title": "المعلومة يمكن أن تصنع الفرق",
                            },
                            {
                                "type": ActivityBlock.BlockType.PARAGRAPH,
                                "text": "تعد التوعية عنصرًا مهمًا لمساعدة المرضى وعائلاتهم على فهم ارتفاع ضغط الدم الشرياني الرئوي بشكل أفضل.",
                            },
                            {
                                "type": ActivityBlock.BlockType.PARAGRAPH,
                                "text": "من خلال المحتوى التثقيفي والأنشطة المجتمعية، تشجع HTaP ALGERIA على الحوار والتضامن حول التحديات التي يواجهها المرضى.",
                            },
                        ],
                    },
                },
            },
        ]

        created_count = 0
        updated_count = 0

        for data in activities:
            activity, created = Activity.objects.update_or_create(
                slug=data["slug"],
                defaults={
                    "activity_type": data["type"],
                    "status": Activity.Status.PUBLISHED,
                    "location": data["location"],
                    "start_date": timezone.make_aware(data["start_date"]),
                    "end_date": timezone.make_aware(data["end_date"]),
                    "is_featured": data["featured"],
                },
            )

            if created:
                created_count += 1
            else:
                updated_count += 1

            for language, translation_data in data["translations"].items():
                translation, _ = ActivityTranslation.objects.update_or_create(
                    activity=activity,
                    language=language,
                    defaults={
                        "title": translation_data["title"],
                        "excerpt": translation_data["excerpt"],
                        "meta_title": translation_data["meta_title"],
                        "meta_description": translation_data["meta_description"],
                    },
                )

                translation.blocks.all().delete()

                for order, block_data in enumerate(
                    translation_data.get("blocks", []),
                    start=1,
                ):
                    ActivityBlock.objects.create(
                        translation=translation,
                        block_type=block_data["type"],
                        order=order,
                        title=block_data.get("title", ""),
                        text=block_data.get("text", ""),
                    )

            self.stdout.write(
                self.style.SUCCESS(
                    f"Seeded: {activity.slug}"
                )
            )

        self.stdout.write("")
        self.stdout.write(
            self.style.SUCCESS(
                f"Done. Created: {created_count}, Updated: {updated_count}"
            )
        )
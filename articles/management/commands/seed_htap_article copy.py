from django.core.management.base import BaseCommand
from django.utils import timezone

from articles.models import (
    Article,
    ArticleCategory,
    ArticleTranslation,
    ArticleBlock,
)


class Command(BaseCommand):
    help = "إنشاء المقال 01 - حول ارتفاع ضغط الدم الشرياني الرئوي HTAP"

    def handle(self, *args, **options):

        category, _ = ArticleCategory.objects.get_or_create(
            slug="htap",
            defaults={
                "name": "ارتفاع ضغط الدم الشرياني الرئوي",
                "is_active": True,
                "order": 1,
            },
        )

        article, _ = Article.objects.get_or_create(
            slug="a-propos-htap"
        )

        translation = ArticleTranslation.objects.create(
            article=article,
            language="ar",
            title="حول ارتفاع ضغط الدم الشرياني الرئوي",
            excerpt=(
                "فهم ماهية ارتفاع ضغط الدم الشرياني الرئوي، "
                "وأعراضه وأسبابه والأشخاص المعرضين للإصابة به."
            ),
            meta_title="حول ارتفاع ضغط الدم الشرياني الرئوي | HTaP ALGERIA",
            meta_description=(
                "معلومات حول ارتفاع ضغط الدم الشرياني الرئوي، "
                "وأعراضه وأسبابه والأشخاص المعرضين للإصابة به."
            ),
        )

        blocks = [

            # ==========================================================
            # المقدمة
            # ==========================================================

            {
                "type": "heading",
                "title": (
                    "ما هو ارتفاع ضغط الدم الشرياني الرئوي "
                    "المعروف اختصارًا بـ HTAP؟"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "ارتفاع ضغط الدم الشرياني الرئوي، واختصاره HTAP، "
                    "هو مرض خطير. في الوقت الحالي، يمكن علاج HTAP "
                    "بوسائل فعالة، لكنها غالبًا ما تكون مرهقة ومقيدة "
                    "للحياة اليومية. لذلك، ولزيادة فرص الاستفادة من "
                    "العلاج، من المهم تكييف نمط الحياة مع المرض."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "يحتوي هذا القسم المعلوماتي على شروحات ضرورية "
                    "لمساعدتك ومساعدة أفراد عائلتك على فهم ماهية HTAP. "
                    "كما يحاول الإجابة عن أهم تساؤلاتكم وانشغالاتكم."
                ),
            },

            {
                "type": "heading",
                "title": "ماذا تعني حروف HTAP؟",
            },

            {
                "type": "paragraph",
                "text": (
                    "HT = فرط الضغط\n"
                    "A = شرياني\n"
                    "P = رئوي"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "ارتفاع ضغط الدم الشرياني الرئوي، أو HTAP، "
                    "هو مرض يؤثر في دوران الدم داخل الرئتين."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "يختلف HTAP عن ارتفاع ضغط الدم «الكلاسيكي» أو "
                    "ارتفاع ضغط الدم العام المعروف بعبارة «لدي ضغط الدم». "
                    "وهذا الأخير يصيب عددًا كبيرًا من الأشخاص في الجزائر."
                ),
            },

            # ==========================================================
            # الأعراض
            # ==========================================================

            {
                "type": "heading",
                "title": "ما هي أعراض المرض؟",
            },

            {
                "type": "paragraph",
                "text": (
                    "في المراحل الأولى من HTAP، تشبه الأعراض إلى حد كبير "
                    "أعراض أمراض أخرى تصيب القلب والرئتين. ومن أكثر "
                    "العلامات شيوعًا ضيق التنفس أثناء بذل مجهود بدني "
                    "كبير في البداية، مثل الجري أو حمل أشياء ثقيلة، "
                    "ثم أثناء مجهودات أكثر اعتيادية مثل صعود الدرج، "
                    "أو ترتيب السرير، أو حتى المشي لبضع خطوات، "
                    "بالإضافة إلى التعب."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "يمكن أن يتجلى HTAP في:"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "• التعب وضيق التنفس أثناء بذل المجهود البدني،\n"
                    "• تورم الساقين والقدمين (الوذمة)،\n"
                    "• تضخم الكبد، المصحوب بألم في منطقة الكبد،\n"
                    "• آلام في منطقة القلب،\n"
                    "• خفقان القلب (تسارع ضربات القلب أو عدم انتظامها)."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "ومع تطور HTAP، قد تظهر الأعراض التالية:"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "• علامات تدل على ضعف وظيفة القلب، ويُطلق على ذلك "
                    "قصور القلب، مثل وذمة الأطراف السفلية وضيق التنفس،\n"
                    "• حالات من الدوخة أو الإغماء، مع أو دون فقدان الوعي، "
                    "بعد بذل مجهود بدني،\n"
                    "• آلام في الصدر،\n"
                    "• سعال مصحوب بخروج الدم،\n"
                    "• تغير في الصوت، بحيث يصبح أضعف ومتغيرًا قليلًا، "
                    "وهو ما يُعرف بمتلازمة أورتنر،\n"
                    "• متلازمة رينو، حيث تصبح أصابع اليدين بيضاء وباردة "
                    "وأحيانًا فاقدة للإحساس أو مخدرة،\n"
                    "• ظهور لون أزرق على الشفتين والأصابع."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "إذا نظرنا إلى ما يحدث داخل الجسم، فإن HTAP هو مرض "
                    "يتطور على مستوى الرئتين، لكنه يؤثر بسرعة في الشريان "
                    "الرئوي والقلب."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "أعراض HTAP غير محددة ويمكن أن تكون مرتبطة بالعديد "
                    "من أمراض القلب والرئتين، وهو ما يفسر أحيانًا تأخر "
                    "تشخيص المرض."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "يساعد ضيق التنفس الذي يشعر به المريض على تقييم "
                    "درجة شدة HTAP في البداية، بالاعتماد على تصنيف "
                    "جمعية نيويورك للقلب NYHA (New York Heart Association)، "
                    "كما يساعد في توجيه اختيار العلاج."
                ),
            },

            # ==========================================================
            # ما المسؤول عن HTAP؟
            # ==========================================================

            {
                "type": "heading",
                "title": "ما المسؤول عن ارتفاع ضغط الدم الشرياني الرئوي؟",
            },

            {
                "type": "paragraph",
                "text": (
                    "HTAP هو نوع من ارتفاع ضغط الدم. وبالتعريف، يعني ذلك "
                    "أن ضغط الدم داخل الشريان الرئوي يكون مرتفعًا بشكل "
                    "غير طبيعي."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "في الحالة الطبيعية، يبلغ متوسط ضغط الدم في الشريان "
                    "الرئوي حوالي 14 ملم زئبق (mmHg) أثناء الراحة."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "يُعتبر هناك ارتفاع في ضغط الدم الشرياني الرئوي "
                    "عندما يتجاوز هذا الضغط 25 ملم زئبق أثناء الراحة."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "HTAP مرض مزمن ومتطور، وينتج عن تضيق قطر الشرايين "
                    "الرئوية التي تربط القلب بالرئتين. وهذا يجبر القلب "
                    "على بذل قوة أكبر لضخ الدم، مما يؤدي إلى ارتفاع الضغط، "
                    "وقد يؤدي على المدى الطويل إلى قصور شديد في الجانب "
                    "الأيمن من القلب."
                ),
            },

            # ==========================================================
            # الصور التوضيحية
            # ==========================================================

            {
                "type": "image",
                "image": "articles/source/schema1.jpg",
                "image_caption": (
                    "رسم توضيحي لارتفاع ضغط الدم الشرياني الرئوي."
                ),
            },

            {
                "type": "image",
                "image": "articles/source/schema2.jpg",
                "image_caption": (
                    "رسم توضيحي لارتفاع ضغط الدم الشرياني الرئوي."
                ),
            },

            {
                "type": "image",
                "image": "articles/source/schema3.jpg",
                "image_caption": (
                    "رسم توضيحي لارتفاع ضغط الدم الشرياني الرئوي."
                ),
            },

            # ==========================================================
            # ضغط الدم في الشريان الرئوي
            # ==========================================================

            {
                "type": "heading",
                "title": (
                    "لماذا يرتفع ضغط الدم في الشريان الرئوي؟"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "لدى الأشخاص المصابين بـ HTAP، تصبح حركة الدم داخل "
                    "الرئتين أكثر صعوبة."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "ويترتب على هذه الظاهرة نتيجتان:"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "• أثناء بذل المجهود البدني، تواجه الرئتان صعوبة في "
                    "زيادة أكسجة الدم، وهو ما يؤدي إلى ضيق التنفس، حيث "
                    "يحتاج الشخص إلى بذل جهد أكبر من أجل التنفس،\n\n"
                    "• عندما لا يتحرك الدم بشكل جيد داخل الرئتين، فإنه "
                    "يميل إلى التراكم قبل وصوله إلى الرئتين، مثل النهر "
                    "عندما تسقط فيه شجرة فتعيق جريان الماء، فيتراكم الماء "
                    "قبل العائق. ومع تراكم الدم، يزداد الضغط على الأوعية "
                    "والعناصر التي تحتويه، فيرتفع الضغط داخل الشريان "
                    "الرئوي وكذلك في الجزء الأيمن من القلب، وخاصة "
                    "البطين الأيمن."
                ),
            },

            {
                "type": "image",
                "image": "articles/source/Untitled.png",
                "image_caption": (
                    "رسم توضيحي للدورة الدموية الرئوية."
                ),
            },

            # ==========================================================
            # كيف يتباطأ تدفق الدم؟
            # ==========================================================

            {
                "type": "heading",
                "title": "كيف يتباطأ تدفق الدم داخل الرئتين؟",
            },

            {
                "type": "paragraph",
                "text": (
                    "في 9 حالات من أصل 10، لا يتحرك الدم بشكل جيد داخل "
                    "الرئتين لأن الشرايين الصغيرة في الرئتين تصبح مسدودة. "
                    "ومن بين العناصر التي يمكن أن تسد الشرايين الصغيرة "
                    "داخل الرئتين جلطات دموية صغيرة أو مناطق ليفية."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "وفي الحالات الأخرى، تكون الأوردة الرئوية الصغيرة "
                    "هي التي تصبح مسدودة، وغالبًا بسبب جلطات دموية صغيرة. "
                    "وعندها يتراكم الدم على مستوى الشرايين الصغيرة في "
                    "الرئتين، وقد تبدأ الرئتان في الانتفاخ، وهو ما يُعرف "
                    "بالانسداد أو الانصمام الرئوي."
                ),
            },

            # ==========================================================
            # من يصاب بـ HTAP؟
            # ==========================================================

            {
                "type": "heading",
                "title": "من هم الأشخاص الذين يصابون بـ HTAP؟",
            },

            {
                "type": "paragraph",
                "text": (
                    "HTAP مرض نادر يصيب حوالي 15 شخصًا من كل مليون شخص. "
                    "ويمكن أن يصيب الرجال والنساء من جميع الأعمار "
                    "ومن مختلف المجموعات العرقية. إلا أنه أكثر شيوعًا "
                    "لدى النساء اللواتي تتراوح أعمارهن بين 30 و50 سنة."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "وكغيره من الأمراض النادرة، لا يزال HTAP غير معروف "
                    "بشكل كافٍ لدى عامة الناس، وأحيانًا حتى لدى بعض "
                    "الأطباء أنفسهم."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "ومع ذلك، يمكن للتشخيص المبكر أن يؤثر في كثير من "
                    "الأحيان بشكل إيجابي في تطور المرض، بفضل العلاجات "
                    "المناسبة."
                ),
            },

            # ==========================================================
            # CTA
            # ==========================================================

            {
                "type": "heading",
                "title": "حجز موعد",
            },
        ]

        # ==============================================================
        # إنشاء الكتل
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
                f"تم إنشاء المقال بنجاح: "
                f"{article.title if hasattr(article, 'title') else article}"
            )
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"معرّف المقال: {article.pk}"
            )
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"عدد الكتل التي تم إنشاؤها: {len(blocks)}"
            )
        )

        translation = ArticleTranslation.objects.create(
            article=article,
            language="en",
            title="About Pulmonary Arterial Hypertension",
            excerpt=(
                "Learn about pulmonary arterial hypertension, "
                "its symptoms, causes, and the people affected by it."
            ),
            meta_title=(
                "About Pulmonary Arterial Hypertension | HTaP ALGERIA"
            ),
            meta_description=(
                "Information about pulmonary arterial hypertension, "
                "its symptoms, causes, and the people affected by it."
            ),
        )

        blocks = [

            # ==========================================================
            # INTRODUCTION
            # ==========================================================

            {
                "type": "heading",
                "title": (
                    "What is pulmonary arterial hypertension, "
                    "also known as PAH?"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Pulmonary Arterial Hypertension, abbreviated as PAH, "
                    "is a serious disease. Today, PAH can be treated with "
                    "effective treatments, although they are often demanding "
                    "and restrictive. Therefore, in order to give yourself "
                    "the best possible chance, it is important to adapt "
                    "your lifestyle."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "This information section provides explanations "
                    "to help you and your loved ones understand what PAH is. "
                    "It aims to answer your main questions and concerns."
                ),
            },

            {
                "type": "heading",
                "title": "What do the letters PAH stand for?",
            },

            {
                "type": "paragraph",
                "text": (
                    "P = Pulmonary\n"
                    "A = Arterial\n"
                    "H = Hypertension"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Pulmonary Arterial Hypertension, or PAH, is a disease "
                    "that disrupts blood circulation inside the lungs."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "PAH is different from conventional systemic arterial "
                    "hypertension, commonly referred to as having "
                    "high blood pressure, which affects a large number "
                    "of people in Algeria."
                ),
            },

            # ==========================================================
            # SYMPTOMS
            # ==========================================================

            {
                "type": "heading",
                "title": "What are the symptoms of the disease?",
            },

            {
                "type": "paragraph",
                "text": (
                    "In the early stages of PAH, symptoms are very similar "
                    "to those of other heart and lung conditions. The two "
                    "most common symptoms are shortness of breath during "
                    "significant physical exertion at first, such as jogging "
                    "or carrying a heavy load, and later during more ordinary "
                    "activities such as climbing stairs, making the bed, "
                    "or walking a few steps, as well as fatigue."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "PAH may cause:"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "• fatigue and shortness of breath during physical exertion,\n"
                    "• swelling (edema) of the legs and feet,\n"
                    "• enlargement of the liver, accompanied by pain in the liver area,\n"
                    "• pain around the heart,\n"
                    "• palpitations (the heart beats faster or irregularly)."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "As PAH progresses, it may be accompanied by:"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "• signs of impaired heart function, known as heart "
                    "failure, such as swelling of the lower limbs and "
                    "shortness of breath,\n"
                    "• episodes of dizziness or fainting, with or without "
                    "loss of consciousness, following physical exertion,\n"
                    "• chest pain,\n"
                    "• coughing up blood,\n"
                    "• a change in the voice, which may become weaker "
                    "and slightly altered — Ortner syndrome,\n"
                    "• Raynaud syndrome, in which the fingers become white, "
                    "cold, and sometimes numb or insensitive,\n"
                    "• bluish discoloration of the lips and fingers."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Inside the body, PAH is a disease that develops "
                    "in the lungs but quickly affects the pulmonary artery "
                    "and the heart."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "The symptoms are not specific and can be associated "
                    "with many different heart and lung diseases, which "
                    "can sometimes lead to a delayed diagnosis."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "The shortness of breath experienced by the patient "
                    "helps assess the initial severity of PAH according "
                    "to the NYHA (New York Heart Association) classification "
                    "and helps guide the choice of treatment."
                ),
            },

            # ==========================================================
            # CAUSES / RESPONSIBLE FACTORS
            # ==========================================================

            {
                "type": "heading",
                "title": "What causes pulmonary arterial hypertension?",
            },

            {
                "type": "paragraph",
                "text": (
                    "PAH is a form of hypertension. By definition, this "
                    "means that the pressure of the blood inside the "
                    "pulmonary artery is abnormally high."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Normally, the average blood pressure in the pulmonary "
                    "artery is approximately 14 mmHg at rest."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Pulmonary arterial hypertension is considered to be "
                    "present when this pressure exceeds 25 mmHg at rest."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "PAH is a chronic and progressive disease caused by "
                    "narrowing of the pulmonary arteries that connect "
                    "the heart to the lungs. This forces the heart to "
                    "work harder, causing an increase in pressure and, "
                    "over time, potentially leading to severe right-sided "
                    "heart failure."
                ),
            },

            # ==========================================================
            # IMAGES
            # ==========================================================

            {
                "type": "image",
                "image": "articles/source/schema1.jpg",
                "image_caption": (
                    "Illustration of pulmonary arterial hypertension."
                ),
            },

            {
                "type": "image",
                "image": "articles/source/schema2.jpg",
                "image_caption": (
                    "Illustration of pulmonary arterial hypertension."
                ),
            },

            {
                "type": "image",
                "image": "articles/source/schema3.jpg",
                "image_caption": (
                    "Illustration of pulmonary arterial hypertension."
                ),
            },

            # ==========================================================
            # BLOOD PRESSURE
            # ==========================================================

            {
                "type": "heading",
                "title": (
                    "Why does blood pressure increase "
                    "in the pulmonary artery?"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "In people with PAH, blood flow is restricted "
                    "at the level of the lungs."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "This phenomenon has two consequences:"
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "• during physical exertion, the lungs have difficulty "
                    "increasing the oxygenation of the blood, resulting "
                    "in shortness of breath because more effort is required "
                    "to breathe,\n\n"
                    "• because blood does not circulate properly through "
                    "the lungs, it tends to accumulate before reaching "
                    "the lungs, similar to a river where a tree has fallen "
                    "across the water and causes the water to accumulate "
                    "upstream. As the blood accumulates, it puts pressure "
                    "on the structures containing it. Pressure therefore "
                    "increases in the pulmonary artery and also in the "
                    "right side of the heart, particularly the right ventricle."
                ),
            },

            {
                "type": "image",
                "image": "articles/source/Untitled.png",
                "image_caption": (
                    "Illustration of pulmonary blood circulation."
                ),
            },

            # ==========================================================
            # BLOOD FLOW
            # ==========================================================

            {
                "type": "heading",
                "title": "How is blood flow restricted in the lungs?",
            },

            {
                "type": "paragraph",
                "text": (
                    "In 9 out of 10 cases, blood does not circulate properly "
                    "through the lungs because the small pulmonary arteries "
                    "become blocked. The elements that can block these "
                    "small arteries inside the lungs include small blood "
                    "clots or areas of fibrous tissue."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "In other cases, the small pulmonary veins become blocked, "
                    "most often by small blood clots. Blood then accumulates "
                    "at the level of the small pulmonary arteries, and "
                    "the lungs may begin to swell. This is referred to "
                    "as pulmonary embolism."
                ),
            },

            # ==========================================================
            # WHO IS AFFECTED?
            # ==========================================================

            {
                "type": "heading",
                "title": "Who is affected by PAH?",
            },

            {
                "type": "paragraph",
                "text": (
                    "PAH is a rare disease that affects approximately "
                    "15 people per million. It affects men and women "
                    "of all ages and ethnic backgrounds. However, it is "
                    "more common among women between the ages of 30 and 50."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "Like many rare diseases, PAH remains relatively "
                    "unknown to the general public and sometimes even "
                    "to healthcare professionals themselves."
                ),
            },

            {
                "type": "paragraph",
                "text": (
                    "However, early diagnosis can often positively "
                    "influence the progression of the disease through "
                    "appropriate treatment."
                ),
            },

            # ==========================================================
            # CTA
            # ==========================================================

            {
                "type": "heading",
                "title": "Book an Appointment",
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
                f"Article created successfully: "
                f"{article.title if hasattr(article, 'title') else article}"
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
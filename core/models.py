from django.db import models
from django.utils.translation import gettext_lazy as _, get_language


# class AssociationInfo(models.Model):
#     name = models.CharField(_("name"), max_length=200, default="HTaP ALGERIA")
#     full_name = models.CharField(_("full name"), max_length=300, blank=True)
#     description = models.TextField(_("description"), blank=True)
#     history = models.TextField(_("history"), blank=True)
#     mission = models.TextField(_("mission"), blank=True)
#     objectives = models.TextField(_("objectives"), blank=True)
#     logo = models.ImageField(_("logo"), upload_to="association/", blank=True, null=True)
#     address = models.TextField(_("address"), blank=True)
#     phone = models.CharField(_("phone"), max_length=50, blank=True)
#     email = models.EmailField(_("email"), blank=True)
#     facebook_url = models.URLField(_("Facebook"), blank=True)
#     instagram_url = models.URLField(_("Instagram"), blank=True)
#     youtube_url = models.URLField(_("YouTube"), blank=True)
#     map_url = models.URLField(_("map URL"), blank=True)
#     updated_at = models.DateTimeField(_("updated at"), auto_now=True)

#     class Meta:
#         verbose_name = _("Association information")
#         verbose_name_plural = _("Association information")

#     def __str__(self):
#         return self.name


# class Statistic(models.Model):
#     title = models.CharField(_("title"), max_length=100)
#     value = models.CharField(_("value"), max_length=50)
#     description = models.CharField(_("description"), max_length=200, blank=True)
#     icon = models.CharField(_("icon"), max_length=50, blank=True, help_text=_("Icon name used by the frontend."))
#     order = models.PositiveIntegerField(_("order"), default=0)
#     is_active = models.BooleanField(_("active"), default=True)

#     class Meta:
#         ordering = ["order"]
#         verbose_name = _("Statistic")
#         verbose_name_plural = _("Statistics")

#     def __str__(self):
#         return f"{self.title} - {self.value}"

class Member(models.Model):
    name = models.CharField(_("Name (Latin characters)"), max_length=150)
    name_ar = models.CharField(_("Name (Arabic)"), max_length=150, blank=True)
    role_ar = models.CharField(_("Role (Arabic)"), max_length=150, blank=True)
    role_en = models.CharField(_("Role (English)"), max_length=150, blank=True)
    role_fr = models.CharField(_("Role (French)"), max_length=150)
    photo = models.ImageField(_("Photo"), upload_to="members/", blank=True, null=True)
    bio = models.TextField(_("Bio"), blank=True)
    order = models.PositiveIntegerField(_("order"), default=0)
    is_active = models.BooleanField(_("active"), default=True)

    class Meta:
        ordering = ["order", "name"]
        verbose_name = _("Member")
        verbose_name_plural = _("Members")

    @property
    def display_name(self):
        lang = get_language()
        if lang == "ar" and self.name_ar:
            return self.name_ar
        return self.name or self.name_ar

    @property
    def display_role(self):
        lang = get_language()
        if lang == "ar":
            return self.role_ar or self.role_fr
        if lang == "fr":
            return self.role_fr or self.role_en
        return self.role_en or self.role_fr
    
    def __str__(self):
        return f"{self.display_name} - {self.display_role}"


class ContactMessage(models.Model):
    class Subject(models.TextChoices):
        INFO = "info", _("Information about HTAP")
        HELP = "help", _("Request for assistance / support")
        DONATE = "donate", _("Make a donation or volunteer")
        PARTNERSHIP = "partnership", _("Request for partnership / collaboration")
        ACTIVITIES = "activities", _("Information about activities / events")
        OTHER = "other", _("Other inquiry")

    class Wilaya(models.TextChoices):
        NOT_IN_ALGERIA = "not_in_algeria", _("I am not living in Algeria")

        ADRAR = "01", _("Adrar")
        CHLEF = "02", _("Chlef")
        LAGHOUAT = "03", _("Laghouat")
        OUM_EL_BOUAGHI = "04", _("Oum El Bouaghi")
        BATNA = "05", _("Batna")
        BEJAIA = "06", _("Béjaïa")
        BISKRA = "07", _("Biskra")
        BECHAR = "08", _("Béchar")
        BLIDA = "09", _("Blida")
        BOUIRA = "10", _("Bouira")
        TAMANRASSET = "11", _("Tamanrasset")
        TEBESSA = "12", _("Tébessa")
        TLEMCEN = "13", _("Tlemcen")
        TIARET = "14", _("Tiaret")
        TIZI_OUZOU = "15", _("Tizi Ouzou")
        ALGIERS = "16", _("Algiers")
        DJELFA = "17", _("Djelfa")
        JIJEL = "18", _("Jijel")
        SETIF = "19", _("Sétif")
        SAIDA = "20", _("Saïda")
        SKIKDA = "21", _("Skikda")
        SIDI_BEL_ABBES = "22", _("Sidi Bel Abbès")
        ANNABA = "23", _("Annaba")
        GUELMA = "24", _("Guelma")
        CONSTANTINE = "25", _("Constantine")
        MEDEA = "26", _("Médéa")
        MOSTAGANEM = "27", _("Mostaganem")
        MSILA = "28", _("M'Sila")
        MASCARA = "29", _("Mascara")
        OUARGLA = "30", _("Ouargla")
        ORAN = "31", _("Oran")
        EL_BAYADH = "32", _("El Bayadh")
        ILLIZI = "33", _("Illizi")
        BORDJ_BOU_ARRERIDJ = "34", _("Bordj Bou Arréridj")
        BOUMERDES = "35", _("Boumerdès")
        EL_TARF = "36", _("El Tarf")
        TINDOUF = "37", _("Tindouf")
        TISSEMSILT = "38", _("Tissemsilt")
        EL_OUED = "39", _("El Oued")
        KHENCHELA = "40", _("Khenchela")
        SOUK_AHRAS = "41", _("Souk Ahras")
        TIPAZA = "42", _("Tipaza")
        MILA = "43", _("Mila")
        AIN_DEFLA = "44", _("Aïn Defla")
        NAAMA = "45", _("Naâma")
        AIN_TEMOUCHENT = "46", _("Aïn Témouchent")
        GHARDAIA = "47", _("Ghardaïa")
        RELIZANE = "48", _("Relizane")
        TIMIMOUN = "49", _("Timimoun")
        BORDJ_BADJI_MOKHTAR = "50", _("Bordj Badji Mokhtar")
        OULED_DJELLAL = "51", _("Ouled Djellal")
        BENI_ABBES = "52", _("Béni Abbès")
        IN_SALAH = "53", _("In Salah")
        IN_GUEZZAM = "54", _("In Guezzam")
        TOUGGOURT = "55", _("Touggourt")
        DJANET = "56", _("Djanet")
        EL_MGHAIER = "57", _("El M'Ghair")
        EL_MENIAA = "58", _("El Meniaa")

        # New wilayas — 2026
        AFLOU = "59", _("Aflou")
        BARIKA = "60", _("Barika")
        KSAR_CHELLALA = "61", _("Ksar Chellala")
        MESSAAD = "62", _("Messaad")
        AIN_OUSSERA = "63", _("Aïn Oussera")
        BOUSAADA = "64", _("Bou Saâda")
        EL_BAYADH_SIDI_CHEIKH = "65", _("El Bayadh Sidi Cheikh")
        EL_KANTARA = "66", _("El Kantara")
        BIR_EL_ATER = "67", _("Bir El Ater")
        KSAR_EL_BOUKHARI = "68", _("Ksar El Boukhari")
        EL_ARICHA = "69", _("El Aricha")

    class Status(models.TextChoices):
        NEW = "new", _("New")
        READ = "read", _("Read")
        REPLIED = "replied", _("Replied")
        ARCHIVED = "archived", _("Archived")

    first_name = models.CharField(_("first name"), max_length=100)
    last_name = models.CharField(_("last name"), max_length=100, blank=True)
    email = models.EmailField(_("email"))
    phone = models.CharField(_("phone"), max_length=50, blank=True)
    wilaya = models.CharField(_("wilaya"), max_length=20, choices=Wilaya.choices)

    subject = models.CharField(_("subject"), choices=Subject.choices, max_length=200)
    message = models.TextField(_("message"))

    consent = models.BooleanField( _("consent"), default=False)
    status = models.CharField(_("status"), max_length=20, choices=Status.choices, default=Status.NEW)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = _("Contact message")
        verbose_name_plural = _("Contact messages")

    def __str__(self):
        return f"{self.subject} - {self.email}"
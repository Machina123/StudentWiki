from .Handler import *
from django.utils.translation import ugettext_lazy as _

_form = get_form()
_degree = get_degree()
_year = get_year()
_date = get_first_date()

CHOICES_DATE = [
    ("blank", _('A whole week')),
    (_date[0], _('Monday')),
    (_date[1], _("Tuesday")),
    (_date[2], _("Wednesday")),
    (_date[3], _("Thursday")),
    (_date[4], _("Friday"))
]
CHOICES_FORM = [
    (_form[2], _("Full-time studies")),
    (_form[1], _("Part-time studies"))
]
CHOICES_DEGREE = [
    (_degree[2], _("Undergraduate studies")),
    (_degree[1], _("Graduate studies"))
]
CHOICES_YEAR = [
    (_year[0], _year[0]),
    (_year[1], _year[1]),
    (_year[2], _year[2])
]
CHOICES_SPECIALITY = [
    ("ASI", _("IT Systems Administration")),
    ("MiTI", _("Multimedia and Internet Technologies"))
]


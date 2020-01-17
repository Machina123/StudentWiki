from .Handler import *

_form = get_form()
_degree = get_degree()
_year = get_year()
_date = get_first_date()

CHOICES_DATE = [
    ("blank", "Cały tydzień"),
    (_date[0], "Poniedziałek"),
    (_date[1], "Wtorek"),
    (_date[2], "Środa"),
    (_date[3], "Czwartek"),
    (_date[4], "Piątek")
]
CHOICES_FORM = [
    (_form[2], "Stacjonarne"),
    (_form[1],"Niestacjonarne")
]
CHOICES_DEGREE = [
    (_degree[2], "I Stopien"),
    (_degree[1],"II Stopien")
]
CHOICES_YEAR = [
    (_year[0],_year[0]),
    (_year[1], _year[1]),
    (_year[2], _year[2])
]
CHOICES_SPECIALITY = [
    ("ASI", "Administracja Systemami Informatycznymi"),
    ("MiTI", "Multimedia i Technologie Internetowe")
]


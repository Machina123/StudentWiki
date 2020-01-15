def index(request):
    return {
        'project_name': 'StudentWiki',
        'logout': 'Wyloguj',
        'upload': 'Dodaj plik',
        'file_list': 'Lista plików',
        'contact': 'Kontakt',
    }

def files(request):
    return {
        'file_upload': 'Dodaj plik',
        'files': 'Dodane pliki',
        'new_file': 'Dodaj nowy plik',
        'file_list': 'Lista plików',
        'file_preview': 'Podgląd pliku',
        'file_description': 'Opis pliku',
        'download': "Pobierz",
        'users_file': 'Pliki dodane przez użytkowników',
        'details': 'Szczegóły',
        'error': 'Błąd',
        'no_files': 'Nie znaleziono plików',

    }

def footer(request):
    return {
        'university_name': 'Uniwersytet Pedagogiczny im. KEN ',
        'institute_name': 'Instytut Informatyki',
        'address': 'ul. Podchorążych 2, 30-084 Kraków',
        'phone': '''telefon: (+48 12) 662 78 45\n
             (+48 12) 662 78 46\n
             fax: (+48 12) 662 78 46\n''',
        'email': 'email: ii@up.krakow.pl',
    }

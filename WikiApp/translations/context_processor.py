from django.utils.translation import ugettext_lazy as _

def index(request):
    return {
        'project_name': 'StudentWiki',
        'logout': _('Logout'),
        'contact': _('Contact'),
        'search': _("Searching"),
        'search_results': _("Search result"),
        'searching_for': _('Searching for'),
        'schedule': _('Schedule'),
        'consultations': _("Consultations"),
    }

def files(request):
    return {
        'upload': _('Upload file'),
        'file_list': _('File list'),
        'files': _('Uploaded files'),
        'new_file': _('Upload new file'),
        'file_preview': _('File preview'),
        'file_description': _('File description'),
        'download': _('Download'),
        'file_upload': _('Upload'),
        'users_file': _('Files added by users'),
        'details': _('Details'),
        'error': _('Error'),
        'no_files': _('No such files exist'),
        'file_remove': _('Remove file'),
        'owner': _('Owner'),
        'description': _("Description"),
        'file_name': _('File name'),
        'course': _('Course'),
        'select_file': _('Select file'),
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

def resources(request):
    return {
        'add_res': _('Add resource'),
        'res_list': _('Resource list'),
        'resources': _('External resources'),
        'new_res': _('Add new resource'),
        'res_preview': _('Resource preview'),
        'res_description': _('Resource description'),
        'res_open': _('Open external resource'),
        'users_res': _('External resources added by users'),
        'no_resources': _('No resources available'),
        'res_creation': _('New external resource'),
        'res_remove': _('Remove resource'),
        'res_address': _('Resource address'),
        'res_name': _('Resource name'),
    }

def consultations(request):
    return {
        'lecturer': _("Lecturer"),
        'hours': _("Hours"),
        'room': _("Room"),
        'monday': _("Monday"),
        'tuesday': _("Tuesday"),
        'wednesday': _("Wednesday"),
        'thursday': _("Thursday"),
        'friday': _("Friday"),
        'day_of_the_week': _('Day of the week'),
        'type_of_studies': _('Type of studies'),
        'semester': _('Semester'),
        'speciality': _('Speciality'),
        'subject_name': _('The name of subject'),
        'teacher': _('Teacher'),
        'date': _('Date'),
        'start': _('Start time'),
        'end': _('End time'),
        'class': _('Classroom'),
        'class_form': _('Class form'),
        'group': _('Group'),
    }


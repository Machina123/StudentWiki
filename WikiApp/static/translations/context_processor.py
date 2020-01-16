from django.utils.translation import ugettext_lazy as _

def index(request):
    return {
        'project_name': 'StudentWiki',
        'logout': _('Logout'),
        'contact': _('Contact'),
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
        'file_upload': _("Upload"),
        'users_file': _('Files added by users'),
        'details': _('Details'),
        'error': _('Error'),
        'no_files': _('No such files exist'),
        'file_remove': _('Remove file'),
        'owner': _("Owner")
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
        'res_address': _('Resource address')
    }
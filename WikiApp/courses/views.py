from django.shortcuts import render
from django.urls import reverse_lazy

from resources.models import Subject, ExternalResource
from Files.models import FileModel
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url=reverse_lazy("user:my_login"))
def courses_list(request):
    courses = Subject.objects.all()
    context = {
        "courses": courses
    }
    return render(request, "courses/course_list.html", context=context)

@login_required(login_url=reverse_lazy("user:my_login"))
def course_details(request, pk):
    course = Subject.objects.get(pk=pk)
    files = FileModel.objects.filter(file_subject=course)
    resources = ExternalResource.objects.filter(rsrc_subject=course)

    context = {
        "course": course,
        "files": files,
        "resources": resources
    }
    return render(request, "courses/course_details.html", context=context)
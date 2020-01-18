from itertools import chain

from django.db.models import Q
from django.forms import forms
from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from resources.models import ExternalResource, Subject
from Files.models import FileModel


def homepage(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        return render(request, 'users/login.html')


class SearchResultsView(ListView):
    model = [FileModel, ExternalResource, Subject]
    template_name = 'search_results.html'


    def get_queryset(self):
        query = self.request.GET.get('q')

        object_list1 = FileModel.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )

        object_list2 = ExternalResource.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )

        object_list3 = Subject.objects.filter(
            Q(sub_name__icontains=query)
        )

        dicLength = len(object_list1) + len(object_list2) + len(object_list3)
        object_list = {'query':query,'dicLength': dicLength, 'q1':object_list1,'q2':object_list2,'q3':object_list3}



        return object_list
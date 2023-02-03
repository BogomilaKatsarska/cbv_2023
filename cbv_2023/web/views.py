import random
from django.views.generic import TemplateView
from django.views import generic as views
from django import views
from django.http import HttpResponse
from django.shortcuts import render

from cbv_2023.web.models import Employee


def index(request):
    context = {
       'title': 'FBV',
    }
    return render(request, 'index.html', context)


class IndexView(views.View):
    def get(self, request):
        return HttpResponse('It works from CBV')


class IndexViewWithTemplate(views.TemplateView):
    template_name = 'index.html'
    extra_context = {
        'title': 'Template view',
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employees'] = Employee.objects.all()
        return context

# class IndexView:
#
#     def __init__(self):
#         self.values = [random.randint(1, 15)]
#
#     @classmethod
#     def get_view(cls):
#         return cls().view
#
#     def view(self, request):
#         return HttpResponse(f'IT WORKS:{self.values} !')
#
#
# class IndexViewWithProfile(IndexView):
#     pass
#
#
# class Index2View(IndexView):
#     def __init__(self):
#         super().__init__()
#         self.values.append(random.randint(15, 30))
#
#
# index()
#
# index_view = IndexView().get_view()


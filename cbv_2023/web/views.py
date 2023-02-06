import random

import form as form
from django.urls import reverse, reverse_lazy
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


class IndexViewWithListView(views.ListView):
    context_object_name = 'employees'
    model = Employee
    template_name = 'index.html'
    extra_context = {
        'title': 'List view',
    }


class EmployeeCreateForm(form.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {
            'first_name': form.TextInput(
                attrs={
                    'placeholder': 'Enter Name',
                }
            )
        }


class EmployeeCreateView(views.CreateView):
    template_name = 'employees/create.html'
    # model = Employee
    # fields = "__all__"
    form_class = EmployeeCreateForm
    # success_url = '/' --> static success url

    def get_success_url(self):
        created_object = self.object
        return reverse_lazy('employee details', kwargs={
            'pk': created_object.pk,
        })

    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)

    def post(self, *args, **kwargs):
        return super().post(*args, **kwargs)

    def get_form(self, form_class = None):
        form = super().get_form(form_class=form_class)
        for name, field in form.fields.items():
            field.widget.attrs['placeholder'] = 'Enter' + name

        return form


class EmployeeUpdateView(views.UpdateView):
    model = Employee
    fields = '__all__'
    template_name = 'employees/create.html'

    def get_success_url(self):
        created_object = self.object
        return reverse_lazy('employee details', kwargs={
            'pk': created_object.pk,
        })


class EmployeeDetailsView(views.DetailView):
    model = Employee
    template_name = 'employees/details.html'

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


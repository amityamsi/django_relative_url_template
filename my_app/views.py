from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (View,TemplateView,
                                 ListView,DetailView,
                                 CreateView,UpdateView,
                                 DeleteView)
from my_app import models


class indexview(TemplateView):
    template_name='index.html'

class SchoolListView(ListView):
    context_object_name='schools'
    model=models.school

class SchoolDetailView(DetailView):
    context_object_name='school_details'
    model=models.school
    template_name='my_app/school_details.html'

class SchoolCreateView(CreateView):
    fields=('name','principal','location')
    model=models.school

class SchoolUpdateView(UpdateView):
    fields=('name','principal')
    model=models.school

class SchoolDeleteView(DeleteView):
    model=models.school
    success_url=reverse_lazy('my_app:list')
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.db.models import Q

# Create your views here.
from .forms import SeialnumberModelForm  # using forms in [create, update]
from .models import SeialNumber, Person

# create


def create_view(request):
    # if request.method == 'POST':
    #     #print(request.POST)
    #     form = SeialnumberModelForm(request.POST)
    #     if form.is_valid():
    #         form.save(commit=False)
    #         print(form.cleaned_data)

    form = SeialnumberModelForm(request.POST or None)

    context = {
        'form': form
    }

    if form.is_valid():
        obj = form.save(commit=False)
        # print(obj.running_number)
        obj.save()

        # Alert messages
        messages.success(request, 'Create a new Seial Number')
        context = {
            'form': SeialnumberModelForm()
        }
        # return HttpResponseRedirect('/blog/{id}'.format(id=obj.id)) # redirect to view

    template = 'create_views.html'
    return render(request, template_name=template, context=context)

# update


def update_view(request, id=None):
    # if request.method == 'POST':
    #     #print(request.POST)
    #     form = SeialnumberModelForm(request.POST)
    #     if form.is_valid():
    #         form.save(commit=False)
    #         print(form.cleaned_data)

    obj = get_object_or_404(SeialNumber, id=int(id))
    form = SeialnumberModelForm(request.POST or None, instance=obj)

    context = {
        # 'object':obj,
        'form': form
    }

    if form.is_valid():
        obj = form.save(commit=False)
        # print(obj.running_number)
        obj.save()

        # Alert messages
        messages.success(request, 'Update Seial Number')
        # return HttpResponseRedirect('/blog/{id}'.format(id=obj.id)) # redirect to view

    template = 'update_view.html'
    return render(request, template_name=template, context=context)

# List


def list_views(request):
    query = request.GET.get('q')
    obj = SeialNumber.objects.all()
    if query is not None:
        obj = obj.filter(
            Q(id__icontains=query)|
            Q(running_number__icontains=query)
            )
        # obj = obj.filter(running_number__icontains=query)
    context = {
        'object_list': obj
    }
    template = 'list_views.html'
    return render(request, template_name=template, context=context)


# Detail
def detail_view(request, id=None):
    template = 'detail_view.html'

    # obj = SeialNumber.objects.get(id=100) # // select * from seial_number where id =100
    # get_object_or_404(Model.name, value)
    obj = get_object_or_404(SeialNumber, id=int(id))

    context = {
        'object': obj
    }

    return render(request, template_name=template, context=context)

# Delete
def delete_view(request, id=None):
    template = 'delete_view.html'

    obj = get_object_or_404(SeialNumber, id=int(id))

    if request.method == "POST":
        obj.delete()
        messages.success(request, 'Seial Nuber deelte')
        return HttpResponseRedirect('/blog/') # redirect to view

    context = {
        'object': obj
    }

    return render(request, template_name=template, context=context)

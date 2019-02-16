from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, resolve_url
# Create your views here.
#클래스형 :
#보통 제네릭 뷰를 상속받아서 쓰기 위해서
#제네릭 뷰를 사용하는 이유는
#많이 사용하는 기능을 미리 구현했기때문에
from django.urls import reverse
from django.views.generic import TemplateView
from tagging.models import Tag, TaggedItem
from tagging.views import TaggedObjectList
from .models import *
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView


class PhotoList(ListView):
    model = Photo
    template_name = 'photo/photo_list.html'


class PhotoCreate(LoginRequiredMixin, CreateView):
    model = Photo
    fields = ['image', 'text']
    template_name = 'photo/photo_create.html'

    def form_valid(self, form):
        form.instance.writer_id = self.request.user.id
        if form.is_valid():
            form.instance.save()
            pk = Photo.objects.first()
            return redirect('photo:photo_detail', pk.id)
        else:
            return self.render_to_response({'form':form})




class PhotoUpdate(LoginRequiredMixin, UpdateView):
    model = Photo
    fields = ['image', 'text']
    template_name = 'photo/photo_update.html'


class PhotoDelete(LoginRequiredMixin, DeleteView):
    model = Photo
    template_name = 'photo/photo_delete.html'
    success_url = '/'

    # def get(self, request, *arg, **kwargs):
    #     object = self.get_object()
    #     if object.writer != request.user:
    #         return HttpResponseRedirect(object.get_absolute_url())
    #     return super(PhotoDelete, self.get(request,  *arg, **kwargs))


class PhotoDetail(DetailView):
    model = Photo
    template_name = 'photo/photo_detail.html'

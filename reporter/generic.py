'''
Created on 1/8/2016

@author: natalia
'''

from __future__ import unicode_literals
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from reporter.models import Galleta
from django.core.urlresolvers import reverse_lazy
from django.views.generic.list import ListView


class GalletaCreate(CreateView):
    model = Galleta
    fields =  "__all__"
    success_url="/"

class GalletaUpdate(UpdateView):
    model = Galleta
    fields =  "__all__"
    success_url= "/"
    
class GalletaDelete(DeleteView):
    model= Galleta
    success_url = reverse_lazy('galleta-list')

class GalletaList(ListView):
    model = Galleta

   
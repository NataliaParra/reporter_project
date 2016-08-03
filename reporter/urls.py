'''
Created on 1/8/2016

@author: natalia
'''
from __future__ import unicode_literals
from django.conf.urls import url
from reporter.generic import GalletaCreate, GalletaUpdate, GalletaDelete
from reporter.generic import GalletaList

urlpatterns= [
url("create$", GalletaCreate.as_view(),name="galleta_Create"),
url("update$", GalletaUpdate.as_view(),name="galleta_Update"),
url("delete$", GalletaDelete.as_view(),name="galleta_Delete"),
url("list$", GalletaList.as_view(), name='galleta-list')
]

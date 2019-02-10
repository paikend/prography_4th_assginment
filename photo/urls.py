
from django.urls import path
from .views import *


app_name = 'photo'

urlpatterns = [
    path('', PhotoList.as_view(), name='index'),
    path('create/', PhotoCreate.as_view(), name='photo_create'),
    path('detail/<int:pk>/', PhotoDetail.as_view(), name='photo_detail'),
    path('update/<int:pk>/', PhotoUpdate.as_view(), name='photo_update'),
    path('delete/<int:pk>/', PhotoDelete.as_view(), name='photo_delete'),

]

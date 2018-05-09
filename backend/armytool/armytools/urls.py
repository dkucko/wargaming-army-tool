from django.urls import path

from . import views

urlpatterns = [
    path('equipment/', views.EquipmentView.as_view(), name='equipment')
]
from django.urls import path

from . import views

urlpatterns = [
    path('abilities/', views.get_ability_list),
    path('armies/', views.get_army_list),
    path('battlelogs/', views.get_battle_log_list),
    path('contingents/', views.get_contingent_list),
    path('contingenttypes/', views.get_contingent_type_list),
    path('equipment/', views.get_equipment_list),
    path('models/', views.get_model_list),
    path('modeltypes/', views.get_model_type_list),
    path('players/', views.get_player_list),
    path('scenarios/', views.get_scenario_list),
    path('units/', views.get_unit_list),
    path('unittypes/', views.get_unit_type_list),
]
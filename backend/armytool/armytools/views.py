from django.views import View
from django.http import JsonResponse
from .models import *


def get_equipment_list(request):
    response = {'content': [{e.id: e.name} for e in Equipment.objects.all()]}
    return JsonResponse(response)


def get_model_list(request):
    response = {'content': [{m.id: m.name} for m in Model.objects.all()]}
    return JsonResponse(response)


def get_ability_list(request):
    response = {'content': [{a.id: a.name} for a in Ability.objects.all()]}
    return JsonResponse(response)


def get_model_type_list(request):
    response = {'content': [{mt.id: mt.name} for mt in ModelType.objects.all()]}
    return JsonResponse(response)


def get_unit_list(request):
    response = {'content': [{u.id: u.name} for u in Unit.objects.all()]}
    return JsonResponse(response)


def get_army_list(request):
    response = {'content': [{a.id: a.name} for a in Army.objects.all()]}
    return JsonResponse(response)


def get_battle_log_list(request):
    response = {'content': [{b.id: b.name, 'date': b.date} for b in BattleLog.objects.all()]}
    return JsonResponse(response)


def get_player_list(request):
    response = {'content': [{p.id: p.name} for p in Player.objects.all()]}
    return JsonResponse(response)


def get_scenario_list(request):
    response = {'content': [{s.id: s.name} for s in Scenario.objects.all()]}
    return JsonResponse(response)

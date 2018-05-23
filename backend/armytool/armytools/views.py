from django.views import View
from django.http import JsonResponse
from .models import *


def get_equipment_list(request):
    response = {'Equimpent': [{e.name: e.name} for e in Equipment.objects.all()]}
    return JsonResponse(response)


def get_model_list(request):
    response = {'Models': [{m.name: m.name} for m in Model.objects.all()]}
    return JsonResponse(response)


def get_ability_list(request):
    response = {'Abilities': [{a.name: a.name} for a in Ability.objects.all()]}
    return JsonResponse(response)


def get_model_type_list(request):
    response = {'Model types': [{mt.name: mt.name} for mt in ModelType.objects.all()]}
    return JsonResponse(response)


def get_unit_list(request):
    response = {'Units': [{u.name: u.name} for u in Unit.objects.all()]}
    return JsonResponse(response)


def get_army_list(request):
    response = {'Armies': [{a.name: a.name} for a in Army.objects.all()]}
    return JsonResponse(response)


def get_battle_log_list(request):
    response = {'Battle logs': [{b.name: b.name, 'date': b.date} for b in BattleLog.objects.all()]}
    return JsonResponse(response)


def get_player_list(request):
    response = {'Players': [{p.name: p.name} for p in Player.objects.all()]}
    return JsonResponse(response)


def get_scenario_list(request):
    response = {'Scenarios': [{s.name: s.name} for s in Scenario.objects.all()]}
    return JsonResponse(response)

from django.views import View
from django.http import JsonResponse
from .models import *


def get_equipment_list(request):
    response = {'Equimpent': [{'name': e.name} for e in Equipment.objects.all()]}
    return JsonResponse(response)


def get_model_list(request):
    response = {'Models': [{'name': m.name} for m in Model.objects.all()]}
    return JsonResponse(response)


def get_ability_list(request):
    response = {'Abilities': [{'name': a.name} for a in Ability.objects.all()]}
    return JsonResponse(response)


def get_model_type_list(request):
    response = {'Model types': [{'name': mt.name} for mt in ModelType.objects.all()]}
    return JsonResponse(response)


def get_unit_list(request):
    response = {'Units': [{'name': u.name} for u in Unit.objects.all()]}
    return JsonResponse(response)


def get_unit_type_list(request):
    response = {'Unit types': [{'name': ut.name} for ut in UnitType.objects.all()]}
    return JsonResponse(response)


def get_contingent_list(request):
    response = {'Contingents': [{'name': c.name} for c in Contingent.objects.all()]}
    return JsonResponse(response)


def get_contingent_type_list(request):
    response = {'Contingent types': [{'name': ct.name} for ct in ContingentType.objects.all()]}
    return JsonResponse(response)


def get_army_list(request):
    response = {'Armies': [{'name': a.name} for a in Army.objects.all()]}
    return JsonResponse(response)


def get_battle_log_list(request):
    response = {'Battle logs': [{'name': b.name, 'date': b.date} for b in BattleLog.objects.all()]}
    return JsonResponse(response)


def get_player_list(request):
    response = {'Players': [{'name': p.name} for p in Player.objects.all()]}
    return JsonResponse(response)


def get_scenario_list(request):
    response = {'Scenarios': [{'name': s.name} for s in Scenario.objects.all()]}
    return JsonResponse(response)

from django.views import View
from django.http import JsonResponse
from .models import *


def get_equipment_list(request):
    response = {'Equipment': [
        {'name': e.name,
         'point_cost': e.point_cost} for e in Equipment.objects.all()]}
    return JsonResponse(response)


def get_model_list(request):
    response = {'Models': [
        {'name': m.name,
         'model_type': str(m.model_type),
         'equipment': [str(e.name) for e in m.equipment_set.all()]
         } for m in Model.objects.all()]}
    return JsonResponse(response)


def get_ability_list(request):
    response = {'Abilities': [{'name': a.name} for a in Ability.objects.all()]}
    return JsonResponse(response)


def get_model_type_list(request):
    response = {'Model types': [
        {'name': mt.name,
         'point_cost': mt.point_cost} for mt in ModelType.objects.all()]}
    return JsonResponse(response)


def get_unit_list(request):
    response = {'Units': [
        {'name': u.name,
         'might': u.might,
         'unit_type:': str(u.unit_type),
         'models': [(str(m.model), m.amount) for m in u.modelcount_set.objects.all()]
         } for u in Unit.objects.all()]}
    return JsonResponse(response)


def get_unit_type_list(request):
    response = {'Unit types': [{'name': ut.name} for ut in UnitType.objects.all()]}
    return JsonResponse(response)


def get_contingent_list(request):
    response = {'Contingents': [
        {'name': c.name,
         'command_point_bonus': c.command_point_bonus,
         'contingent_type': str(c.contingent_type),
         'units': [u.name for u in c.unit_set.objects.all()]
         } for c in Contingent.objects.all()]}
    return JsonResponse(response)


def get_contingent_type_list(request):
    response = {'Contingent types': [{'name': ct.name} for ct in ContingentType.objects.all()]}
    return JsonResponse(response)


def get_army_list(request):

    response = {'Armies': [
        {'name': a.name,
         'faction': a.faction,
         'contingents': [c.name for c in a.contingent_set.objects.all()]
         } for a in Army.objects.all()]}
    return JsonResponse(response)


def get_battle_log_list(request):
    response = {'Battle logs': [
        {'name': b.name,
         'date': b.date,
         'scenario': str(b.scenario),
         'winner': str(b.winner)} for b in BattleLog.objects.all()]}
    return JsonResponse(response)


def get_player_list(request):
    response = {'Players': [{'name': p.name} for p in Player.objects.all()]}
    return JsonResponse(response)


def get_scenario_list(request):
    response = {'Scenarios': [{'name': s.name} for s in Scenario.objects.all()]}
    return JsonResponse(response)

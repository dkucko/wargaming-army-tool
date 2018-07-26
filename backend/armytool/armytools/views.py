from django.views import View
from django.http import JsonResponse
from .models import *


def get_equipment_list(request):
    response = {'Equipment': [
        {'id': e.pk,
         'name': e.name,
         'point_cost': e.point_cost} for e in Equipment.objects.all()]}
    return JsonResponse(response)


def get_model_list(request):
    response = {'Models': [
        {'id': m.pk,
         'name': m.name,
         'model_type': str(m.model_type),
         'equipment': [str(e.name) for e in m.equipment_set.all()]
         } for m in Model.objects.all()]}
    return JsonResponse(response)


def get_ability_list(request):
    response = {'Abilities': [
        {'name': a.name,
         'id': a.pk} for a in Ability.objects.all()]}
    return JsonResponse(response)


def get_model_type_list(request):
    response = {'Model types': [
        {'name': mt.name,
         'point_cost': mt.point_cost,
         'id': mt.pk} for mt in ModelType.objects.all()]}
    return JsonResponse(response)


def get_unit_list(request):
    response = {'Units': [
        {'name': u.name,
         'might': u.might,
         'unit_type:': str(u.unit_type),
         'models': [(str(m.model), m.amount) for m in u.modelcount_set.all()],
         'id': u.pk
         } for u in Unit.objects.all()]}
    return JsonResponse(response)


def get_unit_type_list(request):
    response = {'Unit types': [
        {'name': ut.name,
         'id': ut.pk
         } for ut in UnitType.objects.all()]}
    return JsonResponse(response)


def get_contingent_list(request):
    response = {'Contingents': [
        {'name': c.name,
         'contingent_type': str(c.contingent_type),
         'units': [u.name for u in c.unit_set.all()],
         'id': c.pk
         } for c in Contingent.objects.all()]}
    return JsonResponse(response)


def get_contingent_type_list(request):
    response = {'Contingent types': [
        {'name': ct.name,
         'command_point_bonus': ct.command_point_bonus,
         'id': ct.pk
         } for ct in ContingentType.objects.all()]}
    return JsonResponse(response)


def get_army_list(request):

    response = {'Armies': [
        {'name': a.name,
         'faction': a.faction,
         'contingents': [c.name for c in a.contingent_set.all()],
         'id': a.pk
         } for a in Army.objects.all()]}
    return JsonResponse(response)


def get_battle_log_list(request):
    response = {'Battle logs': [
        {'name': b.name,
         'date': b.date,
         'scenario': str(b.scenario),
         'winner': str(b.winner),
         'id': b.pk} for b in BattleLog.objects.all()]}
    return JsonResponse(response)


def get_player_list(request):
    response = {'Players': [
        {'name': p.name,
         'id': p.pk} for p in Player.objects.all()]}
    return JsonResponse(response)


def get_scenario_list(request):
    response = {'Scenarios': [
        {'name': s.name,
         'id': s.pk} for s in Scenario.objects.all()]}
    return JsonResponse(response)

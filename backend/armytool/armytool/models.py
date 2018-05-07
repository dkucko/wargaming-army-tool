from django.utils import timezone
from django.db import models as django_models


class Scenario(django_models.Model):
    name = django_models.CharField(max_length=200)


class BattleLog(django_models.Model):
    date = django_models.DateTimeField(default=timezone.now())
    name = django_models.CharField(max_length=200)
    scenario = django_models.ForeignKey(Scenario, on_delete=django_models.DO_NOTHING)
    winner = django_models.ForeignKey(Player, on_delete=django_models.DO_NOTHING)


class Player(django_models.Model):
    name = django_models.CharField(max_length=200)


class Army(django_models.Model):
    name = django_models.CharField(max_length=200)
    faction = django_models.CharField(max_length=100)
    players = django_models.ManyToManyField(Player)


class PlayerArmy(django_models.Model):
    battle_logs = django_models.ManyToManyField(BattleLog)
    player = django_models.ForeignKey(Player, on_delete=django_models.CASCADE)
    army = django_models.ForeignKey(Army, on_delete=django_models.CASCADE)


class Unit(django_models.Model):
    name = django_models.CharField(max_length=100)
    might = django_models.IntegerField()
    armies = django_models.ManyToManyField(Army)


class ModelType(django_models.Model):
    name = django_models.CharField(max_length=100)
    point_cost = django_models.IntegerField(default=0)


class Model(django_models.Model):
    name = django_models.CharField(max_length=100)
    model_type = django_models.ForeignKey(ModelType, on_delete=django_models.DO_NOTHING)
    units = django_models.ManyToManyField(Unit)


class Equipment(django_models.Model):
    name = django_models.CharField(max_length=100)
    point_cost = django_models.IntegerField()
    models = django_models.ManyToManyField(Model)


class Ability(django_models.Model):
    name = django_models.CharField(max_length=100)
    models = django_models.ManyToManyField(Model)

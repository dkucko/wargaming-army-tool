from django.utils import timezone
from django.db import models as django_models


class Scenario(django_models.Model):
    name = django_models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Player(django_models.Model):
    name = django_models.CharField(max_length=200)

    def __str__(self):
        return self.name


class BattleLog(django_models.Model):
    date = django_models.DateTimeField(default=timezone.now())
    name = django_models.CharField(max_length=200)
    scenario = django_models.ForeignKey(Scenario, on_delete=django_models.DO_NOTHING)
    winner = django_models.ForeignKey(Player, on_delete=django_models.DO_NOTHING)

    def __str__(self):
        return self.name


class Army(django_models.Model):
    name = django_models.CharField(max_length=200)
    faction = django_models.CharField(max_length=100)
    players = django_models.ManyToManyField(Player)
    point_cost = django_models.IntegerField(default=0)
    might = django_models.IntegerField(default=0)

    def get_total_points(self):
        cost = 0
        for unit in self.unit_set().all():
            cost += unit.get_total_points()

        return cost

    def get_total_might(self):
        might = 0
        for unit in self.unit_set().all():
            might += unit.might

        return might

    def __str__(self):
        return self.name


class PlayerArmy(django_models.Model):
    battle_logs = django_models.ManyToManyField(BattleLog)
    player = django_models.ForeignKey(Player, on_delete=django_models.DO_NOTHING)
    army = django_models.ForeignKey(Army, on_delete=django_models.DO_NOTHING)

    def __str__(self):
        return str(self.player) + ': ' + str(self.army)


class Unit(django_models.Model):
    name = django_models.CharField(max_length=100)
    might = django_models.IntegerField()
    armies = django_models.ManyToManyField(Army)
    point_cost = django_models.IntegerField(default=0)

    def get_total_points(self):
        cost = 0
        for model in self.model_set.all():
            cost += model.get_total_points()

        return cost

    def __str__(self):
        return self.name


class ModelType(django_models.Model):
    name = django_models.CharField(max_length=100)
    point_cost = django_models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Model(django_models.Model):
    name = django_models.CharField(max_length=100)
    model_type = django_models.ForeignKey(ModelType, on_delete=django_models.DO_NOTHING)
    units = django_models.ManyToManyField(Unit)
    point_cost = django_models.IntegerField(default=0)

    def get_total_points(self):
        cost = self.model_type.point_cost
        for equipment in self.equipment_set.all():
            cost += equipment.point_cost

        return cost

    def __str__(self):
        return self.name


class Equipment(django_models.Model):
    name = django_models.CharField(max_length=100)
    point_cost = django_models.IntegerField()
    models = django_models.ManyToManyField(Model)

    def __str__(self):
        return self.name


class Ability(django_models.Model):
    name = django_models.CharField(max_length=100)
    models = django_models.ManyToManyField(Model)

    def __str__(self):
        return self.name

from django.test import TestCase
from .models import *


class EquipmentTest(TestCase):

    def setUp(self):
        mt = ModelType(name='Testmodel', point_cost=10)
        mt.save()
        Model.objects.create(name='Testmodel1', model_type=mt)
        Equipment.objects.create(name='TestEquipment', point_cost=20)

    def test_add_equipment_to_model(self):
        e = Equipment.objects.first()
        m = Model.objects.first()
        m.equipment_set.add(e)
        m.save()
        self.assertEqual(len(m.equipment_set.all()), 1)
        self.assertEqual(m.point_cost, 30)


class ModelTest(TestCase):

    def setUp(self):
        ModelType.objects.create(name='Testmodel', point_cost=10)
        Model.objects.create(name='Testmodel1', model_type=ModelType.objects.first())
        ModelCount.objects.create(model=Model.objects.first(), amount=3)

    def test_add_model_to_model_count(self):
        m = Model.objects.first()
        mc = ModelCount(model=m, amount=1)
        mc.save()
        self.assertEqual(10, mc.get_total_points())

    def test_add_model_to_unit(self):
        mc = ModelCount.objects.first()
        u = Unit(name='Testunit')
        u.save()
        u.modelcount_set.add(mc)
        u.save()
        self.assertEqual(30, u.get_total_points())



from __future__ import unicode_literals
from django.apps import AppConfig


class BattleConfig(AppConfig):
    name = 'battle'

    def ready(self):
        from battle import battles, signals, views

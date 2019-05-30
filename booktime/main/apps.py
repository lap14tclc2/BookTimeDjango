from django.apps import AppConfig


class MainConfig(AppConfig):
    name = 'main'

    def ready(self):
        # make sure this file is initialized when Django app launch
        from .import signals

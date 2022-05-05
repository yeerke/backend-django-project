from django.apps import AppConfig


class MainConfig(AppConfig):
    name = 'recruting.main'

    def ready(self):
        import recruting.main.signals
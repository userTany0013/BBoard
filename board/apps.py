from django.apps import AppConfig


class ResponsesConfig(AppConfig):
    name = 'board'

    def ready(self):
        import board.signals


class BoardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'board'

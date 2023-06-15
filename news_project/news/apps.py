from django.apps import AppConfig

class NewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'news'

    def ready(self):
        from .templatetags.censor import censor
        from django.template import Library

        Library().filters['censor'] = censor
from django.apps import AppConfig
from material.admin.apps import ModuleMixin

class UserConfig(AppConfig, ModuleMixin):
    name = 'user'
    icon = '<i class="material-icons">flag</i>'

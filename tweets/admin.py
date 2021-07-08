from django.contrib import admin
from django.apps import apps

app_name = apps.app_configs.get('tweets')
# Register your models here.

for model in app_name.get_models():
	try:
		admin.site.register(model)
	except admin.sites.AlreadyRegistered:
		pass

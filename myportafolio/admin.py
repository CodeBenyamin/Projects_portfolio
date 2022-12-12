from django.contrib import admin
from .models import PortafolioModel, Tags
# Register your models here.

admin.site.register(PortafolioModel)
admin.site.register(Tags)
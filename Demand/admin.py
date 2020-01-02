from django.contrib import admin
from .models import island,western,eastern,norms
# Register your models here.

admin.site.register(island)
admin.site.register(western)
admin.site.register(eastern)
admin.site.register(norms)
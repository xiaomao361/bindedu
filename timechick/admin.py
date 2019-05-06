from django.contrib import admin
from . import models

# Register your models here.

admin.site.site_title = "时光鸡"
admin.site.site_header = "时光鸡"
admin.site.index_title = "时光鸡"

admin.site.register(models.User)
admin.site.register(models.Song)
admin.site.register(models.PlayList)

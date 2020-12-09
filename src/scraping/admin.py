from django.contrib import admin
from scraping.models import *


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(City, PostAdmin)
admin.site.register(Language, PostAdmin)
admin.site.register(Vacancy)

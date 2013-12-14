from django.contrib import admin
from labluz.core.models import Noticia, FotoNoticia


class FotoNoticiaInline(admin.TabularInline):
    model = FotoNoticia


class NoticiaAdmin(admin.ModelAdmin):
    inlines = [FotoNoticiaInline]
    prepopulated_fields = {'slug': ('titulo',)}


admin.site.register(Noticia, NoticiaAdmin)

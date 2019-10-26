from django.contrib import admin
from .models import Page
from .models import *

# Register your models here.
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_approved', 'created',)

    class Media:
        css = {
            'all': ('pages/css/custom_ckeditor.css',)
        }

admin.site.register(Page, PageAdmin)


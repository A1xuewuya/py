from django.contrib import admin
from models import *


# Register your models here.
# class HeroaInfoInLine(admin.StackedInline):
class HeroaInfoInLine(admin.TabularInline):
    model = HeroInfo
    extra = 2


class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'btitle', 'bpub_date']
    list_filter = ['btitle']
    search_fields = ['btitle']
    list_per_page = 10
    # fields = ['btitle', 'bpub_date']
    fieldsets = [
        ('basic', {'fields': ['btitle']}),
        ('more', {'fields': ['bpub_date']}),
    ]
    inlines = [HeroaInfoInLine]


admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo)

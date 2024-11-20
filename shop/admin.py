from django.contrib import admin
from .models import Shop, Review
# Register your models here.
class ShopAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ['title', 'description']
    list_editable = ('description',)


admin.site.register(Shop, ShopAdmin)
admin.site.register(Review)

from django.contrib import admin

from .models import Review

class ReviewAdmin(admin.ModelAdmin):

    list_display    = ["shop","dt","comment","ip","approval"]
    list_editable   = ["approval"]


admin.site.register(Review,ReviewAdmin)


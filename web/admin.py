from django.contrib import admin
from .models import Project, Skill, Image


class ImageAdminInline(admin.TabularInline):
    model = Image


class ProjectAdmin(admin.ModelAdmin):
    inlines = (ImageAdminInline,)


admin.site.register(Project, ProjectAdmin)
admin.site.register(Skill)

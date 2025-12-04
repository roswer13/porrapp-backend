"""
Django admin customization.
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from core import models


@admin.register(models.User)
class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users."""
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (
            _('Permissions'),
            {'fields': ('is_active', 'is_staff', 'is_superuser')}
        ),
        (_('Important dates'), {'fields': ('last_login',)})
    )
    readonly_fields = ['last_login']
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'password1', 'password2', 'name',
                'is_active', 'is_staff', 'is_superuser'
            )
        }),
    )


@admin.register(models.Competition)
class CompetitionAdmin(admin.ModelAdmin):
    """Define the admin pages for competitions."""
    list_display = ['name', 'year', 'host_country']


@admin.register(models.Team)
class TeamAdmin(admin.ModelAdmin):
    """Define the admin pages for teams."""
    ordering = ['name']
    list_display = ['name', 'competition']
    list_filter = ['competition']
    search_fields = ['name']
    raw_id_fields = ['competition']


@admin.register(models.Match)
class MatchAdmin(admin.ModelAdmin):
    """Define the admin pages for matches."""
    ordering = ['-date']
    list_display = ['competition', 'stage', 'home_team', 'away_team', 'date', 'home_score', 'away_score', 'is_finished']
    list_filter = ['competition', 'stage', 'is_finished']
    search_fields = ['home_team__name', 'away_team__name']
    raw_id_fields = ['home_team', 'away_team', 'competition']
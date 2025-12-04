"""
Database models.
"""
from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import Competition, Team


class Match(models.Model):
    competition = models.ForeignKey(
        Competition,
        on_delete=models.CASCADE,
        related_name='matches',
        verbose_name=_('Competition'),
        help_text=_('Competition this match belongs to')
    )
    home_team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name='home_matches',
        verbose_name=_('Home Team'),
        help_text=_('The home team for this match')
    )
    away_team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name='away_matches',
        verbose_name=_('Away Team'),
        help_text=_('The away team for this match')
    )
    stage = models.CharField(
        verbose_name=_('Stage'),
        help_text=_('Stage of the competition (e.g., Group Stage, Quarterfinal)'),
        max_length=64
    )
    date = models.DateTimeField(
        verbose_name=_('Date and Time'),
        help_text=_('Date and time when the match is scheduled')
    )
    home_score = models.PositiveIntegerField(
        verbose_name=_('Home Team Score'),
        help_text=_('Score of the home team'),
        default=0
    )
    away_score = models.PositiveIntegerField(
        verbose_name=_('Away Team Score'),
        help_text=_('Score of the away team'),
        default=0
    )
    is_finished = models.BooleanField(
        verbose_name=_('Is Finished'),
        help_text=_('Indicates if the match has finished'),
        default=False
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Created At'),
        help_text=_('Timestamp when the match record was created')
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_('Updated At'),
        help_text=_('Timestamp when the match record was last updated')
    )

    def __str__(self):
        return f"{self.home_team} vs {self.away_team} on {self.date.strftime('%Y-%m-%d %H:%M')}"
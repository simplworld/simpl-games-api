from django import forms

from . import models


class DecisionForm(forms.ModelForm):
    class Meta:
        model = models.Decision
        fields = [
            'name',
            'data',
            'period',
            'role',
        ]


class GameForm(forms.ModelForm):
    class Meta:
        model = models.Game
        fields = [
            'name',
            'active',
        ]


class PeriodForm(forms.ModelForm):
    class Meta:
        model = models.Period
        fields = [
            'scenario',
            'order',
            'data',
        ]


class PhaseForm(forms.ModelForm):
    class Meta:
        model = models.Phase
        fields = [
            'name',
            'game',
            'order',
        ]


class ResultForm(forms.ModelForm):
    class Meta:
        model = models.Result
        fields = [
            'name',
            'data',
            'period',
            'role',
        ]


class RoleForm(forms.ModelForm):
    class Meta:
        model = models.Role
        fields = [
            'name',
            'slug',
            'game',
            'data',
        ]


class RunForm(forms.ModelForm):
    class Meta:
        model = models.Run
        fields = [
            'name',
            'active',
            'game',
            'data',
        ]


class ScenarioForm(forms.ModelForm):
    class Meta:
        model = models.Scenario
        fields = [
            'name',
            'runuser',
            'world',
        ]


class WorldForm(forms.ModelForm):
    class Meta:
        model = models.World
        fields = [
            'name',
            'run',
            'data',
            'external_ids',
        ]

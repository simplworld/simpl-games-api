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
            'game',
            'data',
        ]


class RoundForm(forms.ModelForm):

    class Meta:
        model = models.Round
        fields = [
            'name',
            'world',
            'order',
            'data',
        ]


class RunForm(forms.ModelForm):

    class Meta:
        model = models.Run
        fields = [
            'name',
            'active',
            'game',
            'start_date',
            'end_date',
            'data',
        ]


class ScenarioForm(forms.ModelForm):

    class Meta:
        model = models.Scenario
        fields = [
            'name',
            'runuser',
            'round',
            'player_periods',
            'current_period',
            'last_period',
            'seed_periods',
            'total_periods',
        ]


class WorldForm(forms.ModelForm):

    class Meta:
        model = models.World
        fields = [
            'name',
            'run',
            'data',
            'canvas_ids',
        ]

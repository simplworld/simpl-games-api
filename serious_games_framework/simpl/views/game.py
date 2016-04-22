from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from ..forms import GameForm
from ..models import Game


class GameCreateView(SuccessMessageMixin, CreateView):
    model = Game
    form_class = GameForm
    template_name = 'simpl/games/game_create.html'
    success_message = '%(name)s was created successfully'

    def get_success_url(self):
        return reverse('simpl:game_list')


class GameDeleteView(DeleteView):
    model = Game
    template_name = 'simpl/games/game_delete.html'
    context_object_name = 'game'
    success_message = 'Game was deleted successfully'

    def get_success_url(self):
        messages.success(self.request, self.success_message)
        return reverse('simpl:game_list')


class GameDetailView(DetailView):
    model = Game
    template_name = 'simpl/games/game_detail.html'
    context_object_name = 'game'


class GameListView(ListView):
    model = Game
    template_name = 'simpl/games/game_list.html'
    paginate_by = 20
    context_object_name = 'game_list'
    allow_empty = True


class GameUpdateView(SuccessMessageMixin, UpdateView):
    model = Game
    form_class = GameForm
    template_name = 'simpl/games/game_update.html'
    context_object_name = 'game'
    success_message = '%(name)s was updated successfully'

    def get_success_url(self):
        return reverse('simpl:game_list')

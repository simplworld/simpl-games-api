from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from ..forms import WorldForm
from ..models import World


class WorldCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = World
    form_class = WorldForm
    template_name = 'simpl/worlds/world_create.html'
    success_message = '%(name)s was created successfully'

    def get_success_url(self):
        return reverse('simpl:world_detail', args=(self.object.pk,))


class WorldDeleteView(LoginRequiredMixin, DeleteView):
    model = World
    template_name = 'simpl/worlds/world_delete.html'
    context_object_name = 'world'
    success_message = 'World was deleted successfully'

    def get_success_url(self):
        messages.success(self.request, self.success_message)
        return reverse('simpl:world_list')


class WorldDetailView(LoginRequiredMixin, DetailView):
    model = World
    template_name = 'simpl/worlds/world_detail.html'
    context_object_name = 'world'


class WorldListView(LoginRequiredMixin, ListView):
    model = World
    template_name = 'simpl/worlds/world_list.html'
    paginate_by = 20
    context_object_name = 'world_list'
    allow_empty = True


class WorldUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = World
    form_class = WorldForm
    template_name = 'simpl/worlds/world_update.html'
    context_object_name = 'world'
    success_message = '%(name)s was updated successfully'

    def get_success_url(self):
        return reverse('simpl:world_detail', args=(self.object.pk,))

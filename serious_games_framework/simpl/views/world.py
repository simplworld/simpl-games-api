from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from django.http import Http404
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from ..forms import WorldForm
from ..models import World


class WorldCreateView(SuccessMessageMixin, CreateView):
    model = World
    form_class = WorldForm
    template_name = 'simpl/worlds/world_create.html'
    success_message = '%(name)s was created successfully'

    def get_success_url(self):
        return reverse('simpl:world_detail', args=(self.object.pk,))


class WorldDeleteView(DeleteView):
    model = World
    template_name = 'simpl/worlds/world_delete.html'
    context_object_name = 'world'
    success_message = 'World was deleted successfully'

    def get_success_url(self):
        messages.success(self.request, self.success_message)
        return reverse('simpl:world_list')


class WorldDetailView(DetailView):
    model = World
    template_name = 'simpl/worlds/world_detail.html'
    context_object_name = 'world'


class WorldListView(ListView):
    model = World
    template_name = 'simpl/worlds/world_list.html'
    paginate_by = 20
    context_object_name = 'world_list'
    allow_empty = True


class WorldUpdateView(UpdateView):
    model = World
    form_class = WorldForm
    template_name = 'simpl/worlds/world_update.html'
    context_object_name = 'world'
    success_message = '%(name)s was updated successfully'

    def get_success_url(self):
        return reverse('simpl:world_detail', args=(self.object.pk,))

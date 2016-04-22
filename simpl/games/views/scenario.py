from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from django.http import Http404
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from ..forms import ScenarioForm
from ..models import Scenario


class ScenarioCreateView(SuccessMessageMixin, CreateView):
    model = Scenario
    form_class = ScenarioForm
    template_name = 'simpl/scenarios/scenario_create.html'
    success_message = '%(name)s was created successfully'

    def get_success_url(self):
        return reverse('simpl:scenario_detail', args=(self.object.pk,))


class ScenarioDeleteView(DeleteView):
    model = Scenario
    template_name = 'simpl/scenarios/scenario_delete.html'
    context_object_name = 'scenario'
    success_message = 'Scenario was deleted successfully'

    def get_success_url(self):
        messages.success(self.request, self.success_message)
        return reverse('simpl:scenario_list')


class ScenarioDetailView(DetailView):
    model = Scenario
    template_name = 'simpl/scenarios/scenario_detail.html'
    context_object_name = 'scenario'


class ScenarioListView(ListView):
    model = Scenario
    template_name = 'simpl/scenarios/scenario_list.html'
    paginate_by = 20
    context_object_name = 'scenario_list'
    allow_empty = True


class ScenarioUpdateView(UpdateView):
    model = Scenario
    form_class = ScenarioForm
    template_name = 'simpl/scenarios/scenario_update.html'
    context_object_name = 'scenario'
    success_message = '%(name)s was updated successfully'

    def get_success_url(self):
        return reverse('simpl:scenario_detail', args=(self.object.pk,))

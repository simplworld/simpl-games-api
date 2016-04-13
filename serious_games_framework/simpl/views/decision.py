from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from django.http import Http404
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from ..forms import DecisionForm
from ..models import Decision


class DecisionCreateView(SuccessMessageMixin, CreateView):
    model = Decision
    form_class = DecisionForm
    template_name = 'simpl/decisions/decision_create.html'
    success_message = '%(name)s was created successfully'

    def get_success_url(self):
        return reverse('simpl:decision_detail', args=(self.object.pk,))


class DecisionDeleteView(DeleteView):
    model = Decision
    template_name = 'simpl/decisions/decision_delete.html'
    context_object_name = 'decision'
    success_message = 'Decision was deleted successfully'

    def get_success_url(self):
        messages.success(self.request, self.success_message)
        return reverse('simpl:decision_list')


class DecisionDetailView(DetailView):
    model = Decision
    template_name = 'simpl/decisions/decision_detail.html'
    context_object_name = 'decision'


class DecisionListView(ListView):
    model = Decision
    template_name = 'simpl/decisions/decision_list.html'
    paginate_by = 20
    context_object_name = 'decision_list'
    allow_empty = True


class DecisionUpdateView(UpdateView):
    model = Decision
    form_class = DecisionForm
    template_name = 'simpl/decisions/decision_update.html'
    context_object_name = 'decision'
    success_message = '%(name)s was updated successfully'

    def get_success_url(self):
        return reverse('simpl:decision_detail', args=(self.object.pk,))

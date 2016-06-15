from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from ..forms import DecisionForm
from ..models import Decision


class DecisionCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Decision
    form_class = DecisionForm
    template_name = 'simpl/decisions/decision_create.html'
    success_message = '%(name)s was created successfully'

    def get_success_url(self):
        return reverse('simpl:decision_detail', args=(self.object.pk,))


class DecisionDeleteView(LoginRequiredMixin, DeleteView):
    model = Decision
    template_name = 'simpl/decisions/decision_delete.html'
    context_object_name = 'decision'
    success_message = 'Decision was deleted successfully'

    def get_success_url(self):
        messages.success(self.request, self.success_message)
        return reverse('simpl:decision_list')


class DecisionDetailView(LoginRequiredMixin, DetailView):
    model = Decision
    template_name = 'simpl/decisions/decision_detail.html'
    context_object_name = 'decision'


class DecisionListView(LoginRequiredMixin, ListView):
    model = Decision
    template_name = 'simpl/decisions/decision_list.html'
    paginate_by = 20
    context_object_name = 'decision_list'
    allow_empty = True


class DecisionUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Decision
    form_class = DecisionForm
    template_name = 'simpl/decisions/decision_update.html'
    context_object_name = 'decision'
    success_message = '%(name)s was updated successfully'

    def get_success_url(self):
        return reverse('simpl:decision_detail', args=(self.object.pk,))

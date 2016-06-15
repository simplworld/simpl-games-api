from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from ..forms import PhaseForm
from ..models import Phase


class PhaseCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Phase
    form_class = PhaseForm
    template_name = 'simpl/phases/phase_create.html'
    success_message = '%(name)s was created successfully'

    def get_success_url(self):
        return reverse('simpl:phase_detail', args=(self.object.pk,))


class PhaseDeleteView(LoginRequiredMixin, DeleteView):
    model = Phase
    template_name = 'simpl/phases/phase_delete.html'
    context_object_name = 'phase'
    success_message = 'Phase was deleted successfully'

    def get_success_url(self):
        messages.success(self.request, self.success_message)
        return reverse('simpl:phase_list')


class PhaseDetailView(LoginRequiredMixin, DetailView):
    model = Phase
    template_name = 'simpl/phases/phase_detail.html'
    context_object_name = 'phase'


class PhaseListView(LoginRequiredMixin, ListView):
    model = Phase
    template_name = 'simpl/phases/phase_list.html'
    paginate_by = 20
    context_object_name = 'phase_list'
    allow_empty = True


class PhaseUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Phase
    form_class = PhaseForm
    template_name = 'simpl/phases/phase_update.html'
    context_object_name = 'phase'
    success_message = '%(name)s was updated successfully'

    def get_success_url(self):
        return reverse('simpl:phase_detail', args=(self.object.pk,))

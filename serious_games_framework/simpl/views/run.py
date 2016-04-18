from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from django.http import Http404
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from ..forms import RunForm
from ..models import Run


class RunCreateView(SuccessMessageMixin, CreateView):
    model = Run
    form_class = RunForm
    template_name = 'simpl/runs/run_create.html'
    success_message = '%(name)s was created successfully'

    def get_success_url(self):
        return reverse('simpl:run_detail', args=(self.object.pk,))


class RunDeleteView(DeleteView):
    model = Run
    template_name = 'simpl/runs/run_delete.html'
    context_object_name = 'run'
    success_message = 'Run was deleted successfully'

    def get_success_url(self):
        messages.success(self.request, self.success_message)
        return reverse('simpl:run_list')


class RunDetailView(DetailView):
    model = Run
    template_name = 'simpl/runs/run_detail.html'
    context_object_name = 'run'


class RunListView(ListView):
    model = Run
    template_name = 'simpl/runs/run_list.html'
    paginate_by = 20
    context_object_name = 'run_list'
    allow_empty = True


class RunUpdateView(UpdateView):
    model = Run
    form_class = RunForm
    template_name = 'simpl/runs/run_update.html'
    context_object_name = 'run'
    success_message = '%(name)s was updated successfully'

    def get_success_url(self):
        return reverse('simpl:run_detail', args=(self.object.pk,))

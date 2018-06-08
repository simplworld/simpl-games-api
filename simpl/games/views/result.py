from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from ..forms import ResultForm
from ..models import Result


class ResultCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Result
    form_class = ResultForm
    template_name = 'simpl/results/result_create.html'
    success_message = '%(name)s was created successfully'

    def get_success_url(self):
        return reverse('simpl:result_detail', args=(self.object.pk,))


class ResultDeleteView(LoginRequiredMixin, DeleteView):
    model = Result
    template_name = 'simpl/results/result_delete.html'
    context_object_name = 'result'
    success_message = 'Result was deleted successfully'

    def get_success_url(self):
        messages.success(self.request, self.success_message)
        return reverse('simpl:result_list')


class ResultDetailView(LoginRequiredMixin, DetailView):
    model = Result
    template_name = 'simpl/results/result_detail.html'
    context_object_name = 'result'


class ResultListView(LoginRequiredMixin, ListView):
    model = Result
    template_name = 'simpl/results/result_list.html'
    paginate_by = 20
    context_object_name = 'result_list'
    allow_empty = True


class ResultUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Result
    form_class = ResultForm
    template_name = 'simpl/results/result_update.html'
    context_object_name = 'result'
    success_message = '%(name)s was updated successfully'

    def get_success_url(self):
        return reverse('simpl:result_detail', args=(self.object.pk,))

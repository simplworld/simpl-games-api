from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from django.http import Http404
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from ..forms import WebhookLogForm
from ..models import WebhookLog


class WebhookLogCreateView(SuccessMessageMixin, CreateView):
    model = WebhookLog
    form_class = WebhookLogForm
    template_name = 'simpl/webhooks/webhook_log_create.html'
    success_message = '%(name)s was created successfully'

    def get_success_url(self):
        return reverse('simpl:webhook_log_detail', args=(self.object.pk,))


class WebhookLogDeleteView(DeleteView):
    model = WebhookLog
    template_name = 'simpl/webhooks/webhook_log_delete.html'
    context_object_name = 'webhook_log'
    success_message = 'WebhookLog was deleted successfully'

    def get_success_url(self):
        messages.success(self.request, self.success_message)
        return reverse('simpl:webhook_log_list')


class WebhookLogDetailView(DetailView):
    model = WebhookLog
    template_name = 'simpl/webhooks/webhook_log_detail.html'
    context_object_name = 'webhook_log'


class WebhookLogListView(ListView):
    model = WebhookLog
    template_name = 'simpl/webhooks/webhook_log_list.html'
    paginate_by = 20
    context_object_name = 'webhook_log_list'
    allow_empty = True


class WebhookLogUpdateView(UpdateView):
    model = WebhookLog
    form_class = WebhookLogForm
    template_name = 'simpl/webhooks/webhook_log_update.html'
    context_object_name = 'webhook_log'
    success_message = '%(name)s was updated successfully'

    def get_success_url(self):
        return reverse('simpl:webhook_log_detail', args=(self.object.pk,))

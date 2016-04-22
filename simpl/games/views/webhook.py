from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from django.http import Http404
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from ..forms import WebhookForm
from ..models import Webhook


class WebhookCreateView(SuccessMessageMixin, CreateView):
    model = Webhook
    form_class = WebhookForm
    template_name = 'simpl/webhooks/webhook_create.html'
    success_message = '%(name)s was created successfully'

    def get_success_url(self):
        return reverse('simpl:webhook_detail', args=(self.object.pk,))


class WebhookDeleteView(DeleteView):
    model = Webhook
    template_name = 'simpl/webhooks/webhook_delete.html'
    context_object_name = 'webhook'
    success_message = 'Webhook was deleted successfully'

    def get_success_url(self):
        messages.success(self.request, self.success_message)
        return reverse('simpl:webhook_list')


class WebhookDetailView(DetailView):
    model = Webhook
    template_name = 'simpl/webhooks/webhook_detail.html'
    context_object_name = 'webhook'


class WebhookListView(ListView):
    model = Webhook
    template_name = 'simpl/webhooks/webhook_list.html'
    paginate_by = 20
    context_object_name = 'webhook_list'
    allow_empty = True


class WebhookUpdateView(UpdateView):
    model = Webhook
    form_class = WebhookForm
    template_name = 'simpl/webhooks/webhook_update.html'
    context_object_name = 'webhook'
    success_message = '%(name)s was updated successfully'

    def get_success_url(self):
        return reverse('simpl:webhook_detail', args=(self.object.pk,))

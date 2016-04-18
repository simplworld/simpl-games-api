# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse
from django.views.generic import RedirectView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .forms import UserForm
from .models import User


class UserCreateView(SuccessMessageMixin, CreateView):
    model = User
    form_class = UserForm
    fields = ['password', 'last_login', 'is_superuser', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'date_joined', 'name', 'canvas_id', 'data']
    template_name = 'users/user_create.html'
    success_message = '%(name)s was created successfully'

    def get_success_url(self):
        return reverse('users:detail', args=(self.object.pk,))


class UserDeleteView(DeleteView):
    model = User
    template_name = 'users/user_delete.html'
    context_object_name = 'user'
    success_message = 'User was deleted successfully'

    def get_success_url(self):
        messages.success(self.request, self.success_message)
        return reverse('users:list')


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = "username"
    slug_url_kwarg = "username"

    # TODO: template_name = 'users/user_detail.html'
    # TODO: context_object_name = 'user'


class UserListView(LoginRequiredMixin, ListView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = "username"
    slug_url_kwarg = "username"

    # TODO: template_name = 'users/user_list.html'
    # TODO: paginate_by = 20
    # TODO: context_object_name = 'user_list'
    # TODO: allow_empty = True


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail",
                       kwargs={"username": self.request.user.username})


class UserUpdateView(LoginRequiredMixin, UpdateView):

    fields = ['name', ]

    # we already imported User in the view code above, remember?
    model = User

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse("users:detail",
                       kwargs={"username": self.request.user.username})

        # TODO: return reverse('users:user_detail', args=(self.object.pk,))

    def get_object(self):
        # Only get the User record for the user making the request
        return User.objects.get(username=self.request.user.username)


class ManageUserUpdateView(UpdateView):
    model = User
    form_class = UserForm
    template_name = 'users/user_update.html'
    context_object_name = 'user'
    success_message = '%(name)s was updated successfully'

    def get_success_url(self):
        return reverse('users:detail', args=(self.object.username,))

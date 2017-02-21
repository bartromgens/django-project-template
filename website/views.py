import logging

from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import TemplateView, UpdateView

logger = logging.getLogger(__name__)


class UserProfileView(SuccessMessageMixin, UpdateView):
    model = User
    template_name = 'website/userprofile.html'
    fields = ['username', 'first_name', 'last_name', 'email']
    success_message = 'Userprofile saved'

    def get_context_data(self, **kwargs):
        if not self.request.user == self.get_object():
            raise PermissionDenied
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        if self.request.user != form.instance:
            raise PermissionDenied
        email = form.cleaned_data['email']
        users = User.objects.exclude(id=self.request.user.id).filter(email=email)
        if users.exists():
            form.add_error('email', 'Email is already used by another user.')
            logger.info('email is already used by another user')
            return self.form_invalid(form)
        return super().form_valid(form)

    def get_success_url(self):
        return '/userprofile/' + str(self.request.user.id) + '/'

from django.contrib import messages
from django.views.generic.edit import CreateView
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView,\
    PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.contrib.auth import logout

from authentication.forms import UserRegisterForm


class RegisterView(CreateView):
    template_name = 'authentication/sign_up.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy("authentication:login")

    def form_valid(self, form):
        form.save()

        user = authenticate(
            email=form.cleaned_data.get('email'),
            password=form.cleaned_data.get('password1')
        )

        if user is not None:
            login(self.request, user)
            messages.success(self.request, "Login successful")
        else:
            messages.error(self.request, "Cannot login")

        return super().form_valid(form)


class CustomLoginView(LoginView):
    template_name = 'authentication/login.html'

    def get_success_url(self):
        return reverse_lazy("authentication:sign_up")


class CustomLogoutView(LogoutView):
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return reverse_lazy("authentication:login")


class ResetPasswordView(PasswordResetView):
    template_name = "authentication/password_reset_form.html"
    subject_template_name = "email/password_reset_subject.txt"
    email_template_name = "email/password_reset_email.html"
    success_url = reverse_lazy("authentication:password-reset-done")


class ResetPasswordDoneView(PasswordResetDoneView):
    template_name = "message/password_reset_done.html"


class ResetPasswordConfirmView(PasswordResetConfirmView):
    template_name = "authentication/password_reset_confirm.html"
    success_url = reverse_lazy("authentication:password-reset-complete")


class ChangePasswordCompleteView(PasswordResetCompleteView):
    template_name = "message/password_reset_complete.html"

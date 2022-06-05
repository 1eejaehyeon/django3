from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from acconts.froms import porfileForm
from django.views.generic import TemplateView, CreateView

from accounts.forms import ProfileForm
from accounts.models import profile, Profile

# Create your views here.


User = get_user_model()

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'

profile = ProfileView.as_view()


@login_required
def profile_edit(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = None

    if request.method == 'POST':
        form = ProfileForm(request.Post,request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
        else:
            form = ProfileForm(instance=profile)
        return render(request, 'accounts/profile_form.html', {
            'from' : form,
        })

    class SignupView(CreateView):
        model = User
        form_class = UserCreationForm
        success_url = settings.LOGIN_REDIRECT_URL
        template_name = 'accounts/signup_form.html'

        def form_valid(self, form):
            resp
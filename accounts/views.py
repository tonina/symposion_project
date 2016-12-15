from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def create_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            username = cd['username']
            email = cd['email']
            password = cd['password']
            user = User.objects.create_user(username,email,password)
            user.save()
            return HttpResponseRedirect(reverse('dashboard'))
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form':form})


def profile(request):
    return render(request, 'accounts/profile.html')


def prof_edit(request):
    return render(request, 'accounts/profedit.html')


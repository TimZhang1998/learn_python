from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm


def logout_view(request):
    """logout"""

    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))


def register(request):
    """register a new user"""

    if request.method != 'POST':
        # show a empty form
        form = UserCreationForm()
    else:
        # handle the finished form
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # automatically login, then return to index
            authenticate_user = authenticate(username=new_user.username,
                                             password=request.POST['password1'])
            login(request, authenticate_user)
            return HttpResponseRedirect(reverse('learning_logs:index'))

    context = {'form': form}
    return render(request, '../templates/users/register.html', context)
from django.contrib.auth.models import Group
from django.shortcuts import redirect, get_object_or_404
from .models import *
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from .forms import *
from django.contrib.auth import get_user_model

User = get_user_model()


def homepage(request):
    return render(request, 'base.html')


class MyLoginView(LoginView):
    template_name = 'account/login.html'
    form_class = AuthUserForm

    def get_success_url(self):
        return reverse_lazy('home')


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})


class MyLogoutView(LogoutView):
    new_page = reverse_lazy('home')


class Groups(ListView):
    # model = Category_groups
    queryset = Group.objects.all()
    template_name = 'groups.html'
    context_object_name = 'groups_list'

    def join_group(request, *args, **kwargs):
        if request.method == 'POST':
            pass


def users(request):

    context = {'users': UserAbstract.objects.all()}
    return render(request, 'groups.html', context)


def join(request, group_id):
    group = get_object_or_404(Group, pk= group_id)
    if request.method == 'POST':
        group.members.add(request.user)
        group.save()
        return redirect('/groups_detail' + str(group_id) )
    else:
        return render(request, 'groups', {'group': group})

def leave(request, user_id):
    if request.method == 'POST':
        group = get_object_or_404(Group, pk='group_id')
        if request.user in group.members.all():
            group.members.remove(request.user)
            group.save()
            return redirect('home')
            return HttpResponse("You have been removed successfully " + str(user.username))
            
    else:
        return render(request, '/groups')
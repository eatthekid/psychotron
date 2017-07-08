from django.contrib import auth
from django.shortcuts import render, render_to_response, HttpResponseRedirect, get_object_or_404
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from main_app.forms import RegForm, ProfileForm, UserForm
from tests_app.models import Test
from .models import Profile

def index(request):
    return render(request,'index.html',)

@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST['login']
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return HttpResponseRedirect('/profile/')
        else:
            return render(request, 'index.html', {'username': username, 'errors': True})
    raise Http404

@csrf_exempt
def registration(request):
    if request.method == 'POST':
        reg_form = RegForm(request.POST)
        if reg_form.is_valid():
            reg_form.save()
            username = reg_form['username']
            password = reg_form['password1']
            user = auth.authenticate(username=username, password=password)
            return HttpResponseRedirect('/profile/', {'user':user})
        context = {'reg_form': reg_form}
        return render(request, 'reg_form.html', context)
    context = {'reg_form': RegForm()}
    return render(request, 'reg_form.html', context)

@csrf_exempt
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

def profile(request):
    user = request.user
    user_profile = Profile.objects.filter(user=user)
    context = {'user_profile': user_profile,}
    return render(request, 'profile.html', context)

@csrf_exempt
def editProfile(request):
    if request.method == 'POST':
        uform = UserForm(request.POST)
        pform = ProfileForm(request.POST)
        pform.user = request.user
        if uform.is_valid() and pform.is_valid():
            uform.save()
            pform.save()
            return HttpResponseRedirect('/profile/')
        else:
            context = {'uform': uform, 'pform': pform,}
            return render(request, 'profile.html', context)
    if request.method == 'GET':
        user = request.user
        try:
            profile = Profile.objects.get(user=user)
        except:
            profile = Profile.objects.create(user=user)
        context = {'uform': UserForm(initial={
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
             }),
            'pform': ProfileForm(initial={
                'middle_name': profile.middle_name,
                'sex': profile.sex,
                'birthday': profile.birthday,
                 }),
                }
        return render(request, 'profile.html', context)


def tests(request):
    available_tests = Test.objects.all()
    context = {'available_tests': available_tests,}
    return render(request, 'test_catalog.html', context)
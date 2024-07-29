from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import LoginForm, Registerform, EditUserForm
from django.contrib import messages

def user_login(request):
    # if request.user.is_authenticated == True:
    #     return redirect('home')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username = form.cleaned_data.get('username'), password = form.cleaned_data.get('password'))
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error('username','Invalid User')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form':form})
 



def user_logout(request):
    logout(request)
    return redirect('home')



 
def user_register(request):
    if request.method == 'POST':
        form = Registerform(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username = username, password = password)
            if user is not None:
                messages.success(request, 'Account was created for ' + username)
                login(request, user)
                return redirect('user_login')

    else:
        form = Registerform()
    return render(request, 'account/register.html', {'form':form})



def user_edit(request):
    form = EditUserForm(instance=request.user)
    if request.method == 'POST':
        form = EditUserForm(instance=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'user information was updated')
    return render(request, 'account/edit.html',{'form':form})







# def user_register(request):
#     context = {'errors':[]}
#     if request.user.is_authenticated == True:
#         return redirect('home')
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password1 = request.POST.get('password1')
#         password2 = request.POST.get('password2')
#         if password1 != password2:
#             context['errors'].append('Passwords are not same!')
#             return render(request, 'account/register.html', context)
#         # if User.objects.get(username=username):
#         #     context['errors'].append('This username is exist!')
#             return render(request, 'account/register.html', context)
#         user = User.objects.create(username=username, email=email, password=password1)
#         login(request, user)
#         return redirect('home') 
#     return render(request, 'account/register.html') 
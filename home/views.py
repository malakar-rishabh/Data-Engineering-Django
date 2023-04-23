from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.shortcuts import redirect
from django.contrib import messages
from .models import SiteUser
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

# code for login
def login(request):
    # here we are checking for valid user
    if request.method == 'POST':
        username = request.POST['login_user_name']
        password = request.POST['login_password']
        x = authenticate(request, username=username,
                         password=password)
        if x is not None:
            auth_login(request, x)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid Username or Password')
            return redirect('/')
    else:
        return render(request, 'index.html')

#code for forgot password
def forgot(request):
    return render(request, 'forgot.html')

#code for signup
def Signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user_name = request.POST['signup_user_name']
        password = request.POST['signup_password']
        confirm__password = request.POST['confirm_password']
        email = request.POST['email']
        phone_number = request.POST['contact_number']
        company_name = request.POST['company_name']

        if password == confirm__password:
            if SiteUser.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
                return redirect('signup')
            else:
                my_user = SiteUser(first_name=first_name, last_name=last_name, username=user_name,
                                   confirm_password=confirm__password, email=email, contact_number=phone_number, company_name=company_name)
                my_user.set_password(password)
                my_user.save()
                # sending mail to user
                subject = "About Registration"
                message = f'Hi {user_name},\n\nThank you for registering with us.\n\nRegards,\nTeam Data Engineering'
                email_from = 'rishabhmalakar27@gmail.com'
                recipient_list = [email,]
                send_mail( subject, message, email_from, recipient_list )
                messages.success(request, 'User created successfully')
                return redirect('/')
        else:
            print("Password does't match")
            messages.error(request, 'Password does not match')
            return redirect('signup')
    return render(request, 'signup.html')

#code for dashboard
@login_required(login_url='/')
def dashboard(request):
    return render(request, 'home.html')

#code for logout
def logout(request):
    auth_logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('/')

#code for profile page
@login_required(login_url='/')
def profile(request):
    if request.user.is_authenticated:
        context = {'first_name': request.user.first_name,
                   'last_name': request.user.last_name,
                   'email': request.user.email,
                   'company_name': request.user.company_name,
                   'contact_number': request.user.contact_number,
                   }
        return render(request, 'profile.html', context)
    else:
        return render(request, 'index.html')
    
    

#code for updating user details
def update_profile(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.contact_number = request.POST.get('contact_number')
        user.company_name = request.POST.get('company_name')
        user.save()
        return redirect('profile')
    else:
        user = request.user
        context = {'first_name': user.first_name,
                   'last_name': user.last_name,
                   'email': user.email,
                   'contact_number': user.contact_number,
                   'company_name': user.company_name}
        return render(request, 'profile.html', context)
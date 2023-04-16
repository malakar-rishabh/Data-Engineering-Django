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

def reset(request):
    if request.method == 'POST':
       new_password = request.POST['new_password']
       confirm_password = request.POST['confirm_password']
       if new_password == confirm_password:
           gmail = request.POST['email']
           my_user = SiteUser.objects.get(email=gmail)
        #    breakpoint()
        #    new = SiteUser.make_password(new_password)
           my_user.set_password(new_password)
           my_user.save()
           subject = "About Password Change"
           message = 'Hi,\n\nYour password has been changed successfully.\n\nRegards,\nTeam Data Engineering'
           email_from = 'rishabhmalakar27@gmail.com'
           recipient_list = [gmail,]
           send_mail( subject, message, email_from, recipient_list )
           messages.success(request, 'Password changed successfully')
           return redirect('/')
       else:
              messages.error(request, 'Password does not match')
              return redirect('forgot')
    email = request.GET.get('email')
    return render(request, 'reset.html', {'email':email})
                  
           

# gmail = '' #global variable for email
def forgot(request):
    if request.method == 'POST':
        email = request.POST['email']
        if SiteUser.objects.filter(email=email).exists():
            return render(request, 'reset.html', {'email':email})
            
        else:
            messages.error(request, 'Email does not exist')
            print("Email does not exist")
            return redirect('forgot')
    email= request.GET.get('email')
    return render(request, 'forgot.html' , {'email':email})

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

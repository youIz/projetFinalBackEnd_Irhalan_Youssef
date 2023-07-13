from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate, logout, update_session_auth_hash
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from MyApp.forms import UserForm
from MyApp.models import User, Role
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail

# Create your views here.

# HOME VIEWS ______________________________
def home(request):
    return render(request, 'MyApp/home.html')


# CART VIEWS ______________________________
def cart(request):
    return render(request, 'MyApp/cart.html')


# CHECKOUT VIEWS ______________________________
def checkout(request):
    return render(request, 'MyApp/checkout.html')


# CONTACT VIEWS ______________________________
def contact(request):
    return render(request, 'MyApp/contact.html')


# ERROR VIEWS ______________________________
def error(request):
    return render(request, 'MyApp/error-404.html')

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            img_url = request.POST.get('img_url')
            default_role = Role.objects.get(name='member')
            user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name, img_url=img_url, role=default_role)
            user.newsletter = request.POST.get('newsletter') == 'on'
            user.save()
            
                # Log the user in
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                # Redirect them to the index (or wherever you want)
            
                    # Send a welcome email
            send_mail(
                'Welcome to our webshop!', # subject
                'Thank you for registering.', # message
                'moass2uranus@gmail.com', # from email
                [email], # to email
                fail_silently=False,
            )
                        # If the user has opted in for the newsletter, send another email
            if user.newsletter:
                send_mail(
                    'You\'ve subscribed to our newsletter!', # subject
                    'You will now receive updates from us.', # message
                    'moass2uranus@gmail.com', # from email
                    [email], # to email
                    fail_silently=False,
                )
            return redirect('index')
    else:
        form = RegistrationForm()
    return render(request, 'MyApp/signup.html',  {'form': form})

def singleBlog(request):
    return render(request, 'MyApp/singleBlog.html')

def track(request):
    return render(request, 'MyApp/track.html')


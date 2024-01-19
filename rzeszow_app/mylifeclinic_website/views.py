from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Appointment, Patient
from datetime import date


def home(request):
    return render(request, 'home.html', {})

def register_user(request):
    # Check if the request method is POST
    if request.method == 'POST':
        # Create a SignUpForm instance with the POST data
        form = SignUpForm(request.POST)
         # Check if the form is valid
        if form.is_valid():
             # Save the form data and create a new user
            form.save()
            # Authenticate and log in the user
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request, user)
            # Display a success message and redirect to the user panel
            messages.success(request, "You have successfully registered! Welcome!")
            return redirect('panel')
    else:
        # If the request method is not POST, create an empty SignUpForm instance
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})
    
    return render(request, 'register.html', {'form':form})
    
   

def login_user(request):
    # Chack to see if logging in
    if request.method == 'POST':
        # Retrieve the username and password from the POST data
        username = request.POST['email']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        # Check if authentication was successful
        if user is not None:
            # Log in the authenticated user
            login(request, user)
            # Display a success message and redirect to the user panel
            messages.success(request, "Zalogowano pomyślnie!")
            return redirect('panel')
        else:
            # Display an error message if authentication fails and redirect to the login page
            messages.success(request, "Wystąpił błąd podczas logowania, spróbuj ponownie...")
            return redirect('login')
    else:
        return render(request, 'login.html', {})
    
def doc_user(request):
    return render(request,'doc_login.html',{})

def logout_user(request):
    logout(request)
    messages.success(request, "Wylogowano pomyślnie...")
    return redirect('home')

def statute(request):
    return render(request,'statute.html',{})

def panel_user(request):
    
    # Take user info
    user = request.user
    
    records = Appointment.objects.filter(
        # Select only if user email matches patient email so next visit appears for user that is logged in
        patient__email=user.username,
        # Only select data after current date, because we want visits that are in the future
        date_of__gt=date.today()
    ).select_related(
        # select_related is used to optimize queries by performing a SQL join
        'employee__postion',
        'patient__employee'
    ).order_by(
        # Order by the date so we get first aopointment
        'date_of'
    ).values(
        # Values selected
        'date_of', 'employee__postion__nazwa' , 'employee__imie', 'employee__nazwisko', 'patient__email'
    )
    login_name = user.username
    '''
    # Query for doctor rankings
    results = (Ranking.objects.values('employee__imie', 'employee__nazwisko').annotate(avg_ranking=Round(Avg('ranking'), 2))
               .filter(employee_id=F('employee__id'))
               .order_by('employee__nazwisko')[:5])
               
    return render(request, 'panel.html', {'records': records, 'results': results})
    '''
    
    return render(request, 'panel.html', {'records': records, 'login_name': login_name})


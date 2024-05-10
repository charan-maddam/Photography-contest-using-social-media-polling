from django.shortcuts import render, redirect
from .models import AdminLogin, createcontest, register
from django.contrib.auth.decorators import login_required
# Create your views here.

def Home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'user.html')

def dashboard(request):
    return render(request, 'vote_participate.html')

def vote(request):
    return render(request, 'vote_page.html')

def participate(request):
    return render(request, 'participate_page.html')

def profile(request):
    return render(request, 'profile.html')

def forgotpassword(request):
    return render(request, 'reset_password.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        phone = request.POST['phone']
        password = request.POST['password']
        conpass = request.POST['conpass']
        user = register(username=username, phone=phone, password=password, conpass=conpass)
        user.save()
        return redirect('login')
    return render(request, 'registration.html')


def adminpage(request):
    if request.method == 'POST':
        # print('Post Method')
        phone = request.POST['phone']
        password = request.POST['password']

        try:
            user = AdminLogin.objects.get(phone=phone)
            if user.password == password:
                # print("password correct")
                return render(request, 'create_manage.html')
            else:
                # print("Password incorrect")
                return render(request, 'admin.html')
        except AdminLogin.DoesNotExist:
            print("User does not exist")
            return render(request, 'admin.html')
    else:    
        print("POST not opened")
        return render(request, 'admin.html')

@login_required(login_url='adminpage')
def createpage(request):
    return render(request, 'create_manage.html')

def create(request):
    if request.method == 'POST':
        print("POST login")
        theme = request.POST['theme']
        startdate = request.POST['startdate']
        enddate = request.POST['enddate']

        contest = createcontest(theme=theme, startdate=startdate, enddate=enddate)
        contest.save()
        return render(request, 'create_manage.html')
        
    return render(request, 'create_contest.html')

def manage(request):
    return render(request, 'manage_contest.html')
